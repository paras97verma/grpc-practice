from __future__ import print_function

import grpc
import users_pb2
import users_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = users_pb2_grpc.UsersStub(channel)
        response = stub.GetUsersUser(users_pb2.GetUsersRequest())
    print(response.users)