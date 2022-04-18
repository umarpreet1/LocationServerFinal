import grpc
import serve_data_pb2 as sd
import serve_data_pb2_grpc as sd_grpc
import random
import dataset
import threading

data_obj = dataset.Dataset(500,1000)
data_global = data_obj.create_dataset()


def thread(thread_id,data):
    host = 'localhost'
    server_port = 50051


    channel = grpc.insecure_channel(
                '{}:{}'.format(host, server_port))


    stub = sd_grpc.data_serverStub(channel)
    added_keys = []
    list_data = list(data)
    for i in range(10000):
        if random.random() >0.75:
            r = random.randint(0,len(list_data)-1)
            key = list_data[r]
            print(thread_id,"Locking key:",key)
            message = sd.lock_request(request_id = 'temp',ls_id = thread_id,key = key)
            response = stub.lock(message)
            if response.status == 'LOCKED':
                print(thread_id,"key is locked now writing",)
                message = sd.write_request(key = key, value = data[key],request_id = 'temp',ls_id = thread_id)
                response = stub.write(message)
                if response.status == 'SUCCESS':
                    print(thread_id,"data written")
                    added_keys.append(key)
                else:
                    print(response)
                    print(thread_id,"***************************some error happened while writing********************************")
        else:
            if len(added_keys)>1:
                r = random.randint(0,len(added_keys)-1)
                key = added_keys[r]
                print(thread_id,"reading key",key)
                message = sd.read_request(key=key)
                response = stub.read(message)
                if response.value != data[key]:
                    print(response)
                    print(thread_id,"***********************************Value is different******************************",data[key])
                else:
                    print(thread_id,"value is same")

trds = []
for i in range(4):
    t = threading.Thread(target=thread,args=(str(i),data_global))
    t.start()
    trds.append(t)

for j in trds:
    j.join()