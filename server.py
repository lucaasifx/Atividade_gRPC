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
    def CreateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        lista.tasks.append(request)
        print('Tarefa adicionada com sucesso!')
        print(f"""
            ID = {request.id}
            Tittle= {request.title}
            Description = {request.description}
            Status = {request.is_completed}
            Date = {request.date}
            Responsible = {request.responsible}
        """)
        return model_pb2.TaskID(id = request.id)

    def ListAllTasks(self, request: model_pb2.Void, context) -> model_pb2.TaskList:
        return lista

    def UpdateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        # Implementar
        return model_pb2.TaskID(id = request.id)

    def DeleteTask(self, request: model_pb2.TaskID, context) -> model_pb2.TaskID:
        # sem tratamento de erros por enquanto
        for task in lista.tasks:
            if task.id == request.id:
                lista.tasks.remove(task)
                break
        return model_pb2.TaskID(id = request.id)

    def FinishTask(self, request: model_pb2.TaskID, context) -> model_pb2.TaskID:
        # Implementar
        return model_pb2.TaskID(id = request.id)

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