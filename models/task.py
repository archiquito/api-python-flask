class Task:
    """Modelo de Tarefa com métodos otimizados"""
    
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        """Marca a tarefa como concluída"""
        self.completed = True

    def update(self, title=None, description=None, completed=None):
        """Atualiza os dados da tarefa"""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if completed is not None:
            self.completed = completed

    def to_dict(self):
        """Converte a tarefa para um dicionário"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }
    
    def __repr__(self):
        """Representação em string da tarefa"""
        return f"<Task {self.id}: {self.title}>"