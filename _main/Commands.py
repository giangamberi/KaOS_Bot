# -*- coding: utf-8 -*-

__author__ = "Gian Gamberi, Gui Reis, Rone FIlho, Marcelo Takayama"
__copyright__ = "GadosComp"
__version__ = "2.0"
__status__ = "Production"
__license__ = """

MIT License

Copyright (c) 2021 GadosComp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


## Bibliotecas necessárias
# Arquivos globais

from discord import Client, Member, Message, Colour, Guild, Embed, Game, Activity, ActivityType, FFmpegPCMAudio    # Configurações do dircord

# import discord
from mutagen.mp3 import MP3                                                                 # Mexe com audio .mp3
from mutagen.mp4 import MP4                                                                 # Mexe com audio .mp4
from os import listdir 	 														            # Permitir import do Token de outro arquivo
from random import randint																    # Pega algo aleatório
from time import sleep 																	    # Daley nas mensagens e comandos

# Arquivos locais
from dicionarios import *

class Commands:
    r"""
    Classe com todos os principais comandos do bot que podem ser usados em qualquer server que ele está conectado.

    ## Parâmetros
    
    :class:`discord.Client` c_: Recebe o cliente conectado ao Discord para a partir dele fazer as operações.

    ## Atributos
    
    |   Atributos   |            Descrição            |
    |:--------------|:--------------------------------|
    | msg           | Mensagem lida em string         |
    | userId        | Id do usuário                   |
    | botId         | Id do bot                       |
    | copypastas    | Lista com os copypastas         |
    | msgSpams      | Lista com as mensagens de spam  |
    |---------------|---------------------------------|
    
    ## Métodos
    
    |    Métodos      |                                    Descrição                                    |
    |:----------------|:--------------------------------------------------------------------------------|
    | setMsg          | Define a mensagem string.                                                       |
    | getMsg          | Retorna a mensagem em string.                                                   |  
    | setUserId       | Define o id de um usuário.                                                      |
    | getUserId       | Retorna o id de um usuário .                                                    |
    | padrao          | Verifica se tem palavras que na frase que manda alguma resposta.                |
    | spam            | Spamar uma mensagem n vezes no servidor.                                        |
    | spamPv          | Spamar uma mensagem n vezes no privado de alguém de forma anônima.              |
    | mensagem        | Manda uma mensagem entre as frases reservadas.                                  |
    | status          | Alterar status do bot.                                                          |
    | alerta          | Envia uma mensagem de alerta marcando todo mundo, em todos os canais do server. |
    | magnetize       | Junta ou distancia duas pessoas nos canais de voz de um servidor                |
    | attract         | Mantém no mesmo canal de voz duas pessoas distintas                             |
    | repulse         | Mantém o mais distante possível duas pessoas distintas dos canais de voz        |
    | purge           | Tira todo mundo do canal de voz.                                                |
    | erradicate      | Tira todo mundo de todos os canais de voz do server.                            |
    | shake           | Fica movendo uma usuário entre os canais de voz por 1 minuto.                   |
    | milkshake       | Muda todo mundo do server de canal aleatoriamente.                              |
    | copypastas      | Manda algum texto de algum copypasta.                                           |
    | roll            | Tira alguém do canal aleatóriamente.                                            |
    | ban             | Desconecta alguém do server.                                                    |
    | silence         | Silencia ou desilencia todos do canal de voz.                                   |
    | headfone        | Tira/coloca áudio e mic de alguém.                                              |
    | listCommands    | Mostra todos os comandos.                                                       |
    | playSounds      | Reproduz um áudio já salvo na pasta.                                            |
    | halo            | ATENÇÃO: Tira todo mundo do server, deixando apenas o adm e o bot.              |
    |-----------------|---------------------------------------------------------------------------------|
    """

    msg:str = ""
    userId:int = 0
    botId:int = 832785093117476884
    copypastas = listdir("copypastas/")
    msgSpams:list = []
    
    def __init__(self, c_:Client) -> None:
        r"""
        ## Construtor
        Cria a lista com as palavras de spam aleatória.

        ## Parâmetros

        :class:`discord.Client` c_: Recebe o cliente conectado ao Discord para a partir dele fazer as operações.
        """
        self.client = c_

        f = open("arquivos/mensagens.txt", "r")
        while True:
            aux = f.readline()
            if aux == '': break
            self.msgSpams.append(aux)
        f.close
        self.copypastas.sort()

        f = aux = None
        del f, aux


    def __del__(self) -> None:
        r"""
        ## Destrutor
        Limpa as variáveis e deleta elas.
        """
        self.msg = self.userId = self.copypastas = self.client = self.msgSpams =None
        del self.msg, self.userId, self.copypastas, self.client, self.msgSpams
            

    def setMsg(self, m_:Message) -> None:
        r"""
        ## Setter -> msg
        Salva a linha de texto escrita no discord.

        ## Parâmetros

        :class:`discord.Message` m_: Mensagem enviado em algum canal de texto do server.
        """
        self.message = m_
        self.msg = m_.content
        self.setUserId()
    

    def getMsg(self) -> str: 
        r"""
        ## Getter -> msg
        Retorna a mensagem escrita no discord.
        """
        return self.msg


    def setUserId(self, id_:int = 0) -> None:
        r"""
        ## Setter -> userId
        Define o id do usuário

        ## Parâmetros

        :class:`int` id_: Id já pré definido
        """
        try:
            if (id_ == 0):
                self.userId = self.getUserId(self.msg.split(" ",1)[1])
            else: 
                self.userId = id_
        except: pass
        

    def getUserId(self, user_:str) -> int:
        r"""
        ## Getter -> userId
        :class:`int`: Retorna o id do usuário.

        ## Parâmetros

        :class:`str` user_: Usuario pra pegar o ip
        """
        user_id:str = ""
        for i in range (3, len(user_)-1):
            user_id += user_[i]
        return int(user_id)
        
    

    #### COMANDOS ####


    async def padrao(self) -> None:
        r"""
        ## Retruca mensagens
        Se em algum texto mandado tiver uma palavra específica ou que termina com uma sílaba específica, manda uma frase.
        - `ao` e `ão`: Meu pau na sua mão
        - `ta`: Meu pau te cotuca
        - `el`: Meu pau no teu anel
        - `duvido`: Meu pau no teu ouvido
        """
        
        if (("duvido" in self.msg.lower()) and (self.message.author != self.client.user)):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau no teu ouvido.")

        if ((self.msg.lower().endswith("ao") or self.msg.lower().endswith("ão")) and (self.message.author != self.client.user)):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau na sua mão.")

        elif ((self.msg.lower().endswith("ta")) and (self.message.author != self.client.user) and (not self.msg.lower().startswith("~copypasta"))):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau te cutuca.")

        elif ((self.msg.lower().endswith("el")) and (self.message.author != self.client.user)):
            await self.message.channel.send(f"{self.message.author.mention} Meu pau no teu anel.")    


    async def spam(self) -> None:
        r"""
        ## Spam
        Manda n vezes uma mensagem no mesmo canal que foi digitado o comando.

        ### Comando: `~flood n mensagem`
        :class:`int` n: vezes que vai ser mandado a mensagem
        :class:`str` mensagem: mensagem que vai ser mandada.
        """
        spam:str = self.msg.split(" ",1)[1]
        n, spam = spam.split(' ', 1)
        
        for i in range(int(n)):
            await self.message.channel.send(spam)
            sleep(0.6)
        await self.mensagem()
        
        spam = n = i = None
        del spam, n, i


    async def spamPv(self) -> None:
        r"""
        ## SpamPv
        Manda n vezes uma mensagem na conversa em privado pra algúem anonimamaente.\
        O commando que foi digitado é apagado do canal de texto

        ### Comando: `~floodPv n @usuario mensagem`
        :class:`int` n: vezes que vai ser mandado a mensagem.
        `@` @usuario: marca a usuário.
        :class:`str` mensagem: mensagem que vai ser mandada.
        """
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
            await user.send(self.msgSpams[randint(0,len(self.msgSpams))])

        
        texto = n = user = found = userId = guild = member = None
        del texto, n, user, found, userId, guild, member


    async def mensagem(self) -> None:
        r"""
        ## Mensagem aleatória
        Pega uma frase aleatória que está salva e manda no mesmo canal que foi digitado o comando.
        
        ### Comando: `~mensagem`
        """
        await self.message.channel.send(self.msgSpams[randint(0, len(self.msgSpams)-1)])


    async def status(self) -> None:
        r"""
        ## Status
        Muda o status do bot (texto de descrição do perfil)

        ### Comando: `~status type mensagem`
        `str` type: opção entre: jogo, musica ou filme
        :class:`str` mensagem: mensagem que vai ser mostrada.
        """
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
        r"""
        ## Alerta
        Manda uma mensagem em todos os canais do server marcando todo mundo (@everyone)

        ### Comando: `~yall mensagem`
        :class:`str` mensagem: mensagem que vai ser mandada.
        """
        alerta:str = "@everyone " + self.msg.split(" ",1)[1]

        for channel in self.message.guild.text_channels:
            await channel.send(alerta)
        
        alerta = None
        del alerta


    async def magnetize(self) -> None:
        r"""
        ## Magnetize
        Junta ou distancia duas pessoas, mantendo elas sempre juntas ou afastadas.

        ### Comando: `~magnetiza tipo @pessoa1 @pessoa2`
        :class:`str` tipo: attract/repulse
        :class:`member` @pessoa1/2: membros que vai ser magnetizado.
        """
        relation:str = self.msg.split(" ", 1)[1]
        relation,userA,userB = relation.split(" ",2)
        relation.lower()
        userA:int = self.getUserId(userA)
        userB:int = self.getUserId(userB)
        
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                if (member.id == userA):
                    userA = member
                elif (member.id == userB):
                    userB = member

        if ((type(userA) is not Member) or (type(userB) is not Member) or (relation != "attract" and relation != "repulse")):
            await self.message.channel.send("Formato Invalido")
            return

        if (relation == "attract"):
            await self.attract(userA, userB, self.message.guild)
        elif (relation == "repulse"):
            await self.repulse(userA, userB, self.message.guild)

    async def attract(self, userA:Member, userB:Member, server:Guild) -> None:
        r"""
        ## Attract
        Função auxiliar que gera um loop que mantém duas pessoas sempre juntas no canal.

        ### Comando: `~demagnetize`
        Cancela a atração, outra alternativa seria sair do servidor.
        """
        await self.message.channel.send("Attract ligado")
        while (not self.msg.startswith("~demagnetize")):
            try: await userB.move_to(userA.voice.channel)
            except: break
            sleep(0.25)
        await self.message.channel.send("Attract cancelado")
    
    async def repulse(self, userA:Member, userB:Member, server:Guild) -> None:
        r"""
        ## repulse
        Função auxiliar que gera um loop que afasta dois usuarios de um server
        ### Comando: `~demagnetize`
        cancela a repulsão, alternativa seria sair do servidor
        """
        await self.message.channel.send("Repulse ligado")
        while (not self.msg.startswith("~demagnetize")):
            try:
                await userA.move_to(server.voice_channels[0])
                await userB.move_to(server.voice_channels[len(server.voice_channels)-1])
            except: break
            sleep(0.25)
        await self.message.channel.send("Repulse cancelado")

    async def purge(self) -> None:
        r"""
        ## Purge
        Disconecta todos os usuários que estão no mesmo canal que o usuário responsável pelo comando digitado.

        ### Comando: `~purge`
        """
        for channel in self.message.guild.voice_channels:
            if self.message.author in channel.members:
                for member in channel.members:
                    await member.move_to(None)
                break

    async def erradicate(self) -> None:
        r"""
        ## Erradicate
        Disconecta todos os usuários de todos os canais de voz.

        ### Comando: `~erradicate`
        """
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                await member.move_to(None)


    async def shake(self) -> None:
        r"""
        ## Shake
        Por um período de 1 minuto, fica movendo um usuário entre os canais.

        ### Comando: `~shake @usuario`
        `@` @usuario: usuário que vai ficar se mexendo entre os canais.
        """
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                if member.id == self.userId:
                    for i in range (60):
                        try:
                            await member.move_to(self.message.guild.voice_channels[randint(0, len(self.message.guild.voice_channels)-1)])
                        except: continue
                        sleep(1)


    async def milkshake(self) -> None:
        r"""
        ## Milkshake
        Aleatoriamente escolhe um canal de voz para os todos os usuários conectados em algum canal de voz.

        ### Comando: `~milkshake`
        """
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                await member.move_to(self.message.guild.voice_channels[randint(0, len(self.message.guild.voice_channels)-1)])


    async def copypasta(self) -> None:
        r"""
        ## Copypasta
        Seleciona um copypasta pronto e envia cada frase que está nele no mesmo canal de texto que o\
        comando foi digitado.

        ### Comando: `~copypasta` ou `~copypasta index`
        :class:`int` index (opcional): número do copypasta que vai ser mandado
        """

        try:                                                        # Caso tenha recebido um index por parâmetro
            index:str = self.msg.split(' ', 1)[1]
            if (index == "help"):
                lista:str = "copypastas disponiveis:\n"
                for i in range (len(self.copypastas)):
                    lista += str(i) + ": " + self.copypastas[i] + "\n"
                await self.message.channel.send(lista)
                return
            else: index = int(index)
        except: index:int = randint(0, len(self.copypastas)-1)		# Pega um arquivo aleatório

        path:str = "copypastas/" + self.copypastas[index]
        
        doc = open(path,"rb")
        
        while True:
            aux = doc.readline()
            aux = aux.decode('utf-8')
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
        r"""
        ## Roll
        Aleatóriamente disconecta um usuário no mesmo canal de voz que o usuário responsável por digitar o comando.

        ### Comando: `~rollette`
        """
        for channel in self.message.guild.voice_channels:
            if self.message.author in channel.members:
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
        r"""
        ## Ban
        Disconecta um usuário esepcifico no mesmo canal de voz que o usuário responsável por digitar o comando.

        ### Comando: `~ban @usuario`
        `@` @usuario: usuário que vai ser disconectado.
        """
        for guild in self.client.guilds:
            for member in guild.members:
                if self.userId == member.id:
                    await member.move_to(None)
                    break


    async def silence(self, b_:bool) -> None:
        r"""
        ## Silence
        Silencia ou desilencia todos os usuários no mesmo canal de voz que o usuário responsável pelo comando que foi digitado.

        ## Parâmetros 

        > :class:`bool` b_: ativa ou desativa o "mute".
            - True: silencia todos
            - False:  Desilencia todos

        ### Comando: `silence patrick` ou `~unsilence`
        """
        for channel in self.message.guild.voice_channels:
            if self.message.author in channel.members:
                for member in channel.members:
                    await member.edit(mute=b_)
                break


    async def headFone(self, b_:bool) -> None:
        r"""
        ## Deafen
        Muta e tira áudio de um usuário específico no mesmo canal de voz que o usuário responsável por ter digitado o comando.

        ## Parâmetros

        > :class:`bool` b_: ativa ou desativa o `mute` e o `deafen`.
            - True: ativa o `mute` e o `deafen`.
            - False: desativa o `mute` e o `deafen`.

        ### Comando: `~deafen` ou `~undeafen`
        """
        if (self.message.author.voice.deaf and self.message.author.voice.mute):
            return

        for member in self.message.guild.members:
            if self.userId == member.id:
                await member.edit(deafen=b_)
                await member.edit(mute=b_)
                break
        

    async def listCommands(self) -> None:

        #define a cor que voce quer
        cor  = Colour.from_rgb(255, 102, 102)

        embedVar = Embed(title="~help para ter os comandos", description="Para voce infernizar seus amigos", colour=cor, )
        
        r"""
        ## Help
        Mostra uma lista de todos os comando que o bot faz.

        ### Comando: `~help`
        """

        for x in range(len(allComands.keys())):
            embedVar.add_field(name=list(allComands.keys())[x], value=list(allComands.values())[x], inline=False)

        await self.message.channel.send(embed=embedVar)

        embedVar = None
        del embedVar

 
    async def playSound(self):
        r"""
        ## Playsound
        Reproduz um áudio pronto (já salvo no banco de dados) e reproduz no mesmo canal de voz que o usuário\
        responsável pelo comando difitado

        ### Comando: `~shout file`
        :class:`str` file: nome do arquivo com o seu tipo de áudio (.mp3 ou .mp4)
        """
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
                if member.id == self.botId:
                    await member.move_to(None)
                    break
        
        voice_channel = file = path = tam = None
        del voice_channel, file, path, tam

    
    # Jamais precisar usar
    async def halo(self) -> None:
        r"""
        ## Halo
        [ATENÇÃO] Remove todos os usuários (e bots) do SERVER, deixando apenas o dono e o bot.

        ### Comando: `~halo`
        """
        for member in self.message.guild:
            if member.id == self.botId: continue
            try: await member.kick()
            except: pass