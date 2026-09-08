import grpc
import model_pb2
import model_pb2_grpc

tasks_mock = [
    model_pb2.Task(id=1, title="Fazer o Almoço", description="Cozinhar o arroz e assar o frango",is_completed=True, date="05/09/2026"),
    model_pb2.Task(id=2, title="Fazer a Janta", description="Cozinhar a macaxeira e fritar o ovo",is_completed=False, date="05/09/2026"),
    model_pb2.Task(id=3, title="Fazer o Café da Manhã", description="Fazer tapioca com ovo e um cafézinho",is_completed=True, date="06/09/2026"),
    model_pb2.Task(id=4, title="Comprar mantimentos", description="Ir ao supermercado comprar frutas, leite e ovos",is_completed=False, date="06/09/2026"),
    model_pb2.Task(id=5, title="Implementar RPC ListAll", description="Escrever a função ListAll no APIServicer do server.py",is_completed=True, date="06/09/2026"),
    model_pb2.Task(id=6, title="Implementar RPC FinishTask", description="Completar lógica para marcar tarefa como concluída no gRPC",is_completed=False, date="07/09/2026"),
    model_pb2.Task(id=7, title="Implementar RPC DeleteTask", description="Adicionar remoção de tarefas por ID no servidor",is_completed=False, date="07/09/2026"),
    model_pb2.Task(id=8, title="Limpar o apartamento", description="Varrer a sala, passar pano nos quartos e lavar a louça",is_completed=False, date="08/09/2026"),
    model_pb2.Task(id=9, title="Estudar Sistemas Distribuídos", description="Ler capítulo sobre RPC e gRPC do livro do Tanenbaum",is_completed=True, date="08/09/2026"),
    model_pb2.Task(id=10, title="Trocar lâmpada da cozinha", description="Comprar lâmpada LED de 12W e substituir a queimada",is_completed=True, date="09/09/2026"),
    model_pb2.Task(id=11, title="Criar testes unitários do client", description="Testar chamadas AddTask, ListAll e UpdateTask via client.py",is_completed=False, date="09/09/2026"),
    model_pb2.Task(id=12, title="Lavar roupas", description="Separar roupas escuras e bater na máquina de lavar",is_completed=False, date="10/09/2026"),
    model_pb2.Task(id=13, title="Pagar conta de internet", description="Acessar app do banco e quitar fatura com vencimento no dia 10",is_completed=True, date="10/09/2026"),
    model_pb2.Task(id=14, title="Revisar model.proto", description="Verificar tipos de dados e nomes dos métodos no protobuf",is_completed=True, date="10/09/2026"),
    model_pb2.Task(id=15, title="Atualizar documentação", description="Descrever passos de compilação e execução no README",is_completed=False, date="11/09/2026"),
    model_pb2.Task(id=16, title="Levar o pet ao veterinário", description="Consulta de rotina e vacinação anual do cachorro",is_completed=False, date="11/09/2026"),
    model_pb2.Task(id=17, title="Fazer backup do banco", description="Exportar dados da aplicação para arquivo JSON",is_completed=False, date="12/09/2026"),
    model_pb2.Task(id=18, title="Treino na academia", description="Treino de pernas e 30 minutos de cardio",is_completed=True, date="12/09/2026"),
    model_pb2.Task(id=19, title="Implementar RPC UpdateTask", description="Atualizar os dados de uma tarefa existente no servidor",is_completed=False, date="13/09/2026"),
    model_pb2.Task(id=20, title="Comprar remédios na farmácia", description="Comprar analgésico, antialérgico e curativos",is_completed=True, date="13/09/2026"),
    model_pb2.Task(id=21, title="Preparar apresentação", description="Montar slides explicando a arquitetura gRPC e fluxo de mensagens",is_completed=False, date="14/09/2026"),
    model_pb2.Task(id=22, title="Configurar tratamento de erros", description="Capturar exceções gRPC e is_completed= codes apropriados",is_completed=False, date="14/09/2026"),
    model_pb2.Task(id=23, title="Agendar revisão do carro", description="Marcar troca de óleo e alinhamento para o fim de semana",is_completed=False, date="15/09/2026"),
    model_pb2.Task(id=24, title="Regar as plantas", description="Molhar os vasos da varanda e do jardim de inverno",is_completed=True, date="15/09/2026"),
    model_pb2.Task(id=25, title="Simular concorrência", description="Disparar requisições simultâneas para testar o ThreadPoolExecutor",is_completed=False, date="16/09/2026")
]

# vou tentar deixar o terminal pronto
def menu():
    print(f'{"-=" * 30}')
    print(f"{" The best gRPC Todo App ":=^60}")
    print("""
        [1] Adicionar Tarefa
        [2] Listar Tarefas
        [3] Atualizar Tarefa
        [4] Excluir Tarefa
        [5] Concluir Tarefa
        [6] Sair
    """)
    print(f"{"-=" * 30}")



# definições da conexão
ip = "localhost"
port = "32768"

# ID INCREMENTAL HARDCODADO APENAS PARA TESTES (gohorse papai sao 4 da manha hihihi)
taskId = 1

# uma unica conexão
with grpc.insecure_channel(ip + ':' + port) as channel:
    stub = model_pb2_grpc.TaskServiceStub(channel)
    opt = 0
    while True:
        menu()
        try:
            opt = int(input("Escolha uma opção: "))
        except ValueError:
            print("Valor inválido! Digite um inteiro!")
            continue

        # aqui tratamos as opções
        match opt:
            case 1:
                taskTitle = input("Título: ")
                taskDescription = input("Descrição: ")
                taskDate = input("Data: ")

                new_task = model_pb2.Task(
                    id= taskId,
                    title = taskTitle,
                    description = taskDescription,
                    is_completed = False,
                    date = taskDate
                )
                response = stub.CreateTask(new_task)
                print(f"Tarefa criada com sucesso! ID: {taskId}")
                # incrementa o id!! 
                taskId += 1
            case 2:
                # deixa essa linha aqui se não o linter não entende o tipo
                taskList: model_pb2.TaskList
                taskList = stub.ListAllTasks(model_pb2.Void())
                # essa tabela aqui ficou fina falatu
                print("-" * 94)
                print(
                    f"{'ID':<4} | "
                    f"{'Título':<25} | "
                    f"{'Descrição':<25} | "
                    f"{'Data':<12} | "
                    f"{'Status':<14}"
                )
                print("-" * 94)
                for task in taskList.tasks:
                    # pra ficar bonitinho, sem isso fica 0 ou 1
                    status = "Finalizada" if task.is_completed == True else "Não finalizada"
                    # quebrado assim fica mais facil de mudar a ordem da exibição na tabela
                    print(
                        f"{task.id:<4} | "
                        f"{task.title:<25} | "
                        f"{task.description:<25} | "
                        f"{status:<15} | "
                        f"{task.date:<12}"
                    )
                print("-" * 94)
            case 6:
                print("Saindo...")

        if opt == 6:
            break