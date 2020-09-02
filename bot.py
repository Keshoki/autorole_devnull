from discord.ext import commands
import discord, chalk

import os

bot = commands.Bot(command_prefix="!", status = discord.Status.idle, activity=discord.Game(name = "Ébredezek ne nézzé.."))

bot.remove_command("help")

@bot.event
async def on_ready():
    print(chalk.green("Online vagyok!"))
    print(chalk.blue(f"{len(bot.guilds)} szerveren vagyok fent"))
    await bot.change_presence(status = discord.Status.online, activity=discord.Game(name = "Sex on the beach"))

@bot.event
async def on_message(message):
    id = bot.get_guild(706679716907843635)
    user = message.author.name
    msg = message.content
    if msg == "!users":
        await message.channel.send("{} köcsög bassza itt a rezet.".format(id.member_count))
    print(chalk.green(f"{user} üzenete: {msg}"))

    await bot.process_commands(message)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 750722441722069022:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'bash':
            role = discord.utils.get(guild.roles, name='BASH')
        if payload.emoji.name == 'htb':
            role = discord.utils.get(guild.roles, name='HTB')
        if payload.emoji.name == 'cpp':
            role = discord.utils.get(guild.roles, name='C++')
        elif payload.emoji.name == 'python':
            role = discord.utils.get(guild.roles, name='Python')
        elif payload.emoji.name == 'lua':
            role = discord.utils.get(guild.roles, name='Lua')
        elif payload.emoji.name == 'clang':
            role = discord.utils.get(guild.roles, name='C')
        elif payload.emoji.name == 'nodejs':
            role = discord.utils.get(guild.roles, name='NodeJS')
        elif payload.emoji.name == 'postgresql':
            role = discord.utils.get(guild.roles, name='PostgreSQL')
        elif payload.emoji.name == 'go':
            role = discord.utils.get(guild.roles, name='Go')
        elif payload.emoji.name == 'java':
            role = discord.utils.get(guild.roles, name='Java')
        elif payload.emoji.name == 'rust':
            role = discord.utils.get(guild.roles, name='Rust')
        elif payload.emoji.name == 'php':
            role = discord.utils.get(guild.roles, name='PHP')
        elif payload.emoji.name == 'csharp':
            role = discord.utils.get(guild.roles, name='C#')
        elif payload.emoji.name == 'mysql':
            role = discord.utils.get(guild.roles, name='MySQL')
        elif payload.emoji.name == 'javascript':
            role = discord.utils.get(guild.roles, name='JavaScript')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print(chalk.green("Role hozzáadva."))
            else:
                print(chalk.red("Nincs ilyen tag."))
        else:
            print(chalk.red("Nincs ilyen role."))

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 750722441722069022:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

        if payload.emoji.name == 'bash':
            role = discord.utils.get(guild.roles, name='BASH')
        if payload.emoji.name == 'htb':
            role = discord.utils.get(guild.roles, name='HTB')
        if payload.emoji.name == 'cpp':
            role = discord.utils.get(guild.roles, name='C++')
        elif payload.emoji.name == 'python':
            role = discord.utils.get(guild.roles, name='Python')
        elif payload.emoji.name == 'lua':
            role = discord.utils.get(guild.roles, name='Lua')
        elif payload.emoji.name == 'clang':
            role = discord.utils.get(guild.roles, name='C')
        elif payload.emoji.name == 'nodejs':
            role = discord.utils.get(guild.roles, name='NodeJS')
        elif payload.emoji.name == 'postgresql':
            role = discord.utils.get(guild.roles, name='PostgreSQL')
        elif payload.emoji.name == 'go':
            role = discord.utils.get(guild.roles, name='Go')
        elif payload.emoji.name == 'java':
            role = discord.utils.get(guild.roles, name='Java')
        elif payload.emoji.name == 'rust':
            role = discord.utils.get(guild.roles, name='Rust')
        elif payload.emoji.name == 'php':
            role = discord.utils.get(guild.roles, name='PHP')
        elif payload.emoji.name == 'csharp':
            role = discord.utils.get(guild.roles, name='C#')
        elif payload.emoji.name == 'mysql':
            role = discord.utils.get(guild.roles, name='MySQL')
        elif payload.emoji.name == 'javascript':
            role = discord.utils.get(guild.roles, name='JavaScript')

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print(chalk.green("Role levéve."))
            else:
                print(chalk.red("Nincs ilyen tag."))
        else:
            print(chalk.red("Nincs ilyen role."))

@bot.event
async def on_message_delete(message):
    user = message.author.name
    msg = message.content
    print(chalk.red(f"{user} üzenete törölve lett: {msg}"))

@bot.command()
async def kill(ctx):
    await bot.logout()

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)

    embed = discord.Embed(title=f"**{ping}ms pingem van** :ping_pong:", colour=discord.Color.green())

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    await ctx.send(embed=embed)



@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=member)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"lekérdező tag: {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Becenév:", value=member.display_name)

    embed.add_field(name=f"Rangok ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Legmagasabb rang:", value=member.top_role.mention)

    embed.add_field(name="Fiók létrehozva:", value=member.created_at.strftime("%a, %Y %B %#d, %I:%M %p"))
    embed.add_field(name="Csatlakozás dátuma:", value=member.joined_at.strftime("%a, %Y %B %#d, %I:%M %p"))

    await ctx.send(embed=embed)



bot.run(os.environ['TOKEN'])
