#!/usr/bin/python3

"""A script reading stdin line by line then calculates the metrics"""

import sys


def printstats(dict, size):
    """ WWPrints information """
    print("File size: {:d}".format(size))
    for i in sorted(dict.keys()):
        if dict[i] != 0:
            print("{}: {:d}".format(i, dict[i]))


stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printsts(stats, size)

        statlist = line.split()
        count += 1

        try:
            size += int(statlist[-1])
        except:
            pass

        try:
            if statlist[-2] in sts:
                stats[statlist[-2]] += 1
        except:
            pass
    printstats(stats, size)


except KeyboardInterrupt:
    printstats(stats, size)
    raise
