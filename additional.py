import time
from dateutil import parser

def format_time(val):
    dt=parser.parse(val)
    dt=dt.astimezone()
    return dt.strftime('%d %B, %Y %H:%M')




def display_profile(user):
    print("\n\n-------------------------------------------------------------------------------------\n")
    print((user['name']))
    print("@" + (user['screen_name']))
    print((user['description']))
    print((user['location']))
    print("Followers : " + str(user['followers_count']))
    print("Following : " + str(user['friends_count']))
    print("Joined Twitter : " + str((format_time(user['created_at']))))
    print("\n\n-------------------------------------------------------------------------------------\n\n")