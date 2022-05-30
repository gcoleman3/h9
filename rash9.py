
from ast import parse
import telebot
import requests
import os
from telebot import types

token = '5143471387:AAFdmW6lSK5ECQ14JI_nW4nFqdOwMt3raec'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi,\n=======\nWellcome To InstaUp Coin Hunt!\nNow Send Your Username\n========\nBy : @trprogram</strong>",parse_mode="html")
def sf(sendto,user,coia):
    print("Check Now ..")
    url3 = requests.get(f"https://Insta-up.safajj4.repl.co/oid={user}&uid={sendto}&submit=submit").text
    print(url3)
    if '"status":"Successful"' in url3:
        bot.send_message(message.chat.id,f"<strong>Done Send 300 Followers!</strong>",parse_mode="html")
    if '"status":"Error","message":"To set an order, you must have more than 50 coins."' in url3:
        bot.send_message(message.chat.id,f"<strong>Error Less Coins In : {user}</strong>",parse_mode="html")
    if '"status":"Error","message":"Your accound suspended due to unfollowing. If you think there is a mistake, call us at instaup.developers@gmail.com."' in url3:
        bot.send_message(message.chat.id,f"<strong>Account : {user} Is Suppesend !</strong>",parse_mode="html")
    else:
        pass       
def coins(message,user,sendto):
    url2 = requests.get(f'https://Instaup.safajj4.repl.co/?oid={user}&submit=submit').text

    if 'coins":"' in url2:
        coins = str(url2.split('coins":"')[1])
        coia = str(coins.split('"')[0])
        bot.send_message(message.chat.id,f"<strong>Username : {user}\nCoins : {coia}</strong>",parse_mode="html")
        url3 = requests.get(f"https://Insta-up.safajj4.repl.co/oid={user}&uid={sendto}&submit=submit").text
    try:
        if '"status":"Successful"' in url3:
            bot.send_message(message.chat.id,f"<strong>Done Send 300 Followers!</strong>",parse_mode="html")
        if '"status":"Error","message":"To set an order, you must have more than 50 coins."' in url3:
            bot.send_message(message.chat.id,f"<strong>Error Less Coins In : {user}</strong>",parse_mode="html")
        if '"status":"Error","message":"There is a problem registering the order. Contact support"' in url3:
            bot.send_message(message.chat.id,f"<strong> Order Erorr </strong>",parse_mode="html")
    except:
        pass
@bot.message_handler(func=lambda m:True)
def sta(message):
    sendto = message.text
    bot.send_message(message.chat.id,f"<strong>Ok .. Bot Started</strong>",parse_mode="html")
    file = "usernames.txt"
    for r in open(file,"r").read().splitlines():
        user = str(r.split('\n')[0])
        coins(message,user,sendto)
bot.polling()