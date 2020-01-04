from enum import Enum

class status(Enum):
    WAITING = 1   # Waiting for green light
    INTERSEC = 2  # In the intersection
    EXIT = 3      # Passed the intersection


class Car:
    
    # STATUS should be status.WAITING or status.EXIT
    def __init__(self, index, arrival_time, coming_direction, action, status, waiting_time=0):
        self.index = index # For debug maybe
        self.arrival_time = int(arrival_time)
        self.coming_direction = coming_direction
        self.action = action
        self.status = status
        self.waiting_time = int(waiting_time)

    # Increase waiting time by TIME
    def increase_waiting_time(self, time):
        self.waiting_time += time
    
    # Change the status of car to STATUS(status.EXIT or status.WAITING)
    def change_status(self, status):
        if (self.status == status):
            print("Change status to the same one!") # Should not happen
        self.status = status
    

    # For debugging
    # print(car) is ok now
    def __str__(self):
        return "car index: %s   arrival_time: %s   status: %s  action: %s   waiting_time: %s" % \
                (self.index, self.arrival_time, self.status, self.action, self.waiting_time)
    

