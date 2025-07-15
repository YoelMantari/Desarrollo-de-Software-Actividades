import json
from dependency import DependsOn
from network import NetworkFactoryModule
from server import ServerFactoryModule
from firewall import FirewallFactoryModule
from load_balancer import LoadBalancerFactoryModule
from local_file_module import LocalFileModule

class Mediator:
    def __init__(self, module, enable_logging=True):
        self.module = module
        self.order = []
        self.creation_log = []  # Registro del orden de creación
        self.enable_logging = enable_logging

    def _create(self, module):
        # Crear red si es necesario
        if isinstance(module, NetworkFactoryModule):
            self.order.append(module.build())
            self.creation_log.append("network")
            return module.outputs()

        # Crear servidor si es necesario
        if isinstance(module, ServerFactoryModule):
            net_out = self._create(NetworkFactoryModule())
            module.depends = net_out
            self.order.append(module.build())
            self.creation_log.append("server")
            return module.outputs()

        # Crear firewall si es necesario
        if isinstance(module, FirewallFactoryModule):
            srv_out = self._create(ServerFactoryModule(self._create(NetworkFactoryModule())))
            module.depends = srv_out
            self.order.append(module.build())
            self.creation_log.append("firewall")
            return module.outputs()

        # Crear load balancer si es necesario
        if isinstance(module, LoadBalancerFactoryModule):
            fw_out = self._create(FirewallFactoryModule())
            module.depends = fw_out
            self.order.append(module.build())
            self.creation_log.append("load_balancer")
            return module.outputs()

        # Crear archivo de log local si es necesario
        if isinstance(module, LocalFileModule):
            # El archivo de log debe ser el último recurso creado
            module.creation_order = self.creation_log.copy()
            if module.depends:
                self.order.append(module.build())
            else:
                self.order.append(module.build())
            self.creation_log.append("local_file_log")
            return module.outputs()

        # Módulo desconocido
        self.order.append(module.build())
        return module.outputs()

    def build(self):
        # Inicia la creación con el módulo principal
        self._create(self.module)
        
        # Si el logging está habilitado, añadir el módulo de archivo local al final
        if self.enable_logging and not isinstance(self.module, LocalFileModule):
            # Crear módulo de log que depende del último recurso creado
            last_output = None
            if isinstance(self.module, LoadBalancerFactoryModule):
                last_output = DependsOn("null_resource", "load_balancer", {"port": "80"})
            elif isinstance(self.module, FirewallFactoryModule):
                last_output = DependsOn("null_resource", "firewall", {"port": "22"})
            elif isinstance(self.module, ServerFactoryModule):
                last_output = DependsOn("null_resource", "server", {"name": "hello-world-server"})
            elif isinstance(self.module, NetworkFactoryModule):
                last_output = DependsOn("null_resource", "network", {"name": "hello-world-network"})
            
            log_module = LocalFileModule(creation_order=self.creation_log.copy(), depends=last_output)
            self._create(log_module)
        
        # Fusionar todos los bloques
        merged = {
            "terraform": {
                "required_providers": {
                    "local": {
                        "source": "hashicorp/local",
                        "version": "~> 2.0"
                    }
                }
            }, 
            "resource": {}
        }
        for block in self.order:
            for res_type, res_defs in block["resource"].items():
                merged_resources = merged["resource"].setdefault(res_type, {})
                merged_resources.update(res_defs)
        return merged

if __name__ == "__main__":
    # Crear mediador con logging habilitado
    mediator = Mediator(LoadBalancerFactoryModule(), enable_logging=True)
    cfg = mediator.build()
    
    # Guardar configuración
    with open("main.tf.json", "w") as f:
        json.dump(cfg, f, indent=2)
    
    print("Configuración generada con logging local:")
    print(f"Orden de creación registrado: {mediator.creation_log}")
    print("Archivo main.tf.json actualizado con módulo local_file")
