import grpc
import model_pb2
import model_pb2_grpc

tasks_mock = [
    model_pb2.Task(id=1, title="Fazer o Almoço", description="Cozinhar o arroz e assar o frango", status=True, data="05/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=2, title="Fazer a Janta", description="Cozinhar a macaxeira e fritar o ovo", status=False, data="05/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=3, title="Fazer o Café da Manhã", description="Fazer tapioca com ovo e um cafézinho", status=True, data="06/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=4, title="Comprar mantimentos", description="Ir ao supermercado comprar frutas, leite e ovos", status=False, data="06/09/2026", responsible="Lucas"),
    model_pb2.Task(id=5, title="Implementar RPC ListAll", description="Escrever a função ListAll no APIServicer do server.py", status=True, data="06/09/2026", responsible="Lucas"),
    model_pb2.Task(id=6, title="Implementar RPC FinishTask", description="Completar lógica para marcar tarefa como concluída no gRPC", status=False, data="07/09/2026", responsible="Lucas"),
    model_pb2.Task(id=7, title="Implementar RPC DeleteTask", description="Adicionar remoção de tarefas por ID no servidor", status=False, data="07/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=8, title="Limpar o apartamento", description="Varrer a sala, passar pano nos quartos e lavar a louça", status=False, data="08/09/2026", responsible="Mariana"),
    model_pb2.Task(id=9, title="Estudar Sistemas Distribuídos", description="Ler capítulo sobre RPC e gRPC do livro do Tanenbaum", status=True, data="08/09/2026", responsible="Lucas"),
    model_pb2.Task(id=10, title="Trocar lâmpada da cozinha", description="Comprar lâmpada LED de 12W e substituir a queimada", status=True, data="09/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=11, title="Criar testes unitários do client", description="Testar chamadas AddTask, ListAll e UpdateTask via client.py", status=False, data="09/09/2026", responsible="Beatriz"),
    model_pb2.Task(id=12, title="Lavar roupas", description="Separar roupas escuras e bater na máquina de lavar", status=False, data="10/09/2026", responsible="Mariana"),
    model_pb2.Task(id=13, title="Pagar conta de internet", description="Acessar app do banco e quitar fatura com vencimento no dia 10", status=True, data="10/09/2026", responsible="Lucas"),
    model_pb2.Task(id=14, title="Revisar model.proto", description="Verificar tipos de dados e nomes dos métodos no protobuf", status=True, data="10/09/2026", responsible="Rafael"),
    model_pb2.Task(id=15, title="Atualizar documentação", description="Descrever passos de compilação e execução no README", status=False, data="11/09/2026", responsible="Beatriz"),
    model_pb2.Task(id=16, title="Levar o pet ao veterinário", description="Consulta de rotina e vacinação anual do cachorro", status=False, data="11/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=17, title="Fazer backup do banco", description="Exportar dados da aplicação para arquivo JSON", status=False, data="12/09/2026", responsible="Rafael"),
    model_pb2.Task(id=18, title="Treino na academia", description="Treino de pernas e 30 minutos de cardio", status=True, data="12/09/2026", responsible="Lucas"),
    model_pb2.Task(id=19, title="Implementar RPC UpdateTask", description="Atualizar os dados de uma tarefa existente no servidor", status=False, data="13/09/2026", responsible="Mariana"),
    model_pb2.Task(id=20, title="Comprar remédios na farmácia", description="Comprar analgésico, antialérgico e curativos", status=True, data="13/09/2026", responsible="Beatriz"),
    model_pb2.Task(id=21, title="Preparar apresentação", description="Montar slides explicando a arquitetura gRPC e fluxo de mensagens", status=False, data="14/09/2026", responsible="Rafael"),
    model_pb2.Task(id=22, title="Configurar tratamento de erros", description="Capturar exceções gRPC e retornar status codes apropriados", status=False, data="14/09/2026", responsible="Lucas"),
    model_pb2.Task(id=23, title="Agendar revisão do carro", description="Marcar troca de óleo e alinhamento para o fim de semana", status=False, data="15/09/2026", responsible="Gabriel"),
    model_pb2.Task(id=24, title="Regar as plantas", description="Molhar os vasos da varanda e do jardim de inverno", status=True, data="15/09/2026", responsible="Mariana"),
    model_pb2.Task(id=25, title="Simular concorrência", description="Disparar requisições simultâneas para testar o ThreadPoolExecutor", status=False, data="16/09/2026", responsible="Beatriz")
]


ip = "localhost"
port = "32768"
with grpc.insecure_channel(ip + ':' + port) as channel:
    stub = model_pb2_grpc.APIStub(channel)
    for task in tasks_mock:
        response = stub.AddTask(task)
        print(f'{response.id}')