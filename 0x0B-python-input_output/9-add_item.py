#!/usr/bin/python3
import sys
savejson = __import__("7-save_to_json_file").save_to_json_file
loadjson = __import__("8-load_from_json_file").load_from_json_file


"""Description of module."""


oldlist = []
try:
    oldlist = loadjson("add_item.json")
except:
    pass
savejson(oldlist + sys.argv[1:], "add_item.json")
