#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of the args"""
    import sys

    net = 0
    for p in range(len(sys.argv) - 1):
        net += int(sys.argv[p + 1])
    print("{}".format(net))
