"""
3 attr:prev(obj) data  next(obj) 
  
 1   inse: begi
           midd 
           end 
 2  delet: begi
           midd 
           end 
 3  traversing 

[]
"""
class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class sll:
    def __init__(self):
        self.head=None
        self.tail=None

    def IAB(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail=self.head
        else:
            new_node = node(val)
            new_node.next = self.head
            new_node.prev=None
            self.head = new_node
    
    def IAM(self,val,pos):
        temp=self.head
        traverse =0
        while temp.next!=None and traverse<pos-1:
            temp=temp.next
            traverse+=1
        new_node = node(val)
        new_node.prev=temp
        if temp.next!=None:
            new_node.next=temp.next
        temp.next=new_node


    def IAE(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail=self.head
            return
        new_node=node(val)
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        

    
    def DAB(self):
        if self.head==None:
            print('empty')
        else:
            a=self.head
            self.head=self.head.next
            self.head.prev=None
            del a
    def DAM(self,pos):
        if self.head==None:
            print('empty')
        else:
            temp=self.head
            i=0
            while temp.next!=None and i<pos-1:
                temp=temp.next
                i+=1
            del_node=temp.next
            if del_node.next!=None:
                temp.next=del_node.next
                del_node.next.prev=temp
            else:
                temp.next=None
            del del_node
            
    def DAE(self):
        if self.head == None:
            print("empty")
            return
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        va=temp.next
        temp.next=None
        self.tail=temp
        del va

    
    def display(self):
        pr=self.head
        l = []
        while pr is not None:
            l.append(str(pr.data))
            pr=pr.next
        print("->".join(l))

sl=sll()
sl.IAB(1)
sl.IAE(2)
sl.display()
#sl.DAB()
sl.IAE(3)
sl.IAM(7,1)
sl.display()
sl.DAM(3)
sl.display()

#,2,1,3