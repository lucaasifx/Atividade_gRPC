python -m grpc_tools.protoc --proto_path=. --python_out=. ./model.proto;
python -m grpc_tools.protoc --proto_path=. --pyi_out=. ./model.proto;
python -m grpc_tools.protoc --proto_path=. --grpc_python_out=. ./model.proto;

# unico comando
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --pyi_out=. ./model.proto