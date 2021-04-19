# video utilizado: freeCodeCamp.org
# https://www.youtube.com/watch?v=SPTfmiYiuok

# criar bot -> https://discord.com/developers/applications/


## Bibliotecas necessárias
# Arquivos globais
from discord import Client, Intents, Message, Embed, Game, Activity, ActivityType		# Configurações do dircord
from os import listdir, getenv 	 														# Permitir import do Token de outro arquivo
from random import randint																# Pega algo aleatório
from time import sleep 																	# Daley nas mensagens e comandos

# Arquivos locais
from dicionarios import *



# Para checar membros, é necessario permitir intents nas configurações do bot
# DiscordBot -> Bot -> permitir todas as intents
intents = Intents.default()
intents.members = True
client = Client(intents=intents)

@client.event  # registrar um evento
async def on_ready():  # eventos ja prontos, quando o bot estiver pronto:
	print(f"Bot ativado com o nome {client.user}")

	await client.change_presence(activity=Game(name="~help for commands"))

copypastas = listdir("copypastas/")

@client.event  					# Próximo evento, se bot receber uma mensagem
async def on_message(message:Message):
	global msg
	msg:str = message.content  	# Substituir mais facilmente

	user:str = msg.split(" ", 1)[1]

	if ((msg.lower().endswith("ao") or msg.lower().endswith("ão")) and (message.author != client.user)):
		await message.channel.send(f"{message.author.mention} Meu pau na sua mão.")
	
	elif ((msg.lower().endswith("ta")) and (message.author != client.user) and (not msg.startswith("~copypasta"))):
		await message.channel.send(f"{message.author.mention} Meu pau te cutuca.")
	
	if (("duvido" in msg.lower()) and (message.author != client.user)):
		await message.channel.send(f"{message.author.mention} Meu pau no teu ouvido.")

	
	#### Dar spam em pessoas ####
	if msg.startswith("~spam"):
		#~spam 20 mensagem

		spam:str = msg.split(" ",1)[1]
		n, spam = spam.split(' ', 1)

		for i in range(int(n)):
			await message.channel.send(spam)
			sleep(0.6)
		await message.channel.send(mensagensImportantes[randint(0, len(mensagensImportantes))])

		spam = n = i = None
		del spam, n, i
	
	#### Dar spam em pessoas no privado ####
	elif msg.startswith("~spamPv"):
		#~spamPv 20 @pessoa mensagem

		texto:str = msg.split(" ",1)[1]
		n, texto = texto.split(" ",1)
		user, texto = texto.split(" ",1)
		found:bool = False

		userId:int = getUserId(user)

		await message.delete()
		for guild in client.guilds:
			for member in guild.members:
				if (userId == member.id):
					user = member
					found = True
					break

		if (found):
			for i in range(int(n)):
				await user.send(texto)
				sleep(0.6)
			await user.send(mensagensImportantes[randint(0,len(mensagensImportantes))])
			i = None
			del i
		
		texto = n = user = found = userId = guild = member = None
		del texto, n, user, found, userId, guild, member

	#### Define o status do bot ####
	elif msg.startswith("~status"):
		#~status tipo mensagem

		status:str = msg.split(" ",1)[1]
		n, status = status.split(' ', 1)

		if (n == "jogo"):
			await client.change_presence(activity=Game(name=status))
		
		elif (n == "musica"):
			await client.change_presence(activity=Activity(type=ActivityType.listening, name=status))

		elif (n == "filme"):
			await client.change_presence(activity=Activity(type=ActivityType.watching, name=status))
		
		status = n = None
		del status, n
		

	#### Marca todo mundo em todos os canais do server ####
	elif msg.startswith("~alerta"):
		#~alerta mensagem
		
		alerta:str = "@everyone " + msg.split(" ",1)[1]

		for channel in message.guild.text_channels:
			await channel.send(alerta)
		
		alerta = channel = None
		del alerta, channel


	#### A eliminação suprema ####
	elif msg.startswith("~purge"):
		#~purge

		found:bool = False
		
		for channel in message.guild.voice_channels:			# Percorre os canais
			if message.author in channel.members:				# Acha quem mandou a mensagem
				for member in channel.members:					# Pega todos os membros
					await member.move_to(None)					# Tira todos
				break
		
		found = channel = member = None
		del found, channel, member
	
   #### Manda o copypasta selecionado ou aleatório ####
	elif msg.startswith("~copypasta"):
		#~copypasta
		#~copypasta index

		try: index:int = int(msg.split(' ', 1)[1])				# Caso tenha recebido um index por parâmetro
		except: index:int = randint(0, len(copypastas)-1)		# Pega um arquivo aleatório

		path:str = "copypastas/" + copypastas[index]
		
		doc = open(path,"r")
		
		while True:
			aux:str = doc.readline()
			if aux == "": break
			if aux in ["\n", " \n"]: continue
			try:
				await message.channel.send(aux)
				sleep(0.55)
			except:	continue
		doc.close

		index = path = doc = aux = None
		del index, path, doc, aux
				


	#### Elimina alguém aleatório ####
	elif msg.startswith("~roll"):
		#~roll

		for channel in message.guild.voice_channels:			# Acessa os canais
			if message.author in channel.members:				# Procura o autor da mensagem no canal
				n:int = randint(0, len(channel.members)-1)	
				i:int = 0
				for member in channel.members:
					if (i == n):
						await member.move_to(None)
						break
					i += 1
				break
		
		channel = n = i = member = None
		del channel, n, i, member


	#### Desconecta da sala ####
	elif msg.startswith("~ban"):
		#~ban @pessoa

		userId:int = getUserId(user)
	
		for guild in client.guilds:
			for member in guild.members:
				if userId == member.id:
					await member.move_to(None)
					break
		
    	
	#### Muta a pessoa em todos os servidores possiveis ####
	elif msg.startswith("~mute"): setMute(user, True)
		#~mute pessoa#1234

		
	#### Desmuta a pessoa em todos os servidores possiveis ####
	elif msg.startswith("~unmute"): setMute(user, False)
		#~mute pessoa#1234

		
	#### Muta e remove o áudio (só no server) ####
	elif msg.startswith("~headfone"): setHeadfone(user, message, True)
		#~headphone @pessoa
		

	#### Desmuta e volta o áudio (só no server) ####
	elif msg.startswith("~unheadfone"): setHeadfone(user, message, False)
		#~unheadfone @pessoa
		
					
	#### Muta todo mundo no canal ####
	elif msg.startswith("~silence"): setSilence(True)
		#~silence


	#### Desmuta todo mundo no canal ####
	elif msg.startswith("~unsilence"): setSilence(False)
		#~unsilence

		
	elif msg.startswith("~teste"):
		teste = msg.split(" ",1)[1]
		print(teste)

	#### Mostra os comandos ####
	elif msg.startswith("~help"):
		embedVar = Embed(title="~help for commands", description="-------------------------------", color=0x00ff00)

		for x in range(len(allComands)):
			embedVar.add_field(name=allComands.keys[x], value=allComands.values[x], inline=False)
	
		await message.channel.send(embed=embedVar)


## Pega o id do usuário
def getUserId(user_:str) -> int:
	user_id:str = ""
	for i in range (3,len(user_)-1):
		user_id += user_[i]
	return int(user_id)


## Muta/Desmuta no canal
def setSilence(msg_:Message, b_:bool) -> None:
	for channel in msg_.guild.voice_channels:
		if msg_.author in channel.members:
			for member in channel:
				member.edit(mute=b_)
			break


## Muta/Desmuta nos servers
async def setMute(user_:str, b_:bool):
	userId:int = getUserId(user_)
	
	for guild in client.guilds:
		for member in guild.members:
			if userId == member.id:
				await member.edit(mute=b_)


## Muta/Desmuta e com/sem áudio no canal
async def setHeadfone(u_:str, msg_:Message, b_:bool) -> None:
	userId:int = getUserId(u_)
	
	for member in msg_.guild.members:
		if userId == member.id:
			await member.edit(deafen=b_)
			await member.edit(mute=b_)
			break

#executar bot, TOKEN em arquivo secreto .env
client.run(getenv('TOKEN'))






# from discord import Client, Intents, Message, Game		# Configurações do dircord
# from os import getenv 

# from Commands import Commands

# cmds = Commands()

# intents = Intents.default()
# intents.members = True
# client = Client(intents=intents)

# @client.event  # registrar um evento
# async def on_ready():  # eventos ja prontos, quando o bot estiver pronto:
# 	print(f"Bot ativado com o nome {client.user}")

# 	await client.change_presence(activity=Game(name="~help for commands"))

# @client.event  					# Próximo evento, se bot receber uma mensagem
# async def on_message(message:Message):
#     cmds.setMsg(message)
#     cmds.padrao()
#     msg = cmds.getMsg()

#     if msg.startswith("~spam"): cmds.spam()

#     elif msg.startswith("~spamPv"): cmds.spamPv()
        
#     elif msg.startswith("~status"): cmds.status()
        
#     elif msg.startswith("~alerta"): cmds.alerta()
        
#     elif msg.startswith("~purge"): cmds.purge()
            
#     elif msg.startswith("~copypasta"): cmds.copypasta()

#     elif msg.startswith("~roll"): cmds.roll()

#     elif msg.startswith("~ban"): cmds.ban()        
        
#     elif msg.startswith("~mute"):  cmds.muteAll(True)
        
#     elif msg.startswith("~unmute"):  cmds.muteAll(False)

#     elif msg.startswith("~headfone"):  cmds.headFone(True)        

#     elif msg.startswith("~unheadfone"):  cmds.headFone(False)

#     elif msg.startswith("~silence"):  cmds.silence(True)

#     elif msg.startswith("~unsilence"):  cmds.silence(False)
    
#     elif msg.startswith("~help"): cmds.help()

# client.run(getenv('TOKEN'))