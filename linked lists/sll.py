"""
2 attr: data  next(obj) 
  
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
            self.head = new_node
    
    def IAM(self,val,pos):
        temp=self.head
        traverse =0
        while temp.next!=None and traverse<pos-1:
            temp=temp.next
            traverse+=1
        new_node = node(val)
        if temp.next!=None:
            new_node.next=temp.next
        temp.next=new_node


    def IAE(self,val):
        if self.head == None:
            self.head = node(val)
            self.tail=self.head
            return
        new_node=node(val)
        self.tail.next=new_node
        self.tail=new_node

    
    def DAB(self):
        if self.head==None:
            print('empty')
        else:
            a=self.head
            self.head=self.head.next
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