#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    i = dir(hidden_4)
    for r in i:
        if r[:2] != "__":
            print("{}".format(r))
