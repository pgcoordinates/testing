import discord
import asyncio

bot = discord.Client(chunk_guilds_at_startup=False, request_guilds=False)
   
@bot.event
async def on_message(message: discord.Message):
    if message.author.id == bot.user.id:
        if message.content == "!start":
            await message.delete()
            
            
bot.run(token='TOKEN')
