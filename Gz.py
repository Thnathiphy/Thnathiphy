from httpx import post
from threading import Thread
from time import sleep
from random import choice
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
from colorama import Fore
import os

print(Colorate.Horizontal(Colors.rainbow, f"""
╔══╗╔═╗╔═╗╔╗─╔╗╔═╗╔═╗     ╔══╗╔═╗╔═╦╗╔═╗     
║╔═╣║╬║║║║║╚╦╝║║╦╝║╬║     ╠══║║║║║║║║║╦╝     
║╚╗║║╗╣║║║╚╗║╔╝║╩╗║╗╣     ║══╣║║║║║║║║╩╗     
╚══╝╚╩╝╚═╝─╚═╝─╚═╝╚╩╝     ╚══╝╚═╝╚╩═╝╚═╝      """))
os.system(f"title Spam")

token = input("[ Token ] >>> : ")
guild = input("[ Guild id ] >>> :  ")
name = input("[ Channel name ] >>> :  ")
amount = int(input("[ Amount ] >>> :  "))

def spamchannel(guild,channel_name: str):
    response = post(
        f"https://discord.com/api/v10/guilds/{guild}/channels",
        json={"name": channel_name, "type": 0},
        headers= {"authorization": token}
    )
    print(response.status_code)
    if response.status_code == 429:
        sleep(response.json()["retry_after"])
        t = Thread(
            target=spamchannel,
            args=(
                channel_name,
            ),
        )
        t.start()
        t.join()

    else:
        jsonObj = response.json()
        print(f"[{Fore.GREEN}Success] Created {jsonObj['id']}")

task_done = 0
with ThreadPoolExecutor(max_workers=amount) as executor:
    for i in range(amount):
        executor.submit(spamchannel, guild,f"{name}")
        task_done += 1
        if task_done > 49:
            sleep(0.8)
            task_done = 0
#spamchannel
