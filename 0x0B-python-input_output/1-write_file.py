#!/usr/bin/python3
"""defining read_file function"""

def read_file(filename="", text=""):
    """read filename with utf-8"""
    with open(filename, "w" , encoding='utf-8') as f:
        return f.write(text)
