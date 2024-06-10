#!/usr/bin/python3
"""difining load_from_json_file function"""

import json

def load_from_json_file(filename):
    """ """
    with open(filename, 'r', encoding="utf-8") as file:
       return json.load(file)
