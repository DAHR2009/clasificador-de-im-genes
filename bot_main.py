import discord
from discord.ext import commands
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url 
            
            await attachment.save(f"./{file_name}")
            clase=get_class("keras_model.h5" , "labels.txt" , f"./{file_name}")
            await ctx.send(f"Imagen guardada en./{file_url}")
            if clase[0]== "Coches":
                await ctx.send("Esto es un coche")
            elif clase[0] == "Personas":
                await ctx.send("Esto es una persona")
    else:
        await ctx.send("No has subido ninguna imagen:(")

bot.run("Pon tu token")
