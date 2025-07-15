from dependency import DependsOn
import json
from datetime import datetime

class LocalFileModule:
    def __init__(self, creation_order=None, depends=None):
        self.creation_order = creation_order or []
        self.depends = depends

    def build(self):
        # Generar contenido JSON con el orden de creación
        log_content = {
            "creation_order": self.creation_order,
            "timestamp": datetime.now().isoformat(),
            "total_resources": len(self.creation_order),
            "dependency_chain": " -> ".join(self.creation_order),
            "terraform_provider": "local_file"
        }
        
        # Convertir a JSON formateado
        json_content = json.dumps(log_content, indent=2)
        
        return {
            "resource": {
                "local_file": {
                    "creation_log": {
                        "content": json_content,
                        "filename": "local_file.log"
                    }
                }
            }
        }

    def outputs(self):
        return DependsOn("local_file", "creation_log", {"filename": "local_file.log"})
