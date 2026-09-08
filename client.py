import grpc
import model_pb2
import model_pb2_grpc

# Definições da conexão
ip = "localhost"
port = "32768"

def menu():
    print(f'{"-=" * 30}')
    print(f"{" The best gRPC Todo App ":=^60}")
    print("""
        [1] Adicionar Tarefa
        [2] Listar Tarefas
        [3] Atualizar Tarefa
        [4] Excluir Tarefa
        [5] Concluir Tarefa
        [0] Sair
    """)
    print(f"{"-=" * 30}")

# Uma única conexão
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
        # Aqui tratamos as opções
        match opt:
            case 1:
                taskTitle = input("Título: ")
                taskDescription = input("Descrição: ")
                taskDate = input("Data: ")
                taskResponsible = input("Responsável: ")

                new_task = model_pb2.Task(
                    id= "1",
                    title = taskTitle,
                    description = taskDescription,
                    is_completed = False,
                    date = taskDate,
                    responsible = taskResponsible
                )

                response = stub.CreateTask(new_task)
                print(f"Tarefa criada com sucesso! ID: {response.id}")
            case 2:
                # deixa essa linha aqui se não o linter não entende o tipo
                taskList: model_pb2.TaskList
                taskList = stub.ListAllTasks(model_pb2.Void())
                # essa tabela aqui ficou fina falatu
                print("-" * 136)
                print(
                    f"{'ID':<36} | "
                    f"{'Título':<25} | "
                    f"{'Descrição':<25} | "
                    f"{'Data':<10} | "
                    f"{'Status':<14} | "
                    f"{'Responsável':<25}"
                )
                print("-" * 136)
                for task in taskList.tasks:
                    # pra ficar bonitinho, sem isso fica 0 ou 1
                    status = "Finalizada" if task.is_completed == True else "Não finalizada"
                    # quebrado assim fica mais facil de mudar a ordem da exibição na tabela
                    print(
                        f"{task.id:<36} | "
                        f"{task.title:<25} | "
                        f"{task.description:<25} | "
                        f"{task.date:<10} | "
                        f"{status:<14} | "
                        f"{task.responsible:<25}"
                    )
                print("-" * 136)
            case 3:
                taskID = input("ID: ")
                taskTitle = input("Título: ")
                taskDescription = input("Descrição: ")
                taskDate = input("Data: ")
                taskResponsible = input("Responsável: ")

                updated_task = model_pb2.Task(
                    id= taskID,
                    title = taskTitle,
                    description = taskDescription,
                    is_completed = False,
                    date = taskDate,
                    responsible = taskResponsible
                )

                response = stub.UpdateTask(updated_task)
                print(f"Tarefa atualizada com sucesso! ID: {response.id}")
            case 4:
                taskID = input("ID: ")
                response = stub.DeleteTask(model_pb2.TaskID(id = taskID))
            case 5:
                taskID = input("ID: ")
                response = stub.FinishTask(model_pb2.TaskID(id = taskID))
                print(f"Tarefa concluída! ID: {response.id}")
            case 0: # Tava com sono né Lucas kkkkk
                print("Saindo...")
                break
            case _:
                print("Tá doidão?")