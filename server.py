from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc
import sistask_db

# ---------------------------------------------------------------------------------------

ip = "0.0.0.0"
port = "32768"

# cola .proto
# service TaskService {
#   rpc CreateTask (Task) returns (TaskID); feito
#   rpc ListAllTasks (Void) returns (TaskList); feito
#   rpc UpdateTask (Task) returns (TaskID); feito
#   rpc DeleteTask (TaskID) returns (Void); feito
#   rpc FinishTask (TaskID) returns (TaskID); feito
# }

# Definição dos metodos
class TaskService(model_pb2_grpc.TaskServiceServicer):
    def CreateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        print(f"[{context.peer()}] CreateTask: {request.title}")
        return sistask_db.Task.create(request.title, request.description, request.responsible, request.date)

    def ListAllTasks(self, request: model_pb2.Void, context) -> model_pb2.TaskList:
        print(f"[{context.peer()}] ListAllTasks")
        return sistask_db.Task.get_all_tasks()

    def UpdateTask(self, request: model_pb2.Task, context) -> model_pb2.TaskID:
        print(f"[{context.peer()}] UpdateTask: {request.id}")
        return sistask_db.Task.update(request)

    def DeleteTask(self, request: model_pb2.TaskID, context) -> model_pb2.Void:
        print(f"[{context.peer()}] DeleteTask: {request.id}")
        return sistask_db.Task.delete(request)

    def FinishTask(self, request: model_pb2.TaskID, context) -> model_pb2.TaskID:
        print(f"[{context.peer()}] FinishTask: {request.id}")
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