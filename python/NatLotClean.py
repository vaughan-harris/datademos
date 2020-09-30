#!/usr/bin/env python
# coding: utf-8

# # Collect Data from National Lottery
# ## Set For Life

import urllib.request
from time import sleep
import os
import re


# Cleaner Script
def cleaner(game,contents,type="N"):
    content_new = contents

    if game == "thunderball":
        if type=="B":
            content_new = re.sub('<!doctype.*?<div id="draw_details_breakdown_header".*?<h1>(.*?)</h1>', r'<DATE>\1</DATE>', content_new, flags=re.S)            # Draw details (ball set, machine etc)
            content_new = re.sub(r'<p class="header_draw_details">(.*?)</p>', r'<DETAILS>\1</DETAILS>', content_new, flags=re.S)
            content_new = re.sub(r'<span id="header.*?>(.*?)</span>', r'-\1-', content_new, flags=re.S)
            content_new = re.sub(r'</DETAILS>.*?<NUMBERS>', r'</DETAILS><NUMBERS>', content_new, flags=re.S)
            content_new = re.sub(r'-\s{1,10}', r'-', content_new, flags=re.S)
            content_new = re.sub(r'\s{1,10}-', r'-', content_new, flags=re.S)
            content_new = re.sub(r'<p id="game_header_intro">.*?£(.*?)</p>.*?</div>', r'<TOPPRIZE>\1</TOPPRIZE>', content_new,
                                 flags=re.S)
            content_new = re.sub(r'<td id="winner.*?>.*?>(.*?)<.*?/td>', r'XXXX \1 XXXX', content_new, flags=re.S)
            content_new = re.sub(r'<td id="prize_per_player.*?>.*?£(.*?)</td>', r'XXXX \1 XXXX', content_new, flags=re.S)
            content_new = re.sub(r'<td id="prize_fund_.*?>.*?>.*?£(.*?)</div>', r'XXXX \1 XXXX', content_new, flags=re.S)
            content_new = re.sub(r'(</DETAILS>).*?(XXXX)', r'\1\n\2', content_new, flags=re.S)
            content_new = re.sub(r'\s*XXXX\s*', r'|', content_new, flags=re.S)
            content_new = re.sub(r'<td id="match_count.*?/td>', r'', content_new, flags=re.S)
            content_new = re.sub(r'</tbody>.*</html>', r'|', content_new, flags=re.S)
            content_new = re.sub(r'(\|\|)|(-\|-)', r'|', content_new, flags=re.S)
            content_new = re.sub(r'</td.*?\|', r'|', content_new, flags=re.S)
            content_new = re.sub(r'<DATE>(.*?)</DATE>\s*<TOPPRIZE>(.*?)</TOPPRIZE>\s*<DETAILS>(.*)</DETAILS>', r'|\1|\2|\3|',
                                 content_new, flags=re.S)
            content_new = re.sub(r'\s*\|', r'|', content_new, flags=re.S)
            return("TBALL  "+type+content_new)
        elif type=="D":

            content_new = re.sub('<!doctype.*?<h1>(.*?)</h1>',                      r'<DATE>\1</DATE>', content_new, flags=re.S)
            content_new = re.sub(r'<p class="header_draw_details">(.*?)</p>',       r'<DETAILS>\1</DETAILS>', content_new, flags=re.S)
            content_new = re.sub(r'</DATE>.*?<DETAILS',                             r'</DATE><DETAILS', content_new, flags=re.S)
            content_new = re.sub(r'/DETAILS>.*?<ol class="draw_numbers_list clr">(.*?)</ol>', r'/DETAILS><NUMBERS>\1</NUMBERS>', content_new, flags=re.S)
            content_new = re.sub(r'/NUMBERS>.*</html>', r'/NUMBERS>', content_new, flags=re.S)

            content_new = re.sub('<a href="/results/how-to-claim">.*?/html>', r'', content_new, flags=re.S)
            content_new = re.sub('<li class="(?:normal|special).*?>(.*?)</li>', r'|\1|', content_new, flags=re.S)
            content_new = re.sub(r'<span id="header.*?>(.*?)</span>\s*', r'\1', content_new, flags=re.S)
            content_new = re.sub(r'<span .*?</span>', r'', content_new, flags=re.S)

            content_new = re.sub(r'\s*\|\s*', r'|', content_new, flags=re.S)
            content_new = re.sub(r'\s*<', r'<', content_new, flags=re.S)
            content_new = re.sub(r'>\s*', r'>', content_new, flags=re.S)

            return("TBALL "+type+content_new)
    if game == "lotto":
        if type=="B":
            return("Content " + type )
        elif type=="D":
            content_new = re.sub('<!doctype.*?<h1>(.*?)</h1>.*?<ol class="draw_numbers_list clr">(.*?)</ol>.*</html>', r'<DATE>\1</DATE><NUMBERS>\2</NUMBERS>', content_new, flags=re.S)


            content_new = re.sub('<li.*?>(.*?)</li>\s*', r'|\1|', content_new, flags=re.S)
            content_new = re.sub('<span.*?>(.*?)</span>\s*', r'', content_new, flags=re.S)

            return("Content " + type + content_new)

    else:
        return("NONE")



games = [
    ['lotto', 2531, 2581],
#    ['euromillions', 1305, 1356],
#    ["set-for-life", 107, 158],
#    ["lotto-hotpicks", 2531, 2581],
#    ["euromillions-hotpicks", 1305, 1356],
    ["thunderball", 2622, 2724]
]


#game=games[0]
#dirD = '../data/NationalLottery/' + game[0] + '/Details/'
#filename = os.fsdecode('NatLotthunderballDetails-2622.html')
#filename=dirD+filename
#
#with open(filename, 'r') as f:
#    content = f.read()
#
#content_new=cleaner("thunderball",content,"D")
#
#print(content_new)
#
#print("END")
#
#
#dirB = '../data/NationalLottery/' + game[0] + '/Breakdown/'
#filename = os.fsdecode('NatLotthunderballBreakdown-2622.html')
#filename=dirB+filename
#
#with open(filename, 'r') as f:
#    content = f.read()
#
#content_new=cleaner("thunderball",content,"B")
#
#print(content_new)
#
#print("\nEND\n")


# ########################################################################################
game=games[0]
dirD = '../data/NationalLottery/' + game[0] + '/Details/'
filename = os.fsdecode('NatLotlottoDetails-2584.html')
filename=dirD+filename

with open(filename, 'r') as f:
    content = f.read()

content_new=cleaner(game[0],content,"D")

print(content_new)

print("END")


dirB = '../data/NationalLottery/' + game[0] + '/Breakdown/'
filename = os.fsdecode('NatLotlottoBreakdown-2584.html')
filename=dirB+filename

with open(filename, 'r') as f:
    content = f.read()

content_new=cleaner(game[0],content,"B")

print(content_new)

print("\nEND\n")




# content_new = cleaner('thunderball',content)
