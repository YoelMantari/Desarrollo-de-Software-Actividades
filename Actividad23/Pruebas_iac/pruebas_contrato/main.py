"""
Módulo local para definir una red en JSON, sin dependencia de proveedores de la nube.
"""
import json
import netaddr
import sys
import os

# importar validador si existe
try:
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from module_validator import ModuleValidator
except ImportError:
    ModuleValidator = None

class NetworkFactoryLocal:
    def __init__(self, name: str, ip_range: str):
        self.name = name
        self.network = f"{name}-net"
        self.ip_range = ip_range
        
        # validar inputs si el validador esta disponible
        if ModuleValidator:
            errors = ModuleValidator.validate_network_inputs(name, ip_range, 1)
            if errors:
                print(f"errores de validacion en {name}:")
                for error in errors:
                    print(f"  - {error}")

    def build(self) -> dict:
        """Genera recursos de red en formato JSON local."""
        net = netaddr.IPNetwork(self.ip_range)
        return {
            "resources": [
                {
                    "type": "local_network",
                    "name": self.network,
                    "cidr": str(net),
                    "network_id": f"net-{self.name}-001",
                    "network_cidr": str(net)
                }
            ]
        }

    def write(self, path: str):
        with open(path, 'w') as f:
            json.dump(self.build(), f, indent=4)
