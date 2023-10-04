"""The server python script for the application"""
import time
from concurrent.futures import ThreadPoolExecutor

import grpc

import greet_pb2 as pb2
import greet_pb2_grpc as pb2_grpc


class GreeterService(pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return super().SayHello(request, context)

    def ParrotSaysHello(self, request, context):
        return super().ParrotSaysHello(request, context)

    def ChattyClientSaysHello(self, request_iterator, context):
        return super().ChattyClientSaysHello(request_iterator, context)

    def InteractingHello(self, request_iterator, context):
        return super().InteractingHello(request_iterator, context)


def serve():
    """The greeter server application logic"""
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()