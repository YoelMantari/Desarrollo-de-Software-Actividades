from dependency import DependsOn

class LoadBalancerFactoryModule:
    def __init__(self, depends=None):
        self.depends = depends

    def build(self):
        triggers = {"port": "80"}
        if self.depends:
            triggers["depends_on"] = f"{self.depends.resource_type}.{self.depends.resource_id}"
        return {
            "resource": {
                "null_resource": {
                    "load_balancer": {"triggers": triggers}
                }
            }
        }

    def outputs(self):
        return DependsOn("null_resource", "load_balancer", {"port": "80"})
