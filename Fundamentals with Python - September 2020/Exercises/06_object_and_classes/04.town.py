class Town:
    latitude = None
    longitude = None

    def __init__(self, name):
        self.name = name

    def set_latitude(self, latitude):
        Town.latitude = latitude

    def set_longitude(self, longitude):
        Town.longitude = longitude

    def __repr__(self):
        output = f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
        return output


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
