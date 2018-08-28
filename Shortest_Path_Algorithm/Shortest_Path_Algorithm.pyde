from Grid import *
from NodeConnectionGenerator import *
from PathFinder import *

gridX, gridY = 30, 30
nodes = generateNodes(gridX, gridY, 120)
connections = generateConnections(nodes, 2, 1, 2)
#print("Nodes: ", [str(node) for node in nodes])
#print("Connections: ", [str(connection) for connection in connections])
grid = Grid(gridX, gridY, nodes, connections)
algorithms = PathFinder(nodes)

def mouseClicked(event):
    grid.handleClick(event)

def setup():
    size(1280, 720)
    
    
def keyPressed():
    #print(keyCode)
    if keyCode == 65:
        if grid.shortestPath:
            for node in grid.shortestPath:
                node.isShortestPath = True
        else:
            path = algorithms.a_star()
            grid.shortestPath = path
            for node in path:
                node.isShortestPath = True
    if keyCode == 68:
        if grid.shortestPath:
            for node in grid.shortestPath:
                node.isShortestPath = True
        else:
            path = algorithms.dijkstra()
            grid.shortestPath = path
            for node in path:
                node.isShortestPath = True    
    if keyCode == 8 and grid.shortestPath:
        for node in grid.shortestPath:
            node.isShortestPath = False
            node.t_distance = 0 if node.isStartNode else float("inf")
            node.distanceToGoal = 0
            node.combinedTotal = 0 if node.isStartNode else float("inf")
        algorithms.steps = 0
        grid.shortestPath = []
    if keyCode == 32 and grid.shortestPath:
        for node in grid.shortestPath:
            node.isShortestPath = False

def draw():
    background(255) # refresh background
    
    # draw grid with nodes and connections
    grid.drawGrid()
    
    # draw information on bottom of the screen (steps it took, shortest path)
    textSize(15)
    fill(0)
    text("Steps: " + str(algorithms.steps), 40, 705)
    
    text("Shortest Path: " + ' - '.join([str(node) for node in grid.shortestPath]), 300, 705)
