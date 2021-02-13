from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False },
        { "label": "My second task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()
    # decoded_object = json.loads(original_string)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    removed_todos = todos.pop(position)
    result = {"newList": todos, "removedList": removed_todos}
    return jsonify(result), 200


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)