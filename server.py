from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc
import sistask_db

# ---------------------------------------------------------------------------------------

ip = "localhost"
port = "32768"

# Definição dos metodos
class TaskService(model_pb2_grpc.TaskServiceServicer):
    def CreateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        return sistask_db.Task.create(request.title, request.description, request.responsible, request.date)

    def ListAllTasks(self, request: model_pb2.Void, context) -> model_pb2.TaskList:
        return sistask_db.Task.get_all_tasks()

    def UpdateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        return sistask_db.Task.update(request)

    def DeleteTask(self, request: model_pb2.TaskID, context) -> model_pb2.Void:
        return sistask_db.Task.delete(request)

    def FinishTask(self, request: model_pb2.TaskID, context) -> model_pb2.TaskID:
        return sistask_db.Task.finish_task(request)

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