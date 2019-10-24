import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')   

client.load_extension("bot")                #Loads bot.py

with open('txt/token.txt', 'r') as fp:
    token = str(fp.readline())

client.run(token)                           #Runs the bot with the loaded extensions