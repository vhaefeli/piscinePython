#! /usr/bin/env python3

from datetime import datetime

today = datetime.now()
yesterday = datetime(1970, 1, 1)
delta = (today - yesterday)
nb_sec = delta.total_seconds()
format_nb_sec = "{:,.4f}".format(nb_sec)
eformat_nb_sec = "{: .2e}".format(nb_sec)


print("Seconds since January 1, 1970: ", format_nb_sec, "or ", eformat_nb_sec , "in scientific notation")
print(today.strftime('%b %d %Y'))