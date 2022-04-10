import bot_token

import disnake
from disnake.ext import commands

TOKEN = bot_token.get()

bot = commands.Bot(
    command_prefix=">",
)

# Responds with pong
@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

# Informs the user of the author
@bot.command(name="author")
async def get_author(ctx):
    author = ctx.author 

    if not ctx.author == None: 
        await ctx.send(f'Author of message: {author}')
    else: 
        await ctx.send("Author not found")

@bot.command(name="whatserver")
async def get_server(ctx):
    server = ctx.guild
    await ctx.send(f'This message was sent in {server}')


bot.run(TOKEN)

