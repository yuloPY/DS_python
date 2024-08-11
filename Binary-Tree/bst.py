class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node == None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=",")
    inOrderTraversal(node.right)

def search(node, target):
    if node is None:
        return None
    if node.data == target:
        print(f"Target found: {node.data}")
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)

def insert(node, data):
    if node is None:
        return TreeNode(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node

def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def deleteNode(node,data):
    if not node:
        return None

    if data < node.data:
        node.left = deleteNode(node.left,data)
    elif data > node.data:
        node.right = deleteNode(node.right,data)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        
        node.data = minValueNode(node.right).data
        node.right = deleteNode(node.right,node.data)
    
    return node







root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

inOrderTraversal(root)
print()

search(root, 8)
