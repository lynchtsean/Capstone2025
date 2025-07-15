output "invoke_url" {
  value = "${aws_api_gateway_deployment.deployment.invoke_url}/${aws_api_gateway_resource.chatbot_resource.path_part}"
}
