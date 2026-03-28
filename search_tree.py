user = int(input("Say a number: "))


class treenode():
    def __init__ (self,data):
        self.data = data
        self.leftnode = None
        self.rightnode = None
    
    def search(self,root):
        if root != None:
            if root.data == user:
                print("Your number is in the tree!")
                return True
            self.search(root.leftnode)
            self.search(root.rightnode)
        else:
            return False
        

tree = treenode(50)
tree.leftnode = treenode(40)
tree.leftnode.leftnode = treenode(20)
tree.rightnode = treenode(30)
var = tree.search(tree)
if var != True:
    print("Your number is not in the tree!")


