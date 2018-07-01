from auth_file import api
import time
import tweepy
from additional import format_time , display_profile

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
    display_profile(my_details)
    input("Press any key to go back to main menu....")
    print("Loading main menu\n\n\n\n")
    time.sleep(3)

#function to post a teweet

def post_tweet():
    print("\n\n\n\n")
    tweet_text=input("What would you like to tweet : ")
    print ("Sending your Tweet...")
    try :
        api.update_status(tweet_text)
        time.sleep(1)
        print("Succesfully updated")
    except tweepy.error.TweepError:
        print("Some Errror occured...Trying again")
        post_tweet()
    except:
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
        print("Loading Search interface..")
        search_user()
        time.sleep(2)
        print('\n\n\n')


def search_user():
    print("\n\n\nWelcome to the search user interface ......")
    if_known=input("Do you know the twitter handle of the user you are searching for : (y/n)")
    if if_known=='y' or if_known=='Y':
        try:
            user_name=input('Enter the name of the Handle or Name :')
            result=api.get_user(user_name)._json
            display_profile(result)
        except tweepy.error.TweepError:
            print ("Wrong user details ....Try again..")
            time.sleep(1)
            search_user()

        except:
            print("some error occured ....Trying again...")
            time.sleep(1)
            search_user()
    else:
        search_query=input("\n\n Enter the query for the user you are searching:")
        print("Loading....")
        result=api.search_users(search_query,20,1)
        print("\n\n Displaying Top %d Results ....." %(len(result)))
        if len(result)==0:
            print("No Results found .....Search again")
            print("Going back to MAin Menu...")
            time.sleep(2)
        else:
            for i in range(len(result)):
                print(i+1,"\t",result[i]._json['name'],"\t",result[i]._json['screen_name'],"\t",result[i]._json['location']
                      ,"\t",result[i]._json['description'])
            found=input("Was your search succesfull (y/n) ")
            if found=='y' or found=='Y':

                    while True:
                        selected_user = (int(input("Select the user that you were searching for (1-20)")))
                        if selected_user>=1 and selected_user<=20:
                            display_profile(result[selected_user-1]._json)
                            print("Going Back to main menu...")
                            time.sleep(3)
                            break

                        else :
                            print("invalid Choice .....")
            else:
                    print(" you need to be more specific...Search again")
                    time.sleep(2)
                    search_user()


def display_trends():
    print("Displayin the top trends....\n\n\n")
    res=api.trends_place(1)
    for i in range(10):
        print("\n----------------------------------------------------------------------------------------------------------\n")
        print(i+1,".  "+res[0]['trends'][i]['name'],end=" ")
        print("Find more at :  "+res[0]['trends'][i]['url'],end=" ")
        print("\n\tNo. of tweets :"+str(res[0]['trends'][i]['tweet_volume']),end=" ")
        print("\n")
        print("\n----------------------------------------------------------------------------------------------------------\n")
    print("Going back to Main Menu....\n\n\n")
    time.sleep(3)


def block_menu():
    print("\n\nWhat would you like to do ....")
    choice=int(input("1. Block Someone \n2.UnBlock Someone"))
    if choice==1:
        if_known=input('Do you  know the handle of the user You want to block (y/n) : ')
        if if_known=='y' or if_known=='Y':
            user_name=input("enter the Handle of the user you wan to block : ")
            try:
                api.create_block(user_name)
                print("Blocked Succesfully ....Redirecting")
                time.sleep(2)
            except tweepy.error.TweepError:
                print("Wrong user name.....Try again.. ")
                time.sleep(1)
                block_menu()
            except:
                print("Some error occured.....Try again")
                time.sleep(1)
                block_menu()

        else:
            print("Redirecting to the Search Interface...")
            time.sleep(2)
            search_user()
    elif choice==2:
        print(" The list of users you have blocked...")
        block_list=api.blocks_ids()
        for i in range(len(block_list['ids'])):
            user=api.get_user(block_list['ids'][i])._json
            print("\n\n",i+1, user['name'] ,"@"+ user['screen_name'])
        selected_user=(int(input("select the user you want to unblock"))-1)
        try:
            api.destroy_block(block_list['ids'][selected_user])
            print("Unblocked Succesfully....Redirecting...")
            time.sleep(2)
        except tweepy.error.TweepError:
                print("Wrong user name.....Try again.. ")
                time.sleep(1)
                block_menu()
        except:
                print("Some error occured.....Try again")
                time.sleep(1)
                block_menu()
    else:
        print("invalid choice .....Redirecting")
        time.sleep(2)
        block_menu()




