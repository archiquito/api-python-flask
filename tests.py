import pytest
import requests

BASE_URL = "http://localhost:8080"
tasks = []

def test_create_task():
    new_data = {"title": "Test Task", "description": "This is a test task."}
    response = requests.post(f"{BASE_URL}/tasks", json=new_data)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data['task']
    tasks.append(data['task'])

def test_get_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert 'tasks' in data

def test_update_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert 'tasks' in data
    tasks = data['tasks']
    assert len(tasks) > 0
    task_id = tasks[0]['id']
    update_data = {"title": "Updated Test Task", "completed": True}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data['message'] == 'Task updated successfully'

def test_delete_task():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert 'tasks' in data
    tasks = data['tasks']
    assert len(tasks) > 0
    task_id = tasks[0]['id']
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data['message'] == 'Task deleted successfully'
    