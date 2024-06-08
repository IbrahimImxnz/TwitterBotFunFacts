import tweepy
import tkinter
import schedule
import time
import random
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv()
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_key')
access_token = os.getenv('access_token')
access_secret = os.getenv('access_secret')
bearer_token = os.getenv('bearer_token')
#auth.set_access_token(access_token,access_secret)
#pi = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_secret)
#client = tweepy.Client(bearer_token=bearer_token)
#user = api.verify_credentials()
#if user:
#    print(user.name)

#ffacts = []

#def bs(url):
#    res = requests.get(url)
 #   soup = BeautifulSoup(res.text, "lxml")
#    sections = soup.find_all("p")
#    short = sections[1:]
#   for section in short:  
#        ffacts.append(section.get_text(strip=True))
 #   return ffacts
url = "C:\Users\imxnz\TwBot1\facts.txt"
def funfacts(url):
    with open(url, 'r') as f:
       facts = f.readlines()
    return [fact.strip() for fact in facts]
     

def tweet():
    facts = funfacts(url)
    if facts : 
        fact = random.choice(facts)
        if len(fact) > 280: 
                fact = fact[:277]
        try:
            client.create_tweet(text=fact)
            print("new tweet")
        except tweepy.TweepyException as e:
            print("Error Tweeting", e)
    else:
        print("no elements fetched")

#schedule.every().day.at("21:35").do(tweet)        

#while True:
#    schedule.run_pending()
 #   time.sleep(1)

tweet()




