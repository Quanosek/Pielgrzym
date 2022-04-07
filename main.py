# start 123
import discord
from discord.ext import commands
from server import Website
import os

client = commands.Bot(command_prefix='+', intents=discord.Intents.all())
client.remove_command('help')


# on ready
@client.event
async def on_ready():

    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='Na Straży'))

    print(' * Successfully logged in!')


# błędne komendy
@client.event
async def on_command_error(ctx, error):
    await ctx.message.add_reaction('❌')


# import cogs
from commands import commands
#from special import special


#from special import special
async def setup():
    await client.wait_until_ready()
    client.add_cog(commands(client))
    #client.add_cog(special(client))


# przywitanie

id_testowy = 869910592536866847  # id serwera testowego
id_pana = 797894580485226527  # id serwera Wysławiajcie Pana!

server_id = id_pana  # id serwera
channel_id = 797894580485226530  # id kanału do wysyłania wiadomości


@client.event
async def on_member_join(member):
    guild = client.get_guild(server_id)
    channel = guild.get_channel(channel_id)

    # wiadomość na czacie

    await channel.send(f':wave: Witaj {member.mention} na serwerze!')

    # wiadomość prywatna

    await member.send(
        f'Witaj {member.mention}! Ja wiem kim jesteś, ale aby każdy mógł to wiedzieć, proszę, ustaw swoje imię i nazwisko jako nick na serwerze! Następnie przejdź do kanału z rolami i przydziel sobie role odpowiednie dla siebie. Pamiętaj, że w każdej z kategorii możesz wybrać tylko jedną rolę! Życzę miłego pobytu i dobrej zabawy! :wink:'
    )


# pożegnanie


@client.event
async def on_member_remove(member):
    guild = client.get_guild(server_id)
    channel = guild.get_channel(channel_id)

    # wiadomość na czacie

    await channel.send(f'**{member.name}** opuścił(a) nasz serwer!')


# dodawanie reakcji do wiadomości


@client.command(aliases=['r', 'reakcja', 'reaguj'])
async def react(ctx, emoji="", msgID: int = ""):
    if emoji == '' and msgID == '':  # pomoc
        await ctx.message.add_reaction('✅')
        await ctx.channel.send(
            '**Aby dodać reakcję do wiadomości musisz wpisać:**\n <prefix><react> <emoji> <id wiadomości>\n\n**W polu <react> możesz również użyć:**\nr, reakcja, reaguj.'
        )
    else:
        msg = await ctx.fetch_message(msgID)
        await msg.add_reaction(emoji)
        await ctx.message.delete()


# reaction-roles

import json


@client.command(
    aliases=['rr', 'reactionrole', 'reaction-roles', 'reaction-role'])
async def reactionroles(ctx,
                        emoji='',
                        role: discord.Role = '',
                        msgID: int = '',
                        mode='normal'):

    if emoji == '' and role == '' and msgID == '' and mode == 'normal':  # pomoc
        await ctx.message.add_reaction("✅")
        await ctx.channel.send(
            '**Aby dodać reaction-roles** (reakcja daje rolę) **do wiadomości musisz wpisać:**\n <prefix><reactionroles> <emoji> <rola> <id wiadomości> <typ>\n\n**W polu <typ> dostępne są następujące funkcje:**\n**normal** - po kliknięciu w reakcję otrzymuje się rolę\n**unique** - można wybrać jedynie jedną reakcję\n**verify** - rola może zostać tylko przyznana, nie usunięta\n\n**W polu <reactionroles> możesz również użyć:**\nrr, reactionrole, reaction-roles,reaction-role.'
        )
    else:  # właściwa funkcja
        msg = await ctx.fetch_message(msgID)
        await msg.add_reaction(emoji)
        await ctx.message.delete()

        with open('reactionroles.json') as json_file:
            data = json.load(json_file)

            new_reaction_roles = {
                'role_name': role.name,
                'role_id': role.id,
                'emoji': emoji,
                'message_id': msg.id,
                'mode': mode
            }

            data.append(new_reaction_roles)

        with open('reactionroles.json', 'w') as j:
            json.dump(data, j, indent=4)


@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass
    else:
        with open('reactionroles.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x[
                        'message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles,
                                             id=x['role_id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):

    with open('reactionroles.json') as react_file:

        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name and x[
                    'message_id'] == payload.message_id:
                role = discord.utils.get(client.get_guild(
                    payload.guild_id).roles,
                                         id=x['role_id'])

                await client.get_guild(payload.guild_id
                                       ).get_member(payload.user_id
                                                    ).remove_roles(role)


# end
client.loop.create_task(setup())

Website()
client.run(os.environ['TOKEN'])
