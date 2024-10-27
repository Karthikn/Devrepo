from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "salman",
        "feedback": 2
    }
]
#add 123
@app.route('/addstudents', methods=['POST'])
def add_students():
    new_student = request.get_json()

    # Use max function to find the maximum id in the list and increment it by 1
    if students:
        new_student["id"] = max(student["id"] for student in students) + 1
    else:
        new_student["id"] = 1

    students.append(new_student)

    return jsonify(new_student), 201
#blah 

# PUT method to update a student's information
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    update_data = request.get_json()
    for student in students:
        if student["id"] == student_id:
            student.update(update_data)
            return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@app.route('/addtaskid',methods=['POST'])
def add_tasksid():
    lenght=len(tasks)+1
    task=request.json
    task["id"]=lenght
    tasks.append(task)
    return tasks #returns list

if __name__ == '__main__':
    app.run(debug=True, port=5000)
