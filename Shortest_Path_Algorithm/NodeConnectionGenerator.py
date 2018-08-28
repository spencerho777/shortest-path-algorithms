import random, string
from Node import *
from Connection import *

def generateNodes(gridLimitX, gridLimitY, numberOfNodes):
    if numberOfNodes > gridLimitX * gridLimitY:
        return []

    names = list(string.ascii_uppercase)

    if numberOfNodes // 26 > 0:
        for _ in range(0, numberOfNodes // 26):
            for r in range(1, 27):
                names.append(names[r-1] + (str(_ + 1)))

        

    nodes = [Node(0, 0, names[0], s=True)]
    usedCoords = [(0, 0), (gridLimitX, gridLimitY)]

    for name in names[1:numberOfNodes - 1]:
        x = random.randint(0, gridLimitX)
        y = random.randint(0, gridLimitY)
        while (x, y) in usedCoords:
            x = random.randint(0, gridLimitX)
            y = random.randint(0, gridLimitY)

        usedCoords.append((x, y))
        newNode = Node(x, y, name)
        nodes.append(newNode)
        newNode.distanceToGoal = Connection(newNode, Node(gridLimitX, gridLimitY, names[numberOfNodes - 1], e=True)).distance


    nodes.append(
        Node(gridLimitX, gridLimitY, names[numberOfNodes - 1], e=True))
    return nodes

def generateConnections(nodes, c_to_s, c_to_e, c_to_n):
    connections = []

    def makeConnection(node1):
        other = random.randint(1, len(nodes) - 2)
        if Connection(node1, nodes[other]) not in connections and nodes[other] != node1:
            con = Connection(node1, nodes[other])
            connections.append(con)
            node1.neighbors.append(con)
            nodes[other].neighbors.append(Connection(nodes[other], node1))

    closest = sorted(nodes[1:len(nodes)-1],
                     key=lambda x: math.sqrt((x.x - nodes[0].x) ** 2 +
                                             (x.y - nodes[0].y) ** 2))
    for c in range(c_to_s):
        con = Connection(nodes[0], closest[c])
        connections.append(con)
        nodes[0].neighbors.append(con)
        
    closest = sorted(nodes[1:len(nodes)-1],
                     key=lambda x: math.sqrt((x.x - nodes[-1].x) ** 2 +
                                             (x.y - nodes[-1].y) ** 2))
    
    for c in range(c_to_e):
        con = Connection(closest[c], nodes[-1])
        connections.append(con)
        closest[c].neighbors.append(con)
        
    for node in nodes[1:-1]:
        for c in range(c_to_n):
            makeConnection(node)

    return connections
