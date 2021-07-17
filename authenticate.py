import tweepy
import constants
import openai

def getOpenAI() -> openai:
    """Returns an instance of the OpenAI API"""
    openai.api_key = constants.OPENAI_SECRET
    return openai

def getTwitter() -> tweepy.API:
    """Returns an instance of Twitter API"""
    auth = tweepy.OAuthHandler(constants.TWITTER_API_KEY, constants.TWITTER_API_SECRET, callback=None)

    try:
        redirect_url = auth.get_authorization_url()
        print(redirect_url)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    
    verifier = input('Verifier: ')
    auth.get_access_token(verifier)

    access_token =  auth.access_token
    access_token_secret = auth.access_token_secret

    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api