class node:
    def __init__ (self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
   
root = node(12)
root.insert(3)     
root.insert(456)     
root.insert(35)     
root.printtree()