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

client= commands.Bot(command_prefix=".")
# client=discord.Client()


def news_on(): #NEWS STATIC FUNCTION
	root=requests.get("https://news.google.com/?hl=en-IN&gl=IN&ceid=IN:en")
	soup=BeautifulSoup(root.text,"html.parser")
	ls=[]
	for i in soup.find_all("article"):
		try:
			if i.contents[1].h3.a.get("href")[11:14]!="CBM":
				ls.append("https://news.google.com"+str(i.contents[1].h3.a.get("href"))[1:])
		except AttributeError:
			pass
	print(ls)	
	return ls[:4]


@client.event #ON READY
async def on_ready():
	print(f"i m ready {client.user}")



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
	
	await client.say('PONG!')

@client.command() #NEWS
async def news():
	await client.say("\n".join(news_on()))
	print("DONE NEWS")


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


