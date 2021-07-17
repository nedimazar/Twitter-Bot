import authenticate

try:
    openai = authenticate.getOpenAI()
    print('Authenticated with OpenAI')
except Exception as e:
    print('Error while authenticating with OpenAI: ', e)

try:
    twitter = authenticate.getTwitter()
    print('Authenticated with Tweepy')
except Exception as e:
    print('Error while authenticatin with Tweepy: ', e)

twitter.update_status('YOLO')

