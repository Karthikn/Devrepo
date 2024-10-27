from flask import Flask, jsonify, abort

app = Flask(__name__)
#salman
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',#list of items
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# Get a specific task 
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:                             #ForLoop
        if task['id'] == task_id:
            return jsonify({'task': task})
    abort(404, description="Task not found")

if __name__ == '__main__':
    app.run(debug=True)

