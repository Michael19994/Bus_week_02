class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passenger_number = 0
        self.passenger_list = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return self.passenger_number
    
    def pick_up(self, person):
        self.passenger_number += 1 
        self.passenger_list.append(person)
    
    def drop_off(self, person):
        self.passenger_number -= 1
        self.passenger_list.remove(person)

    def empty(self):
        self.passenger_number = 0
        self.passenger_list.clear()

    def pick_up_from_stop(self, bus_stop):
        self.passenger_number += bus_stop.queue_len
        bus_stop.clear()
        

