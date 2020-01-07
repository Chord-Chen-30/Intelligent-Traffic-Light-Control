from car import Car
from car import status
import copy
import random


class State:
    def __init__(self):
    	self.waiting_car_list_straight_ns = [[],[]]
        self.waiting_car_list_straight_ew = [[],[]]
        self.waiting_car_list_left_ns = [[],[]]
        self.waiting_car_list_left_ew = [[],[]]
    	self.longest_waiting = 0;

        self.passed_car_list = []

    def update_intersection_state(self, action):  

        # Pcik first self.CARS_CAN_PASS cars in corresponding waiting list and kick them out
        # add them into passed_car_list and mark car.status as status.EXIT
        if action == 'straight_ns':
            passed_cars = 0
            while  passed_cars < self.CARS_CAN_PASS:
            	if (len(self.waiting_car_list_straight_ns[0]) != 0):
                	car = self.waiting_car_list_straight_ns[0].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
	                passed_cars += 1
            	if (len(self.waiting_car_list_straight_ns[1]) != 0):
                	car = self.waiting_car_list_straight_ns[1].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
               	 	passed_cars += 1

        elif action == 'straight_ew':
            passed_cars = 0
            while  passed_cars < self.CARS_CAN_PASS:
            	if (len(self.waiting_car_list_straight_ew[0]) != 0):
                	car = self.waiting_car_list_straight_ew[0].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
	                passed_cars += 1
            	if (len(self.waiting_car_list_straight_ew[1]) != 0):
                	car = self.waiting_car_list_straight_ew[1].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
               	 	passed_cars += 1
        elif action == 'left_ns':
            passed_cars = 0
            while  passed_cars < self.CARS_CAN_PASS:
            	if (len(self.waiting_car_list_left_ns[0]) != 0):
                	car = self.waiting_car_list_left_ns[0].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
	                passed_cars += 1
            	if (len(self.waiting_car_list_left_ns[1]) != 0):
                	car = self.waiting_car_list_left_ns[1].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
               	 	passed_cars += 1
        elif action == 'left_ew':
            passed_cars = 0
            while  passed_cars < self.CARS_CAN_PASS:
            	if (len(self.waiting_car_list_left_ew[0]) != 0):
                	car = self.waiting_car_list_left_ew[0].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
	                passed_cars += 1
            	if (len(self.waiting_car_list_left_ew[1]) != 0):
                	car = self.waiting_car_list_left_ew[1].pop(0)
	                car.status = status.EXIT
	                self.passed_car_list.append(car)
               	 	passed_cars += 1
        else:
            print("!?")
        # Second select cars from waiting list -> passed car list 
        # and mark them.status as status.EXIT
        
        # Might be useful, return how many cars passed after action ACTION
        return passed_cars
    
    #
	def state_copy(self):
		state_cp =  State();
		state_cp.waiting_car_list_straight_ns[0] = self.waiting_car_list_straight_ns[0][:];
		state_cp.waiting_car_list_straight_ns[1] = self.waiting_car_list_straight_ns[1][:];
		state_cp.waiting_car_list_straight_ew[0] = self.waiting_car_list_straight_ew[0][:];
		state_cp.waiting_car_list_straight_ew[1] = self.waiting_car_list_straight_ew[1][:];
		state_cp.waiting_car_list_left_ew[0] = self.waiting_car_list_left_ew[0][:];
		state_cp.waiting_car_list_left_ew[1] = self.waiting_car_list_left_ew[1][:];
		state_cp.waiting_car_list_left_ns[0] = self.waiting_car_list_left_ns[0][:];
		state_cp.waiting_car_list_left_ns[1] = self.waiting_car_list_left_ns[1][:];
		state_cp.longest_waiting = self.longest_waiting;
		return state_cp;
    

    # Add one car to waiting list of this intersection
    def add_car_to_waiting_list(self, car):

        # Car that go straight
        if car.action == 'straight':
            if car.comming_direction == 'north':
                self.waiting_car_list_straight_ns[0].append(car)
            elif car.comming_direction == 'south':
                self.waiting_car_list_straight_ns[1].append(car)
            elif car.comming_direction == 'east':
                self.waiting_car_list_straight_ew[0].append(car)
            elif car.comming_direction == 'west':
                self.waiting_car_list_straight_ew[1].append(car)
        
        # Car that turn left
        elif car.action == 'left':
            if car.comming_direction == 'north':
                self.waiting_car_list_left_ns[0].append(car) 
            elif car.comming_direction == 'south':
                self.waiting_car_list_left_ns[1].append(car)
            elif car.comming_direction == 'east':
                self.waiting_car_list_left_ew[0].append(car)
            elif car.comming_direction == 'west':
                self.waiting_car_list_left_ew[1].append(car)
    

class IntersectionAgent:
    def __init__(self, list_of_cars):

        self.__time = 0 # Simulate the real time
        self.TIME_INTERVAL = 20
        self.CARS_CAN_PASS = 10
        self.epsilon = 0.5 # How much probability we choose to take a random action
        self.__light_states = ['straight_ns','straight_ew','left_ns','left_ew']

        self.cur_light_state = 'straight_ns' # For example
        self.buffer_car_list = copy.deepcopy(list_of_cars) # Cars that have not reached intersecion (yet) but generated by test case, store here for now

        self.state = State()


        # Features should be fixed at the beginning
        self.weights = {'straight_ns': 0, 
                        'straight_ew': 0, 
                        'left_ns'	:0,
                        'left_ew'	:0,
                        'longest_waiting': 0}

        self.longest_waiting = 0


    """============Basic functions============"""

    def get_legal_action(self):
        return self.__light_states

    # Update all cars' status after ?? seconds passed
    # Include their status and waiting time
    def update_intersection_state(self, action):  
        # (self.__TIME has been increased)
        inds_to_be_popped_from_buffer = []
        # First select cars from buffer list -> waiting list
        for i, car in enumerate(self.buffer_car_list):
            if car.arrival_time < self.__time: # This car should be waiting at the intersection
                inds_to_be_popped_from_buffer.append(i)

                self.state.add_car_to_waiting_list(car)

                car.status = status.WAITING
                car.waiting_time += car.arrival_time - self.__time

        # pop them out from buffer list, reversing is because if we did it in the 0-n order the later index will be fault
        for i in reversed(inds_to_be_popped_from_buffer):
            self.buffer_car_list.pop(i)

        # Pcik first self.CARS_CAN_PASS cars in corresponding waiting list and kick them out
        # add them into passed_car_list and mark car.status as status.EXIT
        # Select cars from waiting list -> passed car list 
        self.state.update_intersection_state(action)

    
    def time_elapse(self):
        self.__time += self.TIME_INTERVAL


    def all_cars_passed(self):
        if (self.waiting_car_list_straight_ns == [] and \
            self.waiting_car_list_straight_ew == [] and \
            self.waiting_car_list_left_ew     == [] and \
            self.waiting_car_list_left_ns     == []):

            return True
        else:
            return False

    # ACTION should be 'straight_ns' or 'straight_ew' or ...
    def get_next_state(self, state, action):
        """YOUR CODE HERE"""
        # This function served as off-line planning ?
        pass


    """============Functions refer to learnging (Approximate Q learning)============"""
    # Compute  action based on Q values
    def compute_action_from_qvalues(self, state):
        action = None
        lights_choices = self.get_legal_action()

        highest_qvalue = -float('inf')
        for a in lights_choices:
            qvalue = self.get_qvalue(state, a)
            if qvalue > highest_qvalue:
                action = a
                highest_qvalue = qvalue

        # ACTION should be one of ['straight_ns','straight_ew','left_ns','left_ew']
        if (highest_qvalue == 0): # For debug
            print("action: %s computed from q value but zero q value (meaningless)", action)
        return action


    # Get action by random or computing
    def get_action(self, state):
        action = None
        choosing_random = (random.random()>self.epsilon)
        if choosing_random:
            return random.choice(self.get_legal_action())
        else:
            return self.compute_action_from_qvalues(state)


    def get_qvalue(self):
        """ YOUR CODE HERE"""
        pass
    
    def get_value(self):
        """ YOUR CODE HERE"""
        pass

    def reward(self, state, action, next_state):


    	return reward


    def update(self, state, action, next_state, reward):
        """ YOUR CODE HERE"""
        # Update reward based on reward
        features = self.extract_features(state, action)
        # Calculate the difference 
        diff = reward + self.discount * self.get_value(next_state) - self.get_qvalue(state, action)
        # Update our weights
        for f in features:
          self.weights[f] += self.alpha*diff*features[f]
        pass


    def extract_features(self, state, action):
        # Extract features based on STATE and ACTION
        """ YOUR CODE HERE"""
        # Features stand for the degree of crowdness of lanes
        straight_ns = (len(state.waiting_car_list_straight_ns[0]) + len(state.waiting_car_list_straight_ns[1])) //10
        straight_ew = (len(state.waiting_car_list_straight_ew[0]) + len(state.waiting_car_list_straight_ew[1])) //10
        left_ns = (len(state.waiting_car_list_left_ns[0]) + len(state.waiting_car_list_left_ns[1])) //10
        left_ew = (len(state.waiting_car_list_left_ew[0]) + len(state.waiting_car_list_left_ew[1])) //10
        

        return (straight_ns, straight_ew, left_ns, left_ew)


    """============Training and testing============"""
    def train(self):
        """ YOUR CODE HERE"""
        while self.waiting_car_list != []:
            self.time_elapse()
            self.update_intersection_status()

            # Choose green light and learn

        pass

    def test(self, test_cars):
        """ YOUR CODE HERE"""
        pass


    def stupid_ai(self, test_cars):
        """ YOUR CODE HERE"""
        # Solve the problem in a regular way, i.e. a evenly scheme to control traffic light
        # And calculate the total waiting time (or sth. else we use to evaluate our model)
        pass

