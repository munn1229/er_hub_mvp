resource "aws_security_group" "alb_web_sg" {
  name   = "${var.project}-${var.environment}-alb-web-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = var.container_port_web
    to_port     = var.container_port_web
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project}-${var.environment}-alb-web-sg"
  }
}

resource "aws_lb" "web" {
  name               = "${var.project}-${var.environment}-alb-web"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_web_sg.id]
  subnets            = [for sn in aws_subnet.public : sn.id]

  tags = {
    Name = "${var.project}-${var.environment}-alb-web"
  }
}

resource "aws_lb_listener" "web_http" {
  load_balancer_arn = aws_lb.web.arn
  port              = var.container_port_web
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web.arn
  }
}

resource "aws_lb_target_group" "web" {
  name        = "${var.project}-${var.environment}-tg-web"
  port        = var.container_port_web
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"

  health_check {
    path                = "/"
    matcher             = "200-399"
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 3
  }
}

resource "aws_security_group" "alb_api_sg" {
  name   = "${var.project}-${var.environment}-alb-api-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    from_port   = var.container_port_api
    to_port     = var.container_port_api
    protocol    = "tcp"
    cidr_blocks = [for sn in aws_subnet.protected : sn.cidr_block]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project}-${var.environment}-alb-api-sg"
  }
}

resource "aws_lb" "api" {
  name               = "${var.project}-${var.environment}-alb-api"
  internal           = true
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_api_sg.id]
  subnets            = [for sn in aws_subnet.protected : sn.id]
  tags = {
    Name = "${var.project}-${var.environment}-alb-api"
  }
}

resource "aws_lb_listener" "api_http" {
  load_balancer_arn = aws_lb.api.arn
  port              = var.container_port_api
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.api.arn
  }
}

resource "aws_lb_target_group" "api" {
  name        = "${var.project}-${var.environment}-tg-api"
  port        = var.container_port_api
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"

  health_check {
    path                = "/health"
    matcher             = "200-399"
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 3
  }
}
