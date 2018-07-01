import twitter

api=twitter.Api ( consumer_key='DnmLbUfv7159MlaDkczduCrtj',
                  consumer_secret='NlEQVcvKqs0l6Iw5d4kqNXsffnIR9ouOIEAxuX7xi5TWgxPzq7',
                  access_token_key='444500252-2RTMCo6e1bxlGiv735MsL8XINqbB6hKOpLfLXiUv',
                  access_token_secret='2RLhqgN8A5CGS5yuvNw57QNNTCi5vAChgERbC5a2kgj9Y')


users=api.GetUserTimeline(screen_name='anjugoja')

print(users)

status=api.PostUpdate("this is a Twitter bot Tweet")
print(status)






