import math

class Connection():

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.distance = math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)

    def __str__(self):
        return self.node1.name + "---" + self.node2.name + "(" + str(self.distance) + ")"

    def __eq__(self, other):
        if sorted([self.node1.name, self.node2.name]) == sorted([other.node1.name, other.node2.name]):
            return True
        return False
