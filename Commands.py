import discord
from discord.ext import commands
from discord import channel
from discord.ext import commands
from datetime import datetime

client = discord.Client()
self.bot = bot

#on_ready event

@client.event
async def on_ready():
    print(f'Logged in as {self.bot.user} ({self.bot.user.id})')
    
@client.event
async def on_resumed(self):
    print(f'{self.bot.user} has reconnected')
    
@client.event
async def on_command_error(self, cty, error):
    await ctx.send(error)

#status-task

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Aboniert HandOfBlood'))



#help command

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '$help' in message.content:
        embedVar = discord.Embed(title="**Dein Retter in der Not.**",description="...In Wartung <a:error:893544265035161600>...", color=0x00ff0)
        embedVar.add_field(name="<:dogdead:893543302496931862> ", value="Noch gibt es keine Commands", inline=False)
        embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/877878077747785739/893546038982483968/Discordload.gif")
        await message.channel.send(embed=embedVar)



#Roles

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '$Foodpornroles' in message.content:
        embedVar = discord.Embed(title='**Foodpornrols**' ,description='Hier gibts Rollen rund ums Essen.', color=242131)
        embedVar.add_field(name= '<:Chefexcelent:897499031301943317>' , value= 'Du kochst gerne und willst auch ab und an ein geiles Rezept posten.' ,inline=False)
        embedVar.add_field(name='🥘', value=' Du kannst/willst nicht kochen, du Postest nur gerne geiles Essen.',inline=False)
        embedVar.add_field(name='<a:Voollgefressen:897505438441046136>' , value= 'Du isst einfach zu gerne (vielleicht auch zu viel ;). )',inline=False)
        embedVar.set_image(url='https://cdn.discordapp.com/attachments/837348459396202526/897506296473976852/pings-removebg-preview.png')
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('<:Chefexcelent:897499031301943317>')
        await msg.add_reaction('🥘')
        await msg.add_reaction('<a:Voollgefressen:897505438441046136>')
