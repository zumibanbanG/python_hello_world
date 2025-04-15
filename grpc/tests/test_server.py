import pytest
from src.pb import hello_world_pb2
from src.pb import hello_world_pb2_grpc
from src.grpc.server import Greeter


@pytest.fixture(scope="module")
def grpc_add_to_server():
    return hello_world_pb2_grpc.add_GreeterServicer_to_server


@pytest.fixture(scope="module")
def grpc_servicer():
    return Greeter()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return hello_world_pb2_grpc.GreeterStub(grpc_channel)


def test_say_hello(grpc_stub):
    response = grpc_stub.SayHello(hello_world_pb2.HelloRequest(name="test user"))
    assert response.message == "Hello, test user!"


def test_say_hello_again(grpc_stub):
    response = grpc_stub.SayHelloAgain(hello_world_pb2.HelloRequest(name="test user"))
    assert response.message == "Hello again, test user!"
