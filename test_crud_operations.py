#!/usr/bin/env python3
"""
Test script to demonstrate CRUD operations on the Student API
Run with: python test_crud_operations.py
"""

import requests
import json
import time

BASE_URL = "http://localhost:8080/api"

def test_health():
    """Test health check endpoint"""
    print("🔍 Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health Check: {data['status']}")
            print(f"📊 Current students count: {data['students_count']}")
            return True
        else:
            print(f"❌ Health Check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health Check error: {e}")
        return False

def test_create_student():
    """Test creating a new student"""
    print("\n📝 Testing Create Student...")

    student_data = {
        "name": "John Doe",
        "college_id": "12345",
        "age": 20,
        "course": "Computer Science",
        "year": 2
    }

    try:
        response = requests.post(f"{BASE_URL}/students", json=student_data)
        if response.status_code == 201:
            data = response.json()
            print(f"✅ Student created successfully!")
            print(f"🆔 ID: {data['id']}")
            print(f"👤 Name: {data['name']}")
            print(f"🏫 College ID: {data['college_id']}")
            return data['id']
        else:
            print(f"❌ Create failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Create error: {e}")
        return None

def test_get_students():
    """Test getting all students"""
    print("\n📋 Testing Get All Students...")
    try:
        response = requests.get(f"{BASE_URL}/students")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Retrieved {len(data['items'])} students")
            for student in data['items']:
                print(f"  🆔 {student['id'][:8]}... - {student['name']} ({student['course']})")
            return data['items']
        else:
            print(f"❌ Get all failed: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Get all error: {e}")
        return []

def test_get_student_by_id(student_id):
    """Test getting a specific student"""
    print(f"\n🔍 Testing Get Student by ID: {student_id[:8]}...")
    try:
        response = requests.get(f"{BASE_URL}/students/{student_id}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Student found: {data['name']}")
            print(f"  📚 Course: {data['course']}")
            print(f"  🎓 Year: {data['year']}")
            return data
        else:
            print(f"❌ Get by ID failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ Get by ID error: {e}")
        return None

def test_update_student(student_id):
    """Test updating a student"""
    print(f"\n✏️  Testing Update Student: {student_id[:8]}...")

    update_data = {
        "name": "John Smith",
        "college_id": "12345",
        "age": 21,
        "course": "Computer Science",
        "year": 3
    }

    try:
        response = requests.put(f"{BASE_URL}/students/{student_id}", json=update_data)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Student updated successfully!")
            print(f"👤 New name: {data['name']}")
            print(f"🎓 New year: {data['year']}")
            return True
        else:
            print(f"❌ Update failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Update error: {e}")
        return False

def test_delete_student(student_id):
    """Test deleting a student"""
    print(f"\n🗑️  Testing Delete Student: {student_id[:8]}...")
    try:
        response = requests.delete(f"{BASE_URL}/students/{student_id}")
        if response.status_code == 204:
            print("✅ Student deleted successfully!")
            return True
        else:
            print(f"❌ Delete failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Delete error: {e}")
        return False

def create_sample_students():
    """Create multiple sample students"""
    print("\n🌱 Creating Sample Students...")

    students = [
        {"name": "Alice Johnson", "college_id": "67890", "age": 19, "course": "Mathematics", "year": 1},
        {"name": "Bob Wilson", "college_id": "54321", "age": 22, "course": "Physics", "year": 4},
        {"name": "Carol Brown", "college_id": "98765", "age": 21, "course": "Chemistry", "year": 3},
    ]

    created_ids = []
    for student in students:
        try:
            response = requests.post(f"{BASE_URL}/students", json=student)
            if response.status_code == 201:
                data = response.json()
                created_ids.append(data['id'])
                print(f"✅ Created: {student['name']}")
            else:
                print(f"❌ Failed to create: {student['name']}")
        except Exception as e:
            print(f"❌ Error creating {student['name']}: {e}")

    return created_ids

def main():
    """Main test function"""
    print("🧪 Testing Student CRUD API")
    print("=" * 50)

    # Test health check
    if not test_health():
        print("❌ API is not running. Please start the server first with: python simple_student_crud.py")
        return

    # Create sample students
    sample_ids = create_sample_students()

    # Test CRUD operations
    if sample_ids:
        student_id = sample_ids[0]

        # Read all students
        test_get_students()

        # Read specific student
        test_get_student_by_id(student_id)

        # Update student
        test_update_student(student_id)

        # Verify update
        test_get_student_by_id(student_id)

        # Delete student
        test_delete_student(student_id)

        # Verify deletion - should show one less student
        test_get_students()

    print("\n" + "=" * 50)
    print("🎉 CRUD Operations Test Complete!")
    print("\n💡 You can now:")
    print("   • Use any REST client (Postman, Insomnia, etc.) to test the API")
    print("   • Access the API at: http://localhost:8080/api/students")
    print("   • Data is stored in memory and persists during server runtime")

if __name__ == "__main__":
    main()
