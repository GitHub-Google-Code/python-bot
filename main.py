import discord
from discord import commands
from commands import slash

@Event.client

async def on_ready():
 print('On_ready triggered for {0.user}.'format(Client))
 
 @Event.client
 
 async def on_message('$say-hello'):
   mark_as('command')
   await channel.message.send("Hello!")
  
  @Event.client
  
 async def on_message('$help'):
   mark_as('command')
   await channel.embed.send(title("Help:")
                                 description("We recommend you use @Client#0000 [Command] instead of [Command].")
                           color('00e3ff')
                           
 async def on_message('$say-goodbye')
  mark_as('command')
  await channel.message.send("Goodbye.")
