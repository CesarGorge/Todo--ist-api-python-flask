from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    response = jsonify(todos)
    return response
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)  
    todos.append(request_body) 
    return jsonify(todos)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        deleted_todo = todos.pop(position)
        return jsonify(todos)
    else:
        return "Invalid position", 400
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3250, debug=True)