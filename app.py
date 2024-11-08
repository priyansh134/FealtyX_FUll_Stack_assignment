from flask import Flask, jsonify, request
import requests
import threading

app = Flask(__name__)

# In-memory data store for students
students = {}
lock = threading.Lock()

# Helper function to validate student data
def validate_student_data(data):
    return (
        'name' in data and isinstance(data['name'], str) and
        'age' in data and isinstance(data['age'], int) and
        'email' in data and isinstance(data['email'], str)
    )

# CRUD Endpoints
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not validate_student_data(data):
        return jsonify({"error": "Invalid student data"}), 400

    with lock:
        student_id = len(students) + 1
        students[student_id] = {
            'id': student_id,
            'name': data['name'],
            'age': data['age'],
            'email': data['email']
        }
    return jsonify(students[student_id]), 201

@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(list(students.values())), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    if not validate_student_data(data):
        return jsonify({"error": "Invalid student data"}), 400

    with lock:
        student.update({
            'name': data['name'],
            'age': data['age'],
            'email': data['email']
        })
    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    with lock:
        if student_id not in students:
            return jsonify({"error": "Student not found"}), 404
        del students[student_id]
    return '', 204

# Ollama Integration - Generate Student Summary
@app.route('/students/<int:student_id>/summary', methods=['GET'])
def get_student_summary(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    # Ollama API setup - connecting to local Ollama service
    ollama_url = "http://localhost:11434/api/generate"  # Default localhost endpoint
    prompt = f"Generate a summary of student named {student['name']}, who is {student['age']} years old, and has the email {student['email']}."

    ollama_data = {
        "model": "llama3",  # Specify the Llama3.2 model as instructed
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(ollama_url, json=ollama_data)
        if response.status_code != 200:
            return jsonify({"error": "Failed to get summary from Ollama"}), response.status_code
        
        # Print full response for debugging
        print("Ollama API response:", response.json())
        
        # Adjust the response parsing based on actual structure
        return response.json(),200
        
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
