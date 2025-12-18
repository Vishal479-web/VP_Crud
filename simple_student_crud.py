#!/usr/bin/env python3
"""
Simple Student CRUD API using Flask and in-memory database
Run with: python simple_student_crud.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Any

app = Flask(__name__)
CORS(app)

# In-memory database
students_db: Dict[str, Dict[str, Any]] = {}

class Student:
    def __init__(self, name: str, college_id: str, age: int, course: str, year: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.college_id = college_id
        self.age = age
        self.course = course
        self.year = year
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "college_id": self.college_id,
            "age": self.age,
            "course": self.course,
            "year": self.year,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        student = cls(
            name=data["name"],
            college_id=data["college_id"],
            age=data["age"],
            course=data["course"],
            year=data["year"]
        )
        student.id = data["id"]
        student.created_at = datetime.fromisoformat(data["created_at"])
        student.updated_at = datetime.fromisoformat(data["updated_at"])
        return student

# CRUD Operations

@app.route('/api/students', methods=['GET'])
def get_students():
    """Get all students with pagination"""
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    skip = (page - 1) * limit

    students_list = list(students_db.values())[skip:skip + limit]
    total_count = len(students_db)

    return jsonify({
        "items": [Student.from_dict(s).to_dict() for s in students_list],
        "pagination_params": {
            "page": page,
            "limit": limit,
            "total": total_count
        }
    })

@app.route('/api/students/<student_id>', methods=['GET'])
def get_student(student_id: str):
    """Get a specific student by ID"""
    if student_id not in students_db:
        return jsonify({"error": "Student not found"}), 404

    student = Student.from_dict(students_db[student_id])
    return jsonify(student.to_dict())

@app.route('/api/students', methods=['POST'])
def create_student():
    """Create a new student"""
    try:
        data = request.get_json()

        # Basic validation
        required_fields = ["name", "college_id", "age", "course", "year"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        student = Student(
            name=data["name"],
            college_id=data["college_id"],
            age=data["age"],
            course=data["course"],
            year=data["year"]
        )

        students_db[student.id] = student.to_dict()

        return jsonify(student.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/<student_id>', methods=['PUT'])
def update_student(student_id: str):
    """Update an existing student"""
    try:
        if student_id not in students_db:
            return jsonify({"error": "Student not found"}), 404

        data = request.get_json()

        # Basic validation
        required_fields = ["name", "college_id", "age", "course", "year"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        student = Student(
            name=data["name"],
            college_id=data["college_id"],
            age=data["age"],
            course=data["course"],
            year=data["year"]
        )
        student.id = student_id
        student.created_at = datetime.fromisoformat(students_db[student_id]["created_at"])
        student.updated_at = datetime.utcnow()

        students_db[student_id] = student.to_dict()

        return jsonify(student.to_dict())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id: str):
    """Delete a student"""
    if student_id not in students_db:
        return jsonify({"error": "Student not found"}), 404

    del students_db[student_id]
    return '', 204

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "students_count": len(students_db),
        "timestamp": datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting Simple Student CRUD API...")
    print("📊 Database: In-memory (data persists during runtime)")
    print("🌐 Frontend URL: http://localhost:3000 (if running)")
    print("🔗 Backend API: http://localhost:8080")
    print("📋 API Endpoints:")
    print("   GET    /api/students           - List all students")
    print("   GET    /api/students/{id}      - Get student by ID")
    print("   POST   /api/students           - Create new student")
    print("   PUT    /api/students/{id}      - Update student")
    print("   DELETE /api/students/{id}      - Delete student")
    print("   GET    /api/health             - Health check")
    print("\nPress Ctrl+C to stop the server")

    app.run(debug=True, host='0.0.0.0', port=8080)
