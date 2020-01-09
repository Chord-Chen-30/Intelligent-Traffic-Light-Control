from car import Car
from car import Status
import copy
import random

STRAIGHT_CARS_CAN_PASS = 25
LEFT_CARS_CAN_PASS = 10
class State:
    def __init__(self):
        self.waiting_car_list_straight_ns = [[],[]]
        self.waiting_car_list_straight_ew = [[],[]]
        self.waiting_car_list_left_ns = [[],[]]
        self.waiting_car_list_left_ew = [[],[]]
        self.longest_waiting = 0
        self.__time = 0


    # Remove cars from waiting list -> passed car list
    def update_intersection_state(self, action,cur_time):  

        # Pcik first self.CARS_CAN_PASS cars in corresponding waiting list and kick them out
        # add them into passed_car_list and mark car.status as status.EXIT
        passed_car_list = []
        self.__time = cur_time
        if action == 'straight_ns':
            passed_cars = 0
            for i in range(0,STRAIGHT_CARS_CAN_PASS):
                if (len(self.waiting_car_list_straight_ns[0]) != 0):
                    car = self.waiting_car_list_straight_ns[0].pop(0)
                    car.get_waiting_time(cur_time)
                    car.status = Status.EXIT
                    passed_cars += 1
                    passed_car_list.append(car)
                if (len(self.waiting_car_list_straight_ns[1]) != 0):
                    car = self.waiting_car_list_straight_ns[1].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1

        elif action == 'straight_ew':
            passed_cars = 0
            for i in range(0,STRAIGHT_CARS_CAN_PASS):
                if (len(self.waiting_car_list_straight_ew[0]) != 0):
                    car = self.waiting_car_list_straight_ew[0].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1
                if (len(self.waiting_car_list_straight_ew[1]) != 0):
                    car = self.waiting_car_list_straight_ew[1].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1

        elif action == 'left_ns':
            passed_cars = 0
            for i in range(0,LEFT_CARS_CAN_PASS):
                if (len(self.waiting_car_list_left_ns[0]) != 0):
                    car = self.waiting_car_list_left_ns[0].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1
                if (len(self.waiting_car_list_left_ns[1]) != 0):
                    car = self.waiting_car_list_left_ns[1].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1

        elif action == 'left_ew':
            passed_cars = 0
            for i in range(0,LEFT_CARS_CAN_PASS):
                if (len(self.waiting_car_list_left_ew[0]) != 0):
                    car = self.waiting_car_list_left_ew[0].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1
                if (len(self.waiting_car_list_left_ew[1]) != 0):
                    car = self.waiting_car_list_left_ew[1].pop(0)
                    car.status = Status.EXIT
                    car.get_waiting_time(cur_time)
                    passed_car_list.append(car)
                    passed_cars += 1
        else:
            print(action)
            print("!?")
        # Second select cars from waiting list -> passed car list 
        # and mark them.status as status.EXIT
        
        # Might be useful, return how many cars passed after action ACTION
        return passed_cars, passed_car_list

    def update_time(self,cur_time):
        self.__time = cur_time


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
        state_cp.__time = self.__time
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

    def all_passed(self):
        if (len(self.waiting_car_list_straight_ns[0]) == 0 and \
            len(self.waiting_car_list_straight_ns[1]) == 0 and \
            len(self.waiting_car_list_straight_ew[0]) == 0 and \
            len(self.waiting_car_list_straight_ew[1]) == 0 and \
            len(self.waiting_car_list_left_ns[0]) == 0 and \
            len(self.waiting_car_list_left_ns[1]) == 0 and \
            len(self.waiting_car_list_left_ew[0]) == 0 and \
            len(self.waiting_car_list_left_ew[1]) == 0 ):

            return True

        else:
            return False
    
    def extract_features(self, action):
        # Features stand for the degree of crowdness of lanes
        straight_ns = (len(self.waiting_car_list_straight_ns[0]) + len(self.waiting_car_list_straight_ns[1]))
        straight_ew = (len(self.waiting_car_list_straight_ew[0]) + len(self.waiting_car_list_straight_ew[1]))
        left_ns = (len(self.waiting_car_list_left_ns[0]) + len(self.waiting_car_list_left_ns[1]))
        left_ew = (len(self.waiting_car_list_left_ew[0]) + len(self.waiting_car_list_left_ew[1]))
        
        earliest_arrival_time = float('inf')
        if (len(self.waiting_car_list_straight_ns[0]) > 0):
            if self.waiting_car_list_straight_ns[0][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_straight_ns[0][0].arrival_time
        if (len(self.waiting_car_list_straight_ns[1]) > 0):
            if self.waiting_car_list_straight_ns[1][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_straight_ns[1][0].arrival_time
        if (len(self.waiting_car_list_straight_ew[0]) > 0):
            if self.waiting_car_list_straight_ew[0][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_straight_ew[0][0].arrival_time
        if (len(self.waiting_car_list_straight_ew[1]) > 0):
            if self.waiting_car_list_straight_ew[1][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_straight_ew[1][0].arrival_time
        if (len(self.waiting_car_list_left_ns[0]) > 0):
            if self.waiting_car_list_left_ns[0][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_left_ns[0][0].arrival_time
        if (len(self.waiting_car_list_left_ns[1]) > 0):
            if self.waiting_car_list_left_ns[1][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_left_ns[1][0].arrival_time
        if (len(self.waiting_car_list_left_ew[0]) > 0):
            if self.waiting_car_list_left_ew[0][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_left_ew[0][0].arrival_time
        if (len(self.waiting_car_list_left_ew[1]) > 0):
            if self.waiting_car_list_left_ew[1][0].arrival_time < earliest_arrival_time:
                earliest_arrival_time = self.waiting_car_list_left_ew[1][0].arrival_time

        if earliest_arrival_time >= self.__time:
            self.longest_waiting = 0
        else :
            self.longest_waiting = self.__time - earliest_arrival_time
        return {'straight_ns':straight_ns, \
                'straight_ew':straight_ew, \
                'left_ns':    left_ns, \
                'left_ew':    left_ew,
                }

class IntersectionAgent:
    def __init__(self, list_of_cars):

        self.__time = 0 # Simulate the real time
        self.STRAIGHT_TIME_INTERVAL = 30
        self.LEFT_TIME_INTERVAL = 15

        self.__light_states = ['straight_ns','straight_ew','left_ns','left_ew']

        self.cur_light_state = 'straight_ns' # For example
        self.buffer_car_list = copy.deepcopy(list_of_cars) # Cars that have not reached intersecion (yet) but generated by test case, store here for now
        print("init  %d", len(self.buffer_car_list))
        self.discount = 0.9
        self.epsilon = 0.1
        self.alpha = 0.5
        self.state = State()

        # Features should be fixed at the beginning
        self.weights = {'straight_ns': 0, 
                        'straight_ew': 0, 
                        'left_ns'	:0,
                        'left_ew'	:0,}
                        # 'longest_waiting': 0}

        self.longest_waiting = 0
        self.passed_car_list = []

    """============Basic functions============"""

    def get_legal_action(self):
        return self.__light_states


    def all_cars_passed(self):
        return self.state.all_passed()

    # Add cars from buffer to waiting list
    def add_car_from_buffer_to_waiting(self):  
        # (self.__TIME has been increased)
        inds_to_be_popped_from_buffer = []
        # First select cars from buffer list -> waiting list
        for i, car in enumerate(self.buffer_car_list):
            if car.arrival_time < self.__time: # This car should be waiting at the intersection
                inds_to_be_popped_from_buffer.append(i)

                self.state.add_car_to_waiting_list(car)

                car.status = Status.WAITING
                car.waiting_time += car.arrival_time - self.__time

        # pop them out from buffer list, reversing is because if we did it in the 0-n order the later index will be fault
        for i in reversed(inds_to_be_popped_from_buffer):
            self.buffer_car_list.pop(i)
    


    """============Functions refer to learnging (Approximate Q learning)============"""
    # Compute  action based on Q values
    def compute_action_from_qvalues(self, state):
        action = None
        lights_choices = self.get_legal_action()

        highest_qvalue = float('inf')
        for a in lights_choices:
            qvalue = self.get_qvalue(state, a)
            # print("in compute action from qvalue: action:", a, "qvalue: ", qvalue)
            if qvalue < highest_qvalue:
                action = a
                highest_qvalue = qvalue

        # ACTION should be one of ['straight_ns','straight_ew','left_ns','left_ew']
        # if (highest_qvalue == 0): # For debug
            # print("action: %s computed from q value but zero q value (meaningless)", action)
        # if action == None:

        return action


    # Get action by random or computing
    def get_action(self, state):
        action = None
        use_our_model = (random.random()>self.epsilon)
        if not use_our_model:
            return random.choice(self.get_legal_action())
        else:
            return self.compute_action_from_qvalues(state)


    def get_qvalue(self, state, action):

        next_state = state.state_copy()
        next_state.update_intersection_state(action,self.__time)
        if action == 'straight_ns' or action == 'straight_ew':
            next_state.update_time(self.__time + self.STRAIGHT_TIME_INTERVAL)
        else:
            next_state.update_time(self.__time + self.LEFT_TIME_INTERVAL)
        features = next_state.extract_features(action)
        qvalue = 0
        # Implement dot product
        # print("action: ",action)
        for f in features:
            # print("in get qvalue: self.weights[f],  features[f]", self.weights[f], features[f])
            qvalue += self.weights[f] * features[f]
        ##print("action : ",action,"  q_value : ",qvalue)

        return qvalue
    

    def get_value(self, state):
        lights_choices = self.get_legal_action()

        highest_qvalue = float('inf')
        for a in lights_choices:
            qvalue = self.get_qvalue(state, a)
            
            if qvalue < highest_qvalue:
                highest_qvalue = qvalue
        
        return highest_qvalue

        # features = state.extract_features("UNUSED")
        # value = 0
        # for f in features:
        #     value += features[f]*self.weights[f]

        # return value

    def reward(self, state, action):

        if action == 'straight_ns':
            max_lane = max(len(state.waiting_car_list_straight_ns[0]), len(state.waiting_car_list_straight_ns[1]))
        elif action == 'straight_ew':
            max_lane = max(len(state.waiting_car_list_straight_ew[0]), len(state.waiting_car_list_straight_ew[1]))
        elif action == 'left_ns':
            max_lane = max(len(state.waiting_car_list_left_ns[0]), len(state.waiting_car_list_left_ns[1]))
        elif action == 'left_ew':
            max_lane = max(len(state.waiting_car_list_left_ew[0]), len(state.waiting_car_list_left_ew[1]))

        next_state = self.state.state_copy()

        cars_passed, temp_pass_car_list = next_state.update_intersection_state(action,self.__time)
        if action == 'straight_ns' or action == 'straight_ew':
            next_state.update_time(self.__time + self.STRAIGHT_TIME_INTERVAL)
        else:
            next_state.update_time(self.__time + self.LEFT_TIME_INTERVAL)
        feature = next_state.extract_features(action)

        reward = max_lane * cars_passed 
        return (reward, next_state)

    def generator_test_weights(self):
        self.weights = {'straight_ns': 13.364490640765416, 
                        'straight_ew': 39.7475246716086, 
                        'left_ns': 98.23941235499537, 
                        'left_ew': 847.6506358018852}

    def update_weight(self, state, action, next_state, reward):
        """ YOUR CODE HERE"""
        # Update reward based on reward
        features = state.extract_features(action)
        # Calculate the difference 
        diff = reward + self.discount * self.get_value(next_state) - self.get_qvalue(state, action)
        # Update our weights
        sum_weight = 1
        for f in features:
            self.weights[f] += self.alpha*diff*features[f]
            sum_weight += self.weights[f]

        for f in features:
            self.weights[f] /= sum_weight * 0.001

    def update_state(self, action):
        # update state
        # Add waiting time to each car still waiting
        temp_time = self.__time
        if action == 'straight_ns' or action == 'straight_ew':
            self.__time += self.STRAIGHT_TIME_INTERVAL
        else:
            self.__time += self.LEFT_TIME_INTERVAL
        self.add_car_from_buffer_to_waiting()
        passed_cars , temp_pass_car_list = self.state.update_intersection_state(action,temp_time)
        self.state.update_time(self.__time)
        self.passed_car_list += temp_pass_car_list




    """============Training and testing============"""
    def train(self):
        while (not self.all_cars_passed() or (self.buffer_car_list != [])):
            # print("time : ",self.__time)
            action = self.get_action(self.state)
            # print(action)
            reward, next_state = self.reward(self.state, action)
            self.update_weight(self.state, action, next_state, reward)
            self.update_state(action)


    def test(self, test_cars):
        self.__time = 0 # Simulate the real time
        self.epsilon = 0
        self.buffer_car_list = test_cars
        self.passed_car_list = []
        self.state = State()

        # for f in self.weights:
        #     self.weights[f] = -self.weights[f]
            
        for f in self.weights:
            self.weights[f] = abs(self.weights[f])

        while (not self.all_cars_passed()) or (self.buffer_car_list != []):
            
            # print("time : ",self.__time)
            # print(self.state.waiting_car_list_straight_ew)
            action = self.get_action(self.state)
            # print(action)
            self.update_state(action)

            # for car in self.passed_car_list:
            #     print(car)

        total_waiting_time = 0
        cars_passed = len(self.passed_car_list)
        for car in self.passed_car_list:
            total_waiting_time += car.waiting_time

        avg_waiting_time = float(total_waiting_time / cars_passed)
        print(cars_passed)
        print("Our model: avg wait time: ", avg_waiting_time)
        
        return avg_waiting_time
        # return avg_waiting_time
    
    # Return average time using a period traffic light scheme
    def stupid_ai(self, test_cars):
        self.__time = 0 # Simulate the real time
        period_action = 0
        self.buffer_car_list = test_cars
        self.passed_car_list = []
        self.state = State()

        while (not self.all_cars_passed() or (not self.buffer_car_list == [])):
            action = self.get_legal_action()[period_action]
            self.update_state(action)

            period_action += 1
            if period_action == 4:
                period_action = 0

        total_waiting_time = 0
        cars_passed = len(self.passed_car_list)
        print("car passed in stupid AI: ", cars_passed)
        for car in self.passed_car_list:
            total_waiting_time += car.waiting_time

        avg_waiting_time = float(total_waiting_time / cars_passed)
        print("Stupid: avg wait time: ", avg_waiting_time)
        return avg_waiting_time
        # return avg_waiting_time

