
class PathFinder():
    
    def __init__ (self, nodes):
        self.nodes = nodes
        self.steps = 0
        
    def dijkstra(self):

        visited = []
        unvisited = self.nodes[:]
        currentNode = self.nodes[0]
        goalNode = self.nodes[-1]
        completed = False
        predecessor = {}
        path = []
        
        #print([str(u) for u in unvisited])
        while unvisited:
            #print("Current Node: " + str(currentNode))
            for c in currentNode.neighbors:
                self.steps += 1
                if c.node2 in unvisited:
                    #print("  Neighbor: " + str(c.node2))
                    if c.node2.t_distance > currentNode.t_distance + c.distance:
                        c.node2.t_distance = currentNode.t_distance + c.distance
                        predecessor[c.node2] = currentNode
                
            visited.append(currentNode)
            unvisited.remove(currentNode)
            
            if goalNode in visited:
                completed = True
                break
            
            queue = sorted(unvisited, key=lambda x: x.t_distance)
            #print([str(node) for node in queue])
            
            nextNode = queue[0]
            
            currentNode = nextNode
        
        if completed:
            currentNode = goalNode
            while currentNode != self.nodes[0]:
                try:
                    path.insert(0, currentNode)
                    currentNode = predecessor[currentNode]
                except KeyError:
                    print("Path not reachable")
                    break
                
            path.insert(0, currentNode)
            return path
        
            
    def a_star(self):
        visited = []
        unvisited = self.nodes[:]
        currentNode = self.nodes[0]
        goalNode = self.nodes[-1]
        completed = False
        predecessor = {}
        path = []
        
        #print([str(u) for u in unvisited])
        while unvisited:
            #print("Current Node: " + str(currentNode))
            for c in currentNode.neighbors:
                self.steps += 1
                if c.node2 in unvisited:
                    #print("  Neighbor: " + str(c.node2))
                    if c.node2.combinedTotal > c.node1.t_distance + c.distance + c.node2.distanceToGoal:
                        c.node2.t_distance = c.node1.t_distance + c.distance
                        c.node2.combinedTotal = c.node2.t_distance + c.node2.distanceToGoal
                        predecessor[c.node2] = currentNode
                
            visited.append(currentNode)
            unvisited.remove(currentNode)
            
            if goalNode in visited:
                completed = True
                break
            
            queue = sorted(unvisited, key=lambda x: x.combinedTotal)
            #print([str(node) for node in queue])
            
            nextNode = queue[0]
            
            currentNode = nextNode
        
        if completed:
            currentNode = goalNode
            while currentNode != self.nodes[0]:
                try:
                    path.insert(0, currentNode)
                    currentNode = predecessor[currentNode]
                except KeyError:
                    print("Path not reachable", [(str(k), str(predecessor[k])) for k in predecessor])
                    break
                
            path.insert(0, currentNode)
            #print([str(node) for node in self.nodes])
            return path
            
