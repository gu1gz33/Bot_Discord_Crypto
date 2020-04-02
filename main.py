# bot.py
#By Guillaume Desoutter
#Création d'un bot Discord qui récupère les cours des crypto et les envoie sur le chan
# On importe les librairies
import os
import discord
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import urllib3
import re

http = urllib3.PoolManager()

#ON CHARGE LE BOT
load_dotenv()
TOKEN = #Token de ton bot
client = discord.Client()

#Fonction pour récupérer le prix de la crypto choisi à travers l'url sur le site stelareum il suffit de changer le nom avant le html avec l'abréviation de la crypto 
def get_the_price(url):
    global price
    page = http.request('GET', url)
    soup = BeautifulSoup(page.data)
    price = soup.select_one("span[class*=exchange_rate]").text
    #On fait de la regex pour avoir juste le prix et pas les espaces en trop ou les virgules genantes
    pattern = re.compile(r'\s+')
    price = re.sub(pattern, '', price)
    price = price.replace(',','')
    return price

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Je commente juste pour le bitcoin si vous voulez rajouter des crypto il suffira de suivre l'exemple ci-dessous
    #On choisis les messages auxquel le bot réagira, pour en rajouter vous faite juste un: or message.content == 'votre texte'
    if message.content == '!bitcoin' or message.content == '!BTC' or message.content == '!btc' or message.content == '!BITCOIN':
        #changer l'url pour la monnaie que vous voulez, allez sur cette url pour les récupérer: https://www.stelareum.io/currency/
        url = 'https://www.stelareum.io/currency/btc.html'
        #On appelle la fonction avec l'url de la crypto qu'on a choisi
        get_the_price(url)
        #Je rajoute un dollar à la fin du prix
        bot_msg = price + "$"
        #Je colore mon texte
        embed=discord.Embed(color=0x40ff00)
        #Vous pouvez changer le titre du message du bot avec la crypto que vous avez choisi
        embed.add_field(name="Valeur du Bitcoin:", value=bot_msg, inline=False)
        #Le bot envoie le message
        await message.channel.send(embed=embed)

    if message.content == '!ethereum' or message.content == '!ETH' or message.content == '!eth' or message.content == '!ETHEREUM':
        url = 'https://www.stelareum.io/currency/eth.html'
        get_the_price(url)
        bot_msg = price + "$"
        embed=discord.Embed(color=0x40ff00)
        embed.add_field(name="Valeur de l'Ethereum:", value=bot_msg, inline=False)
        await message.channel.send(embed=embed)
    
    if message.content == '!ripple' or message.content == '!XRP' or message.content == '!xrp' or message.content == '!RIPPLE':
        url = 'https://www.stelareum.io/currency/xrp.html'
        get_the_price(url)
        bot_msg = price + "$"
        embed=discord.Embed(color=0x40ff00)
        embed.add_field(name="Valeur du Ripple:", value=bot_msg, inline=False)
        await message.channel.send(embed=embed)

    if message.content == '!litecoin' or message.content == '!LTC' or message.content == '!ltc' or message.content == '!LITECOIN':
        url = 'https://www.stelareum.io/currency/ltc.html'
        get_the_price(url)
        bot_msg = price + "$"
        embed=discord.Embed(color=0x40ff00)
        embed.add_field(name="Valeur du Litecoin:", value=bot_msg, inline=False)
        await message.channel.send(embed=embed)

    if message.content == '!tether' or message.content == '!USDT' or message.content == '!usdt' or message.content == '!TETHER':
        url = 'https://www.stelareum.io/currency/usdt.html'
        get_the_price(url)
        bot_msg = price + "$"
        embed=discord.Embed(color=0x40ff00)
        embed.add_field(name="Valeur du Tether:", value=bot_msg, inline=False)
        await message.channel.send(embed=embed)

    if message.content == '!WazirX' or message.content == '!wrx' or message.content == '!WRX' or message.content == '!WAZIRX' or message.content == '!wazirx':
        url = 'https://www.stelareum.io/currency/wrx.html'
        get_the_price(url)
        bot_msg = price + "$"
        embed=discord.Embed(color=0x40ff00)
        embed.add_field(name="Valeur du WazirX:", value=bot_msg, inline=False)
        await message.channel.send(embed=embed)

client.run(TOKEN)
