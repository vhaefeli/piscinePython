#!/usr/bin/env python3

import sys as sys

if __name__ == "__main__":
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            sys.exit(0)
        assert sys.argv[1].isdigit(), "argument is not an integer"
        nb = int(sys.argv[1])
        if nb % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
