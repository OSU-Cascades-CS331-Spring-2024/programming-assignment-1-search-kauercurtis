import argparse
import city
import map
import actions

'''

    goal_agent - a goal based agent for maps
    Name: Curtis Kauer
    
'''

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
        
        neighbors = neighbors.split('va-')
        
        for neighbor in neighbors:
            if neighbor == '':
                continue
            
            neighbor = neighbor.strip()
            neighbor = neighbor.split(' ')
            graph.add_edge(new_city.city_name, neighbor[0], neighbor[1])

    actions_to_take = actions.Actions(graph)
        
    if searching_method == 'bfs':
        actions_to_take.bfs(starting_city, goal_city)
        actions_to_take.output_visited()
        actions_to_take.output_frontier()
    elif searching_method == 'dls':
        actions_to_take.ids(starting_city, goal_city)
        actions_to_take.output_visited()
        actions_to_take.output_frontier()
    
if __name__ == "__main__":
    main()