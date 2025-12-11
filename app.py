"""
Aplicação Flask para Gerenciamento de Tarefas
Estrutura organizada com blueprints e configuração modular
"""

from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from config import config
from routes.tasks import tasks_bp
from swagger import swagger_spec

def create_app(config_name='development'):
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Carrega configurações
    app.config.from_object(config[config_name])
    
    # Registra blueprints
    app.register_blueprint(tasks_bp)
    
    # Configurar Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = '/swagger.json'
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': 'Flask API - Gerenciamento de Tarefas'}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # Rota para servir a especificação Swagger
    @app.route('/swagger.json')
    def swagger_json():
        return jsonify(swagger_spec)
    
    @app.route('/')
    def index():
        """Rota inicial da API"""
        return {
            'message': 'Bem-vindo à API de Tarefas',
            'version': '1.0.0',
            'documentation': 'http://127.0.0.1:8080/swagger',
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
