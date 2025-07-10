resource "aws_subnet" "public" {
  for_each = toset(var.azs)

  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 4, index(var.azs, each.key))
  availability_zone = each.key

  tags = {
    Name = "${var.project}-${var.environment}-public-${each.key}"
  }
}

resource "aws_subnet" "protected" {
  for_each = toset(var.azs)

  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 4, length(var.azs) + index(var.azs, each.key))
  availability_zone = each.key

  tags = {
    Name = "${var.project}-${var.environment}-protected-${each.key}"
  }
}

resource "aws_subnet" "private" {
  for_each = toset(var.azs)

  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 4, length(var.azs) * 2 + index(var.azs, each.key))
  availability_zone = each.key

  tags = {
    Name = "${var.project}-${var.environment}-private-${each.key}"
  }
}

resource "aws_route_table_association" "public" {
  for_each       = aws_subnet.public
  subnet_id      = each.value.id
  route_table_id = aws_route_table.public.id
}
