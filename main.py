import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')   

extensions = [
    'cogs.listener',
    'cogs.admin',
    'cogs.fun'
]

client.remove_command('help')               #Removes the default 'help' command

for extension in extensions:                #Loads listener.py, admin.py and fun.py
    client.load_extension(extension)

with open('txt/token.txt', 'r') as fp:
    token = fp.readline()
client.run(token)                           #Runs the bot with the loaded extensions