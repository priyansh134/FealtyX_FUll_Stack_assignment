# Student Management API with Ollama Integration

This is a simple Flask-based REST API that allows you to manage student data (create, read, update, delete) and generate student summaries using the Ollama API. The API includes in-memory data storage for students and integrates with Ollama's llama3 model to generate personalized student profiles.

# Features

Create, Read, Update, Delete (CRUD): Add, update, retrieve, or delete student information.

Ollama Integration: Generate a personalized student profile summary based on student data using the Ollama API.

# Technologies

Flask: A lightweight WSGI web application framework for Python.

Ollama: A large language model used for generating summaries of student data.

Requests: To make HTTP requests to the Ollama API.

Threading: Used for locking and ensuring thread safety during CRUD operations.

# Installation


Python 3.6+

Flask

Requests

Ollama API (Ensure you have a running instance of the Ollama service on your machine)

# Steps to Run Locally

Clone this repository or download the code to your local machine.

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies:

pip install Flask requests



# Start Ollama API:
Ensure that you have Ollama running on your local machine at http://localhost:11434. You can start Ollama by running:

ollama start

# Run the Flask app:

python app.py

The application should now be running at http://127.0.0.1:5000.

# API Endpoints
# 1. Create a New Student
URL: /students (POST)

Request Body (JSON):


{

    "name": "John Doe",
    
    "age": 20,
    
    "email": "johndoe@example.com"
}

Response:

{

    "id": 1,
    
    "name": "John Doe",
    
    "age": 20,
    
    "email": "johndoe@example.com"
}

![image](https://github.com/user-attachments/assets/92bbd86c-1c30-4226-ba0a-1716c8518065)

# 2. Get All Students

URL: /students (GET)

Response (JSON Array):



[
    {
    
        "id": 1,
        
        "name": "John Doe",
        
        "age": 20,
        
        "email": "johndoe@example.com"
    }
]

![image](https://github.com/user-attachments/assets/b89c1bb5-ad39-468c-98d4-61e0761861f5)

# 3. Get a Specific Student by ID

URL: /students/<student_id> (GET)

Response (JSON):

{

    "id": 1,
    
    "name": "John Doe",
    
    "age": 20,
    
    "email": "johndoe@example.com"
}

![image](https://github.com/user-attachments/assets/bc508711-57b1-46a7-b051-87b33b832f3c)


# 4. Update a Student by ID
URL: /students/<student_id> (PUT)

Request Body (JSON):

{

    "name": "John Updated",
    
    "age": 21,
    
    "email": "john.doe@newemail.com"
}

Response:

{

    "id": 1,
    
    "name": "John Updated",
    
    "age": 21,
    
    "email": "john.doe@newemail.com"
}

![image](https://github.com/user-attachments/assets/72799c3a-a1e1-46f4-aec7-df6cf7386052)


# 5. Delete a Student by ID

URL: /students/<student_id> (DELETE)

Response: 204 No Content

![image](https://github.com/user-attachments/assets/ff7dfb1f-d656-4299-8a68-09f8ed60025d)


# 6. Generate Student Summary Using Ollama
URL: /students/<student_id>/summary (GET)

Response (JSON):

![image](https://github.com/user-attachments/assets/1dd5c2ab-bb58-4be3-8951-7010aa7b5fc1)

# Error Handling

Invalid or missing student data will result in a 400 Bad Request response.

Non-existing student ID will return a 404 Not Found error.

Ollama API issues will return a 500 Internal Server Error along with a relevant error message.
