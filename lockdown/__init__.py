from .lockdown import Lockdown
from redbot.core.bot import Red


def setup(bot: Red):
    bot.add_cog(Lockdown())
