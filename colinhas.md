python -m grpc_tools.protoc --proto_path=. --python_out=. .\model.proto;
python -m grpc_tools.protoc --proto_path=. --pyi_out=. .\model.proto;
python -m grpc_tools.protoc --proto_path=. --grpc_python_out=. .\model.proto;