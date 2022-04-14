from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called


  
my_secret = os.environ['your key for bot token goes here']
bot.run(my_secret)
