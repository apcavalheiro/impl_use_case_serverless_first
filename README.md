# Capítulo de Estudo de Caso: Implementação de uma API REST Serverless

Neste capítulo, apresentamos um estudo de caso detalhado sobre a implementação de uma API REST para gerenciar uma lista de tarefas utilizando a estratégia Serverless First. Exploramos as vantagens dessa abordagem e realizamos uma análise comparativa entre três formas de implementação: utilizando o Chalice framework, AWS Lambda sem o Chalice e a abordagem tradicional. O objetivo é destacar as diferenças entre as abordagens e ressaltar a importância da estratégia Serverless First na criação de APIs escaláveis, flexíveis e de fácil gerenciamento.

## Cenário e Requisitos

O cenário de implementação envolve o desenvolvimento de uma API REST para gerenciar uma lista de tarefas (to-do list). Os requisitos para a API são:

1. Listar todas as tarefas disponíveis;
2. Criar uma nova tarefa;
3. Atualizar uma tarefa existente;
4. Excluir uma tarefa;
5. Recuperar uma tarefa específica por seu identificador.

Esses requisitos são comuns em muitas aplicações que exigem a gestão de tarefas ou atividades.

## Estratégia Serverless First

A estratégia Serverless First adotada neste estudo de caso enfatiza a utilização de arquiteturas serverless, onde a infraestrutura é gerenciada pelo provedor de serviços em nuvem e o desenvolvedor se concentra exclusivamente na lógica da aplicação. A escolha pela abordagem serverless visa explorar os benefícios de escalabilidade automática, gerenciamento simplificado e cobrança baseada no consumo real de recursos.

Ao adotar a estratégia Serverless First, priorizamos a utilização de AWS Lambda como plataforma de computação sem servidor. A AWS Lambda permite executar código sem a necessidade de provisionar servidores, pagando somente pelo tempo de execução e recursos consumidos durante a invocação da função. Isso proporciona uma escalabilidade automatizada, reduzindo custos e permitindo uma resposta mais rápida a picos de demanda.

## Implementação da API REST utilizando o Chalice framework

Nesta seção, é descrito o passo a passo para implementar a API REST utilizando o Chalice framework, que é um framework serverless fornecido pela AWS. O Chalice simplifica a criação e o gerenciamento de APIs serverless, permitindo que os desenvolvedores foquem na lógica do aplicativo em vez de se preocuparem com a configuração e a integração dos serviços.

### Passos de Implementação

1. Certifique-se de ter uma conta na AWS configurada.
2. Instale o Chalice executando o seguinte comando:
```
pip install chalice
```
3. Crie um novo projeto Chalice executando o seguinte comando:
```
chalice new-project
```
4. Selecione a opção API Rest.
5. Isso criará a estrutura do projeto. Edite o arquivo `app.py` com o código fornecido.

```python
# Código em Python com Chalice

from chalice import Chalice

app = Chalice(app_name='chalice_aws_api')

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return {'todos': todos}

@app.route('/todos', methods=['POST'])
def create_todo():
    request_body = app.current_request.json_body
    todos.append(request_body)
    return {'message': 'Todo created successfully'}

@app.route('/todos/{todo_id}', methods=['GET'])
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {'message': 'Todo not found'}, 404

@app.route('/todos/{todo_id}', methods=['PUT'])
def update_todo(todo_id):
    request_body = app.current_request.json_body
    for todo in todos:
        if todo['id'] == todo_id:
            todo['task'] = request_body['task']
            return {'message': 'Todo updated successfully'}
    return {'message': 'Todo not found'}, 404

@app.route('/todos/{todo_id}', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {'message': 'Todo deleted successfully'}
    return {'message': 'Todo not found'}, 404
```

6. Salve o arquivo e execute o seguinte comando para fazer o deploy da API:
```
chalice deploy
```
7. Aguarde enquanto o Chalice cria os recursos necessários na AWS Lambda e no API Gateway, e implanta a API. Após o deploy, você receberá uma URL de endpoint para a API.
8. Teste a API acessando a URL de endpoint fornecida no passo anterior. Faça uma solicitação GET para a rota `/todos` e você deverá receber uma resposta com a mensagem "todos: [ ]".

### Análise e Comparação

A abordagem utilizando o Chalice framework simplifica significativamente o processo de criação e implantação da API REST. Com algumas poucas linhas de código, o Chalice lida automaticamente com a configuração do AWS Lambda e do API Gateway, permitindo que o desenvolvedor se concentre na lógica da aplicação.

**Vantagens da Abordagem com Chalice:**

1. **Facilidade de Uso:** O Chalice for

nece uma sintaxe simples e intuitiva, facilitando o desenvolvimento da API REST.
2. **Implantação Rápida:** O processo de deploy é automatizado, agilizando o lançamento da API.

**Limitações da Abordagem com Chalice:**

1. **Dependência Específica da AWS:** O Chalice é uma ferramenta da AWS, o que significa que a API fica restrita ao ecossistema AWS.

## Implementação da API REST utilizando apenas o AWS Lambda

Nesta seção, descrevemos o processo de implementação da API REST utilizando apenas o AWS Lambda, sem o uso do Chalice framework.

### Passos de Implementação

1. Certifique-se de ter uma conta na AWS configurada.
2. Acesse o serviço AWS Lambda no console da AWS.
3. Crie uma nova função Lambda com o código fornecido.

```python
# Código em Python para AWS Lambda

import json

todos = []

def lambda_handler(event, context):
    http_method = event['httpMethod']
    if http_method == 'GET':
        return {'statusCode': 200, 'body': json.dumps({'todos': todos})}
    elif http_method == 'POST':
        request_body = json.loads(event['body'])
        todos.append(request_body)
        return {'statusCode': 200, 'body': json.dumps({'message': 'Todo created successfully'})}
    elif http_method == 'PUT':
        request_body = json.loads(event['body'])
        todo_id = event['pathParameters']['todo_id']
        for todo in todos:
            if todo['id'] == todo_id:
                todo['task'] = request_body['task']
                return {'statusCode': 200, 'body': json.dumps({'message': 'Todo updated successfully'})}
        return {'statusCode': 404, 'body': json.dumps({'message': 'Todo not found'})}
    elif http_method == 'DELETE':
        todo_id = event['pathParameters']['todo_id']
        for todo in todos:
            if todo['id'] == todo_id:
                todos.remove(todo)
                return {'statusCode': 200, 'body': json.dumps({'message': 'Todo deleted successfully'})}
        return {'statusCode': 404, 'body': json.dumps({'message': 'Todo not found'})}
```

4. Salve a função Lambda.
5. Crie um API Gateway e configure as rotas manualmente para a função Lambda.

### Análise e Comparação

A abordagem de implementação utilizando apenas o AWS Lambda oferece maior flexibilidade e controle total sobre a API e a infraestrutura. O desenvolvedor tem total liberdade para configurar o API Gateway de acordo com as necessidades específicas do projeto.

**Vantagens da Abordagem com AWS Lambda:**

1. **Flexibilidade:** O desenvolvedor pode personalizar a configuração do API Gateway e ter total controle sobre a implementação.
2. **Controle Total:** Não há dependência de um framework específico.

**Limitações da Abordagem com AWS Lambda:**

1. **Configuração Manual:** A configuração do API Gateway requer mais esforço e configuração manual em comparação com o Chalice framework.
2. **Gerenciamento de Recursos:** O desenvolvedor é responsável por gerenciar a escalabilidade e os recursos da aplicação.

## Implementação da API REST no Modelo Tradicional utilizando Flask

Nesta seção, descrevemos o processo de implementação da API REST no modelo tradicional utilizando o framework Flask.

### Passos de Implementação

1. Certifique-se de ter o Python e o pip instalados em seu ambiente local.
2. Instale o Flask executando o seguinte comando:
```
pip install Flask
```
3. Crie um novo arquivo Python com o código fornecido.

```python
# Código em Python com Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/todos', methods=['POST'])
def create_todo():
    request_body = request.get_json()
    todos.append(request_body)
    return jsonify({'message': 'Todo created successfully'})

@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    request_body = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['task'] = request_body['task']
            return jsonify({'message': 'Todo updated successfully'})
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return jsonify({'message': 'Todo deleted successfully'})
    return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run()
```

4. Salve o arquivo e execute o seguinte comando para iniciar o servidor local:
```
python app.py
```
5. O servidor Flask será executado localmente e estará acessível em `http://localhost:5000`. Teste as rotas com um cliente API, como o Postman.

### Análise e Comparação

A abordagem de implementação utilizando o Flask oferece controle total sobre o servidor e a API, sendo uma opção viável para projetos que requerem total personalização e gerenciamento local do ambiente de desenvolvimento.

**Vantagens da Abordagem com Flask:**

1. **Controle Total:** O desenvolvedor tem controle total sobre o ambiente de desenvolvimento e o servidor local.
2. **Teste Local:** É possível testar a API localmente antes de implantá-la em produção.

**Limitações da Abordagem com Flask:**

1. **Configuração e Gerenciamento Manual:** O desenvolvedor é responsável por configurar e gerenciar os servidores em produção.
2. **Escalabilidade:** O Flask requer configurações adicionais para lidar com a escalabilidade.

## Análise de Custos

A seguir, apresentamos uma análise de custos para cada abordagem de implementação, considerando o período de 12 e 24 meses de utilização na AWS.

### Abordagem com Chalice

| Abordagem           | Custo Mensal | Custo Anual  | Custo 2 Anos  |
|---------------------|--------------|--------------|---------------|
| Chalice (12 meses)  | $0 (Free Tier)| $0 (Free Tier)| $0 (Free Tier)|
| Chalice (24 meses)  | $0.10        | $1.20        | $2.40         |

### Abordagem com AWS Lambda (sem Chalice)

| Abordagem           | Custo Mensal | Custo

 Anual  | Custo 2 Anos  |
|---------------------|--------------|--------------|---------------|
| Lambda (12 meses)   | $0.20        | $2.40        | $4.80         |
| Lambda (24 meses)   | $0.20        | $2.40        | $4.80         |

### Abordagem com Flask (Tradicional)

| Abordagem           | Custo Mensal | Custo Anual  | Custo 2 Anos  |
|---------------------|--------------|--------------|---------------|
| Servidor (12 meses) | $10.00       | $120.00      | $240.00       |
| Servidor (24 meses) | $10.00       | $120.00      | $240.00       |

## Conclusão

A estratégia Serverless First proporciona uma maneira mais eficiente e econômica de implementar APIs REST escaláveis e de fácil gerenciamento. O uso do Chalice framework simplifica a criação e implantação da API na AWS Lambda e no API Gateway, reduzindo o esforço de configuração.

Por outro lado, a implementação utilizando apenas o AWS Lambda e o modelo tradicional com Flask oferecem maior flexibilidade e controle, sendo ideais para projetos que requerem personalização total da infraestrutura.

A escolha da abordagem de implementação depende das necessidades específicas do projeto, do orçamento disponível e da expertise da equipe de desenvolvimento. No entanto, a adoção da estratégia Serverless First é uma tendência crescente devido aos benefícios de escalabilidade automática e gerenciamento simplificado.

Esperamos que este estudo de caso tenha sido útil para compreender as diferentes abordagens e possibilitar uma tomada de decisão informada ao implementar APIs REST com a AWS Lambda.
```