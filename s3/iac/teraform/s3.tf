terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.35.1"
    }
  }
}

provider "aws" {
  # Configuration options
}

resource "aws_s3_bucket" "my_terraform_bucket_12871" {
  bucket = "my-terraform-bucket-12871"

  tags = {
    Name        = "my-terraform_bucket-12871"
    Environment = "Dev"
  }
}

