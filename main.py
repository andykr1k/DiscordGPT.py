import asyncio
import os
import openai

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv("OPENAI_KEY")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "gpt", description = "Ask ChatGPT Anything!")

async def first_command(interaction, message: str):
    await interaction.response.defer()
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    await asyncio.sleep(delay=0)
    print("User: \n" + message)
    print("Bot: \n" + response['choices'][0]['message']['content'].strip())
    await interaction.followup.send("Prompt: " + message + "\n\n" + response['choices'][0]['message']['content'].strip() + "\n", ephemeral = True)

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
