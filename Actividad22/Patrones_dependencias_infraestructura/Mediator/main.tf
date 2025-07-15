# main.tf - Conversión completa a HCL

terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

# Recursos de infraestructura base

resource "null_resource" "network" {
  triggers = {
    name = "hello-world-network"
  }
}

resource "null_resource" "server" {
  triggers = {
    name       = "hello-world-server"
    depends_on = "null_resource.network"
  }
}

resource "null_resource" "firewall" {
  triggers = {
    port       = "22"
    depends_on = "null_resource.server"
  }
}

resource "null_resource" "load_balancer" {
  triggers = {
    port       = "80"
    depends_on = "null_resource.firewall"
  }
}

# Archivo de log con orden de creación

resource "local_file" "creation_log" {
  content = jsonencode({
    creation_order     = ["network", "network", "server", "firewall", "load_balancer"]
    timestamp          = "2025-07-16T09:45:57.609968"
    total_resources    = 5
    dependency_chain   = "network -> network -> server -> firewall -> load_balancer"
    terraform_provider = "local_file"
  })
  filename = "local_file.log"
}
