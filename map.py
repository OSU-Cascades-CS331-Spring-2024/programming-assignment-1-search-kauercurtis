"""

    Map - a class used as a repesentation of a graph

"""

import city

class Map:

    def __init__(self):
        self.graph = {}
        self.number_of_nodes = 0
    
    """
    
        create_node - creates a new node in the graph
        param1 - city - an instance of the City class in city.py
        param2 - neighbors - a dictionary of the neighboring cities with key = city_name and value = distance from instance of City class in param1
        return - node - returns the new node
    
    """
    def add_to_map(self, city, neighbors):
        self.graph[city.city_name] = [city, neighbors]
        
    def output_map(self):
        print(self.graph)
   

'''
test_map = Map()

city_1 = city.City("Calais")
coordinates = {'N': [51, 30, 53], 'E': [1, 51, 23]}
city_1.set_coordinates(coordinates)
print(city_1.get_name() + "- coordinates: ")
print(city_1.get_coordinates())
print(" == 51 30 53 N 1 51 23 E \n")
neighbors = {'Caen': 349, 'Paris': 294, 'Nancy': 478}
node = test_map.create_node(city_1, neighbors)
test_map.add_to_map(node)

city_2 = city.City("Caen")
coordinates = {'N': [50, 11, 0], 'W': [0, 22, 0]}
city_2.set_coordinates(coordinates)
print(city_2.get_name() + "- coordinates: ")
print(city_2.get_coordinates())
print(" == 50 11 0 N 0 22 0 W \n")
neighbors = {'Rennes': 184, 'Paris': 250, 'Calais': 349}
node = test_map.create_node(city_2, neighbors)
test_map.add_to_map(node)

city_3 = city.City("Paris")
coordinates = {'N': [48, 51, 24], 'E': [2, 21, 3]}
city_3.set_coordinates(coordinates)
print(city_3.get_name() + "- coordinates: ")
print(city_3.get_coordinates())
print(" == 48 51 24 N 2 21 3 E \n")
neighbors = {'Caen': 250, 'Rennes': 348, 'Limoges': 393, 'Dijon': 314, 'Nancy': 347, 'Calais': 294}
node = test_map.create_node(city_3, neighbors)
test_map.add_to_map(node)

city_4 = city.City("Nancy")
coordinates = {'N': [49, 41, 37], 'E': [6, 11, 5]}
city_4.set_coordinates(coordinates)
print(city_4.get_name() + "- coordinates: ")
print(city_4.get_coordinates())
print(" == 49 41 37 N 6 11 5 E \n")
neighbors = {'Paris': 347, 'Dijon': 213, 'Strasbourg': 159, 'Calais': 478}
node = test_map.create_node(city_4, neighbors)
test_map.add_to_map(node)

city_5 = city.City("Rennes")
coordinates = {'N': [47, 6, 53], 'W': [1, 40, 46]}
city_5.set_coordinates(coordinates)
print(city_5.get_name() + "- coordinates: ")
print(city_5.get_coordinates())
print(" == 47 6 53 N 1 40 46 W \n")
neighbors = {'Brest': 243, 'Nantes': 113, 'Paris': 348, 'Caen': 184}
node = test_map.create_node(city_5, neighbors)
test_map.add_to_map(node)

city_6 = city.City("Dijon")
coordinates = {'N': [46, 19, 0], 'E': [5, 1, 0]}
city_6.set_coordinates(coordinates)
print(city_6.get_name() + "- coordinates: ")
print(city_6.get_coordinates())
print(" == 46 19 0 N 5 1 0 E \n")
neighbors = {'Paris': 314, 'Lyon': 195, 'Strasbourg': 330, 'Nancy': 213}
node = test_map.create_node(city_6, neighbors)
test_map.add_to_map(node)

city_7 = city.City("Strasbourg")
coordinates = {'N': [47, 35, 0], 'E': [7, 45, 0]}
city_7.set_coordinates(coordinates)
print(city_7.get_name() + "- coordinates: ")
print(city_7.get_coordinates())
print(" == 47 35 0 N 7 45 0 E \n")
neighbors = {'Nancy': 159, 'Dijon': 330}
node = test_map.create_node(city_7, neighbors)
test_map.add_to_map(node)

city_8 = city.City("Brest")
coordinates = {'N': [48, 23, 0], 'W': [5, 29, 0]}
city_8.set_coordinates(coordinates)
print(city_8.get_name() + "- coordinates: ")
print(city_8.get_coordinates())
print(" == 48 23 0 N 5 29 0 W \n")
neighbors = {'Rennes': 243}
node = test_map.create_node(city_8, neighbors)
test_map.add_to_map(node)

city_9 = city.City("Nantes")
coordinates = {'N': [47, 50, 5], 'W': [1, 33, 10]}
city_9.set_coordinates(coordinates)
print(city_9.get_name() + "- coordinates: ")
print(city_9.get_coordinates())
print(" == 47 50 5 N 1 33 10 W \n")
neighbors = {'Bordeaux': 349, 'Limoges': 319, 'Rennes': 113}
node = test_map.create_node(city_9, neighbors)
test_map.add_to_map(node)

city_10 = city.City("Lyon")
coordinates = {'N': [46, 46, 0], 'E': [4, 50, 0]}
city_10.set_coordinates(coordinates)
print(city_10.get_name() + "- coordinates: ")
print(city_10.get_coordinates())
print(" == 46 46 0 N 4 50 0 E \n")
neighbors = {'Limoges': 411, 'Avignon': 230, 'Grenoble': 113, 'Dijon': 195}
node = test_map.create_node(city_10, neighbors)
test_map.add_to_map(node)

city_11 = city.City("Bordeaux")
coordinates = {'N': [43, 35, 14], 'E': [5, 8, 7]}
city_11.set_coordinates(coordinates)
print(city_11.get_name() + "- coordinates: ")
print(city_11.get_coordinates())
print(" == 43 35 14 N 5 8 7 E \n")
neighbors = {'Nantes': 349, 'Toulouse': 244, 'Limoges': 223}
node = test_map.create_node(city_11, neighbors)
test_map.add_to_map(node)

city_12 = city.City("Limoges")
coordinates = {'N': [44, 51, 7], 'E': [1, 15, 45]}
city_12.set_coordinates(coordinates)
print(city_12.get_name() + "- coordinates: ")
print(city_12.get_coordinates())
print(" == 44 51 7 N 1 15 45 E \n")
neighbors = {'Nantes': 319, 'Bordeaux': 223, 'Toulouse': 290, 'Lyon': 411, 'Paris': 393}
node = test_map.create_node(city_12, neighbors)
test_map.add_to_map(node)

city_13 = city.City("Grenoble")
coordinates = {'N': [44, 10, 18], 'E': [5, 43, 21]}
city_13.set_coordinates(coordinates)
print(city_13.get_name() + "- coordinates: ")
print(city_13.get_coordinates())
print(" == 44 10 18 N 5 43 21 E \n")
neighbors = {'Avignon': 221, 'Lyon': 113}
node = test_map.create_node(city_13, neighbors)
test_map.add_to_map(node)

city_14 = city.City("Toulouse")
coordinates = {'N': [43, 35, 16], 'E': [1, 26, 38]}
city_14.set_coordinates(coordinates)
print(city_14.get_name() + "- coordinates: ")
print(city_14.get_coordinates())
print(" == 43 35 16 N 1 26 38 E \n")
neighbors = {'Bordeaux': 244, 'Limoges': 290, 'Montpellier': 243}
node = test_map.create_node(city_14, neighbors)
test_map.add_to_map(node)

city_15 = city.City("Avignon")
coordinates = {'N': [42, 57, 0], 'E': [4, 49, 0]}
city_15.set_coordinates(coordinates)
print(city_15.get_name() + "- coordinates: ")
print(city_15.get_coordinates())
print(" == 42 57 0 N 4 49 0 E \n")
neighbors = {'Montpellier': 95, 'Marseille': 103, 'Grenoble': 221, 'Lyon': 230}
node = test_map.create_node(city_15, neighbors)
test_map.add_to_map(node)

city_16 = city.City("Montpellier")
coordinates = {'N': [42, 36, 43], 'E': [3, 52, 38]}
city_16.set_coordinates(coordinates)
print(city_16.get_name() + "- coordinates: ")
print(city_16.get_coordinates())
print(" == 42 36 43 N 3 52 38 E \n")
neighbors = {'Toulouse': 243, 'Avignon': 95}
node = test_map.create_node(city_16, neighbors)
test_map.add_to_map(node)

city_17 = city.City("Marseille")
coordinates = {'N': [42, 17, 47], 'E': [5, 22, 12]}
city_17.set_coordinates(coordinates)
print(city_17.get_name() + "- coordinates: ")
print(city_17.get_coordinates())
print(" == 42 17 47 N 5 22 12 E \n")
neighbors = {'Avignon': 103}
node = test_map.create_node(city_17, neighbors)
test_map.add_to_map(node)

city_18 = city.City("Nice")
coordinates = {'N': [43, 43, 12], 'E': [7, 15, 59]}
city_18.set_coordinates(coordinates)
print(city_18.get_name() + "- coordinates: ")
print(city_18.get_coordinates())
print(" == 43 43 12 N 7 15 59 E \n")
neighbors = {'Marseille': 199}
node = test_map.create_node(city_18, neighbors)
test_map.add_to_map(node)

test_map.output_map()

'''