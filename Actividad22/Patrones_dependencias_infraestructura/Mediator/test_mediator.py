import pytest
from main import Mediator
from firewall import FirewallFactoryModule
from server import ServerFactoryModule
from network import NetworkFactoryModule

def test_mediator_order():
    """verifica que el orden incluya todos los recursos necesarios"""
    mediator = Mediator(FirewallFactoryModule())
    result = mediator.build()
    
    # el mediador actual crea 4 bloques debido a la duplicacion de network
    # esto demuestra el problema sin idempotencia
    assert len(mediator.order) == 4
    
    # verificar que el resultado final contenga los 3 recursos unicos
    resources = result["resource"]["null_resource"]
    assert "network" in resources
    assert "server" in resources  
    assert "firewall" in resources

def test_depends_on_fields():
    """verifica que los campos depends_on sean correctos"""
    mediator = Mediator(FirewallFactoryModule())
    result = mediator.build()
    
    resources = result["resource"]["null_resource"]
    
    # network no debe tener depends_on
    assert "depends_on" not in resources["network"]["triggers"]
    
    # server debe depender de network
    assert resources["server"]["triggers"]["depends_on"] == "null_resource.network"
    
    # firewall debe depender de server
    assert resources["firewall"]["triggers"]["depends_on"] == "null_resource.server"

def test_mediator_builds_valid_json():
    """verifica que el resultado sea JSON valido con estructura correcta"""
    mediator = Mediator(FirewallFactoryModule())
    result = mediator.build()
    
    # verificar estructura basica
    assert "terraform" in result
    assert "resource" in result
    assert "null_resource" in result["resource"]
    
    # verificar que tiene los 3 recursos esperados
    resources = result["resource"]["null_resource"]
    assert "network" in resources
    assert "server" in resources
    assert "firewall" in resources
