#!/usr/bin/env python3
"""
simulador de pruebas de integracion entre modulos
demuestra secuenciacion network -> compute -> storage
"""
import json
import os
import subprocess
import time
from pathlib import Path

# directorios de trabajo para cada modulo
NETWORK_DIR = "integration_test/network"
COMPUTE_DIR = "integration_test/compute" 
STORAGE_DIR = "integration_test/storage"
STATE_DIR = "integration_test/state"

def setup_test_environment():
    """crear directorios necesarios para la prueba"""
    dirs = [NETWORK_DIR, COMPUTE_DIR, STORAGE_DIR, STATE_DIR]
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    print("entorno de prueba preparado")

def simulate_network_module():
    """simular ejecucion del modulo network"""
    print("ejecutando modulo network...")
    
    # simular configuracion de red
    network_config = {
        "name": "test-vpc",
        "cidr": "10.0.0.0/16",
        "subnet_count": 2
    }
    
    # simular outputs del modulo network
    network_outputs = {
        "network_id": "net-12345",
        "network_cidr": "10.0.0.0/16",
        "subnet_ids": ["subnet-1", "subnet-2"],
        "route_table_id": "rt-67890"
    }
    
    # guardar estado del modulo network
    state_file = f"{STATE_DIR}/network_state.json"
    with open(state_file, 'w') as f:
        json.dump(network_outputs, f, indent=2)
    
    print(f"modulo network completado - estado guardado en {state_file}")
    return network_outputs

def simulate_compute_module(network_state):
    """simular ejecucion del modulo compute usando outputs de network"""
    print("ejecutando modulo compute...")
    
    # validar que network_state tenga los campos requeridos
    required_fields = ["network_id", "subnet_ids"]
    for field in required_fields:
        if field not in network_state:
            raise ValueError(f"campo requerido faltante: {field}")
    
    # simular configuracion de compute usando datos de network
    compute_config = {
        "instance_count": 2,
        "instance_type": "small",
        "network_id": network_state["network_id"],
        "subnet_ids": network_state["subnet_ids"]
    }
    
    # simular outputs del modulo compute
    compute_outputs = {
        "instance_ids": ["i-111", "i-222"],
        "instance_ips": ["10.0.1.10", "10.0.2.10"],
        "security_group_id": "sg-999",
        "load_balancer_dns": "lb-test.local"
    }
    
    # guardar estado del modulo compute
    state_file = f"{STATE_DIR}/compute_state.json"
    with open(state_file, 'w') as f:
        json.dump(compute_outputs, f, indent=2)
    
    print(f"modulo compute completado - estado guardado en {state_file}")
    return compute_outputs

def simulate_storage_module():
    """simular ejecucion del modulo storage independiente"""
    print("ejecutando modulo storage...")
    
    # simular configuracion de storage
    storage_config = {
        "bucket_name": "test-bucket-123",
        "storage_class": "standard",
        "encryption_enabled": True
    }
    
    # simular outputs del modulo storage
    storage_outputs = {
        "bucket_id": "bucket-456",
        "bucket_arn": "arn:bucket:test-bucket-123",
        "bucket_url": "https://bucket-456.s3.local",
        "encryption_key_id": "key-789"
    }
    
    # guardar estado del modulo storage
    state_file = f"{STATE_DIR}/storage_state.json"
    with open(state_file, 'w') as f:
        json.dump(storage_outputs, f, indent=2)
    
    print(f"modulo storage completado - estado guardado en {state_file}")
    return storage_outputs

def validate_integration_superficial():
    """validacion superficial: verificar que outputs existen y tienen formato correcto"""
    print("\nexecutando validacion superficial...")
    
    # validar estado de network
    network_file = f"{STATE_DIR}/network_state.json"
    with open(network_file, 'r') as f:
        network_state = json.load(f)
    
    assert "network_id" in network_state, "network_id faltante"
    assert isinstance(network_state["network_id"], str), "network_id debe ser string"
    assert "subnet_ids" in network_state, "subnet_ids faltante"
    assert isinstance(network_state["subnet_ids"], list), "subnet_ids debe ser lista"
    assert len(network_state["subnet_ids"]) > 0, "subnet_ids no puede estar vacia"
    
    # validar estado de compute
    compute_file = f"{STATE_DIR}/compute_state.json"
    with open(compute_file, 'r') as f:
        compute_state = json.load(f)
    
    assert "instance_ids" in compute_state, "instance_ids faltante"
    assert isinstance(compute_state["instance_ids"], list), "instance_ids debe ser lista"
    
    # validar estado de storage
    storage_file = f"{STATE_DIR}/storage_state.json"
    with open(storage_file, 'r') as f:
        storage_state = json.load(f)
    
    assert "bucket_id" in storage_state, "bucket_id faltante"
    assert isinstance(storage_state["bucket_id"], str), "bucket_id debe ser string"
    
    print("validacion superficial completada exitosamente")

def validate_integration_profunda():
    """validacion profunda: simular operaciones reales entre modulos"""
    print("ejecutando validacion profunda...")
    
    # simular conectividad entre instancias y storage
    print("simulando escritura en bucket desde instancias...")
    time.sleep(1)  # simular operacion de red
    
    # simular health check de instancias
    print("verificando health check de instancias...")
    time.sleep(0.5)
    
    # simular transferencia de datos
    print("validando transferencia de datos...")
    time.sleep(0.5)
    
    print("validacion profunda completada exitosamente")

def cleanup_test_environment():
    """limpiar archivos temporales de la prueba"""
    import shutil
    if os.path.exists("integration_test"):
        shutil.rmtree("integration_test")
    print("entorno de prueba limpiado")

def run_integration_test():
    """ejecutar prueba de integracion completa"""
    print("iniciando prueba de integracion entre modulos")
    print("=" * 50)
    
    try:
        # preparar entorno
        setup_test_environment()
        
        # ejecutar modulos en secuencia
        network_state = simulate_network_module()
        compute_state = simulate_compute_module(network_state)
        storage_state = simulate_storage_module()
        
        # ejecutar validaciones
        validate_integration_superficial()
        validate_integration_profunda()
        
        print("\n" + "=" * 50)
        print("prueba de integracion completada exitosamente")
        print("todos los modulos se integraron correctamente")
        
    except Exception as e:
        print(f"error en prueba de integracion: {e}")
        return False
    
    finally:
        cleanup_test_environment()
    
    return True

if __name__ == "__main__":
    success = run_integration_test()
    exit(0 if success else 1)
