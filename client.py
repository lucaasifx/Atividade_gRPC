import grpc
import model_pb2
import model_pb2_grpc

task = model_pb2.Task(
    id = 3,
    title = "Fazer o Café da Manhã",
    description = "Fazer tapioca com ovo e um cafézinho",
    status = False,
    data = "06/09/2026",
    responsible = "Gabriel"
    )

ip = "localhost"
port = "32768"
with grpc.insecure_channel(ip + ':' + port) as channel:
    stub = model_pb2_grpc.APIStub(channel)
    response = stub.AddTask(task)
    print(f'{response.id}')