#!/usr/bin/python3
'''Module for lookup method.'''
def lookup(op):
    '''Looks up object attributes and methods.
    Args:
        obj (object): the object to list.

    Returns:
        list: the list of attributes.
    '''

    return dir(op)
