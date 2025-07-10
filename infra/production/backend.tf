terraform {
  backend "s3" {
    bucket       = "erhub-tf-state-prod"
    key          = "global/terraform.tfstate"
    region       = "ap-northeast-1"
    encrypt      = true
    use_lockfile = true
  }
}

resource "aws_s3_bucket" "state" {
  bucket = "erhub-tf-state-prod"

  tags = {
    Name = "erhub-tf-state-prod"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "state_sse" {
  bucket = aws_s3_bucket.state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "state_versioning" {
  bucket = aws_s3_bucket.state.id

  versioning_configuration {
    status = "Enabled"
  }
}
