user = input("Say a number: ")


class treenode():
    def __init__ (self,data):
        self.data = data
        self.leftnode = None
        self.rightnode = None

    def search_root(self,root):
        if root.data == user:
            print("Your number is the root!!")
        else:
            return
    
    def search_leftnode(self,root):
        if root != None:
            if root.leftnode.data == user:
                print("Your number is in the left root!")
                return
            self.search_leftnode(root.leftnode)
        else:
            return


    def search_rightnode(self,root):
        if root != None:
            rightnodes = self.search_rightnode(root.rightnode)
        elif rightnodes == user:
            print("Your number is in the right root!")
        else:
            return


tree = treenode(50)
tree.leftnode = treenode(40)
tree.leftnode.leftnode = treenode(20)
tree.rightnode = treenode(30)
tree.search_root(tree)
tree.search_leftnode(tree)
#tree.search_rightnode(tree)

        