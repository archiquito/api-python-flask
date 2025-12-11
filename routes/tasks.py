import sys
from pathlib import Path

# Adiciona o diretório pai ao caminho de importação
sys.path.insert(0, str(Path(__file__).parent.parent))

from flask import Blueprint, request, jsonify
from models.task import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

# Lista de tarefas (em produção seria um banco de dados)
tasks = []

@tasks_bp.route('', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas"""
    return jsonify({'tasks': [t.to_dict() for t in tasks], 'total_tasks': len(tasks)}), 200

@tasks_bp.route('', methods=['POST'])
def create_task():
    """Cria uma nova tarefa"""
    data = request.get_json()
    
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    title = data.get('title')
    description = data.get('description', '')
    
    # Calcula o próximo ID baseado no maior ID existente
    next_id = max([t.id for t in tasks], default=0) + 1
    
    new_task = Task(next_id, title, description)
    tasks.append(new_task)
    
    return jsonify({'message': 'Task created successfully', 'task': new_task.to_dict()}), 201

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Retorna uma tarefa específica"""
    task = next((t for t in tasks if t.id == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(task.to_dict()), 200

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente"""
    data = request.get_json()
    task = next((t for t in tasks if t.id == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task.update(
        title=data.get('title'),
        description=data.get('description'),
        completed=data.get('completed')
    )
    
    return jsonify({'message': 'Task updated successfully', 'task': task.to_dict()}), 200

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Deleta uma tarefa"""
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks = [t for t in tasks if t.id != task_id]
    
    return jsonify({'message': 'Task deleted successfully'}), 200
