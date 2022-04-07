from discord.ext import commands

#podstawowe komendy


class commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    #pomoc

    @commands.command(aliases=['p', 'h', 'help'])
    async def pomoc(self, ctx):
        await ctx.message.add_reaction("✅")
        await ctx.channel.send(
            '**Pamiętaj, że ten bot jest nieustannie rozwijany!**\n\nMój prefix to ``+``, wypróbuj go!\n\n...a jeśli nie wiesz jak dokładnie działa jakaś komenda wystarczy, że wpiszesz ``+lista``.\nZostanie wtedy do Ciebie wysłana pełna lista wszystkich dostępnych komend :D'
        )

    #lista komend

    @commands.command(aliases=['l', 'list'])
    async def lista(self, ctx):
        await ctx.message.delete()
        await ctx.author.send(
            '**Witaj!**\nOto przed Tobą lista wszystkich moich komend:\n\n>> **pomoc** oraz ``p``, ``h``, ``help`` - wiadomość informacyjna\n>> **clear** oraz ``c``, ``u``, ``usun``, ``usuń``, ``d``, ``delete``, ``del`` - komenda służąca do usuwania poprzednich wiadomości. Aby jej poprawnie użyć należy wpisać ``<prefix><clear> <ilość>``. W przypadku nie wpisania żadnej liczby zostanie usunięta 1 wiadomość!\n\n>> **react** - służy do dodawania reakcji pod określoną wiadomością.\n>> **reactionroles** - służy do tworzenia reaction-roles (reakcja daje rolę) pod określoną wiadomością.\n\n**... i to na razie tyle :D**\n\nStrona internetowa:\nhttps://bit.ly/379ANMC'
        )

    #ping-pong

    @commands.command(aliases=['Ping', 'Ping!', 'ping!'])
    async def ping(self, ctx):
        await ctx.message.add_reaction('🏓')
        await ctx.channel.send('Pong!')

    @commands.command(aliases=['Pong', 'Pong!', 'pong!'])
    async def pong(self, ctx):
        await ctx.message.add_reaction('🏓')
        await ctx.channel.send('Ping!')

    #usuwanie wiadomości

    @commands.command(aliases=['c', 'u', 'usun', 'usuń', 'd', 'delete', 'del'])
    async def clear(self, ctx, amount: str = '1'):
        if amount == 'all':
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=(int(amount) + 1))


def setup(client):
    client.add_cog(commands(client))
