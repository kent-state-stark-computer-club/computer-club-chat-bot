import discord
import openai
from discord.ext import commands

#replace with api keys for discord dev api and openai api
TOKEN = 'discord key here'
GEEPY_TOKEN = 'chatGPT key here'


# Declaring intents
intents = discord.Intents.default()  # enable default permissions
intents.typing = False  # disabling uneeded default permissions
intents.presences = False  ####

#some more permissions, not too versed on exactly which intents correspond to what functionality
intents.messages = True
intents.guilds = True
intents.message_content = True


# Create a new instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

#chatGPT token validation
openai.api_key = GEEPY_TOKEN


#checks if chatGPTs response is too long, truncates and adds a message
##currently the system prompt keeps the length short enough
##but if chatGPT over sends this will prevent a discord msg length error
def truncate_message(msg):
    if len(msg) > 1800:
        msg = msg[:1800]
        msg += "...\nMessage Too Long for Discord: For more details, please use the web interface of ChatGPT."
    return msg

# Event: When the bot is ready, print its username
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} (ID: {bot.user.id})')
  
#declaring a new bot command function named ask  
@bot.command()
async def ask(ctx, *, user_input):
    
    #ignores requests from bots
    if ctx.author.bot:
        return
    
    #system message first to give chatGPT some guidance on how to respond to chat requests
    messages = [{"role": "system", "content": "Please keep your responses under 500 characters in length. If your response would require detailed steps please just summarize it and suggest asking chatGPT at chat.openai.com"},  
                {"role": "user", "content": user_input}]
    
    try:
        # Get response from chatGPT
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        # Extract the content from the bot's message 
        bot_response = response.choices[0].message['content']
        
        #Check if message is too long
        bot_response = truncate_message(bot_response)
        
        # Send the response to the Discord channel
        await ctx.send(bot_response)
        
        
        
        #handling some errors
        
        #openai throws invalid request error
    except openai.error.InvalidRequestError:
        await ctx.send("The request to this chat bot was invalid.")
        
        #rate limit exceeded
    except openai.error.RateLimitError:
        await ctx.send("The bot is being heavily used right now. Please wait and try again.")
        
        #handle non specific errors
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

#starts the bot
bot.run(TOKEN)
