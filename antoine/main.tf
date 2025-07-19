provider "aws" {
  region = "us-east-1"
}

resource "aws_lambda_function" "reminder_lambda" {
  function_name = "ReminderLambda"
  runtime       = "python3.9"
  handler       = "lambda_function.lambda_handler"
  role          = aws_iam_role.lambda_exec.arn

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_execution_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Action": "sts:AssumeRole",
    "Principal": {
      "Service": "lambda.amazonaws.com"
    },
    "Effect": "Allow",
    "Sid": ""
  }]
}
EOF
}

resource "aws_lambda_permission" "allow_invoke" {
  statement_id  = "AllowExecutionFromTrigger"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.reminder_lambda.function_name
  principal     = "apigateway.amazonaws.com"  # or change this to the service you’ll use
}


