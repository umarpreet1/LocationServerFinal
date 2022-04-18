# Searching a key on a B-tree in Python
from random import random, randint
from threading import Lock
from time import time
from threading import Thread
import compressIO

# Create a node
class BTreeNode:
    def __init__(self,  leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []
        self.lock = Lock()

    def wait_for_unlock(self):
        while(self.lock.locked()):
            continue
        return True


# Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
        self.write_lock = Lock()
        # Insert node

    def insert(self, k):
        self.write_lock.acquire(blocking=True)
        self.root.wait_for_unlock()
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)
        self.write_lock.release()

        # Insert nonfull

    def insert_non_full(self, x, k):
        x.wait_for_unlock()
        i = len(x.keys) - 1
        if x.leaf:
            if k[0] in x.keys:
                index = x.keys.index(k[0])
                x.keys[index] = k
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            x.child[i].wait_for_unlock()
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            x.child[i].wait_for_unlock()
            self.insert_non_full(x.child[i], k)

        # Split the child

    def split_child(self, x, i):
        t = self.t
        x.wait_for_unlock()
        y = x.child[i]
        y.wait_for_unlock()
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    # Print the tree
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

    # Search key in the tree
    def search_key(self, k, parent=None, x=None, ):

        if x is not None:
            if parent != None:
                x.lock.acquire(blocking=True)
                parent.lock.release()
            else:
                x.lock.acquire(blocking=True)
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                x.lock.release()
                return x.keys[i][1]
            elif x.leaf:
                x.lock.release()
                return None
            else:
                return self.search_key(k, x, x.child[i])

        else:
            while self.write_lock.locked():
                 continue
            return self.search_key(k, None, self.root)


def thread(bTree,operations,keys):
    inserted = []
    j = 0
    print("running operations")
    for i in range(operations):
        if i%100==0:
            print(i,"done")
        o = random()
        if o >0.7:
            k = keys[j]
            inserted.append(k)
            j = j + 1
            bTree.insert((k,k*3))
        else:
            if len(inserted)>0:
                r = randint(0,len(inserted)-1)
                k = inserted[r]
                res = bTree.search_key(k)
                if res!=None and res!= k*3:
                    print("some error ")


def main():
    B = BTree(64)
    insertions = 1000
    keys = list(range(1000))
    thread(B,100,keys)
    trds =[]
    for i in range(4):
        t = Thread(target=thread,args=(B,1000,keys))
        t.start()
        trds.append(t)
    for t in trds:
        t.join()


if __name__ == '__main__':
    main()