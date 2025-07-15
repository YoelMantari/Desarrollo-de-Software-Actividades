#!/usr/bin/env python3
"""
simulador de pruebas con contenedores
demuestra testing de conectividad con servicios simulados
"""
import json
import time
import socket
from contextlib import closing

class ContainerSimulator:
    """simula un contenedor docker para pruebas"""
    
    def __init__(self, name, service_type, port):
        self.name = name
        self.service_type = service_type
        self.port = port
        self.is_running = False
    
    def start(self):
        """simular inicio del contenedor"""
        print(f"iniciando contenedor {self.name} ({self.service_type}) en puerto {self.port}")
        time.sleep(1)  # simular tiempo de inicio
        self.is_running = True
        print(f"contenedor {self.name} iniciado correctamente")
    
    def stop(self):
        """simular parada del contenedor"""
        print(f"deteniendo contenedor {self.name}")
        self.is_running = False
        print(f"contenedor {self.name} detenido")
    
    def health_check(self):
        """verificar si el servicio responde"""
        if not self.is_running:
            return False
        
        # simular health check del servicio
        print(f"verificando health check de {self.name}...")
        time.sleep(0.3)
        return True

def check_port_available(port):
    """verificar si un puerto esta disponible"""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        result = sock.connect_ex(('localhost', port))
        return result != 0

def simulate_terraform_instances():
    """simular creacion de instancias terraform"""
    instances = [
        {"id": "i-001", "ip": "10.0.1.10", "name": "web-1"},
        {"id": "i-002", "ip": "10.0.1.11", "name": "web-2"}
    ]
    
    print("creando instancias terraform simuladas...")
    for instance in instances:
        print(f"  instancia {instance['id']} creada en {instance['ip']}")
    
    return instances

def test_connectivity(instances, container):
    """probar conectividad entre instancias y contenedor"""
    print(f"\nprobando conectividad desde instancias hacia {container.name}...")
    
    for instance in instances:
        print(f"probando conexion desde {instance['name']} ({instance['ip']}) al puerto {container.port}")
        
        # simular intento de conexion
        time.sleep(0.2)
        
        if container.health_check():
            print(f"  conexion exitosa desde {instance['name']}")
        else:
            print(f"  error de conexion desde {instance['name']}")
            return False
    
    return True

def run_container_integration_test():
    """ejecutar prueba completa con contenedores"""
    print("iniciando prueba de integracion con contenedores")
    print("=" * 50)
    
    # encontrar puerto disponible
    test_port = 5432
    while not check_port_available(test_port):
        test_port += 1
    
    # crear contenedor simulado
    db_container = ContainerSimulator("postgres-test", "database", test_port)
    
    try:
        # fase 1: preparacion del entorno
        print("fase 1: preparando entorno de contenedores")
        db_container.start()
        
        # verificar que el servicio este listo
        if not db_container.health_check():
            raise Exception("contenedor no responde a health checks")
        
        # fase 2: ejecucion de terraform
        print("\nfase 2: ejecutando terraform con contenedor")
        instances = simulate_terraform_instances()
        
        # fase 3: validacion de conectividad
        print("\nfase 3: validando conectividad")
        connectivity_ok = test_connectivity(instances, db_container)
        
        if not connectivity_ok:
            raise Exception("fallo en pruebas de conectividad")
        
        print(f"\n{'=' * 50}")
        print("prueba de contenedores completada exitosamente")
        print("conectividad validada entre todos los componentes")
        
        return True
        
    except Exception as e:
        print(f"error en prueba de contenedores: {e}")
        return False
    
    finally:
        # limpieza siempre se ejecuta
        print(f"\nfase cleanup: limpiando recursos")
        db_container.stop()

def run_gradual_testing():
    """demostrar testing gradual superficial vs profundo"""
    print("\ndemostrado testing gradual")
    print("=" * 30)
    
    # nivel superficial - solo formato
    print("nivel superficial: validacion de formato")
    test_data = {
        "network_id": "net-123",
        "subnet_ids": ["subnet-1", "subnet-2"],
        "instance_ids": ["i-111", "i-222"]
    }
    
    # validaciones superficiales
    assert isinstance(test_data["network_id"], str)
    assert isinstance(test_data["subnet_ids"], list)
    assert len(test_data["subnet_ids"]) > 0
    print("  validacion superficial: formato correcto")
    
    # nivel profundo - funcionalidad real
    print("nivel profundo: validacion de funcionalidad")
    time.sleep(0.5)  # simular operacion compleja
    print("  simulando escritura en storage...")
    time.sleep(0.3)
    print("  simulando consulta a base de datos...")
    time.sleep(0.2)
    print("  validacion profunda: funcionalidad correcta")

if __name__ == "__main__":
    # ejecutar prueba de contenedores
    container_success = run_container_integration_test()
    
    # ejecutar demo de testing gradual
    run_gradual_testing()
    
    print(f"\nresultado final: {'exitoso' if container_success else 'fallo'}")
    exit(0 if container_success else 1)
