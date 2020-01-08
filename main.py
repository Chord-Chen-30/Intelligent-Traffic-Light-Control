from car import Car
from car import Status
from intersectionAgent import IntersectionAgent
from util import generate_cars

import time

def main():
    train_cars = generate_cars(mode=0)
    print("Cars generated")
    intersec_agnet = IntersectionAgent(train_cars[0:3000])
    print("Agent init done")

    intersec_agnet.train()
    print("Agent training done")
    time.sleep(3)

    # print("weight: ", intersec_agnet.weights)
    # Compare performance
    intersec_agnet.stupid_ai(train_cars[0:500])
    # test_cars = generate_cars(mode=1)
    intersec_agnet.test(train_cars[0:500])
    time.sleep(1)


    print(len(intersec_agnet.passed_car_list))


if __name__ =='__main__':
    main()