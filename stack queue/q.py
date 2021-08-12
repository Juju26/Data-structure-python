'''
FIFO
'''

class queue:
    def __init__(self,size):
        self.data = []
        self.size=size
    def enq(self, value):
        if len(self.data)>=self.size:
            print("Q overflow")
            return 
        self.data.append(value)
    def deq(self):
        try:
            self.data.pop(0)
        except IndexError:
            print('empty q(underflow)')
            return None
    def peek(self):
        try:
            return self.data[0]
        except IndexError:
            print('empty q(underflow)')
    def display(self):
        print(' '.join(str(i) for i in self.data))

q=queue(int(input("Enter Q size ")))
for i in range(1,5):
    q.enq(i)
q.display()
q.peek()
for j in range(1,7):
    q.deq()