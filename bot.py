from settings import *
from roll import *

import discord
from discord.ext import commands

client = discord.Client()


bot = commands.Bot(command_prefix=">")


@bot.command()
async def helpme(ctx):
    await ctx.send(
        """
        Currently our supa-dupa useful bot has two commands:
            - >cast -> Roll da dice in format { <num>d<num> : +- mods : +- }. Last one is (dis)advandtage.
            - >character -> Roll da character stats in format of 3d6 or 4d6. More formats might be added (or not).
        """
    )


@bot.command()
async def cast(ctx, *, arg):
    results = cast_die(arg)
    if len(results) > 1900:
        print(f"{ctx.author.name}#{ctx.author.discriminator}:\n\ttoo much")
        await ctx.send(
            f"{ctx.author.mention}, Wow... That was too much for me to comprehend."
        )
    else:
        print(f"{ctx.author.name}#{ctx.author.discriminator}:{arg}\n\t{results}")
        await ctx.send(f"{ctx.author.mention}\n> {arg}\n{results}")


@bot.command()
async def character(ctx, *, arg):
    if arg is None:
        await ctx.send(
            f"{ctx.author.mention}\nWhy did you do it tho? (no format provided. eg.: 4d6, 3d6)"
        )
    results = roll_character(arg)
    if len(results) > 1900:
        print(f"{ctx.author.name}#{ctx.author.discriminator}:\n\ttoo much")
        await ctx.send(
            f"{ctx.author.mention}, Wow... That was too much for me to comprehend."
        )
    else:
        print(f"{ctx.author.name}#{ctx.author.discriminator}:{arg}\n\t{results}")
        await ctx.send(f"{ctx.author.mention}\n> {arg}\n{str(results)}")


bot.run(TOKEN)
