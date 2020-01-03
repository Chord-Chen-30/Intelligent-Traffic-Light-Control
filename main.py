from car import Car
from intersectionAgent import IntersectionAgent


# mode 0 generate cars for training
# mode 1 generate cars for testing
def generate_cars(mode=0):
    """ YOUR CODE HERE"""
    
    # Generate list of cars (Read from file?)
    # Then
    # return list_of_cars
    pass


def main():
    train_cars = generate_cars(mode=0)

    intersec_agnet = IntersectionAgent(train_cars)

    intersec_agnet.train()

    test_cars = generate_cars(mode=1)
    intersec_agnet.test(test_cars)



if __name__ =='__main__':
    main()