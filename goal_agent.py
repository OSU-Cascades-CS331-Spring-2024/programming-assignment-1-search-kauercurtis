import argparse
import city
import map

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
        neighbor_dictionary = {}
        graph = map.Map()
        
        for neighbor in neighbors:
            if neighbor == '':
                continue
            
            neighbor = neighbor.strip()
            neighbor = neighbor.split(' ')
            neighbor_dictionary[neighbor[0]] = neighbor[1]
    
        graph.add_to_map(new_city, neighbor_dictionary)
    
    # TODO: create map and add city objects
    
if __name__ == "__main__":
    main()