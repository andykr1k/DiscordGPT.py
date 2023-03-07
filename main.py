import os
import openai

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "gpt", description = "Ask ChatGPT Anything!") 

async def first_command(interaction, message: str):
    await interaction.response.send_message("Hello!" + "\nThe text sent was: " + message, ephemeral = True)

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} has connected to Discord!')


# openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )

client.run(TOKEN)
