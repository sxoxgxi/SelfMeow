# use at yer own risk! if u wantto esacpe rate limit change content of line 30 ok peace out meow
import discord
import keep_alive
import os
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=("sex"))

class SogiSB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
  # make it join vc
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

    @commands.command()
  # mak it leave vc
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
  # mass DM
    async def meow(self, ctx):
        for user in ctx.guild.members:
            try:
                await user.send("yer message")
                await asyncio.sleep(5)
                print(f"Sent {user.name} a DM")
            except Exception as meow:
                print(meow)



@bot.event
async def on_ready():
    print(f'{bot.user} Joined the party!')

  
def setup(bot):
 bot.add_cog(SogiSB(bot))

keep_alive.keep_alive()

bot.run(os.getenv("TOKEN"))
