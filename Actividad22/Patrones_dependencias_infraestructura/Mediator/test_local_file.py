import pytest
import json
import os
from main import Mediator
from load_balancer import LoadBalancerFactoryModule
from local_file_module import LocalFileModule

def test_local_file_logging():
    """Verifica que el módulo de logging funcione correctamente"""
    # Crear mediador con logging habilitado
    mediator = Mediator(LoadBalancerFactoryModule(), enable_logging=True)
    result = mediator.build()
    
    # Verificar que se incluye el proveedor local
    assert "local" in result["terraform"]["required_providers"]
    assert result["terraform"]["required_providers"]["local"]["source"] == "hashicorp/local"
    
    # Verificar que existe el recurso local_file
    assert "local_file" in result["resource"]
    assert "creation_log" in result["resource"]["local_file"]
    
    # Verificar el contenido del log
    log_resource = result["resource"]["local_file"]["creation_log"]
    assert log_resource["filename"] == "local_file.log"
    
    # Parsear el contenido JSON del log
    log_content = json.loads(log_resource["content"])
    assert "creation_order" in log_content
    assert "timestamp" in log_content
    assert "total_resources" in log_content
    assert "dependency_chain" in log_content
    assert "terraform_provider" in log_content
    
    # Verificar el orden de creación
    expected_order = ["network", "network", "server", "firewall", "load_balancer"]
    assert log_content["creation_order"] == expected_order
    assert log_content["total_resources"] == 5
    assert log_content["terraform_provider"] == "local_file"

def test_local_file_module_standalone():
    """Verifica que LocalFileModule funcione de forma independiente"""
    creation_order = ["network", "server", "firewall"]
    log_module = LocalFileModule(creation_order=creation_order)
    
    result = log_module.build()
    
    # Verificar estructura básica
    assert "resource" in result
    assert "local_file" in result["resource"]
    assert "creation_log" in result["resource"]["local_file"]
    
    # Verificar contenido
    log_resource = result["resource"]["local_file"]["creation_log"]
    log_content = json.loads(log_resource["content"])
    
    assert log_content["creation_order"] == creation_order
    assert log_content["total_resources"] == 3
    assert "dependency_chain" in log_content
    assert log_content["dependency_chain"] == "network -> server -> firewall"

def test_mediator_logging_disabled():
    """Verifica que el mediador funcione sin logging"""
    mediator = Mediator(LoadBalancerFactoryModule(), enable_logging=False)
    result = mediator.build()
    
    # No debe incluir local_file cuando logging está deshabilitado
    assert "local_file" not in result["resource"]
    
    # Debe incluir todos los otros recursos
    assert "null_resource" in result["resource"]
    null_resources = result["resource"]["null_resource"]
    assert "network" in null_resources
    assert "server" in null_resources
    assert "firewall" in null_resources
    assert "load_balancer" in null_resources

def test_log_file_creation_after_apply():
    """Verifica que el archivo de log se crea después de terraform apply"""
    # Este test requiere que terraform apply haya sido ejecutado
    log_file_path = "local_file.log"
    
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as f:
            content = json.load(f)
        
        # Verificar contenido del archivo real
        assert "creation_order" in content
        assert "timestamp" in content
        assert "total_resources" in content
        assert "dependency_chain" in content
        
        # Verificar que el timestamp es una fecha válida ISO
        from datetime import datetime
        datetime.fromisoformat(content["timestamp"])  # Debe parsear sin error
        
        print(f"✓ Archivo de log verificado: {content}")
    else:
        pytest.skip("Archivo local_file.log no encontrado. Ejecutar terraform apply primero.")
