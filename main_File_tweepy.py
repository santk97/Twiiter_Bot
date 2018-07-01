
from functions_file import my_timeline , my_profile ,post_tweet , send_DM , search_user , display_trends , block_menu
from auth_file import api
import time


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
        print("\t\t6. Get Trending Tweets")
        print("\t\t7. BLock/Unblock someone")
        print("\t\t8. Other options")
        print("\t\t9. Exit")
        #delete tweet
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
        elif main_choice==5:
            search_user()
        elif main_choice==6:
            display_trends()
        elif main_choice==7:
            block_menu()
        elif main_choice==8:
            print("New features coming soon ....Stay tuned!!!!\n\n\n")
            time.sleep(3)
else :
    print("Validation Failed")



