"""
1)push- overflow  top!=len
2)pop- underflow  top!=0

3)insert 

FILO 

"""
class stack:
    def __init__(self,size):
        self.data = []
        self.size=size
    def push(self, value):
        if len(self.data)>=self.size:
            print("Stack overflow")
            return 
        self.data.append(value) 
    def pop(self):
        try:
            self.data.pop(-1)
        except IndexError:
            print('empty stack(underflow)')
            return None
    def peek(self):
        try:
            return self.data[-1]
        except IndexError:
            print('empty stack(underflow)')
    
    def display(self):
        print(' '.join(str(i) for i in self.data))

s = stack(int(input()))
for i in range(1,5):
    print('stack top :',s.peek())
    s.push(i)  
    s.display()
