# 📋 Gerenciador de Tarefas Distribuído (gRPC)

Projeto desenvolvido para a disciplina de **Sistemas Distribuídos I** (Engenharia da Computação - UNIVASF), ministrada pelo Prof. Jairson B. Rodrigues.

Sistema cliente-servidor distribuído para gerenciamento de tarefas (CRUD e conclusão), utilizando **Python**, **gRPC**, **Protocol Buffers**, persistência com **SQLAlchemy (SQLite)** e conteinerização com **Docker**.

---

## 📌 Requisitos

- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/)
- *(Opcional, apenas para execução sem Docker)*: Python 3.12+

---

## 🚀 Como Executar

### Via Docker (Recomendado)

1. **Construir as imagens:**
   ```bash
   docker compose build
   ```

2. **Iniciar o servidor:**
   ```bash
   docker compose up server
   ```

3. **Executar clientes interativos (abra abas/terminais separados):**
   ```bash
   # Cliente 1
   docker compose run --rm client1

   # Cliente 2 (para demonstrar clientes concorrentes com IPs distintos)
   docker compose run --rm client2
   ```
   > Pressione `Enter` ao iniciar o cliente para conectar ao host padrão (`server`).

4. **Encerrar containers:**
   ```bash
   docker compose down
   ```

---

### Execução Local (sem Docker)

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Gerar stubs do Protobuf/gRPC
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --pyi_out=. ./model.proto

# 3. Iniciar servidor
python server.py

# 4. Iniciar cliente (em outro terminal - use 'localhost' como host)
python client.py
```

---

## ⚙️ Métodos do Serviço (`TaskService`)

| RPC | Entrada | Saída | Descrição |
| :--- | :--- | :--- | :--- |
| `CreateTask` | `Task` | `TaskID` | Cria uma nova tarefa (retorna UUID) |
| `ListAllTasks` | `Void` | `TaskList` | Retorna todas as tarefas cadastradas |
| `UpdateTask` | `Task` | `TaskID` | Atualiza os dados de uma tarefa |
| `DeleteTask` | `TaskID` | `Void` | Remove uma tarefa por ID |
| `FinishTask` | `TaskID` | `TaskID` | Marca uma tarefa como finalizada |

---

## 👥 Autores

- Gabriel Cavalcanti Coelho
- Lucas Emanoel Gomes Ferraz
- Pedro Giovanni Ventura Viana Gonçalves
- Maria Bianca Vitoria Coelho Marinho de Lima 

