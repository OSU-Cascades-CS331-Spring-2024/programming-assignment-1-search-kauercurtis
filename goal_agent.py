import argparse
import city
import map
import actions

'''

    goal_agent - a goal based agent for maps
    Name: Curtis Kauer
    
'''

# ArgumentParser object to handle parsing command line
argument_parser = argparse.ArgumentParser()

argument_parser.add_argument("--map_file", "-f", type=str, required=True, help='file with map data')
argument_parser.add_argument("--start_city", "-A", type=str, help='starting location')
argument_parser.add_argument("--end_city", "-B", type=str, help='ending location')
argument_parser.add_argument("--search_method", "-s", type=str, default='bfs')

arguments = argument_parser.parse_args()

def main():
    file = arguments.map_file
    searching_method = arguments.search_method
    starting_city = arguments.start_city
    goal_city = arguments.end_city
    
    map_data = open(file, "r")
    
    graph = map.Map()
    
    # reading data and adding to the map
    # caluclates the longitude and longitude
    while True:
        line = map_data.readline()
        if not line:
            break
            
        line_coordinate_neighbor_split = line.split('-->')
        city_data = line_coordinate_neighbor_split[0]
        neighbors = line_coordinate_neighbor_split[1]
        
        cit_data = city_data.strip()
        neighbors = neighbors.strip()
        
        city_data = city_data.split()
        
        new_city = city.City(city_data[0])
        new_city.set_latitude_direction(city_data[4])
        latitude_degree = city_data[1]
        latitude_minutes = city_data[2]
        latitude_seconds = city_data[3]
        latitude = int(latitude_degree) + (int(latitude_minutes) / 60) + (int(latitude_seconds) / 3600)
        new_city.set_latitude(latitude)
        new_city.set_longitude_direction(city_data[8])
        longitude_degree = city_data[5]
        longitude_minutes = city_data[6]
        longitude_seconds = city_data[7]
        longitude = int(longitude_degree) + (int(longitude_minutes) / 60) + (int(longitude_seconds) / 3600)
        new_city.set_longitude(longitude)
        
        graph.add_city(new_city)
        
        neighbors = neighbors.split('va-')
        
        for neighbor in neighbors:
            if neighbor == '':
                continue
            
            neighbor = neighbor.strip()
            neighbor = neighbor.split(' ')
            graph.add_edge(new_city.city_name, neighbor[0], neighbor[1])
    
    # intialize actions to take
    actions_to_take = actions.Actions(graph)
    
    if starting_city == None or goal_city == None:
        solution_file = open("solutions.txt", "w")
        starting_cities = ["brest", "montpellier", "strasbourg", "paris", "grenoble", "brest", "grenoble", "nice", "caen"]
        goal_city = ["nice", "calais", "bordeaux", "grenoble", "paris", "grenoble", "brest", "nantes", "strasbourg"]
        
        for index in range(len(starting_cities)):
            city_A = starting_cities[index]
            city_B = goal_city[index]
            solution_file.write(city_A + " --> " + city_B + "\n")
            actions_to_take.bfs(city_A, city_B)
            solution_file.write("bfs - explored: " + str(actions_to_take.get_explored()) + " expanded: " + str(actions_to_take.get_expanded()) + " maintained: " + str(actions_to_take.get_maintained()) + "\n")
            solution_file.write("path: " + str(actions_to_take.visited) + " cost: " + str(actions_to_take.get_cost()) + "\n")
            
            actions_to_take.ids(starting_cities[index], goal_city[index])
            solution_file.write("dls - explored: " + str(actions_to_take.get_explored()) + " expanded: " + str(actions_to_take.get_expanded()) + " maintained: " + str(actions_to_take.get_maintained()) + "\n")
            solution_file.write("path: " + str(actions_to_take.visited) + " cost: " + str(actions_to_take.get_cost()) + "\n")
            
            actions_to_take.ucs(starting_cities[index], goal_city[index])
            solution_file.write("ucs - explored: " + str(actions_to_take.get_explored()) + " expanded: " + str(actions_to_take.get_expanded()) + " maintained: " + str(actions_to_take.get_maintained()) + "\n")
            solution_file.write("path: " + str(actions_to_take.visited) + " cost: " + str(actions_to_take.get_cost()) + "\n")
            
            actions_to_take.astar(starting_cities[index], goal_city[index])
            solution_file.write("astar - explored: " + str(actions_to_take.get_explored()) + " expanded: " + str(actions_to_take.get_expanded()) + " maintained: " + str(actions_to_take.get_maintained()) + "\n")
            solution_file.write("path: " + str(actions_to_take.visited) + " cost: " + str(actions_to_take.get_cost()) + "\n")
            
            solution_file.write("\n")
            
    elif searching_method == 'astar':
        actions_to_take.astar(starting_city, goal_city)
        print("astar - explored: ", actions_to_take.get_explored(), " expanded: ", actions_to_take.get_expanded(), " maintained: ", actions_to_take.get_maintained())
        print("path: ", actions_to_take.visited, " cost: ", actions_to_take.get_cost())
        # actions_to_take.output_frontier()
    elif searching_method == 'dls':
        actions_to_take.ids(starting_city, goal_city)
        print("dls - explored: ", actions_to_take.get_explored(), " expanded: ", actions_to_take.get_expanded(), " maintained: ", actions_to_take.get_maintained())
        print("path: ", actions_to_take.visited, " cost: ", actions_to_take.get_cost())
        # actions_to_take.output_frontier()
    elif searching_method == 'ucs':
        actions_to_take.ucs(starting_city, goal_city)
        print("ucs - explored: ", actions_to_take.get_explored(), " expanded: ", actions_to_take.get_expanded(), " maintained: ", actions_to_take.get_maintained())
        print("path: ", actions_to_take.visited, " cost: ", actions_to_take.get_cost())
    else:
        actions_to_take.bfs(starting_city, goal_city)   
        print("bfs - explored: ", actions_to_take.get_explored(), " expanded: ", actions_to_take.get_expanded(), " maintained: ", actions_to_take.get_maintained())
        print("path: ", actions_to_take.visited, " cost: ", actions_to_take.get_cost())
        
if __name__ == "__main__":
    main()