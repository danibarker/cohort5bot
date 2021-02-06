

import requests
import json

import timeit
import discord

from discord.ext import commands, tasks
import datetime
from discord import FFmpegPCMAudio
import os

import random
from discord.ext.tasks import loop
import youtube_dl as yt
from youtube_search import YoutubeSearch


current_list = []
class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.guild = client.get_guild(776122116629725254)
        self.music = discord.utils.get(self.guild.text_channels, name='music')
    @commands.command()
    async def code(self,ctx,*code):
        codemessage = 'To post code in the discord server, you can use a built in discord functionality to highlight code like VS Code does.  \nTo do this just type \\`\\`\\`js before your block of code and then end your block of code with \\`\\`\\` again. (note those are backticks, the key to the left of your 1 key on the keyboard)  \nIt will show up like this: ```js\nconst variable = 23\n\nfor (let n=0;n<5;n++){\n\tvariable = variable + n\n}```'
        await ctx.message.channel.send(codemessage)
    @commands.command()
    async def next(self,ctx):
        try:
            self.playlist.stop() # pylint: disable=undefined-variable
            player.stop()

        except:
            pass 
        try:
            self.playlist.start() # pylint: disable=undefined-variable
        except:
            pass

    @commands.command(aliases=['s', 'sto'])
    async def stop(self,ctx):
        try:
            self.playlist.stop() # pylint: disable=undefined-variable
            player.stop()

        except:
            pass
        
       

    @commands.command()
    async def play(self,ctx, *song):
        
        results = YoutubeSearch(' '.join(song), max_results=1).to_dict()
        print(results)
        for result in results:
    
            filename = result['title']+'-'+result['id']+'.mp3'
            filename = filename.replace(':'," -")
            filename = filename.replace('|', '_')
            filename = filename.replace('"',"'")
            filename = filename.replace('/','_')
            filename = filename.replace('?','')
            
            url = result['url_suffix']

        print(filename)
        y = yt.YoutubeDL({'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]})
        try: 
            f = open('data/music/'+filename,'rb')
            f.close()
        except:
            print(url)
            y.download([f'https://www.youtube.com/{url}'])
            os.rename(filename,'data/music/'+filename)
        try:
            channel = ctx.message.author.voice.channel
            await ctx.message.channel.send(f'Playing {result["title"]}')
        except AttributeError:
            await ctx.message.channel.send(f'Please join a Voice Channel to hear music')
        global player
        import time
        
        try:
            
            player = await channel.connect(timeout=120)
        except:
            pass
        try:
            player.play(FFmpegPCMAudio(executable = 'c:/ffmpeg/bin/ffmpeg.exe',source='data/music/'+filename))
        except:
            pass

    @loop(seconds=3)
    async def playlist(self):
        if not player.is_playing():
            f=os.listdir('data/music')
            for file in f:
                if not file.endswith('.mp3'):
                    f.remove(file)
            player.stop()
            filename = random.choice(f)
            player.play(FFmpegPCMAudio(executable = 'c:/ffmpeg/bin/ffmpeg.exe',source=f'data/music/{filename}'))
            await self.music.send(f'Now Playing {filename}')
        
    @commands.command(aliases=['playlist'])
    async def pl(self,ctx):
        channel = ctx.message.author.voice.channel
        global player
        try:
            player = await channel.connect()
        except:
            pass
        try:
            self.playlist.start() # pylint: disable=undefined-variable
        except:
            pass
    from discord.utils import get

   
   

def setup(client):
    client.add_cog(Music(client))