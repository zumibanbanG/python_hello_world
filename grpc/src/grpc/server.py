from concurrent import futures
import grpc

import sys

sys.path.append("./src")

from pb import hello_world_pb2_grpc
from pb import hello_world_pb2


class Greeter(hello_world_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return hello_world_pb2.HelloReply(message=f"Hello, {request.name}!")

    def SayHelloAgain(self, request, context):
        return hello_world_pb2.HelloReply(message=f"Hello again, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
