class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data,end=" ")
        if self.right:
            self.right.print_tree()
        


    def find_value(self,value):
        if self.data==value:
            print(str(value)+" found\n")

        elif value>self.data:
            if self.right==None:
                print(str(value)+" Not Found")
            else:
                return self.right.find_value(value)
        elif value<self.data:
            if self.left==None:
                print(str(value)+" Not Found")
            else:
                return self.left.find_value(value)
#Traversal
    def Inorder(self,root):#Left Root Right
        if root:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)

    def preorder(self,root):#Root Left Right
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)        
    def postorder(self,root):#Left Right Root
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
    def find_max(self):
        if self.right == None:   
            return self.data
        else:
            return self.right.find_max()
    def find_min(self):
        if self.left ==None:
            return self.data
        else:
            return self.left.find_min()
    

    def delete(self,key):
        if key<self.data:
            if self.left:
                self.left=self.left.delete(key)
        elif key>self.data:
            if self.right:
                self.right=self.right.delete(key)
        else:
            if self.left == None and self.right == None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_value=self.right.find_min()
            self.data=min_value
            self.right=self.right.delete(min_value)
        return self

    def breadth_first_search(self, root):
        to_visit = []
        if root:
            to_visit.append(root)
        while to_visit:
            current = to_visit.pop(0)
            print(current.data,end=" ")
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)



root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(16)
root.insert(1)
root.insert(13)
root.insert(7)
root.insert(4)

root.print_tree()
print("\n")
root.find_value(12)
print("Inorder Travesal ")
root.Inorder(root)
print("\n")
print("Preorder Traversal ")
root.preorder(root)
print("\n")
print("PostOrder Traversal ")
root.postorder(root)
print("\n")

#root.delete(4)
#root.print_tree()
print("Breath First Traversal ")
root.breadth_first_search(root)
