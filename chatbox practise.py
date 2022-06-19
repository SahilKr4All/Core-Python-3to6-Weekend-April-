
from datetime import datetime as dt
from sqlite3 import Date
chat = input("chat with me")
import os, glob , random, webbrowser


hiiIndent = ["hello", "hye" ,"hii"]
musicIndent = ["play music", "start song"]
dateIndent = ["tell me date", "date"]

if chat in hiiIndent :
    print("hnji")

elif chat in musicIndent:
    dir = os.listdir()
    musiclist = glob.glob("*.mp3")
    song = random.choice(musiclist)
    os.startfile(song)
    
elif chat in dateIndent:
    date = dt.now()
    print(date.strftime("%d:%m:%y %a"))

elif chat.startswith("open"):
    url = chat.split()[-1]+".com"
    webbrowser.open(url)


else: 
    print("dont know")
