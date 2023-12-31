"""The server python script for the application"""
import time
from concurrent.futures import ThreadPoolExecutor

import grpc

import greet_pb2 as pb2
import greet_pb2_grpc as pb2_grpc


class GreeterService(pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("Say Hello Request Made: ")
        print(request)
        hello_reply = pb2.HelloReply(message="Hello " + request.name)
        hello_reply.message = f"{request.greeting} {request.name}"
        return hello_reply

    def ParrotSaysHello(self, request, context):
        print("Parrot Says Hello Request Made: ")
        print(request)

        for i in range(3):
            hello_reply = pb2.HelloReply(message="Hello " + request.name)
            hello_reply.message = f"{request.greeting} {request.name} {i+1}"
            yield hello_reply
            time.sleep(3)

    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = pb2.DelayedReply()

        for request in request_iterator:
            print("ChattyClientSays Hello Request Made: ")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed replay"
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello Request Made: ")
            print(request)

            hello_reply = pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply


def serve():
    """The greeter server application logic"""
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
