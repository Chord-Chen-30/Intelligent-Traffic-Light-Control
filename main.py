from car import Car
from car import Status
from intersectionAgent import IntersectionAgent
from util import generate_cars

import time
import xlwt

def main():

    

    train_cars = generate_cars(mode=0)
    test_cars = generate_cars(mode=0)
    print("Cars generated")
    intersec_agnet = IntersectionAgent(train_cars[0:300])
    print("Agent init done")

    intersec_agnet.train()
    print("Agent training done")
    #print("weight: ", intersec_agnet.weights)
    time.sleep(3)

 
    # Compare performance
    ref_result = intersec_agnet.stupid_ai(test_cars[0:300])
    # test_cars = generate_cars(mode=1)
    our_result = intersec_agnet.test(test_cars[0:300])
    time.sleep(1)


    print(len(intersec_agnet.passed_car_list))
    return ref_result,our_result

if __name__ =='__main__':
    wbb = xlwt.Workbook()
    wss = wbb.add_sheet('result')
    wss.write(0,0,'Stupid AI')
    wss.write(0,1,'Our AI')
    # ref_result = 0
    # our_result = 0
    for i in range(50):
        print("\n\n")
        ref_result,our_result = main()
        wss.write(i+1,0,ref_result)
        wss.write(i+1,1,our_result)
        print("num",i)
    wbb.save('./result1111.xls')