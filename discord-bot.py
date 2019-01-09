#!/usr/bin/env python
import asyncio

import discord


client = discord.Client()

@client.event
async def on_ready():
    print("Logged")


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Do not handle bot’s messages.
    await client.send_message(message.channel, message.content[::-1])


client.run("<YOUR_TOKEN_HERE>")

