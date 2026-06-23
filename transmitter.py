#!/usr/bin/env python3
import requests

#get the message id
with open("number.txt", "r") as fn:
    id = fn.read()
    nid = int(id)+1

#get the message
message = requests.get("https://raw.githubusercontent.com/captainofindustry1060/msg_fetcher_py/refs/heads/main/message.txt", timeout=60)

#save the message
with open(f"message{id}.txt", "w") as fm:
    fm.write(message.text)

#set the id for the next message
with open("number.txt", "w") as fn:
    fn.write(str(nid))