terraform {

  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
  backend "azurerm" {
    resource_group_name  = "DevOps"
    storage_account_name = "tearraformstatefiles"
    container_name       = "tfstate"
    key                  = "remote.terraform.tfstate"
  }
}

provider "azurerm" {
    features {}
}

variable "imagebuild" {
  type = string
  description = "latest image builded"
}

resource "azurerm_resource_group" "DevOps_rg" {
  name = "DevOps-container"
  location = "eastus"
}

resource "azurerm_container_group" "appcg"{
  name = "it-project-backend"
  location = azurerm_resource_group.DevOps_rg.location
  resource_group_name = azurerm_resource_group.DevOps_rg.name
  
  ip_address_type = "public"
  dns_name_label = "it-projc-backend"
  os_type = "Linux"

  container {
    name = "it-project"
    image = "santithedev/it-project:${var.imagebuild}"
    cpu = "1"
    memory = "1"

    ports {
      port = "80"
      protocol = "TCP"
    }
  }
}