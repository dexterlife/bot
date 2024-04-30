from email import message
import random
import discord
from discord.ext import commands

# Intents
intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True
intents.members = True

# Initialisation du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Import de la classe Permissions
from discord import Permissions

# Fonction "on_ready" pour confirmer la connexion réussie du bot
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")

# Commande !ping
@bot.command()
async def ping(ctx):
    await ctx.send("pong 🏓")

# Commande !touché
@bot.command()
async def touché(ctx): 
    await ctx.send("coulé ! 💥")
  
# Commande !members
@bot.command()
async def members(ctx):
    members_info = ""
    for member in ctx.guild.members:
        roles = [role.name for role in member.roles]
        members_info += f"{member.display_name}: {', '.join(roles)}\n"
    await ctx.send(members_info)

# Réactions automatiques
@bot.event
async def on_message(message):
    if "bonjour" in message.content.lower():
        await message.add_reaction("👋")
    
    # Vérifie si le message contient un mot spécifique à bannir
    if "merci" in message.content.lower():
        # Bannir l'utilisateur
        await message.author.ban(reason="Utilisation d'un mot interdit")
        await message.channel.send(f"{message.author.mention} a été banni pour avoir utilisé un mot interdit.")
    
    await bot.process_commands(message)

# Liste de blagues
jokes = [
  "  Is there a hole in your shoe? No… Then how’d you get your foot in it?",
    "Did you know crocodiles could grow up to 15 feet? But most just have 4",
    "What kind of magic do cows believe in? MOODOO.",
    "Why are oranges the smartest fruit? Because they are made to concentrate..",
    "Did you hear about the scientist who was lab partners with a pot of boiling water? He had a very esteemed colleague."
]

# Commande !joke
@bot.command()
async def joke(ctx):
    joke = random.choice(jokes)
    await ctx.send(joke)

# Message de bienvenue
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f"Bienvenue {member.mention} sur le serveur CONNARD.")

# Commande !welcome
@bot.command()
async def welcome(ctx):
    await ctx.send("Bienvenue sur notre serveur ! ne me derange pas trop avec tes commandes.")
    
    await bot.process_commands(message)

# Connexion du bot au serveur avec le token
bot.run("TOKEN")
