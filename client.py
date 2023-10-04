import grpc
import greet_pb2 as pb2
import greet_pb2_grpc as pb2_grpc
import time


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.GreeterStub(channel)

        print("1. Say Hello - Unary")
        print("2. Parrot Says Hello - Server Side Streaming")
        print("3. Chatty Client Says Hello - Client Side Streaming")
        print("4. Interactive Hello - Both Sides Streaming")

        rpc_call = input("Which rpc would you like to make?")

        if rpc_call == "1":
            hello_request = pb2.HelloRequest(name="John", greeting="Bonjour")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received")
            print(hello_reply)
        if rpc_call == "2":
            hello_request = pb2.HelloRequest(name="John", greeting="Bonjour")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("Parrot Says Hello Response received")
                print(hello_reply)

        if rpc_call == "3":
            print("Not Implemented")
        if rpc_call == "4":
            print("Not Implemented")


if __name__ == "__main__":
    run()
