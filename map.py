import city

"""

    Map - a class used as a repesentation of a graph

"""

class Map:

    def __init__(self):
        self.graph = {}
        self.cities = {}
    '''
    
        add_edge - adds an edge to the graph class variable
        arg1 - current_node - the node that neighbors neighbor_node
        arg2 - neighbor_node - the neighboring node
        arg3 - weight - the weight between the nodes (distance in city context)
    
    '''
   
    def add_edge(self, current_node, neighbor_node, weight):
        
        # current_node = current_node.lower()
        
        if current_node not in self.graph:
            self.graph[current_node] = {}
            
        self.graph[current_node][neighbor_node] = weight
    
    '''
    
        get_neighbors - returns a dictionary containing neighbors as keys and weights as values
        arg1 - current_node - the node to get neighbors from        
        
    '''
    def get_neighbors(self, current_node):
        # current_node = current_node.lower()
        if current_node in self.graph:
            return self.graph[current_node]
        else:
            return None
    
    '''
        
        node_count - returns the number of nodes in the graph
       
    '''
    def node_count(self):
        return len(self.graph)
    
    def get_city_lat_lon(self, city_name):
        city_name = city_name.lower()
        city = self.cities.get(city_name)
        return [city[0][1], city[1][1]]
    
    def add_city(self, city):
        self.cities[city.city_name] = city.get_coordinates()
    
    '''
       
       output_graph - outputs the graph
       
    '''
    def output_graph(self):
        print(self.graph)
