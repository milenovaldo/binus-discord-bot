import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix='!')   #Specifies a command prefix

extensions = [
    'cogs.listener',
    'cogs.admin',
    'cogs.fun',
    'cogs.music'
]

client.remove_command('help')               #Removes the default 'help' command

for extension in extensions:                #Loads listener.py, admin.py, fun.py and music.py
    client.load_extension(extension)

with open('json/data.json', 'r') as fp:
    idJson = json.load(fp)
token = idJson["KEY"]["botToken"]                         
if token == '0':
    print(
        'Welcome\n' +
        'We have detected that this is your first time running the bot\n' +
        'Please fill in the required information\n'
    )

    '''
    Bot token validation
    '''
    while 1:
        botToken = str(input('Please enter your bot token: '))

        if len(botToken) == 59:
            print('Bot token has been set.\n')
            with open('txt/token.txt', 'w') as fp:
                fp.write(botToken)
            break
        else:
            print('Invalid token.')
        
    
    client.run(botToken) 
else:
    client.run(token)