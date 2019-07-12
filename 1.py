import discord
import pickle
from datetime import datetime
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import os
import asyncio


date=str(datetime.now().date())

dd="2019-02-09"
# client.run(os.getenv('username'))
# client.run(os.getenv('pass'))
client= commands.Bot(command_prefix=".")
# client=discord.Client()


def news_on(): #NEWS STATIC FUNCTION
    root=requests.get("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
    soup=BeautifulSoup(root.text,"html.parser")
    print(root)
    ls=[]
    for i in soup.find_all("article"):
        if i.h3 is not None:
            print(i.h3)
            ls.append("https://news.google.com" + str(i.h3.a.get("href"))[1:])
        print(ls)
    return(ls[:4])


@client.event #ON READY
async def on_ready():
	print(f"i m ready {client.user}")

	
	
import requests
from bs4 import BeautifulSoup

USERNAME=str(input("ENTER THE USERNAME HERE"))
PASSWORD=str(input("ENTER THE PASSWORD HERE"))
PROTECTED_URL = 'https://m.facebook.com/home.php?ref_component=mbasic_home_header'

def login(session, email, password):
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)

    assert response.status_code == 302
    return response.cookies


def filter_feeds(feeds):
    feeds_ret=[]
    i=0
    while i!=len(feeds):
        feeds_ret.append(feeds[i])
        if "shared" not in feeds[i]:
            i+=1
        else:
            i+=2
    return feeds_ret            
                


def Home_feeds(soup,filter):
    feeds=[]        
    data=soup.find_all("h3")
    for link in data:
        if link.strong!=None:
            feeds.append(link.text)

    if filter=="filter":
        feeds=filter_feeds(feeds)
    return feeds            


@client.event
async def on_message(message):
	print(f"{message.channel}:{message.author} : {message.author.name} : {message.content}")
	if "hi" in message.content.lower():
		await client.send_message(message.channel,"WASS UP?")
	if "get out" in message.content.lower():
		await client.close()
	await client.process_commands(message)
	


@client.command()  #ADD IN TODO
async def td(*args):
	todo=pickle.load(open("todo.txt","rb"))
	if date in todo.keys():
		todo[date].append(" ".join(args))
	else: todo[date]=[" ".join(args)]	
	pickle.dump(todo,open("todo.txt","wb"))
	
@client.command()  #DISPLAY TODO
async def todo():
	todo=pickle.load(open("todo.txt","rb"))
	print(todo)
	try:
		await client.say("\n".join(map(str,todo[date])))
	except KeyError:
		await client("Nothing to do today :-)")

@client.command() #REPEAT ON TERMINAL
async def echo(*args):
	print(args)
	print(" ".join(args))

@client.command()   #JUST REPEAT
async def ping():
	print(os.environ.get('username'))
	await client.say('PONG!')

@client.command() #NEWS
async def news():
	await client.say("\n".join(news_on()))
	print("DONE NEWS")

@clienty.command()
async def facebook():
	
    session = requests.session()
    cookies = login(session, os.environ.get('username'), os.environ.get('pass'))
    response = session.get(PROTECTED_URL, cookies=cookies,
allow_redirects=False)
    soup=BeautifulSoup(response.text,"html.parser")
    Home_list=Home_feeds(soup,"filter")
    print(Home_list)


# @client.event
# async def on_message(message):
	# author = message.author
	# content=message.content
	# print("{}:{}".format(author,content))

# @client.command()
# async def ping():
# 	await client.say("Pong!")

# @client.command()
# async def echo(*args):
	# output=""
	# for word in args:
		# output += word
		# output += ' '
	# print(output)
	# mess=" ".join(args)	
	# await client.say(mess)	

# @client.event
# async def on_message_delete(message):
	# author= message.author
	# content=message.content
	# channel=message.channel
	# await client.send_message(channel,content)

# print(datetime.now().date())


client.run(os.getenv('TOKEN'))	
client.run(os.getenv('username'))
client.run(os.getenv('pass'))	


