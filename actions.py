import map
from collections import deque
import math

'''

    class Action - A class representing the actions an agent can take (bfs, iddls, ucs, A star)

'''

class Actions:

    def __init__(self, map):
        self.graph = map
        self.frontier = deque()
        self.visited = []
        self.cost = 0
        self.explored = 0
        self.expanded = 0

    '''
    
        bfs - breath first search
        arg1 - starting_node - the starting point
        arg2 - goal_node - the goal to find
        nodes in frontier = [cost, node name]
    
    '''
    def bfs(self, starting_node, goal_node):
        self.cost = 0
        self.explored = 0
        self.expanded = 0
        self.frontier = deque()
        start = [0, starting_node]
        self.visited = []
        self.frontier.append(start)
        
        # an empty frontier means that the goal node wasn't found
        while self.frontier:
            current_node = self.frontier.pop()
            
            # check if current node hasn't been visited (this might skew maintained value because the frontier can contain a node that is already in the frontier)
            if current_node[1] not in self.visited:
                self.explored += 1
                self.visited.append(current_node[1])
                self.cost += current_node[0]
                
                # grab dictionary of neighbors and costs as weights
                neighbor_dict = self.graph.get_neighbors(current_node[1])
                
                if neighbor_dict is not None:
                    neighbors = list(neighbor_dict.keys())
                    if current_node[1] == goal_node:
                        return
                    else:
                        for neighbor in neighbors:
                            if neighbor not in self.visited:
                                new_node = [int(neighbor_dict[neighbor]), neighbor]
                                self.frontier.append(new_node)
                                self.expanded += 1
        
    '''
        
        dls - depth limited search
        arg1 - starting_node - the starting point
        arg2 - goal_node - the goal to find
        arg3 - depth - the current allowed depth
        arg4 - depth_limit - the maximum depth limit
        
    '''
    def dls(self, starting_node, goal_node, depth, depth_limit):        
        start = [0, starting_node]
        self.frontier.append(start)
        
        # an empty frontier means that the goal wasn't found
        while self.frontier:
            current_node = self.frontier.pop()
            
            # check if current node hasn't been visited (this might skew maintained value because the frontier can contain a node that is already in the frontier)
            if current_node[1] not in self.visited:
                self.explored += 1
                self.visited.append(current_node[1])
                self.cost += current_node[0]
                
                if current_node[1] == goal_node:
                    return
            
                # depth = depth limit means we have met the maximum depth
                if depth == depth_limit:
                    return
                
                # grab dictionary of neighbors and costs as weights                
                neighbor_dict = self.graph.get_neighbors(current_node[1])
                
                if neighbor_dict is not None:
                    neighbors = list(neighbor_dict.keys())

                    for neighbor in neighbors:
                        if neighbor not in self.visited:
                            new_node = [int(neighbor_dict[neighbor]), neighbor]
                            self.expanded += 1
                            self.frontier.append(new_node)    
    
    '''
    
        ids - iterative deepening search (wrapper for dls)
        arg1 - starting_node - the starting point
        arg2 - goal_node - the goal to find
    
    '''
    def ids(self, starting_node, goal_node):
        self.cost = 0
        self.explored = 0
        self.expanded = 0
        self.visited = []
        self.frontier = deque()
        # set max depth as the number of nodes in the graph
        depth_limit = len(self.graph.graph)
        counter = 0
        while counter < depth_limit:
            self.dls(starting_node, goal_node, counter, depth_limit)
            if goal_node in self.visited:
                return
            counter += 1
    
    '''
    
        ucs - uniformed cost search
        arg1 - starting_node - the starting point
        arg2 - goal_node - the goal to find the path to 
        uses a list for the path and cost in the frontier where [cost, [path]]
    
    '''
    def ucs(self, starting_node, goal_node):
        self.cost = 0
        self.explored = 0
        self.expanded = 0
        self.frontier = deque()
        self.frontier.append([0, [starting_node]])
        self.visited = []
        node_path = []
        # an empty frontier means that the goal was never found
        while self.frontier:
            node_path = self.frontier.popleft()
            self.explored += 1
            current_path = node_path[1][len(node_path[1]) - 1]
            
            if goal_node in node_path[1]:
                self.cost = node_path[0]
                self.visited = node_path[1]
                return
            
            cost = node_path[0]
            
            # get dictionary of neighbors
            neighbors = self.graph.get_neighbors(current_path)
            neighbor_keys = list(neighbors.keys())
            # for every neighbor, array is sliced and appended with temp where new paths = the number of neighbors 
            for neighbor in neighbor_keys:
                # slice node_path into temp variable
                temp = node_path[1][:]
                temp.append(neighbor)
                self.expanded += 1
                self.frontier.append([cost + int(neighbors.get(neighbor)), temp])
    
    '''
    
        get_distance - calculates distance based on two different pairs of latitude and longitude_a
        arg1 - latitude_a - latitude of the first pair
        arg2 - lonitude_a - longitude of the first pair
        arg3 - latitude_b - latitude of the second pair
        arg4 - longitude_b - longitude of the second pair
        
        formula from: https://www.movable-type.co.uk/scripts/latlong.html
    '''
    def get_distance(self, latitude_a, longitude_a, latitude_b, longitude_b):

        lat_sin = math.sin(math.radians(latitude_a)) * math.sin(math.radians(latitude_b))
        

        lat_cos = math.cos(math.radians(latitude_a)) * math.cos(math.radians(latitude_b))
        

        lon_cos = math.cos(math.radians(longitude_b) - math.radians(longitude_a))
        
        distance = math.acos(lat_sin + lat_cos * lon_cos) * 6371
        
        return distance
                
    '''        
       
        astar - A star Heuristic algorithm
        arg1 - starting_node - the starting node
        arg2 - goal_node - the goal node
        pseudo code source: https://www.redblobgames.com/pathfinding/a-star/introduction.html
       
    '''        
    def astar(self, starting_node, goal_node):            
        self.cost = 0
        self.explored = 0
        self.expanded = 0
        self.frontier = deque()
        self.frontier.append(starting_node)
        self.visited = []
        
        # helper data structures to track parents and the cost from a current node visited
        came_from = {}
        cost_so_far = {}
        
        came_from[starting_node] = None
        cost_so_far[starting_node] = 0
        
        # if frontier is empty, goal not found
        while self.frontier:
            current_node = self.frontier.popleft()
            self.explored += 1
            
            if current_node == goal_node:
                self.cost = cost_so_far[goal_node]
                
                # loop to get the path taken 
                while starting_node not in self.visited:
                    self.visited.append(current_node)
                    current_node = came_from[current_node]
                break
            
            # get a dictionary of neighbors with their costs as values
            neighbor_dict = self.graph.get_neighbors(current_node)
            neighbors = list(neighbor_dict.keys())
            for neighbor in neighbors:
                new_cost = cost_so_far[current_node] + int(neighbor_dict[neighbor])
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    
                    # get city coordinates from the map
                    goal_coordinates = self.graph.get_city_lat_lon(goal_node)
                    neighbor_coordinates = self.graph.get_city_lat_lon(neighbor)
                    
                    # calculates the new total cost = priority
                    priority = new_cost + self.get_distance(goal_coordinates[0], goal_coordinates[1], neighbor_coordinates[0], neighbor_coordinates[1])
                    
                    self.expanded += 1
                    
                    # maintain priority by checking if the new calculated cost has higher priority 
                    if len(self.frontier) > 0 and cost_so_far[self.frontier[0]] > priority:
                        self.frontier.appendleft(neighbor)
                    else:
                        self.frontier.append(neighbor)
                    
                    came_from[neighbor] = current_node
        
        # reverse list because of how the nodes are appended to visited 
        self.visited.reverse()       
    
    def get_cost(self):
        return self.cost
    
    def get_maintained(self):
        return len(self.frontier)
    
    def get_expanded(self):
        return self.expanded
    
    def get_explored(self):
        return self.explored
    
    def output_maintained(self):
        print("maintained: ", len(self.frontier))
    
    def output_expanded_count(self):
        print("expanded: ", self.expanded)
    
    def output_explored_count(self):
        print("explored: ", self.explored)
    
    ''' 
    
        output_frontier - outputs the frontier
    
    '''
    def output_frontier(self):
        print("frontier: ", self.frontier)
    
    '''
        output_visited - outputs all visited nodes
    '''
    def output_visited(self):
        print("visited: ", self.visited)
        
    def output_cost(self):
        print("cost: ", self.cost)