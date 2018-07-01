import time
from dateutil import parser

def format_time(val):
    dt=parser.parse(val)
    dt=dt.astimezone()
    return dt.strftime('%d %B, %Y %H:%M')




