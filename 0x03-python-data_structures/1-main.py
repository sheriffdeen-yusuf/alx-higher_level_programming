#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
print(len(my_list)) 
idx = 5
print("Element at index {:d} is {}, list length is {}".format(idx, element_at(my_list, idx), len(my_list)))
