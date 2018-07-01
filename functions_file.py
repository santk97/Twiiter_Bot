from auth_file import api
import time
import tweepy
from additional import format_time

def my_timeline():

#function to get user timeline details
    while True:
        main_choice = input("\n\nPress 'R' for refresh and 'Q' to exit" )
        if main_choice=='q' or main_choice=='Q':
            print("Going back to main menu\n\n\n")
            time.sleep(2)
            break
        print("LOADING.....")
        tweets=api.home_timeline()
        print("Dispalyin top 10 Tweets:")
        for i in range(0,10):
            print("\n\t posted by USER: "+tweets[i]._json['user']['name'] )
            print(tweets[i]._json['text'])
            try:
                if (tweets[i]._json['truncated'] == True):
                    print("Full tweet at :"+tweets[i]._json['entities']['urls'][0]['url'])
            except IndexError:
                pass
            print("\t\t\t\t\t\t\t\t\t(" + format_time(tweets[i]._json['created_at'])+")")
            print("\n\n-----------------------------------------------------------------------------------------------------")

#function to view the detials of the user
def my_profile():
    print("Loading Profile.......")
    my_details=api.me()._json
    print((my_details['name']))
    print("@"+(my_details['screen_name']))
    print((my_details['description']))
    print((my_details['location']))
    print("Followers : "+str(my_details['followers_count']))
    print("Following : " +str(my_details['friends_count']))
    print("Joined Twitter : " + str(( format_time(my_details['created_at'] ))))
    main_choice=input("Press any key to go back to main menu....")
    print("Loading main menu\n\n\n\n")
    time.sleep(3)

#function to post a teweet

def post_tweet():
    print("\n\n\n\n")
    tweet_text=input("What would you like to tweet : ")
    print ("Sending your Tweet...")
    if api.update_status(tweet_text):
        time.sleep(1)
        print("Succesfully updated")
    else :
        print("Some Errror occured...Trying again")
        if api.update_status(tweet_text):
            time.sleep(1)
            print("Succesfully updated")
        else:
            print("Failed....Try again later...")
    time.sleep(1)
    print("Loading main menu...")
    time.sleep(1)
    print("\n\n\n\n")

def send_DM():
    if_known=input("Do you know the twitter handle of the person you want to DM (y/n)")
    if if_known=='y'or if_known=='Y':
        send_more='y'
        while send_more=='y' or send_more=='Y':
            print('\n\n')
            handle_name=input('Enter the user name :  @')
            message=input("Enter your message...")

            try:
                api.send_direct_message(handle_name,text=message)
                send_more=input("message was sent Succefully....want to send more...(y/n)")
                if send_more!='y' or send_more=='y':
                    print("Going back to main menu.....")
                    time.sleep(2)
            except tweepy.error.TweepError:
                print("Either the user doesn't exist or you are not allowed to send the message...")
                print("Going back ....")
                time.sleep(2)
                continue
            except:
                print("Some Error occured ....Try again....")
                print("Going back ....")
                time.sleep(2)
                continue
    else:
        print("You need the handle ......Go back and Search for the user")
        print("Loading main menu...")
        time.sleep(2)
        print('\n\n\n')





