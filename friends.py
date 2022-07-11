#!/usr/bin/env python3
#friends.py
#texting friends a easy python tool I use to keep in touch with friends using a simple dictionary and twilio

#imports
from random import randint
import os
import json
from twilio.rest import Client

#setup variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# dictionary with name, weight pair that is aggregated as a lis

# Create list from dictionary
def main():
    #open json
    f = open('friends.json')
    lottery = json.load(f)
    f = open('goals.json')
    goals = json.load(f)
    # go through json object and add correct elements of people
    lottery_list = []
    for (name,weight) in lottery.items():
        for _ in range(weight):
            lottery_list.append(name)
    print(len(lottery_list))

    #Draw Number and text accordingly to myself
    num = randint(0,len(lottery_list)-1)
    message = client.messages \
        .create( 
            body="Tor! You should text:" + lottery_list[num] +
                "\ Your goal of the day is" + goals[Day] +
                "\n Your goal of the week is: " + goals[Week] + 
                "\n Your goal of the year is: " + goals[Year] + 
                "\n Your goal of 5 years is: " + goals[5-Years].map(),
            from_='+19793645040',
            to='+1 651 955 9920'
        )

    print("Success")
            
if __name__ == '__main__':
    main()

