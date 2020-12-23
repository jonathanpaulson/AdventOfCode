import fileinput
import re
import sys

#start = '389125467'
start = '496138527'
N = 1000000

class Node(object):
    def __init__(self, parent, value, prev, next_):
        assert isinstance(parent, LinkedList)
        self.parent = parent
        self.value = value
        self.prev = prev
        self.next = next_
    def insert(self, x):
        node = Node(self.parent, x, self, self.next)
        self.parent.D[x] = node
        self.next = node
        node.next.prev = node
        return node
    def erase(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        del self.parent.D[self.value]

class LinkedList(object):
    def __init__(self):
        self.D = {}
    def append(self, prev, x):
        if prev is None:
            node = Node(self, x, None, None)
            node.next = node
            node.prev = node
            self.D[x] = node
            return node
        else:
            node = Node(self, x, prev, prev.next)
            prev.next = node
            node.next.prev = node
            self.D[x] = node
            return node

    def find(self, x):
        return self.D[x]

    def to_list(self, start):
        node = self.D[start]
        ret = [node.value]
        node = node.next
        while node.value != start:
            ret.append(node.value)
            node = node.next
        return ret

def solve(is_p2):
    nums = [int(x) for x in start]
    X = LinkedList()
    prev = None
    for x in nums:
        prev = X.append(prev, x)
    if is_p2:
        next_ = 10
        while len(X.D) < int(1e6):
            prev = X.append(prev, next_)
            next_ += 1
        assert next_ == int(1e6)+1
    N = len(X.D)

    t = 0 
    current = X.find(nums[0])
    nmoves = int(1e7) if is_p2 else 100
    for _ in range(nmoves):
        t += 1
        #if t%1000 == 0:
        #    print(t)
        #print(t, current.value, X.to_list(1))
        current_num = current.value
        pickup = []
        pickup_node = current.next
        for _ in range(3):
            pickup.append(pickup_node.value)
            tmp = pickup_node.next
            pickup_node.erase()
            pickup_node = tmp

        dest = N if current_num==1 else current_num-1
        while dest in pickup:
            dest = N if dest==1 else dest-1

        dest_node = X.find(dest)
        for x in pickup:
            dest_node = dest_node.insert(x)
        assert current == X.find(current_num)
        current = current.next

    if is_p2:
        node_1 = X.find(1)
        return node_1.next.value*node_1.next.next.value
    else:
        values = X.to_list(1)
        return ''.join([str(x) for x in values[1:]])
print(solve(False))
print(solve(True))

