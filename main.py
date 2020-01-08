from car import Car
from car import Status
from intersectionAgent import IntersectionAgent
from util import generate_cars



def main():
    train_cars = generate_cars(mode=0)
    print("Cars generated")
    intersec_agnet = IntersectionAgent(train_cars[0:500])
    print("Agent init done")

    intersec_agnet.train()
    print("Agent training done")
    print("weight: ", intersec_agnet.weights)
    # test_cars = generate_cars(mode=1)
    intersec_agnet.test(train_cars[0:500])

    # Compare performance
    intersec_agnet.stupid_ai(train_cars[0:500])


    print(len(intersec_agnet.passed_car_list))


if __name__ =='__main__':
    main()