locals {
  nat_subnet_id = aws_subnet.public[var.azs[0]].id
}

data "aws_ssm_parameter" "al2" {
  name = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
}

resource "aws_security_group" "nat" {
  name   = "${var.project}-${var.environment}-nat-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [for sn in aws_subnet.protected : sn.cidr_block]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project}-${var.environment}-nat-sg"
  }
}

resource "aws_instance" "nat" {
  ami                         = data.aws_ssm_parameter.al2.value
  instance_type               = "t3.nano"
  subnet_id                   = local.nat_subnet_id
  associate_public_ip_address = true
  source_dest_check           = false

  vpc_security_group_ids = [aws_security_group.nat.id]

  tags = {
    Name = "${var.project}-${var.environment}-nat"
  }
}

resource "aws_eip" "nat" {
  instance = aws_instance.nat.id
  domain   = "vpc"
}

resource "aws_route_table" "protected" {
  for_each = aws_subnet.protected

  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project}-${var.environment}-protected-rt-${each.key}"
  }
}

resource "aws_route" "nat_route" {
  for_each = aws_route_table.protected

  route_table_id         = each.value.id
  destination_cidr_block = "0.0.0.0/0"
  network_interface_id   = aws_instance.nat.primary_network_interface_id
}

resource "aws_route_table_association" "protected" {
  for_each       = aws_subnet.protected
  subnet_id      = each.value.id
  route_table_id = aws_route_table.protected[each.key].id
}
