#class for creating nodes of binary tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
#function for finding height of a binary tree
def find_Height(root):
    if root is None:
        return 0
    else:
        #recursive call for finding height of left subtree
        l_height=find_Height(root.left)
        #recursive call for finding height of right subtree
        r_height=find_Height(root.right)
        return 1+max(l_height,r_height)
#main programme
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.left.right.right=Node(6)
    print("height of given binary tree is",find_Height(root))
