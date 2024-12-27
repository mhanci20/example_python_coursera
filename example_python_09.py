#!/usr/bin/env python3

#zork = 0
#print('Before', zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + 1
#    print(zork, thing)
#print('After', zork)

#zork = 0
#print('Before', zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + thing
#    print(zork, thing)
#print('After', zork)

#count = 0
#sum = 0
#print('Before', count, sum)
#for value in [9, 41, 12, 3, 74, 15]:
#    count = count + 1
#    sum = sum + value
#    print(count, sum, value)
#print('After', count, sum, sum / value)

#print('Before')
#for value in [9, 41, 12, 3, 74, 15]:
#    if value > 20:
#        print('Large number', value)
#print('After')

#found = False
#print('Before', smallest_so_far)
#for the_num in [9, 41, 12, 3, 74, 15]:
#    if the_num < smallest_so_far:
#        smallest_so_far = the_num
#    print(smallest_so_far, the_num)

#print('After', smallest_so_far)

smallest = None  # flag value
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest) # prime getting start 
