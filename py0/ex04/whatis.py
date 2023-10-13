#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python nom_du_script.py <argument>")
    else:
        argument = sys.argv[1]
        ma_fonction(argument)
