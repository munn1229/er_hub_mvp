variable "aws_region" {
  type    = string
  default = "ap-northeast-1"
}

variable "environment" {
  type    = string
  default = "prod"
}

variable "project" {
  type    = string
  default = "erhub"
}

variable "owner" {
  type    = string
  default = "takeya-kitamura"
}

variable "azs" {
  type    = list(string)
  default = ["ap-northeast-1a", "ap-northeast-1c"]
}

variable "task_cpu_web" {
  type    = string
  default = "256"
}

variable "task_memory_web" {
  type    = string
  default = "512"
}

variable "task_cpu_api" {
  type    = string
  default = "256"
}

variable "task_memory_api" {
  type    = string
  default = "512"
}

variable "web_desired_count" {
  type    = number
  default = 1
}

variable "api_desired_count" {
  type    = number
  default = 1
}

variable "nginx_image_url" {
  type = string
}

variable "php_fpm_image_url" {
  type = string
}

variable "api_image_url" {
  type = string
}

variable "container_port_web" {
  type    = number
  default = 80
}

variable "container_port_api" {
  type    = number
  default = 8000
}
