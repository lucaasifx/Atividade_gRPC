# so comando de compilação
python -m grpc_tools.protoc --proto_path=. --python_out=. ./model.proto;
python -m grpc_tools.protoc --proto_path=. --pyi_out=. ./model.proto;
python -m grpc_tools.protoc --proto_path=. --grpc_python_out=. ./model.proto;
# unico comando
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --pyi_out=. ./model.proto




## cola do dockerkkk

## constroi as imagens
docker compose build

### inicia o servidor
docker compose up server

## pra cada cliente abrir uma aba
## cliente 1 
docker compose run --rm client1
## cliente 2
docker compose run --rm client2

## derruba tudo
docker compose down