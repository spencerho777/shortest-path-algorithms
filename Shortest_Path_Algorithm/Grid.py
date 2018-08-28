import math

class Grid():

    def __init__(self, gridX, gridY, nodes, connections):
        self.gridX = gridX
        self.gridY = gridY
        self.nodes = nodes
        self.connections = connections
        self.p = 40
        self.spacingX = (1280 - 2 * self.p) / self.gridX
        self.spacingY = (720 - 2 * self.p) / self.gridY
        self.shortestPath = []
        
        
    def handleClick(self, click):
        closest = sorted(self.nodes,
                         key=lambda x: math.sqrt((x.x * self.spacingX + self.p - click.x) ** 2 +
                                                  (x.y * self.spacingY + self.p - click.y) ** 2)
                         )
        closest[0].isClicked = not closest[0].isClicked
    
    def drawGrid(self):

        for x in range(0, self.gridX + 1):
            line(x * self.spacingX + self.p, self.p,
                 x * self.spacingX + self.p, height - self.p)

        for y in range(0, self.gridY + 1):
            line(self.p, y * self.spacingY + self.p,
                 self.gridX * ((width - 40) / self.gridX), y * self.spacingY + self.p)
            
            
        for connection in self.connections:
            stroke(0, 0, 255)
            if connection.node1.x == connection.node2.x or connection.node1.y == connection.node2.y:
                strokeWeight(2)
            if connection.node1.isClicked or connection.node2.isClicked:
                stroke(255, 69, 0)
            elif connection.node1.isShortestPath and connection.node2.isShortestPath: 
                stroke(255, 105, 180)
                strokeWeight(4)
            
            line(connection.node1.x * self.spacingX + self.p, connection.node1.y * self.spacingY + self.p,
                 connection.node2.x * self.spacingX + self.p, connection.node2.y * self.spacingY + self.p)
            stroke(0)
            strokeWeight(1)
            
        nodeSize = 5
        for node in self.nodes:
            ellipseMode(CENTER)
            stroke(0)
            if node.isClicked:
                fill(255, 69, 0)
            elif node.isStartNode:
                fill(255, 0, 0)
            elif node.isEndNode:
                fill(0, 255, 0)
            else:
                fill(255, 0, 255)
            ellipse(
                node.x * self.spacingX + self.p, node.y * self.spacingY + self.p, nodeSize, nodeSize)
            textSize(15)
            text(node.name, node.x * self.spacingX + self.p - 10,
                 node.y * self.spacingY + self.p - 8)
