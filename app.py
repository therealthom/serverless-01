from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista en memoria para almacenar tareas
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/task', methods=['POST'])
def add_task():
    task = request.json.get('task', '')
    if task:
        tasks.append(task)
        return jsonify({'message': 'Task added successfully!'}), 200
    else:
        return jsonify({'message': 'No task provided'}), 400

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully!'}), 200
    else:
        return jsonify({'message': 'Invalid task ID'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
