import tweepy
from functions_file import my_timeline , my_profile ,post_tweet , send_DM
from auth_file import api


if api:
    print("validation succesfull starting the main application ...")
    while True:
        #printing the Main menu to the user
        print(" \t\t\tTwitter BOT")
        print("\t\t1. Get My Timeline")
        print("\t\t2. View my Profile")
        print("\t\t3. Post a Tweet ")
        print("\t\t4. Send a message to someone ")
        print("\t\t5. Search someone")
        print("\t\t6. Get Topic related Tweets")
        print("\t\t7. BLock someone")
        print("\t\t8. Other options")
        print("\t\t9. Exit")
        #delete tweet
        #follow someone
        #media upload
        main_choice=int(input("Enter your choice"))

        if main_choice==9:
            print("EXITING!!!!")
            break
        elif main_choice==1:
            my_timeline()
        elif main_choice==2:
            my_profile()
        elif main_choice==3:
            post_tweet()
        elif main_choice==4:
            send_DM()


else :
    print("Validation Failed")



