import time
from random import randint


x = 1000000

temp_list = []

# create temp list and then convert it to tuple
while x > 0:
    temp_list.append(x)
    x = x - 1

# convert list to tuple
demo_tuple = tuple(temp_list)

start = time.clock()

# random find elements from tuple
y = 2000000
while y > 0:
    item = demo_tuple[randint(0, 999999)]
    y = y - 1

print (time.clock() - start)
