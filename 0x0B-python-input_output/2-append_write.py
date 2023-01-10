#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myfile:
        characters = myfile.write(text)
    myfile.close()
    return characters
