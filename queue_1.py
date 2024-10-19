class Node:
    def __init__(self, val, next=None, prev=None):
        self.val= val
        self.next=next
        self.prev=prev


class Queue_1:
    def __init__(self):
        self.rear = self.front = None

    def enqueue(self, val):
        if self.rear:
            node = Node(val, next=self.rear)
            self.rear.prev = node
            self.rear = node
            
        else:
            self.rear = self.front = Node(val)
            

    def dequeue(self):
        if self.rear:
            node = self.front
            if self.front == self.rear:
                self.front == self.rear == None
            else:
                self.front = self.front.prev
                self.front.next = None
            return node.val
        return -1
    
    def print_all(self):
        temp = self.rear
        while temp:
            print(f"value:{temp.val}")
            temp = temp.next
        print("****")

    def print_all_reverse(self):
        temp = self.front
        while temp:
            print(f" value:{temp.val}")
            temp = temp.prev
        print("###")
    
queue_1 = Queue_1()
queue_1.enqueue(1)
queue_1.enqueue(2)
queue_1.enqueue(3)
queue_1.print_all_reverse()
queue_1.print_all()
queue_1.dequeue()
queue_1.enqueue(4)
queue_1.print_all_reverse()
queue_1.print_all()
queue_1.dequeue()
queue_1.dequeue()
queue_1.dequeue()
queue_1.print_all_reverse()
queue_1.print_all()

            