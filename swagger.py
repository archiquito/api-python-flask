"""
Especificação Swagger/OpenAPI para a API de Tarefas
"""

swagger_spec = {
    "swagger": "2.0",
    "info": {
        "title": "Flask API - Gerenciamento de Tarefas",
        "description": "Uma API RESTful para gerenciar tarefas com operações CRUD completas",
        "version": "1.0.0",
        "contact": {
            "name": "archiquito",
            "url": "https://github.com/archiquito"
        }
    },
    "host": "127.0.0.1:8080",
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/json"],
    "paths": {
        "/tasks": {
            "get": {
                "summary": "Listar todas as tarefas",
                "operationId": "get_tasks",
                "responses": {
                    "200": {
                        "description": "Lista de tarefas retornada com sucesso",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "tasks": {
                                    "type": "array",
                                    "items": {"$ref": "#/definitions/Task"}
                                },
                                "total_tasks": {
                                    "type": "integer"
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Criar uma nova tarefa",
                "operationId": "create_task",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Objeto de tarefa a ser criado",
                        "required": True,
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "example": "Minha tarefa"
                                },
                                "description": {
                                    "type": "string",
                                    "example": "Descrição da tarefa"
                                }
                            },
                            "required": ["title"]
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Tarefa criada com sucesso",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"},
                                "task": {"$ref": "#/definitions/Task"}
                            }
                        }
                    },
                    "400": {
                        "description": "Dados inválidos (title é obrigatório)"
                    }
                }
            }
        },
        "/tasks/{id}": {
            "get": {
                "summary": "Obter uma tarefa específica",
                "operationId": "get_task",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "ID da tarefa"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Tarefa encontrada",
                        "schema": {"$ref": "#/definitions/Task"}
                    },
                    "404": {
                        "description": "Tarefa não encontrada"
                    }
                }
            },
            "put": {
                "summary": "Atualizar uma tarefa",
                "operationId": "update_task",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "ID da tarefa"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Dados a atualizar",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "description": {"type": "string"},
                                "completed": {"type": "boolean"}
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Tarefa atualizada com sucesso",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "message": {"type": "string"},
                                "task": {"$ref": "#/definitions/Task"}
                            }
                        }
                    },
                    "404": {
                        "description": "Tarefa não encontrada"
                    }
                }
            },
            "delete": {
                "summary": "Deletar uma tarefa",
                "operationId": "delete_task",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "type": "integer",
                        "required": True,
                        "description": "ID da tarefa"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Tarefa deletada com sucesso"
                    },
                    "404": {
                        "description": "Tarefa não encontrada"
                    }
                }
            }
        }
    },
    "definitions": {
        "Task": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "title": {
                    "type": "string",
                    "example": "Minha tarefa"
                },
                "description": {
                    "type": "string",
                    "example": "Descrição da tarefa"
                },
                "completed": {
                    "type": "boolean",
                    "example": False
                }
            },
            "required": ["id", "title", "description", "completed"]
        }
    }
}
