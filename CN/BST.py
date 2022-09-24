class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def createBT():
    val=[int(ele) for ele in input().split()]
    root=val[0]
    def bt(root):
        
        