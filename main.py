from car import Car
from car import status
from intersectionAgent import IntersectionAgent
from util import generate_cars



def main():
    train_cars = generate_cars(mode=0)

    intersec_agnet = IntersectionAgent(train_cars)

    intersec_agnet.train()

    test_cars = generate_cars(mode=1)
    intersec_agnet.test(test_cars)

    # Compare performance
    intersec_agnet.stupid_ai(test_cars)



if __name__ =='__main__':
    main()