class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next=next
        self.prev=prev


class LRUCache2:
    def __init__(self, size):
        self.front = None
        self.rear = None
        self.size = size
        self.d = {}

    def put(self, key, value):
        node = Node(key, value)
        if not self.rear:
            self.rear = self.front = node
        else:
            if len(self.d) == self.size :
                self.rear = self.rear.next
                self.rear.prev = None
            self.front.next = node
            node.prev = self.front
            self.front = self.front.next
        self.d[node.key] = node
    
    def get(self, key):
        if key in self.d:
            node = self.d[key]
            if node == self.front:
                return node
            elif node == self.rear:
                self.rear = self.rear.next
                self.rear.prev = None
            else:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
            self.put(node.key, node.value)

        return -1

    def print_all(self):
        temp = self.rear
        while temp:
            print(f"key:{temp.key}, value:{temp.value}")
            temp = temp.next
        print("****")
    def print_all_reverse(self):
        temp = self.front
        while temp:
            print(f"key:{temp.key}, value:{temp.value}")
            temp = temp.prev
        print("###")



lRUCache2 = LRUCache2(3)
lRUCache2.put(2,12)
lRUCache2.put(3,13)
lRUCache2.put(4,14)
lRUCache2.put(5,15)
lRUCache2.print_all()
lRUCache2.print_all_reverse()
lRUCache2.get(4)
lRUCache2.print_all()
lRUCache2.print_all_reverse()




