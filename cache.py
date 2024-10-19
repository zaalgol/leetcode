class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next=next
        self.prev=prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head=Node(-1000,-1000)
        self.tail=Node(-1000,-1000)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            # self.remove_from_current_place(node)
            # next = node.next
            # prev = node.prev
            # next.prev = prev
            # prev.next = next
            self.put(key, node.value)
            return node.value
            # tail = self.tail.prev
            # node.prev =tail
            # tail.prev = node
            # node.next = self.tail
            # self.tail.prev = node
        else:
            return -1
            
    def remove_from_current_place(self, node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove_from_current_place(self.d[key])
        node = Node(key,value)
        tail = self.tail.prev
        node.prev =tail
        tail.next = node
        node.next = self.tail
        self.tail.prev = node

        self.d[key] = node

        if len(self.d) > self.capacity:
            old = self.head.next
            del self.d[old.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            
            
    def print_from_head(self):
        t = self.head
        while t:
            print(f"key:{t.key} value:{t.value}")
            t = t.next
            
    def print_from_tail(self):
        t = self.tail
        while t:
            print(f"key:{t.key} value:{t.value}")
            t = t.prev

lRUCache = LRUCache(2)
lRUCache.put(1,1)
lRUCache.put(2,2)
print(f"getting 1: {lRUCache.get(1)}")
lRUCache.put(3,3)
print(f"getting 2: {lRUCache.get(2)}")
print("starting to print from head")
lRUCache.print_from_head()
print("ending to print from head")
print("starting to print from tail")
lRUCache.print_from_tail()
print("ending to print from tail")

# lRUCache.put(2,1)
# lRUCache.put(1,1)
# lRUCache.put(2,3)

# print(f"getting 1: {lRUCache.get(1)}")
# lRUCache.put(3,3)
# print(f"getting 2: {lRUCache.get(2)}")
# print("starting to print from head")
# lRUCache.print_from_head()
# print("ending to print from head")
# print("starting to print from tail")
# lRUCache.print_from_tail()
# print("ending to print from tail")
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)