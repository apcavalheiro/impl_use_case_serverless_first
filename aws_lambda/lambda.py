import json

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path = event['path']
    
    if http_method == 'GET' and path == '/todos':
        return get_todos()
    elif http_method == 'POST' and path == '/todos':
        return create_todo()
    elif http_method == 'GET' and path.startswith('/todos/'):
        return get_todo(path.split('/')[2])
    elif http_method == 'PUT' and path.startswith('/todos/'):
        return update_todo(path.split('/')[2])
    elif http_method == 'DELETE' and path.startswith('/todos/'):
        return delete_todo(path.split('/')[2])
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Route not found.')
        }

def get_todos():
    return {
        'statusCode': 200,
        'body': json.dumps({'todos': []})
    }

def create_todo():
    # Lógica para criar uma nova tarefa
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo created successfully'})
    }

def get_todo(todo_id):
    # Lógica para obter os detalhes de uma tarefa específica
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo not found'})
    }

def update_todo(todo_id):
    # Lógica para atualizar uma tarefa existente
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo updated successfully'})
    }

def delete_todo(todo_id):
    # Lógica para excluir uma tarefa
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Todo deleted successfully'})
    }
