from discord.ext import commands

#komendy specjalnie dla kanału z rolami


class special(commands.Cog):
    def __init__(self, client):
        self.client = client

    #komendy

    @commands.command()
    async def r1(ctx):
        await ctx.channel.send(
            '⠀\n**NA TYM KANALE WYBIERZ ODPOWIEDNIE ROLE (tylko zgodnie z prawdą) PRZEZ KLIKNIĘCIE NA WŁAŚCIWĄ REAKCJĘ!**\n⠀'
        )

    @commands.command()
    async def r2(ctx):
        await ctx.channel.send(
            '```JAKIEJ JESTEŚ PŁCI?```\n:male_sign:⠀|⠀chłopak\n:female_sign:⠀|⠀dziewczyna\n⠀'
        )

    @commands.command()
    async def r3(ctx):
        msg = await ctx.channel.send(
            '⠀\n```TERAZ, ILE MASZ LAT?```\n:chipmunk:⠀|⠀< 13 lat\n:sheep:⠀|⠀13-15 lat\n:elephant:⠀|⠀16-18 lat\n:whale:⠀|⠀18 < lat\n⠀'
        )
        await msg.add_reaction("✅")

    @commands.command()
    async def r4(ctx):
        await ctx.channel.send(
            '⠀\n```A SKĄD JESTEŚ?```\n:green_apple:⠀|⠀dolnośląskie\n:lemon:⠀|⠀kujawsko-pomorskie\n:apple:⠀|⠀lubelskie\n:tangerine:⠀|⠀lubuskie\n:broccoli:⠀|⠀łódzkie\n:watermelon:⠀|⠀małopolskie\n:grapes:⠀|⠀mazowieckie\n:strawberry:⠀|⠀opolskie\n:blueberries:⠀|⠀podkarpackie\n:avocado:⠀|⠀podlaskie\n:pineapple:⠀|⠀pomorskie\n:mango:⠀|⠀śląskie\n:kiwi:⠀|⠀świętokrzyskie\n:corn:⠀|⠀warmińsko-mazurskie\n:coconut:⠀|⠀wielkopolskie\n:onion:⠀|⠀zachodniopomorskie\n:earth_africa:⠀|⠀zza granicy\n⠀'
        )

    @commands.command()
    async def r5(ctx):
        await ctx.channel.send(
            f'⠀\n**KONIECZNIE SPRAWDŹ JESZCZE KANAŁ <#817658444810682379>, gdzie na bieżąco pojawiają się nowe role!**'
        )


def setup(client):
    client.add_cog(special(client))
