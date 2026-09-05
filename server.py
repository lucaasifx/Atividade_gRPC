from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc

# ---------------- Simulação de uma base de dados para testar o servidor ----------------
class Task:
    id: int
    title: str
    description: str
    status: bool
    data: str
    responsible: str

    def __init__(self, id: int, title: str, description: str, status: bool, data: str, responsible: str):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.data = data
        self.responsible = responsible

    def __str__(self):
        return f"ID: {self.id}\nTITLE: {self.title}\nDESCRIPTION: {self.description}\nSTATUS: {self.status}\nDATA: {self.data}\nRESPONSIBLE: {self.responsible}\n"

    def finish(self):
        self.status = True

task_list = [
    Task(1, "Fazer o Almoço", "Cozinhar o arroz e assar o frango", False, "05/09/2026", "Gabriel"),
    Task(2, "Fazer a Janta", "Cozinhar a macaxeira e fritar o ovo", False, "05/09/2026", "Gabriel")
]

def ListAll():
    for task in task_list:
        print(task)

def UpdateTask(new_task : Task):
    for index, old_task in enumerate(task_list):
        if(old_task.id == new_task.id):
            task_list[index] = new_task

def DeleteTask(id: int):
    for task in task_list:
        if(task.id == id):
            task_list.remove(task)

def FinishTask(id: int):
    for task in task_list:
        if(task.id == id):
            task.finish()


# ---------------------------------------------------------------------------------------

ip = "localhost"
port = "32768"

class API(model_pb2_grpc.APIServicer):

    def AddTask(self, request, context):
        task_list.append(Task(request.id, request.title, request.description, request.status, request.data, request.responsible))
        print(task_list[2]) # FUNCIONOU CARAAAAAAAI
        return request

server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
model_pb2_grpc.add_APIServicer_to_server(API(), server)
server.add_insecure_port(ip + ':' + port)
server.start()
print("Server started, listening on " + ip + ':' + port)
server.wait_for_termination()