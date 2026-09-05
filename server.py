from concurrent import futures
import grpc
import model_pb2
import model_pb2_grpc



# ---------------------------------------------------------------------------------------

ip = "localhost"
port = "32768"
lista = model_pb2.TaskList()


class API(model_pb2_grpc.APIServicer):

    def AddTask(self, request, context):
        lista.list.append(request)
        print(f"""
            ID = {request.id}
            Tittle= {request.title}
            Description = {request.description}
            Status = {request.status} | 
            Data = {request.data} | 
            Responsible = {request.responsible}""")
        return request

server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
model_pb2_grpc.add_APIServicer_to_server(API(), server)
server.add_insecure_port(ip + ':' + port)
server.start()
print("Server started, listening on " + ip + ':' + port)
server.wait_for_termination()