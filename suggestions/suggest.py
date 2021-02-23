import discord
from discord.ext import commands
from discord.utils import get


class SuggestPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(
      name="suggest",
      description="Suggest a feature to be added to the server.",
      usage="events"
    )
    @commands.cooldown(2, 600, commands.BucketType.user) 
    async def suggest(self, ctx, *, message):
      await ctx.send("Thank you for your suggestion, it has been posted in <#783624120034263085>")
      embed = discord.Embed(title = "Suggestion", description = message, color = 0x2E9DFF)
      embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

      channel = self.bot.get_channel(783624120034263085)
      suggestion = await channel.send(embed=embed)
      await suggestion.add_reaction("👍")
      await suggestion.add_reaction("👎")

    @suggest.error
    async def suggest_error(self, ctx, error):
     if isinstance(error, commands.CommandOnCooldown):
        err = 'You\'re on a cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(err)
     else:
        raise error



def setup(bot):
    bot.add_cog(SuggestPlugin(bot))
