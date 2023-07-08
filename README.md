# impl_use_case_serverless_first
Implementação de uma API REST utilizando o padrão arquitetural Serverless First. Exploraremos as vantagens dessa abordagem e analisaremos a viabilidade de três formas de implementação: utilizando o Chalice framework, AWS Lambda sem o Chalice e a abordagem tradicional


|    | Chalice framework                          | AWS Lambda sem o Chalice        | Modelo Tradicional                   |
|----|--------------------------------------------|---------------------------------|--------------------------------------|
| 1. | Implantação automática da infraestrutura    | Configuração manual de recursos | Necessidade de configuração manual de recursos |
| 2. | Curva de aprendizado menor                   | Curva de aprendizado intermediária | Curva de aprendizado intermediária |
| 3. | Configuração simplificada da API REST        | Configuração manual do API Gateway | Controle total sobre a configuração da API |
| 4. | Facilidade de integração com serviços da AWS | Integração com serviços da AWS   | Integração com serviços da AWS |
| 5. | Escalabilidade automática e sob demanda      | Escalabilidade automática e sob demanda | Necessidade de configuração manual de escalabilidade |
| 6. | Facilidade de gerenciamento da API REST      | Necessidade de gerenciamento manual dos recursos | Necessidade de gerenciamento manual dos recursos |
| 7. | Uso simplificado de certificados SSL/TLS     | Configuração manual de certificados SSL/TLS | Necessidade de configuração manual de certificados SSL/TLS |
| 8. | Conhecimentos necessários em infraestrutura mínimos | Conhecimentos necessários em infraestrutura intermediários | Conhecimentos necessários em infraestrutura intermediários |

A tabela destaca as principais diferenças entre as três formas de implementação: Chalice framework, AWS Lambda sem o Chalice e o modelo tradicional. Cada abordagem possui suas próprias características e requisitos de configuração, afetando aspectos como facilidade de implantação, escalabilidade, gerenciamento e necessidade de conhecimentos em infraestrutura. 

