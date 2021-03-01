import discord
from discord.ext import commands
from discord.ext.tasks import loop


class StatusPlugin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name = "statusloop")
  async def status_task(self, ctx, *, activity1, activity2, seconds1=15, seconds2=15):
    while True:
        await bot.change_presence(activity=discord.Game(name=activity1))
        await asyncio.sleep(seconds1)
        await bot.change_presence(activity=discord.Game(name=activity2))
        await asyncio.sleep(seconds2)
        
  @commands.Cog.listener()
  async def on_ready():
    self.bot.loop.create_task(status_task())
    
    
def setup(bot):
  bot.add_cog(StatusPlugin(bot))
        
 
    
