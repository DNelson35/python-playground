#!/usr/bin/env python3

import sys  ##the line above makes file executable and sys allows us to call sys.argv to pass an argument at the command line when this file is executed

## so typing from the labs directory "./ex_file.py Damien" would pass damein in as the argument the response would be "The name is Damien"

name = sys.argv[1]

if __name__ == '__main__':
    i = 100
    while i >  0:
        print(f"The name is {name}")
        i -= 1

# import os

# if __name__ == "__main__":
#     os.system('ls -l')


    