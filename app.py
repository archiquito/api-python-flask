"""
Aplicação Flask para Gerenciamento de Tarefas
Estrutura organizada com blueprints e configuração modular
"""

from flask import Flask
from config import config
from routes.tasks import tasks_bp

def create_app(config_name='development'):
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Carrega configurações
    app.config.from_object(config[config_name])
    
    # Registra blueprints
    app.register_blueprint(tasks_bp)
    
    @app.route('/')
    def index():
        """Rota inicial da API"""
        return {
            'message': 'Bem-vindo à API de Tarefas',
            'version': '1.0.0',
            'endpoints': {
                'GET /tasks': 'Lista todas as tarefas',
                'POST /tasks': 'Cria uma nova tarefa',
                'GET /tasks/<id>': 'Retorna uma tarefa específica',
                'PUT /tasks/<id>': 'Atualiza uma tarefa',
                'DELETE /tasks/<id>': 'Deleta uma tarefa'
            }
        }, 200
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
