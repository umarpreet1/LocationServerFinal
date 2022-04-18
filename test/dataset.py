import random
import string
import pickle

class Dataset:
    def __init__(self,num_keys,size_per_key):
        self.num_keys = num_keys
        self.size_per_key = size_per_key
        self.dataset = {}

    def create_dataset(self):
        for i in range(self.num_keys):
            length = random.randint(4,30)
            key = ''.join(random.choice(string.ascii_lowercase ) for _ in range(length))
            value = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.size_per_key))
            self.dataset[key] = value

        return self.dataset

    def dump_data(self):
        fl = open('data', 'wb')
        pickle.dump(self.dataset, fl)
        fl.close()