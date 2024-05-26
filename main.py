import discord
from discord.ext import commands, tasks
import asyncio

bot = commands.Bot(command_prefix=';', case_insensitive=True, self_bot=True, chunk_guilds_at_startup=False, request_guilds=False)
bot.remove_command('help')

channel_id = 1111111111        
    
@tasks.loop(seconds=5)
async def whatever(cmd, channel):
    try:
        await asyncio.sleep(1)
        await cmd.__call__(channel=channel) 
        # if you have arguments in the slash command you have to specify them like this (channel=channel, arg='whatever', arg2='wahtever')
        # example: lets say the slash command has an argument for name and age; (channel=channel, name='Joey', age='18') 
    except discord.errors.InvalidData:
        await asyncio.sleep(2)
        return        
    
@bot.event
async def on_message(message: discord.Message):
    if message.author.id == bot.user.id:
        if message.content == "!start":
            await message.delete()
            channel = bot.get_channel(channel_id)
            
            async for command in channel.slash_commands(command_ids=[851267333665456158]): # Only locked to specific command ids, you can add more ids if you want, this is just an example
                if command.id == 851267333665456158:
                    cmd = command
                # ^^^^^ you can add another one of these for another command or however many you want if you want to start them all at once
                whatever.start(cmd, channel)
                # ^^^^^ Starts task loop
                
    if message.channel.id == channel_id and message.author.id == bot.user.id:
        if message.content == "!stop":
            await message.delete() 
            whatever.cancel()     
            
bot.run(token='OTcwNDQ0OTI2MjYzMzc3OTQw.Ym8DeA.mcuRh0Cm2mKM38utfsq4FqLhl1I', reconnect=True)
