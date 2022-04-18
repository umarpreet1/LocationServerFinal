from concurrent import futures
import grpc
import os
import serve_data_pb2_grpc as sd_grpc
import serve_data_pb2 as sd
from btree import BTree
from trie import BaseTrie


class serve_data(sd_grpc.data_serverServicer):

    def __init__(self,idx, myTree, lockTrie):
        self.idx = str(idx)
        self.myTree = myTree
        self.lockTrie = lockTrie


    def lock(self,request,context):
        ls_id = request.ls_id
        request_id = request.request_id
        key = request.key
        print("lock request received with key:",key)
        required_lock = self.lockTrie.get_lock(key)
        if required_lock.lock():
            required_lock.set_request_id(request_id)
            print("its is unlocked, so i am locking it")
            response = sd.response(status='LOCKED', request_id=request_id, ds_id=self.idx)
            return response
        else:
            response = sd.response(status='FAIL', request_id=request_id, ds_id=self.idx)
            return response

    def write(self, request, context):
        request_id = request.request_id
        key = request.key
        print("Write request received with key:", key)
        value = request.value
        lock = self.lockTrie.get_lock(key)
        if lock.is_locked() and lock.request_id == request_id:
            self.myTree.insert((key,value))
            lock.unlock()
            response = sd.response(status="SUCCESS",request_id=request_id,ds_id=self.idx)
            return response
        elif lock.is_locked() :
            print(lock.request_id)
            response = sd.response(status="LOCKED_ELSE", request_id=request_id, ds_id=self.idx)
            return response
        else:
            response = sd.response(status="UNLOCKED", request_id=request_id, ds_id=self.idx)
            return response


    def read(self, request, context):
        key = request.key
        print("Read request received with key:", key)

        required_lock = self.lockTrie.get_lock(key)
        required_lock.lock(True)
        value = self.myTree.search_key(key)
        required_lock.unlock()
        response = sd.response_read(value = value)

        return response



    def update(self, request, context):
        key = request.key
        print("Update request received with key:", key)
        value = request.value
        file = open('data/data_'+str(self.idx)+'/'+key+'.txt','w')
        file.write(value)
        file.close()
        response = sd.response(status = "SUCCESS")
        return response

class Server:
    def __init__(self,idx,port):
        print("Creating Data server with id : ", idx, " port : ", port)
        self.idx = idx
        self.myTree = BTree(64)
        self.lockTrie = BaseTrie()
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        sd_grpc.add_data_serverServicer_to_server(serve_data(idx=idx,myTree=self.myTree,lockTrie=self.lockTrie), self.server)
        self.server.add_insecure_port('[::]:'+str(port))
        self.port = port
        print("Data server is created with id : ",idx," port : ",port)

    def start(self):
        print("Starting Data server with id : ", self.idx, " port : ", self.port)
        self.server.start()
        print("Data server started with id : ", self.idx, " port : ", self.port)
        self.server.wait_for_termination()

    def stop(self):
        self.server.stop()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sd_grpc.add_data_serverServicer_to_server(serve_data(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    ser = Server(0,50051)
    ser.start()