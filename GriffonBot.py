from discord.ext import commands
from datetime import datetime
import random

'''commandsList = dir(commands)
for i in range(len(commandsList)-1):
    print(commandsList[i])'''

prefix = "%"
bot = commands.Bot(command_prefix=prefix, description='TestBot')

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    #await bot.say("Prefix currently" + prefix)

@bot.command()
async def helpme():
    await bot.say("```" + prefix + "hello (Says Hello world!)\n" + prefix + "showdatetime (Says the current date and Time)\n" + prefix + "showbunny (Shows cute Bunny!!!!)\n" + prefix + "showowl (Shows cute Owl!!!!)\n" + prefix + "color (Says favorite color)\n" + prefix + "add (Adds two numbers together)\n" + prefix + "choose (Randomly pick one of the arguments)\n" + prefix + "savetext (Saves argument to a file on home computer)```")

@bot.command()
async def hello():
    await bot.say("Hello world!")

#date_now = str(datetime.now().date())time_now = str(datetime.now().time())

cutebunny = " ()   ()\n" \
             "(>•,•<)\n" \
             ' (")_(")'

cuteowl = " ,    ,\n" \
          "[O.o]\n" \
          "/)  )\n" \
          '="="=\n' \
          "===="

@bot.command()
async def showdatetime():
    await bot.say("It is currently " + time_now + " on " + date_now)

@bot.command()
async def showbunny():
    await bot.say(cutebunny)

@bot.command()
async def showowl():
    await bot.say(cuteowl)

@bot.command()
async def color():
    await bot.say("Purple")

@bot.command()
async def add(first: int, second: int):
    await bot.say(first + second)

@bot.command()
async def choose(*choices: str):
    await bot.say(random.choice(choices))

@bot.command()
async def savetext(*messages: str):
    file = open("saved.txt", "w")
    message = ''
    for i in range(len(messages)):
        message += messages[i]
        if i < (len(messages) - 1):
            message += ' '
    file.write(message)
    file.close()
    await bot.say("The text `" + message + "` has been saved")

bot.run('NDk5Nzc2MTU1NzY3Nzk5ODA4.DqE5CQ.FjOKHxntn0zj_r7dNH2kurEVpCI')
