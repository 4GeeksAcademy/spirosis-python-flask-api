from flask import Flask
app = Flask(__name__)

from flask import Flask, jsonify
from flask import request

todos = [
  { "label" : "Myfirst task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', method=['DELETE'])
def delete_todo(position):
   print("this is the position to delete: ", position)
   todos.remove(todos[position])
   return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)