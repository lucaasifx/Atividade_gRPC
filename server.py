from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc



# ---------------------------------------------------------------------------------------

ip = "localhost"
port = "32768"
lista = model_pb2.TaskList()

# Definição dos metodos
class TaskService(model_pb2_grpc.TaskServiceServicer):
    def CreateTask(self, request: model_pb2.Task, context) -> model_pb2.Task:
        lista.tasks.append(request)
        print('Tarefa adicionada com sucesso!')
        print(f"""
            ID = {request.id}
            Tittle= {request.title}
            Description = {request.description}
            Status = {request.is_completed}
            Date = {request.date}
        """)
        return request

    def ListAllTasks(self, request, context):
        return lista

    def DeleteTask(self, request: model_pb2.TaskID, context) -> model_pb2.Void:
        # sem tratamento de erros por enquanto
        for task in lista.tasks:
            if task.id == request.id:
                lista.tasks.remove(task)
                break
        return model_pb2.Void()

    



# Configurações do servidor
def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    model_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port(ip + ':' + port)
    server.start()
    print("Server started, listening on " + ip + ':' + port)
    server.wait_for_termination()

# Para subir o servidor
server()