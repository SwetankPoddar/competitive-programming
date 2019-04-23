
### Binary Tree #####################################

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return(str(self.data))

class Tree:
    def __init__(self):
        self.root = None
    def printInOrder(self,root):
        if(root == None):
            print("lol")
        printInOrder(self,root.left)
        print(root)
        printInOrder(self,root.right)

    def insert(self, value):
        position = 1
        if(self.root is None):
            self.root = Node(value)
        else:
            current_node = self.root

            while(current_node is not None):
                #print(current_node)
                if(current_node.data > value):
                    current_node = current_node.left
                    position = position + 1

                else:
                    current_node = current_node.right
                    position = 2 * position + 1
            current_node = Node(value)
        #print position

        print(str(position))

    def minValueNode(node):
        current = node
        while(current != None):
            current = current.left
        return current

    def deleteNode(self,node,data):
    	if node is None:
    		return node
    	if(data < node.data):
    		node.left = deleteNode(node.left,data)
    	elif(data > node.data):
            print(node)
            node.right = deleteNode(node.right,data)
    	else:
    		print(node.position)
    		if(node.left == None):
    			temp = node.right
    			node = None
    			return temp
    		elif(node.right == None):
    			temp = node.left
    			node = None
    			return temp
    		temp = minValueNode(node.right)
    		node.data = temp.data
    		node.right = deleteNode(node.right,temp.data)
    	return node

    def delete(self,value):
        a = deleteNode(self.root, value)



####################################################

numberOfInputs  = int(input())
queries = []

for x in range(numberOfInputs):
    query = input()
    query = query.split()
    queries.append(query)

#Create new Tree
bt = Tree()

#perform the queries
for query in queries:
    action = query[0]
    value  = int(query[1])
    if(action == 'i'):
        bt.insert(value)
    elif(action == 'd'):
        root = bt.root
        #bt.deleteNode(root,value)
bt.printInOrder(root)
