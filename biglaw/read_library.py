__author__ = 'raccoon'

import sys

def read_library(file):
    dictionary = dict()
    content = open(file).read().split('\n')
    for entry in content:
        kv = entry.split(' | ')
        dictionary[kv[0]] = int(kv[1])
    return dictionary

if __name__ == "__main__":
    f = sys.argv[1]
    d = read_library(f)
    print(d)


