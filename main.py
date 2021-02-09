import discord
import os
#import requests
#import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

poop_words = ["grumpy","turd","diareah", "splatter", "shit","Shit","SHIT" , "poop", "thai food", "browns","dooky","feces","fecal","waste","dookie","accident","POOP","crap","shart","fart","excrement","discharge","manure","deuce", "stool", "cook","Cook","dung","BM","bm","bowel","defecate","Poop","dump","brady","tom brady","tb12","Brady","Tom brady"]

starter_poop = ["poop1.jpg","poop2.jpg","poop3.jpg","poop4.jpg","poop5.jpg","poop6.jpg","poop7.jpg","poop8.jpg","poop9.jpg","poop10.jpg","poop11.jpg","poop12.jpg","poop13.jpg","poop14.jpg","poop15.jpg","poop16.jpg","poop17.jpg","poop18.jpg","poop19.jpg","poop20.jpg","poop21.jpg"
]

if "responding" not in db.keys():
  db["responding"] = True

#api need to change to work with images
#def get_quote():
 # response = requests.get()
  #json_data = json.loads(response.text)
  #quote = json_data[0]['q'] + " -" + json_data[0]['a']
  #return(quote)

def update_poop(poop_message):
  if "poop" in db.keys():
    poop = db["poop"]
    poop.append(poop_message)
    db["poop"] = poop
  else:
    db["poop"] = [poop_message]

def delete_poop(index):
  poop = db["poop"]
  if len(poop)>index:
    del poop[index]
    db["poop"] = poop


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$poop'):
    #quote = get_quote()
    await message.channel.send(file=discord.File(random.choice(starter_poop)))#quote goes here
  if db["responding"]:
    options = starter_poop
    msg.lower()
    if "poop" in db.keys():
      options = options + db["poop"]
    msg.lower()
    if any (word in msg for word in poop_words):
      await message.channel.send(file=discord.File(random.choice(starter_poop)))
      await message.channel.send(random.choice(db["poop"]))



  if msg.startswith("$new"):
    poop_message = msg.split("$new ",1)[1]
    update_poop(poop_message)
    await message.channel.send("New poop added")

  if msg.startswith("$del"):
    poop = []
    if "poop" in db.keys():
      index = int (msg.split("$del",1) [1])
      delete_poop(index)
      poop = db["poop"]
      await msg.send(poop)

  if msg.startswith("$list"):
    poop = []
    if "poop" in db.keys():
      poop = db["poop"]
    await message.channel.send(poop)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower()== "on":
      db["responding"] = True
      await msg.send("Responding is on.")
    else:
      db["responding"] = False
      await msg.send("Responding is off.")


keep_alive()
client.run(os.getenv('TOKEN'))
