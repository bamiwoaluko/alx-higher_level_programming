#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        i = str(0) + str(i)
    print("{}".format(i), end=", ")
    if i is 99:
        print("{}".format(i))
