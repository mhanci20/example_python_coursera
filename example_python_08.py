#!/usr/bin/env python3

#print('Before')
#for thing in [9, 41, 12, 3, 74, 15]:
#    print(thing)
#print('After')

#x = 0
#while x < 20:
#    x = x + 3
#print(x)

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
   if the_num > largest_so_far:
      largesr_so_far = the_num
   print(largest_so_far, the_num)

print('After', largest_so_far)
