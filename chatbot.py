from datetime import datetime as dt
import os,glob,random,webbrowser
msg = input("Enter Message =>").lower()

helloIntent = ["hi","hello","hey","hie","hy","wassup"]
byeIntent = ["bye","tata","see you","ttyl","tc","take care"]
timeIntent = ["time","whats the time","time please"]
dateIntent = ["date","whats the date","date please"]
musicIntent = ["music","play music","song"]

if msg in helloIntent:
    print("hey")

elif msg in timeIntent:
    time = dt.now()
    print(time.strftime("%I:%M:%S,%p"))

elif msg in musicIntent:
    dir = os.listdir()
    musicList = glob.glob("*.mp3")
    song = random.choice(musicList)
    os.startfile(song)

elif msg.startswith("open"):
    url = msg.split()[-1]+".com"
    webbrowser.open(url)
    
elif msg in dateIntent:
    date = dt.now()
    print(date.strftime("%d/%m/%y,%a"))

elif msg in byeIntent:
    print("GoodBye...")

else:
    print("Sorry, I dont Understand")

