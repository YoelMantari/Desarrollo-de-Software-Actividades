#!/usr/bin/env python3
"""
script para generar reporte de cobertura de contratos iac
mide que porcentaje de outputs tienen tests asociados
"""
import json
import os
import glob

# definir esquema de contratos para cada modulo
CONTRACT_SCHEMA = {
    "network_module": {
        "outputs": {
            "network_id": {"required": True, "tested": True},
            "network_cidr": {"required": True, "tested": True},
            "subnet_ids": {"required": True, "tested": True},
            "route_table_id": {"required": False, "tested": False}
        }
    },
    "compute_module": {
        "outputs": {
            "instance_ids": {"required": True, "tested": True},
            "instance_ips": {"required": True, "tested": False},
            "security_group_id": {"required": True, "tested": True},
            "load_balancer_dns": {"required": False, "tested": False}
        }
    },
    "storage_module": {
        "outputs": {
            "bucket_id": {"required": True, "tested": True},
            "bucket_arn": {"required": True, "tested": True},
            "bucket_url": {"required": False, "tested": False},
            "encryption_key_id": {"required": False, "tested": False}
        }
    }
}

def calculate_coverage(module_name, outputs):
    """calcular cobertura de un modulo especifico"""
    total = len(outputs)
    tested = sum(1 for output in outputs.values() if output.get("tested", False))
    required_total = sum(1 for output in outputs.values() if output.get("required", False))
    required_tested = sum(1 for output in outputs.values() 
                         if output.get("required", False) and output.get("tested", False))
    
    overall_coverage = (tested / total * 100) if total > 0 else 0
    required_coverage = (required_tested / required_total * 100) if required_total > 0 else 0
    
    return {
        "module": module_name,
        "total_outputs": total,
        "tested_outputs": tested,
        "overall_coverage": round(overall_coverage, 1),
        "required_outputs": required_total,
        "required_tested": required_tested,
        "required_coverage": round(required_coverage, 1)
    }

def scan_test_files():
    """buscar archivos de test para identificar outputs validados"""
    test_files = glob.glob("*/test_*.py", recursive=True)
    validated_outputs = set()
    
    for test_file in test_files:
        try:
            with open(test_file, 'r') as f:
                content = f.read()
                # buscar patrones que indiquen validacion de outputs
                if "network_id" in content:
                    validated_outputs.add("network_id")
                if "subnet_ids" in content:
                    validated_outputs.add("subnet_ids")
                if "bucket_id" in content:
                    validated_outputs.add("bucket_id")
                # agregar mas patrones segun necesidad
        except Exception:
            continue
    
    return validated_outputs

def generate_report():
    """generar reporte completo de cobertura"""
    print("reporte de cobertura de contratos iac")
    print("=" * 50)
    
    total_coverage = 0
    module_count = 0
    
    for module_name, module_data in CONTRACT_SCHEMA.items():
        coverage_data = calculate_coverage(module_name, module_data["outputs"])
        
        print(f"\nmodulo: {coverage_data['module']}")
        print(f"outputs totales: {coverage_data['total_outputs']}")
        print(f"outputs con tests: {coverage_data['tested_outputs']}")
        print(f"cobertura general: {coverage_data['overall_coverage']}%")
        print(f"outputs requeridos: {coverage_data['required_outputs']}")
        print(f"requeridos con tests: {coverage_data['required_tested']}")
        print(f"cobertura requeridos: {coverage_data['required_coverage']}%")
        
        # evaluar estado del modulo
        if coverage_data['required_coverage'] >= 100:
            status = "excelente"
        elif coverage_data['required_coverage'] >= 80:
            status = "bueno"
        elif coverage_data['required_coverage'] >= 50:
            status = "aceptable"
        else:
            status = "necesita mejora"
        
        print(f"estado: {status}")
        
        total_coverage += coverage_data['overall_coverage']
        module_count += 1
    
    # resumen general
    average_coverage = total_coverage / module_count if module_count > 0 else 0
    print(f"\n{'=' * 50}")
    print(f"cobertura promedio: {round(average_coverage, 1)}%")
    print(f"modulos analizados: {module_count}")
    
    # recomendaciones
    print(f"\nrecomendaciones:")
    if average_coverage >= 80:
        print("- cobertura satisfactoria")
        print("- mantener tests actualizados")
    elif average_coverage >= 60:
        print("- agregar tests para outputs criticos")
        print("- revisar modulos con baja cobertura")
    else:
        print("- cobertura insuficiente")
        print("- priorizar tests para outputs requeridos")
        print("- establecer plan de mejora")

def update_schema_from_tests():
    """actualizar esquema basado en tests encontrados"""
    validated_outputs = scan_test_files()
    print(f"\noutputs validados encontrados en tests:")
    for output in sorted(validated_outputs):
        print(f"- {output}")

if __name__ == "__main__":
    generate_report()
    update_schema_from_tests()
