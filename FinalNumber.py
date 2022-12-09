from discord.ext import commands

NUMBER_CODE_DICT = {'A': '1', 'B': '2',
                    'C': '3', 'D': '4', 'E': '5',
                    'F': '6', 'G': '7', 'H': '8',
                    'I': '9', 'J': '10', 'K': '11',
                    'L': '12', 'M': '13', 'N': '14',
                    'O': '15', 'P': '16', 'Q': '17',
                    'R': '18', 'S': '19', 'T': '20',
                    'U': '21', 'V': '22', 'W': '23',
                    'X': '24', 'Y': '25', 'Z': '26', }


def number_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += NUMBER_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' / '

    return cipher


def number_decrypt(message):
    message = message.split()
    number_dict = dict((v, k) for (k, v) in NUMBER_CODE_DICT.items())
    decipher = ''
    for i in message:
        decipher += number_dict[i]
    return decipher


def number(message):
    try:
        return number_decrypt(message)
    except:
        return number_encrypt(message)


class Number(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def number(self, ctx, *, arg):
        await ctx.send(f'```{number_encrypt(arg)}```')


def setup(bot):
    bot.add_cog(Number(bot))
