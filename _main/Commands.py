## Bibliotecas necessárias
# Arquivos globais
from discord import Client, Message, Embed, Game, Activity, ActivityType, FFmpegPCMAudio    # Configurações do dircord
from mutagen.mp3 import MP3                                                                 # Mexe com audio .mp3
from mutagen.mp4 import MP4                                                                 # Mexe com audio .mp4
from os import listdir 	 														            # Permitir import do Token de outro arquivo
from random import randint																    # Pega algo aleatório
from time import sleep 																	    # Daley nas mensagens e comandos

# Arquivos locais
from dicionarios import *

class Commands:
    msg:str = ""
    user:str = ""
    text:str = ""
    userId:int = 0
    botID:int = 832785093117476884
    copypastas = listdir("copypastas/")
    mensagensImportantes:list = []
    

    def __init__(self, c_:Client) -> None:
        self.client = c_

        f = open("arquivos/mensagens.txt", "r")
        while True:
            aux = f.readline()
            if aux == '': break
            self.mensagensImportantes.append(aux)
        f.close
        self.copypastas.sort()

        f = aux = None
        del f, aux


    def __del__(self) -> None: 
        self.msg = self.user = self.text = self.copypastas = self.client = None
        del self.msg, self.user, self.text, self.copypastas, self.client
            

    def setMsg(self, m_:Message) -> None:
        self.message = m_
        self.msg = m_.content
        try: self.userId = self.getUserId(self.msg.split(" ",1)[1])
        except: pass
        

    def getUserId(self, user_:str) -> int:
        user_id:str = ""
        for i in range (3, len(user_)-1):
            user_id += user_[i]
        return int(user_id)
        
    def getMsg(self) -> str: return self.msg
    

    #### COMANDOS ####


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
        await self.mensagem()
        
        spam = n = i = None
        del spam, n, i


    async def spamPv(self) -> None:
        texto = self.msg.split(" ", 1)[1]
        n, texto = texto.split(" ",1)
        user, texto = texto.split(" ",1)
        found:bool = False

        userId:int = self.getUserId(user)

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
            await user.send(self.mensagensImportantes[randint(0,len(self.mensagensImportantes))])

        
        texto = n = user = found = userId = guild = member = None
        del texto, n, user, found, userId, guild, member


    async def mensagem(self) -> None:
        await self.message.channel.send(self.mensagensImportantes[randint(0, len(self.mensagensImportantes)-1)])


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
        
        alerta = None
        del alerta
        

    async def purge(self) -> None:
        found:bool = False
        for channel in self.message.guild.voice_channels:			# Percorre os canais
            if self.message.author in channel.members:				# Acha quem mandou a mensagem
                for member in channel.members:					# Pega todos os membros
                    await member.move_to(None)					# Tira todos
                break
        
        found = None
        del found


    async def erradicate(self) -> None:
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                await member.move_to(None)


    async def shake(self) -> None:
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                if member.id == self.userId:
                    for i in range (60):
                        try:
                            await member.move_to(self.message.guild.voice_channels[randint(0, len(self.message.guild.voice_channels)-1)])
                        except: continue
                        sleep(1)


    async def milkshake(self) -> None:
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                await member.move_to(self.message.guild.voice_channels[randint(0, len(self.message.guild.voice_channels)-1)])


    async def copypasta(self) -> None:
        try: 
            index:str = self.msg.split(' ', 1)[1]				# Caso tenha recebido um index por parâmetro
            if (index == "help"):
                lista:str = "copypastas disponiveis:\n"
                for i in range (len(self.copypastas)):
                    lista += str(i) + ": " + self.copypastas[i] + "\n"
                await self.message.channel.send(lista)
                return
            else: index = int(index)
        except: index:int = randint(0, len(self.copypastas)-1)		# Pega um arquivo aleatório

        path:str = "copypastas/" + self.copypastas[index]
        
        doc = open(path, "r")
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
        
        n = i = None
        del n, i
        

    async def ban(self) -> None:
        for guild in self.client.guilds:
            for member in guild.members:
                if self.userId == member.id:
                    await member.move_to(None)
                    break


    async def silence(self, b_:bool) -> None:
        for channel in self.message.guild.voice_channels:
            if self.message.author in channel.members:
                for member in channel.members:
                    await member.edit(mute=b_)
                break


    async def headFone(self, b_:bool) -> None:
        if (self.message.author.voice.deaf and self.message.author.voice.mute):
            return

        for member in self.message.guild.members:
            if self.userId == member.id:
                await member.edit(deafen=b_)
                await member.edit(mute=b_)
                break
        

    async def listCommands(self) -> None:
        embedVar = Embed(title="~help for commands", description="-------------------------------", color=0x00ff00)

        for x in range(len(allComands.keys())):
            embedVar.add_field(name=list(allComands.keys())[x], value=list(allComands.values())[x], inline=False)

        await self.message.channel.send(embed=embedVar)

        embedVar = None
        del embedVar


    async def playSound(self):
        voice_channel = self.message.author.voice.channel
        file:str = self.msg.split(" ",1)[1]
        path:str = f"audios/{file}"

        if (file[-4:] in [".mp3", ".mp4"]):
            try: 
                if (file[-4:] == ".mp3"):
                    tam:int = MP3(path).info.length +1
                else: 
                    tam:int = MP4(path).info.length +1
            except: return
                
            if voice_channel != None:
                vc = await voice_channel.connect()
                vc.play(FFmpegPCMAudio(path, executable="Arquivos/ffmpeg.exe"))
                sleep(tam)
                vc = None
                del vc
            else:
                await self.message.channel.send('Usuário não está em um canal de voz')

            for member in self.message.guild.members:
                if member.id == self.botID:
                    await member.move_to(None)
                    break
        
        voice_channel = file = path = tam = None
        del voice_channel, file, path, tam

    
    # Jamais precisar usar
    async def halo(self) -> None:
        for member in self.message.guild:
            if member.id == self.botID: continue
            try: await member.kick()
            except: pass