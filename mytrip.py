''' This is a Trip module '''


class Trip:
    ''' This is trip class '''

    def __init__(self, source, dest, dist):
        self.source = source
        self.dest = dest
        self.dist = dist

        if self.dist < 0:
            raise Exception("Sorry, Please provide a valid distance")

    def origin(self):
        ''' This function will return origin '''
        return self.origin

    def destination(self):
        ''' This function will return destination '''
        return self.origin

    def distance(self):
        ''' This function will return distance '''
        return self.dist

    def compute_fare(self):
        ''' This function will compute and return total fare '''
        fare_per_km = 10
        return fare_per_km * self.dist

    def compute_travel_time(self):
        ''' This function will return total travel time '''
        time_per_km = 5
        return time_per_km * self.dist


class FlightTrip(Trip):
    ''' This is flighttrip class '''

    def __init__(self, source, dest, dist, operator, speed):
        super().__init__(source, dest, dist)

        self.operator = operator
        self.speed = speed
        self.fare_per_km = 0

    def compute_fare(self):
        ''' This function will compute and return fare for flight '''
        if self.operator == "indigo":
            self.fare_per_km = 20
        else:
            self.fare_per_km = 30

        return self.fare_per_km * self.dist

    def compute_travel_time(self):
        ''' This function will return travel time for flight '''
        return self.dist / self.speed


OBJ1 = Trip("pune", "chennai", 1000)
# OBJ2 = FlightTrip("indigo", 500)
