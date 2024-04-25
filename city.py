class City: 

    def __init__(self, name):
        self.city_name = name
        self.latitude_direction = ''
        self.latitude = 0
        self.longitude_direction = ''
        self.longitude = 0
    
    def get_name(self):
        return self.city_name;
    
    def set_latitude_direction(self, direction):
        self.latitude_direction = direction
    
    def set_latitude(self, latitude):
        self.latitude = latitude
        
    def set_longitude_direction(self, direction):
        self.longitude_direction = direction
   
    def set_longitude(self, longitude):
        self.longitude = longitude

