import xlwt
import xlrd
from car import Car
from car import Status

NUM_OF_CARS = 5

# mode 0 generate cars for training
# mode 1 generate cars for testing
def generate_cars(mode=0):
    
    car_list = []

    if mode == 0:

        # # Write
        # workbook = xlwt.Workbook(encoding='utf-8')       #新建工作簿
        # sheet1 = workbook.add_sheet("cars")    #新建sheet

        # sheet1.write(0,0,"car index")      #第1行第1列数据
        # sheet1.write(0,1,"arrival_time")      #第1行第2列数据
        # sheet1.write(0,2,"action")      #第1行第3列数据
        # sheet1.write(0,3,"coming_direction")      #第1行第4列数据
        # sheet1.write(0,4,"waiting_time")      #第1行第5列数据


        # for i in range(1, NUM_OF_CARS+1):
        #     sheet1.write(i,0,str(i))      #第2行第1列数据 index
        #     sheet1.write(i,1,str(i+1))      #第2行第2列数据 arrval time
        #     sheet1.write(i,2,"south")      #第2行第3列数据  coming direction
        #     sheet1.write(i,3,"straight")      #第2行第4列数据  action
        #     sheet1.write(i,4,"waiting")      #第2行第5列数据  status
        #     sheet1.write(i,5,'0')      #第2行第6列数据  waiting time

        # try:
        #     workbook.save('cars.xls') #保存
        # except:
        #     print("Remove the current excel of cars first\n")
        #     exit(0)


        # Read
        book = xlrd.open_workbook('cars2.xls')
        sheet1 = book.sheets()[0]

        nrows = sheet1.nrows
        print("rows",nrows)
        for i in range(1,nrows):

            index = sheet1.cell(i,0).value
            arrival_time = sheet1.cell(i,1).value
            coming_direction = sheet1.cell(i,2).value
            action = sheet1.cell(i,3).value
            # status = sheet1.cell(i,4).value
            waiting_time = sheet1.cell(i,5).value
        
            status = Status.WAITING
        
            c = Car(int(index), int(arrival_time), coming_direction, action, status ,int(waiting_time))
        
            car_list.append(c)

        # print(car_list)

        return car_list



    elif mode == 1:
        pass
