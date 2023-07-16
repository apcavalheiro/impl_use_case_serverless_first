from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/todos', methods=['POST'])
def create_todo():
    request_data = request.get_json()
    todos.append(request_data)
    return jsonify({'message': 'Todo created successfully'})

@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo)
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    request_data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['task'] = request_data['task']
            return jsonify({'message': 'Todo updated successfully'})
    return jsonify({'message': 'Todo not found'}), 404

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return jsonify({'message': 'Todo deleted successfully'})
    return jsonify({'message': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run()
