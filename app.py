import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://VoiceOfSha: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@github.com/VoiceOfSha/Alexa okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
