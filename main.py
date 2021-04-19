# video utilizado: freeCodeCamp.org
# https://www.youtube.com/watch?v=SPTfmiYiuok

# criar bot -> https://discord.com/developers/applications/

import discord  # Importar configurações discord
import os  # Permitir import do Token de outro arquivo
import random  #hehehe
import time #sleep p as mensagems
import json

# Para checar membros, é necessario permitir intents nas configurações do bot
# DiscordBot -> Bot -> permitir todas as intents
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event  # registrar um evento
async def on_ready():  # eventos ja prontos, quando o bot estiver pronto:
	print(f"We have logged in as {client.user}")

	await client.change_presence(activity=discord.Game(
			name="~help for commands"))

# manda alguma coisa aleatoria
#await message.channel.send(mensagem_motivacional[random.randint(0,mensagensImportantes.len())])
f = open("mensagens.txt", "r")
mensagensImportantes = []
while True:
	aux = f.readline()
	if aux == '':
		break
	mensagensImportantes.append(aux)

copypastas = os.listdir("copypastas/")

@client.event  # proximo evento, se bot receber uma mensagem
async def on_message(message):

	# #evita fazer algo se a mensagem for do proprio bot
	# if message.author == client.user:
	#   return 0

	msg = message.content  # substituir mais facilmente

	if msg.endswith("ao") or msg.endswith("ão") and message.author != client.user:
		# await message.channel.send("Meu pau na sua mão.")
		await message.channel.send(f"{message.author.mention} Meu pau na sua mão.")
	
	elif msg.endswith("ta") and message.author != client.user and not msg.startswith("~copypasta"):
		# await message.channel.send("Meu pau te cutuca.")
		await message.channel.send(f"{message.author.mention} Meu pau te cutuca.")
	
	if "duvido" in msg and message.author != client.user:
		# await message.channel.send("Meu pau no teu ouvido.")
		await message.channel.send(f"{message.author.mention} Meu pau no teu ouvido.")

	

	# Dar spam em pessoas
	if msg.startswith("~spam"):
		#~spam 20 mensagem

		spam = msg.split(" ",1)[1]
		n,spam = spam.split(' ', 1)

		for i in range(int(n)):
			await message.channel.send(spam)
			time.sleep(0.6)
		await message.channel.send(mensagensImportantes[random.randint(0,len(mensagensImportantes))])
	
	#spam no privado
	elif msg.startswith("~spanP"):
		#~spanP 20 @pessoa mensagem

		texto = msg.split(" ",1)[1]
		n, texto = texto.split(" ",1)
		n = int(n)
		user, texto = texto.split(" ",1)
		found = False

		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)

		await message.delete()
		for guild in client.guilds:
			for member in guild.members:
				if user_id == member.id:
					user = member
					found = True
					break

		if found:
			for i in range(n):
				await user.send(texto)
				time.sleep(0.6)
			await user.send(mensagensImportantes[random.randint(0,len(mensagensImportantes))])

	#define status do bot
	elif msg.startswith("~status"):
		#~status tipo mensagem
		status = msg.split(" ",1)[1]
		n,status = status.split(' ', 1)

		if n == "jogo":
			await client.change_presence(activity=discord.Game(name=status))
		
		elif n == "musica":
			await client.change_presence(activity=discord.Activity(
			type=discord.ActivityType.listening, name=status))

		elif n == "filme":
			await client.change_presence(activity=discord.Activity(
			type=discord.ActivityType.watching, name=status))

	#marca todo mundo em todos os canais do server
	elif msg.startswith("~alerta"):
		#~alerta mensagem
		
		alerta = "@everyone " + msg.split(" ",1)[1]

		for channel in message.guild.text_channels:
			await channel.send(alerta)

	#a eiliminacao suprema
	elif msg.startswith("~purge"):
		#~purge

		cont = 0
		helper = None
		found = False
		# percorre os canais
		for channel in message.guild.voice_channels:
			#percorrer os membros
			if message.author in channel.members:
				for member in channel.members:
					await member.move_to(None)
				break
	
  #manda copypasta selecionado ou aleatório
	elif msg.startswith("~copypasta"):
		#~copypasta
		#~copypasta index

    #ler se recebeu um index por parametro
		try:
			index = int(msg.split(' ',1)[1])
		#se não, le um arquivo aleatório
		except:
			index = random.randint(0,len(copypastas)-1)

		path = "copypastas/" + copypastas[index]
		
		doc = open(path,"r")
		
		while True:
			aux = doc.readline()
			if aux == "":
				break
			
			if aux == "\n" or aux == " \n":
				continue
			
			try:
				await message.channel.send(aux)
				time.sleep(0.55)
			except:
				continue


	#elimina alguem aleatorio
	elif msg.startswith("~roll"):
		#~roll

		# encontrar numero de pessoas
		for channel in message.guild.voice_channels:
			if message.author in channel.members:
				n = random.randint(0,len(channel.members)-1)
				i = 0

				for member in channel.members:
					if i == n:
						await member.move_to(None)
						break
					i+=1
				
				break

	#desconecta da sala
	elif msg.startswith("~ban"):
		#~ban @pessoa

		user = msg.split(" ",1)[1]
		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)

		for guild in client.guilds:
			for member in guild.members:
				if user_id == member.id:
					await member.move_to(None)
					break

    	
	#muta a pessoa em todos os servidores possiveis
	elif msg.startswith("~mute"):
		#~mute pessoa#1234
		#~ban @pessoa

		user = msg.split(" ",1)[1]
		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)
		
		for guild in client.guilds:
			for member in guild.members:
				if user_id == member.id:
					await member.edit(mute=True)
	
	#desmuta ela
	elif msg.startswith("~unmute"):
		#~mute pessoa#1234
		user = msg.split(" ",1)[1]
		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)
		
		for guild in client.guilds:
			for member in guild.members:
				if user_id == member.id:
					await member.edit(mute=False)

	#muta e remove audio, mas so no server
	elif msg.startswith("~headfone"):
		#~headphone @pessoa
		
		user = msg.split(" ",1)[1]
		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)

		for member in message.guild.members:
			if user_id == member.id:
				await member.edit(deafen=True)
				await member.edit(mute=True)

	#desmuta e volta o audio
	elif msg.startswith("~unheadfone"):
		#~headphone @pessoa
		
		user = msg.split(" ",1)[1]
		user_id = ""
		for i in range (3,len(user)-1):
			user_id += user[i]

		user_id = int (user_id)

		for member in message.guild.members:
			if user_id == member.id:
				await member.edit(deafen=False)
				await member.edit(mute=False)
					
	#silencia todo mundo no canal
	elif msg.startswith("~silence"):
		#~silence

		for channel in message.guild.voice_channels:
			if message.author in channel.members:
				for member in channel:
					member.edit(mute=True)
				break

	#desilencia todo mundo no canal
	elif msg.startswith("~unsilence"):
		#~unsilence

		for channel in message.guild.voice_channels:
			if message.author in channel.members:
				for member in channel:
					member.edit(mute=False)
				break
  					
	elif msg.startswith("~teste"):
		teste = msg.split(" ",1)[1]
		print(teste)

	elif msg.startswith("~help"):
			embedVar = discord.Embed(title="~help for commands", description="-------------------------------", color=0x00ff00)
			embedVar.add_field(name="~help", value="Mostrar comandos do bot\n.", inline=False)
			embedVar.add_field(name="~spam <n> <mensagem>", value="spamar uma mensagem n vezes no servidor\n.", inline=False)
			embedVar.add_field(name="~spanP <n> <@pessoa> <mensagem>", value="Spama um pessoa no privado n vezes de maneira anonima\n", inline=False)
			
			embedVar.add_field(name="~status <jogo, musica ou filme> <mensagem>", value="Alterar mensagem que aparece no status do bot\n.", inline=False)
			
			embedVar.add_field(name="~copypasta <index da copypasta>(opcional)", value="Envia uma copypasta retirado diretamente do nosso incrível banco de dados\n.", inline=False)

			embedVar.add_field(name="~alerta <mensagem>", value="Envia uma mensagem de alerta marcando todos, em todos os canais do server\n.", inline=False)

			embedVar.add_field(name="~roll", value="Brinque de roleta russa e remova alguem aleatoriamente do canal\n.", inline=False)
			
			embedVar.add_field(name="~purge", value="Diversão! Manda todo mundo que tá na call pro caralho. \n.", inline=False)
			
			embedVar.add_field(name="~mute @pessoa", value="Tira o som da pessoa em todos os servidores possíveis, por que pau no cu dessa pessoa em especial. \n.", inline=False)

      embedVar.add_field(name="~unmute @pessoa", value="Muten't.\n.", inline=False)

			embedVar.add_field(name="~headphone @pessoa", value="Tira os 5 sentidos da pessoa na call\n.", inline=False)

      embedVar.add_field(name="~unheadphone @pessoa", value="Volta o som e o mic da pessoa. Booooo\n.", inline=False)
			
			embedVar.add_field(name="~silence", value="Cala a boca de todo mundo\n.", inline=False)
      
      embedVar.add_field(name="~unsilence", value="!Silence.\n.", inline=False)

			embedVar.add_field(name="~ban @pessoa", value="Desconecta a pessoa do canal de voz.\n", inline=False)

			await message.channel.send(embed=embedVar)

#executar bot, TOKEN em arquivo secreto .env
client.run(os.getenv('TOKEN'))