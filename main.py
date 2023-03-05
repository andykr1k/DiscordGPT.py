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
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}])
    print("User: \n" + message)
    print("Bot: \n" + response['choices'][0]['message']['content'].strip())
    await interaction.response.send_message("Prompt: " + message + response['choices'][0]['message']['content'], ephemeral = True)

@client.event
async def on_ready():
    await tree.sync()
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
