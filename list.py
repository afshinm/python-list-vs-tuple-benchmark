import time
from random import randint


x = 1000000

demo_list = []

# add items to list
while x > 0:
    demo_list.append(x)
    x = x - 1

start = time.clock()

# find random items from list
y = 2000000
while y > 0:
    item = demo_list[randint(0, 999999)]
    y = y - 1

# print the elapsed time
print (time.clock() - start)
