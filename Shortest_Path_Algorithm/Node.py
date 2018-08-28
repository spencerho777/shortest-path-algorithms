class Node():

    def __init__(self, x, y, name, s=False, e=False):
        self.x = x
        self.y = y
        self.name = name
        self.isStartNode = s
        self.isEndNode = e
        self.isClicked = False
        self.isShortestPath = False
        self.t_distance = 0 if s else float("inf")
        self.distanceToGoal = 0
        self.combinedTotal = 0 if s else float("inf")
        self.neighbors = []

    def __str__(self):
        return self.name + "(" + str(self.x) + ", " + str(self.y) + ")"
    
