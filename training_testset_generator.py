import xlwt
import random
wb = xlwt.Workbook() # new a workbook

ws = wb.add_sheet('test1') # new a sheet in the wb

ws.write(0,0,"car index")       
ws.write(0,1,"arrival_time")     
    
ws.write(0,2,"coming_direction") 
ws.write(0,3,"action")  
ws.write(0,4,"status")    
ws.write(0,5,"waiting_time")    

def ws_write(car_num, now_sec, action, coming_direction):
    ws.write(car_num, 1, now_sec) # arrive time
    ws.write(car_num, 2, coming_direction) #coming_direction
    ws.write(car_num, 3, action)  #action




data_num = 5000
threshold_south =0.992
threshold_north = 0.98
threshold_east = 0.995
threshold_west = 0.92

# to print some info of dataset
num_straight = data_num
num_south = 0
num_north = 0
num_west = 0
num_east = 0
straight_north = 0
straight_south = 0
straight_east = 0
straight_west = 0


# for column 0 
for i in range(data_num):
    ws.write(i+1,0,i)
    ws.write(i+1,4,0)
    ws.write(i+1,5,0)

# for column 1
def time_to_sec(hour,mins,sec):
    return hour*3600 + mins*60 + sec

def action_selection(coming_direction,incoming):
    global straight_south,straight_north,straight_west,straight_east
    ran = random.uniform(0.9,1.2)
    incoming *= ran
    if (coming_direction == 'south' and incoming > 0.95) :
        straight_south += 1
        return True
    elif (coming_direction == 'north'and incoming > 0.991) :
        straight_north += 1
        return True
    elif (coming_direction == 'east'and incoming > 0.95) :
        straight_east += 1
        return True
    elif (coming_direction == 'west'and incoming > 0.85) :
        straight_west += 1
        return True
    
    global num_straight
    num_straight -=1
    return False


car_num = 0
now_sec = 0
while (car_num < data_num):
    random_south = random.random()
    random_north = random.random()
    random_east = random.random()
    random_west = random.random()
    now_sec += 1
    t_west = threshold_west * random.uniform(0.8,1.25)
    t_east = threshold_east * random.uniform(0.8,1.25) 
    t_north = threshold_north * random.uniform(0.8,1.25)
    t_south = threshold_south * random.uniform(0.8,1.25) 
    # for coming from south
    if (random_south > t_south ) :
        car_num +=1
        num_south +=1
        coming_direction = 'south'

        if (action_selection(coming_direction,random_south) ) :
            action = 'straight'
        else :
            action = 'left'
        
        ws_write(car_num, now_sec, action, coming_direction)
        
        if (car_num >= data_num):
            break
    # for coming from north
    if (random_north > t_north ) :
        car_num +=1
        coming_direction = 'north'
        num_north +=1
        if (action_selection(coming_direction,random_north) ) :
            action = 'straight'
        else :
            action = 'left'
        
        ws_write(car_num, now_sec, action, coming_direction)
        if (car_num >= data_num):
            break
    # for coming from east
    if (random_east > t_east ) :
        car_num +=1
        num_east +=1
        coming_direction = 'east'

        if (action_selection(coming_direction,random_east) ) :
            action = 'straight'
        else :
            action = 'left'
        
        ws_write(car_num, now_sec, action, coming_direction)
        if (car_num >= data_num):
            break
    # for coming from west
    if (random_west > t_west ) :
        car_num +=1
        coming_direction = 'west'
        num_west += 1
        if (action_selection(coming_direction,random_west) ) :
            action = 'straight'
        else :
            action = 'left'

        ws_write(car_num, now_sec, action, coming_direction)
        if (car_num >= data_num):
            break



print("all_time:",now_sec)
print("num_straight: ",num_straight)
print("cars from south: ",num_south)
print("cars from north: ",num_north)
print("cars from east: ", num_east)
print("cars from west: ", num_west)
print("straight_north",straight_north)
print("straight_south",straight_south)
print("straight_east",straight_east)
print("straight_west",straight_west)

ws.col(7).width = 256 *15
ws.col(1).width = 256 *15
ws.col(2).width = 256 *15
ws.write(3,7,'num_straight')
ws.write(4,7,'cars from south')
ws.write(5,7,'cars from north')
ws.write(6,7,'cars from east')
ws.write(7,7,'cars from west')

ws.write(3,8,num_straight)
ws.write(4,8,num_south)
ws.write(5,8,num_north)
ws.write(6,8,num_east)
ws.write(7,8,num_west)




wb.save('./carsasdf.xls')

