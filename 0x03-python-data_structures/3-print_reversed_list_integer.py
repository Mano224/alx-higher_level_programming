#!/usr/bin/python3
def  def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
