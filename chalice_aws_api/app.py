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


