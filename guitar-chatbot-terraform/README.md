+-------------------+
|   User's Browser  |
|  (Frontend UI)    |
+--------+----------+
         |
         v
+--------+----------+
|   API Gateway     |
| (HTTPS Endpoint)  |
+--------+----------+
         |
         v
+--------+----------+
|    AWS Lambda     |
| (Chatbot Logic)   |
+--------+----------+
         |
         v
+-------------------+
|  Terraform Config |
| (Manages Infra)   |
+-------------------+
