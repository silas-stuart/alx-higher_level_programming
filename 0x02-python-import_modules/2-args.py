#!/usr/bin/python3
if __name__ == "__main__":
    """First import sys"""
    import sys
    total = len(sys.argv) - 1
    if total == 0:
        print("0 arguments.")
    elif total == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total))
    for p in range(total):
        print("{}: {}".format(p + 1, sys.argv[p + 1]))
