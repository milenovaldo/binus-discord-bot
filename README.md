<p align="left"><img width=20% src="https://image.psikolif.com/wp-content/uploads/2018/10/Logo-Binus-University-Universitas-Bina-Nusantara-PNG.png"></p>

![Python](https://img.shields.io/badge/python-v3.5+-blue.svg)

# Discord Bot 
 Simple general purpose discord bot made for a BINUS University project (Mr. Jude's Computer Science 2023 class).

 ## Installation and setup

 ### Requires Python 3.5+ (Tested on 3.7.5)

 Installing requirements:
 ```
 # Windows
 pip install -r requirements.txt

 # OSX/Linux
 sudo pip install -r requirements.txt
 ```

 Clone the git:
 ```
 git clone https://github.com/milenovaldo/binus-discord-bot
 ```

Setup:<br/>
<a href = "https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token">Get the Discord token</a><br/>
Then paste your token in "txt/token.txt"<br/><br/>
<a href = "https://steamcommunity.com/dev/apikey">Get steam API key</a><br/>
Then paste it in "txt/steamapi.txt"<br/><br/>


## Functionalities

### Passive functionalities:

<ul>
    <li>Sends new members a personal message containing the server rules.</li>
    <li>Adds user to json database when a user joins a server.</li>
    <li>Removes user from database when they get banned.</li>
    <li>Dirty word filtering. Deletes offensive messages and warns the user.</li>
    <li>Leveling system. Encourages user activity in the server.</li>
</ul>

### Available commands:

<img width = 50% src = 'https://i.imgur.com/LuT1ViO.jpg'>

Or type '!help' when the bot is running.
