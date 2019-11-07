<p align="left"><img width=20% src="https://image.psikolif.com/wp-content/uploads/2018/10/Logo-Binus-University-Universitas-Bina-Nusantara-PNG.png"></p>

![Python](https://img.shields.io/badge/python-v3.5+-blue.svg)

# Discord Bot 
 Simple general purpose discord bot made for a BINUS University project (Mr. Jude's Computer Science 2023 class).

 ## Installation and setup

 ### Requires Python 3.5+ (Tested on 3.7.5)

 Clone the git:
 ```
 git clone https://github.com/milenovaldo/binus-discord-bot
 ```

 Installing requirements:
 ```
 # Windows/OSX/Linux
 pip install -r requirements.txt
 ```

 Install FFMPEG and add to PATH in Windows <br/><br/>
 <b>OR</b><br/>
```
# OSX/Linux
sudo apt-get install ffmpeg
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
    <li>Server wide logging saved to a txt file</li>
    <li>Encourages you to get a girlfriend/boyfriend</li>
</ul>

### Available commands:

<img width = 50% src = 'https://i.ibb.co/b2VHbyZ/ss.jpg'><br/>

<img width = 50% src = 'https://i.imgur.com/HsLTeUH.jpg'><br/>

Or type <b>'!help'</b> when the bot is running.
