terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "resource_group_name" {
  description = "Nome do Resource Group"
  type        = string
  default     = "rg-exemplo-terraform"
}

variable "location" {
  description = "Regiao do Azure"
  type        = string
  default     = "East US"
}

resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    environment = "dev"
    managed_by  = "terraform"
  }
}

output "resource_group_id" {
  description = "ID do Resource Group criado"
  value       = azurerm_resource_group.rg.id
}
