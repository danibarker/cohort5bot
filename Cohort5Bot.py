
from discord.ext import commands

client = commands.Bot(command_prefix='!',case_insensitive=True)
channel_id = 0
COGS = ['music']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for filename in COGS:
        try:
            client.load_extension(f'cogs.{filename}')
        except Exception as e:
            print(e)



@client.command()
async def load(message, extension):
    if extension.upper() == 'ALL':
        for filename in COGS:
            try:
                client.load_extension(f'cogs.{filename}')
            except Exception as e:
                print(e)
        await message.channel.send('All cogs loaded')
    else:
        try:
            client.load_extension(f'cogs.{extension.lower()}_cog')
            msg = f'{extension} cog loaded'
        except Exception as e:
            msg = e
        await message.channel.send(msg)


@client.command()
async def unload(message, extension):
    if extension.upper() == 'ALL':
        for filename in COGS:
            try:
                client.unload_extension(f'cogs.{filename}')
            except Exception as e:
                print(e)
        await message.channel.send('All cogs unloaded')
    else:
        try:
            client.unload_extension(f'cogs.{extension}_cog')
            msg = f'{extension} cog unloaded'
        except Exception as e:
            msg = e
        await message.channel.send(msg)

client.run('Nzc3MzczMzIxMDUwMTkzOTQx.X7CfUg.GrwR5rzZFSUczOLSkc69_eKlt18')