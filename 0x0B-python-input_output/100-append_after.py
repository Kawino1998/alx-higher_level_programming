#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as myfile:
        lines = myfile.readlines()
    myfile.close()

    with open(filename, "w") as writefile:
        for line in lines:
            if search_string in line:
                line = line + new_string
            writefile.write(line)
