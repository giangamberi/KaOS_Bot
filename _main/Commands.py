## Bibliotecas necessárias
# Arquivos globais
from discord import Client, Intents, Message, Embed, Game, Activity, ActivityType		# Configurações do dircord
from os import listdir, getenv 	 														# Permitir import do Token de outro arquivo
from random import randint																# Pega algo aleatório
from time import sleep 																	# Daley nas mensagens e comandos

# Arquivos locais
from dicionarios import *


class Commands:
    msg:str = ""
    user:str = ""
    text:str = ""
    copypastas = listdir("copypastas/")

    def __init__(self) -> None:
        intents = Intents.default()
        intents.members = True
        self.client = Client(intents=intents)


    def __del__(self) -> None: 
        self.msg = self.user = self.text = self.copypastas = self.client = None
        del self.msg, self.user, self.text, self.copypastas, self.client


    def setMsg(self, m_:Message) -> None:
        self.message = m_
        self.msgStr = m_.content
        self.user = self.msg.split(" ", 1)[1]    


    def getUserId(self) -> int:
        user_id:str = ""
        for i in range (3, len(self.user)-1):
            user_id += self.user[i]
        return int(user_id)

    def getMsg(self) -> str: return self.msg
    

    async def padrao(self) -> None:
        if ((self.msg.lower().endswith("ao") or self.msg.lower().endswith("ão")) and (self.message.author != self.client.user)):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau na sua mão.")
	
        elif ((self.msg.lower().endswith("ta")) and (self.message.author != self.client.user) and (not self.msg.startswith("~copypasta"))):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau te cutuca.")
        
        if (("duvido" in self.msg.lower()) and (self.message.author != self.client.user)):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau no teu ouvido.")


    async def spam(self) -> None:
        spam:str = self.msg.split(" ",1)[1]
        n, spam = spam.split(' ', 1)
        
        for i in range(int(n)):
            await self.message.channel.send(spam)
            sleep(0.6)
        await self.message.channel.send(mensagensImportantes[randint(0, len(mensagensImportantes))])
        
        spam = n = i = None
        del spam, n, i


    async def spamPv(self) -> None:
        n, texto = self.user.split(" ",1)
        user, texto = texto.split(" ",1)
        found:bool = False

        userId:int = self.getUserId()

        await self.message.delete()
        for guild in self.client.guilds:
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


    async def status(self) -> None:
        status:str = self.msg.split(" ",1)[1]
        n, status = status.split(' ', 1)

        if (n == "jogo"):
            await self.client.change_presence(activity=Game(name=status))
        
        elif (n == "musica"):
            await self.client.change_presence(activity=Activity(type=ActivityType.listening, name=status))

        elif (n == "filme"):
            await self.client.change_presence(activity=Activity(type=ActivityType.watching, name=status))
        
        status = n = None
        del status, n


    async def alerta(self) -> None:
        alerta:str = "@everyone " + self.msg.split(" ",1)[1]

        for channel in self.message.guild.text_channels:
            await channel.send(alerta)
        
        alerta = channel = None
        del alerta, channel


    async def purge(self) -> None:
        found:bool = False
        
        for channel in self.message.guild.voice_channels:			# Percorre os canais
            if self.message.author in channel.members:				# Acha quem mandou a mensagem
                for member in channel.members:					# Pega todos os membros
                    await member.move_to(None)					# Tira todos
                break
        
        found = channel = member = None
        del found, channel, member

    async def copypasta(self) -> None:
        try: index:int = int(self.msg.split(' ', 1)[1])				# Caso tenha recebido um index por parâmetro
        except: index:int = randint(0, len(self.copypastas)-1)		# Pega um arquivo aleatório

        path:str = "copypastas/" + self.copypastas[index]
        
        doc = open(path,"r")
        
        while True:
            aux:str = doc.readline()
            if aux == "": break
            if aux in ["\n", " \n"]: continue
            try:
                await self.message.channel.send(aux)
                sleep(0.55)
            except:	continue
        doc.close

        index = path = doc = aux = None
        del index, path, doc, aux


    async def roll(self) -> None:
        for channel in self.message.guild.voice_channels:			# Acessa os canais
            if self.message.author in channel.members:				# Procura o autor da mensagem no canal
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

    async def ban(self) -> None:
        userId:int = self.getUserId()
    
        for guild in self.client.guilds:
            for member in guild.members:
                if userId == member.id:
                    await member.move_to(None)
                    break

    async def silence(self, b_:bool) -> None:
        for channel in self.message.guild.voice_channels:
            if self.message.author in channel.members:
                for member in channel:
                    member.edit(mute=b_)
                break

    async def muteAll(self, b_:bool) -> None:
        userId:int = self.getUserId()
    
        for guild in self.client.guilds:
            for member in guild.members:
                if userId == member.id:
                    await member.edit(mute=b_)

    async def headFone(self, b_:bool) -> None:
        userId:int = self.getUserId()
    
        for member in self.message.guild.members:
            if userId == member.id:
                await member.edit(deafen=b_)
                await member.edit(mute=b_)
                break

    async def help(self) -> None:
        embedVar = Embed(title="~help for commands", description="-------------------------------", color=0x00ff00)

        for x in range(len(allComands)):
            embedVar.add_field(name=allComands.keys[x], value=allComands.values[x], inline=False)
    
        await self.message.channel.send(embed=embedVar)


cmds = Commands()

intents = Intents.default()
intents.members = True
client = Client(intents=intents)

@client.event  # registrar um evento
async def on_ready():  # eventos ja prontos, quando o bot estiver pronto:
	print(f"Bot ativado com o nome {client.user}")

	await client.change_presence(activity=Game(name="~help for commands"))

@client.event  					# Próximo evento, se bot receber uma mensagem
async def on_message(message:Message):
    cmds.setMsg(message)
    cmds.padrao()
    msg = cmds.getMsg()

    if msg.startswith("~spam"): cmds.spam()

    elif msg.startswith("~spamPv"): cmds.spamPv()
        
    elif msg.startswith("~status"): cmds.status()
        
    elif msg.startswith("~alerta"): cmds.alerta()
        
    elif msg.startswith("~purge"): cmds.purge()
            
    elif msg.startswith("~copypasta"): cmds.copypasta()

    elif msg.startswith("~roll"): cmds.roll()

    elif msg.startswith("~ban"): cmds.ban()        
        
    elif msg.startswith("~mute"):  cmds.muteAll(True)
        
    elif msg.startswith("~unmute"):  cmds.muteAll(False)

    elif msg.startswith("~headfone"):  cmds.headFone(True)        

    elif msg.startswith("~unheadfone"):  cmds.headFone(False)

    elif msg.startswith("~silence"):  cmds.silence(True)

    elif msg.startswith("~unsilence"):  cmds.silence(False)
    
    elif msg.startswith("~help"): cmds.help()

client.run(getenv('TOKEN'))