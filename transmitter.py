#!/usr/bin/env python3
import requests

#get the message ID
with open("number.txt", "r") as fn:
    ID=fn.read()
    nID=int(ID)+1

#get the message
message=requests.get("https://raw.githubusercontent.com/captainofindustry1060/msg_fetcher_py/refs/heads/main/message.txt", timeout=60)

#save the message
with open(f"message{ID}.txt", "w") as fm:
    fm.write(message.text)

#set the ID for the next message
with open("number.txt", "w") as fn:
    fn.write(str(nID))