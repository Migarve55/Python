
class Node:

    childs = []
    layer = 0
    value = 0
    
    def __init__(self, layer, childs, value):
        self.childs = childs
        self.layer = layer
        self.value = value

    def calculateValue():
        totalSum = 0
        if layer < 1:
            return value
        for child in childs:
            totalSum += child.calculateValue()
        return totalSum

def generateNodes(layers, size):
    nodeList = []
    for node_layer in range(layers):
        for n in range(size):
            nodeList.append(Node(layers-node_layer, 1))
    return nodeList

Node(5,generateNodes(3, 3),0)



    
        
        
    




    
