__author__ = 'raccoon'

import sys
from biglaw.read_library import read_library


if __name__ == "__main__":
    search_string = sys.argv[1]

    d = read_library('library.txt')

    for k, v in ((k, d[k]) for k in sorted(d, key=d.get)):
        if search_string in k:
            print(k, v)
