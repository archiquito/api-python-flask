# Flask API - Gerenciamento de Tarefas

Uma API RESTful construída com Flask para gerenciar tarefas. O projeto segue boas práticas de desenvolvimento com estrutura modular, blueprints e separação de responsabilidades.

## 🚀 Características

- ✅ API RESTful simples para estudo do python/flask
- ✅ Estrutura modular e escalável
- ✅ Tratamento robusto de erros
- ✅ IDs únicos que não se repetem ao deletar tarefas
- ✅ Documentação de endpoints
- ✅ Configurações separadas por ambiente (desenvolvimento/produção)

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)
- Git

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/archiquito/api-python-flask.git
cd api-python-flask
```

### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

### Opção 1: Executar no PowerShell (Windows) - Recomendado

```powershell
# Navegue até o diretório do projeto
cd C:\testesProgram\python\flask-api

# Ative o ambiente virtual
.\.venv\Scripts\activate

# Execute a aplicação
python app.py
```

### Opção 2: Executar no CMD (Windows)

```cmd
cd C:\testesProgram\python\flask-api
.venv\Scripts\activate.bat
python app.py
```

### Opção 3: Executar em macOS/Linux

```bash
cd api-python-flask
source .venv/bin/activate
python app.py
```

A API estará disponível em: **http://127.0.0.1:8080**

## 📖 Documentação Swagger/OpenAPI

Após iniciar a aplicação, acesse a documentação interativa do Swagger em:

**http://127.0.0.1:8080/swagger**

Nesta página você pode:

- ✅ Visualizar todos os endpoints
- ✅ Ver os modelos de dados
- ✅ Testar as requisições diretamente no navegador
- ✅ Copiar exemplos de código

## 📚 Endpoints da API

### 1. Listar todas as tarefas

```
GET /tasks
```

**Resposta (200 OK):**

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Flask",
      "description": "Aprender a criar APIs com Flask",
      "completed": false
    }
  ],
  "total_tasks": 1
}
```

### 2. Criar uma nova tarefa

```
POST /tasks
Content-Type: application/json
```

**Body:**

```json
{
  "title": "Estudar Flask",
  "description": "Aprender a criar APIs com Flask"
}
```

**Resposta (201 Created):**

```json
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Estudar Flask",
    "description": "Aprender a criar APIs com Flask",
    "completed": false
  }
}
```

### 3. Obter uma tarefa específica

```
GET /tasks/{id}
```

**Resposta (200 OK):**

```json
{
  "id": 1,
  "title": "Estudar Flask",
  "description": "Aprender a criar APIs com Flask",
  "completed": false
}
```

### 4. Atualizar uma tarefa

```
PUT /tasks/{id}
Content-Type: application/json
```

**Body:**

```json
{
  "title": "Estudar Flask avançado",
  "description": "Aprender APIs REST com Flask",
  "completed": true
}
```

**Resposta (200 OK):**

```json
{
  "message": "Task updated successfully",
  "task": {
    "id": 1,
    "title": "Estudar Flask avançado",
    "description": "Aprender APIs REST com Flask",
    "completed": true
  }
}
```

### 5. Deletar uma tarefa

```
DELETE /tasks/{id}
```

**Resposta (200 OK):**

```json
{
  "message": "Task deleted successfully"
}
```

## 🏗️ Estrutura do Projeto

```
flask-api/
├── app.py                  # Aplicação principal
├── config.py               # Configurações da app
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
├── .gitignore              # Arquivos ignorados pelo Git
├── models/                 # Modelos de dados
│   ├── __init__.py
│   └── task.py             # Modelo de Tarefa
├── routes/                 # Rotas/Blueprints
│   ├── __init__.py
│   └── tasks.py            # Rotas das tarefas
└── .venv/                  # Ambiente virtual (não commitado)
```

## 🔄 Como Funciona

### Geração de IDs

O sistema de IDs foi implementado para **nunca repetir**, mesmo ao deletar tarefas:

```python
# Calcula o próximo ID baseado no maior ID existente
next_id = max([t.id for t in tasks], default=0) + 1
```

**Exemplo:**

1. Cria tarefa 1 → ID = 1
2. Cria tarefa 2 → ID = 2
3. Deleta tarefa 1
4. Cria tarefa 3 → ID = 3 (não repete o ID 1)

## 📝 Exemplo de Uso com cURL

```bash
# Criar uma tarefa
curl -X POST http://127.0.0.1:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Minha tarefa","description":"Descrição"}'

# Listar tarefas
curl http://127.0.0.1:8080/tasks

# Obter tarefa específica
curl http://127.0.0.1:8080/tasks/1

# Atualizar tarefa
curl -X PUT http://127.0.0.1:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Tarefa atualizada","completed":true}'

# Deletar tarefa
curl -X DELETE http://127.0.0.1:8080/tasks/1
```

## 🚀 Implantação em Produção

Para usar em produção, altere a configuração em `app.py`:

```python
if __name__ == '__main__':
    app = create_app('production')  # Mude para production
    app.run(...)
```

E use um servidor WSGI como **Gunicorn**:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 app:create_app()
```

## 📦 Dependências

- **Flask** 2.3.0 - Framework web
- **Flask-SQLAlchemy** 3.1.1 - ORM para banco de dados
- **Flask-Cors** 3.0.10 - Suporte a CORS
- **Werkzeug** 2.3.0 - Utilitários WSGI

## 🐛 Troubleshooting

### Erro: `ModuleNotFoundError: No module named 'models'`

- Certifique-se de estar executando no diretório `flask-api`
- Verifique se o arquivo `models/__init__.py` existe

### Erro de permissão ao executar

- Tente com: `python app.py` ao invés de `.venv\Scripts\python.exe app.py`
- Ou desabilite o reloader: `use_reloader=False`

### Porta já em uso

- Altere a porta em `config.py`:

```python
PORT = 8081  # ou outra porta
```

## 📄 Licença

Este projeto está disponível sob a licença MIT.

## 👤 Autor

**archiquito** - [GitHub](https://github.com/archiquito)

## 📞 Suporte

Para reportar problemas ou sugerir melhorias, abra uma issue no repositório.
