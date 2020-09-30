#!/usr/bin/env python
# coding: utf-8

# # Collect Data from National Lottery
# ## Set For Life

import urllib.request
from time import sleep
import os

games = [
    ['lotto', 2582,2584],
    ["lotto-hotpicks", 2582,2584],

    ['euromillions', 1357,1358],
    ["euromillions-hotpicks", 1357,1358],

    ["set-for-life", 159,161],

    ["thunderball", 2725,2729]
]

for game in games:
    print(game[0])
    urlbaseDetails = 'https://www.national-lottery.co.uk/results/' + game[0] + '/draw-history/draw-details/'
    urlbaseBreakdown = 'https://www.national-lottery.co.uk/results/' + game[0] + '/draw-history/prize-breakdown/'

    dirB = '../data/NationalLottery/' + game[0] + '/Breakdown/'
    dirD = '../data/NationalLottery/' + game[0] + '/Details/'

    start = game[1]
    end = game[2]
    for i in range(start, end + 1):
        dlURLD = urlbaseDetails + str(i)
        dlULRB = urlbaseBreakdown + str(i)

        fullfileB = "NatLot" + game[0] + "Breakdown-" + str(i) + ".html"
        fullfileD = "NatLot" + game[0] + "Details-" + str(i) + ".html"

        print(fullfileB)

        print(os.path.exists(dirB + fullfileB))
        # If the file does not exist, download
        if not os.path.exists(dirB + fullfileB):
            responseD = urllib.request.urlopen(dlURLD)
            responseB = urllib.request.urlopen(dlULRB)
            #
            htmlD = responseD.read()
            htmlB = responseB.read()
            #
            textB = htmlB.decode('utf-8')
            textD = htmlD.decode('utf-8')
            # print("FILENAME-B:" + dirB + fullfileB)
            # print("PATH: " + dirB + fullfileB)
            #
            fb = open(dirB + fullfileB, "w", encoding="utf-8")
            fb.write(textB)
            fb.close()
            #
            fd = open(dirD + fullfileD, "w", encoding="utf-8")
            fd.write(textD)
            fd.close()
