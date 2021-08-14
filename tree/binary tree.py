'''
1)The maximum number of nodes at level ‘l’ of a binary tree is 2l.
2) The Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1. 
3) In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is? Log2(N+1) 
4) A Binary Tree with L leaves has at least | Log2L? |+ 1   levels 
5) In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children
'''
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return "-> %s" %(self.data)

class tree:
    def __init__(self):
        self.root=None
    
    def __repr__(self):
        return "root %s" %(self.root)
    
    def insert(self,data):
        if self.root==None:
            self.root=node(data)
            
        temp=self.root
        while True:
            if data<temp.data:
                if temp.left!=None:
                    temp=temp.left
                else:
                    temp.left=node(data)
                    break
            elif data>temp.data:
                if temp.right!=None:
                    temp=temp.right
                else:
                    temp.right=node(data)
                    break
            else:
                break
    
    def InOrder(self,node=None):
        if node==None:
            node = self.root
        if node.left!=None:
            self.InOrder(node.left)
        if node!=None:
            print(node.data,end=' ')
        if node.right!=None:
            self.InOrder(node.right)
    
    def PreOrder(self,node=None):
        if node==None:
            node = self.root
        if node!=None:
            print(node.data,end=' ')
        if node.left!=None:
            self.PreOrder(node.left)
        if node.right!=None:
            self.PreOrder(node.right)
    
    def PostOrder(self,node=None):
        if node==None:
            node = self.root
        if node.left!=None:
            self.PostOrder(node.left)
        if node.right!=None:
            self.PostOrder(node.right)
        if node!=None:
            print(node.data,end=' ')
            
t = tree()
print(t)
print()
l=[8,3,10,1,6,14,2,7,13]
for i in l:
    t.insert(i)
print("Given array :")
print(' '.join(str(i) for i in l))
print()
print("Inorder trav :",end=' ')
print(t)
t.InOrder()
print()
print("\n Preorder trav :",end=' ')
print(t)
t.PreOrder()
print()
print("\n Postorder trav :",end=' ')
print(t)
t.PostOrder()
print()
