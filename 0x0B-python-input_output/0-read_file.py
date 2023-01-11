#!/usr/bin/python3
#Author:Jeremy
# Function that read a file

def read_file(filename=""):
    with open(filename, encoding='UTF8') as f:
        data = f.read()
        print(data)
