# replit-only feature

from replit import db
import datetime

while True:
    option = input("1. Add Tweet\n2. View Tweets\n3.Quit\n> ")
    if option == "1":
        tweet = input("Enter your tweet: ")
        timestamp = datetime.datetime.now()
        db[timestamp] = tweet
    if option == "2":
        keys = db.keys()
        for key in keys:
            print(f"{key}: {db[key]}")
    if option == "3":
        break
