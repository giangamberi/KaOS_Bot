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

# Configurações do discord
from discord import Client, Member, Message, Colour, Guild, Embed, Game, Activity, ActivityType, FFmpegPCMAudio
from mutagen.mp3 import MP3                         # Mexe com audio .mp3
from mutagen.mp4 import MP4                         # Mexe com audio .mp4
from os import listdir                              # Permitir import do Token de outro arquivo
from random import randint	                        # Pega algo aleatório
from time import sleep 		                        # Daley nas mensagens e comandos

# Arquivos locais
from dicionarios import *

class Commands:
    r"""
    Classe com todos os principais comandos do bot que podem ser usados em qualquer server que ele está conectado.

    ## Parâmetros
    
    :class:`discord.Client` c_: Recebe o cliente conectado no Discord para a partir dele fazer as operações.

    ## Atributos
    
    |   Atributos   |            Descrição            |
    |:--------------|:--------------------------------|
    | msg           | Mensagem lida em string         |
    | userId        | Id do usuário                   |
    | botId         | Id do bot                       |
    | copypastas    | Lista com os copypastas         |
    | sounds        | Lista com os áudios             |
    | msgSpams      | Lista com as mensagens de spam  |
    |---------------|---------------------------------|
    
    ## Métodos
    
    |    Métodos    |                                    Descrição                                    |
    |:--------------|:--------------------------------------------------------------------------------|
    | setMsg        | Define a mensagem string.                                                       |
    | getMsg        | Retorna a mensagem em string.                                                   |  
    | setUserId     | Define o id de um usuário.                                                      |
    | getUserId     | Retorna o id de um usuário .                                                    |
    | options       | Manda uma lista dos arquivos salvos e disponiveis.                              |
    | padrao        | Verifica se tem palavras que na frase que manda alguma resposta.                |
    | spam          | Spamar uma mensagem n vezes no servidor.                                        |
    | spamPv        | Spamar uma mensagem n vezes no privado de alguém de forma anônima.              |
    | erase         | Apaga n mensagens do canal onde foi mandado, além do próprio comando.           |
    | mensagem      | Manda uma mensagem entre as frases reservadas.                                  |
    | status        | Alterar status do bot.                                                          |
    | alerta        | Envia uma mensagem de alerta marcando todo mundo, em todos os canais do server. |
    | magnetize     | Junta ou distancia duas pessoas nos canais de voz de um servidor                |
    | magnetizeAct  | Acão do magnetize                                                               |
    | purge         | Tira todo mundo do canal de voz.                                                |
    | erradicate    | Tira todo mundo de todos os canais de voz do server.                            |
    | shake         | Fica movendo uma usuário entre os canais de voz por 1 minuto.                   |
    | milkshake     | Muda todo mundo do server de canal aleatoriamente.                              |
    | copypastas    | Manda algum texto de algum copypasta.                                           |
    | roll          | Tira alguém do canal aleatóriamente.                                            |
    | ban           | Desconecta alguém do server.                                                    |
    | silence       | Silencia ou desilencia todos do canal de voz.                                   |
    | headfone      | Tira/coloca áudio e mic de alguém.                                              |
    | listCommands  | Mostra todos os comandos.                                                       |
    | playSound     | Reproduz um áudio já salvo na pasta.                                            |
    | barricade     | Limita um chat pelo total de pessoas que estão nele                             |
    | halo          | ATENÇÃO: Tira todo mundo do server, deixando apenas o adm e o bot.              |
    |---------------|---------------------------------------------------------------------------------|
    """

    msg:str = ""
    userId:int = 0
    botId:int = 832785093117476884
    copypastas = listdir("copypastas/")
    sounds = listdir("audios/")
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
        f.close()
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
        except: self.userId = 0
            
        
    def getUserId(self, user_:str) -> int:
        r"""
        ## Getter -> userId
        :class:`int`: Retorna o id do usuário.

        ## Parâmetros

        :class:`str` user_: Usuario pra pegar o ip
        """
        return (int(user_[3:-1]))
        
    
    async def options(self, tipo_:str, list_) -> None:
        r"""
        ## Opções
        Retorna todos os arquieovs listados em um diretório

        ## Parâmetros

        > :class:`str` tipo_: Tipo do arquivo que vai ser postado.
        > :class:`list` list_: Lista com os arquivo de um diretório.
        """
        lista:str = f"{tipo_} disponíveis: \n"
        for x in range(len(list_)):
            if (x < 9): lista += f"0{x+1} : {list_[x]}\n"
            else:        lista += f"{x+1} : {list_[x]}\n"
        await self.message.channel.send(lista)


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
        msg:str = self.msg.split(" ", 3)
        userId:int = self.getUserId(msg[2])

        await self.message.delete()
        for guild in self.client.guilds:
            for member in guild.members:
                if (userId == member.id):
                    for i in range(int(msg[1])):
                        await member.send(msg[3])
                        sleep(0.6)
                    await member.send(self.msgSpams[randint(0,len(self.msgSpams))])
                    break

        msg, userId = None
        del msg, userId


    async def erase(self) -> None:
        r"""
        ## Erase
        Apaga n mensagens no mesmo canal que o comando foi digitado mais o próprio comando.

        ### Comando: `~erase n`
        :class:`int` n: quantidade de mensagens que vão ser apagadas.
        """
        await self.message.channel.purge(limit=int(self.msg.split(" ",1)[1])+1)

    
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
        status:str = self.msg.split(" ",2)
        
        if (status[1] == "jogo"):
            await self.client.change_presence(activity=Game(name=status[2]))
        
        elif (status[1] == "musica"):
            await self.client.change_presence(activity=Activity(type=ActivityType.listening, name=status[2]))

        elif (status[1] == "filme"):
            await self.client.change_presence(activity=Activity(type=ActivityType.watching, name=status[2]))
        
        status = None
        del status
        

    async def alerta(self) -> None:
        r"""
        ## Alerta
        Manda uma mensagem em todos os canais do server marcando todo mundo (@everyone)

        ### Comando: `~yall mensagem`
        :class:`str` mensagem: mensagem que vai ser mandada.
        """
        for channel in self.message.guild.text_channels:
            await channel.send("@everyone " + self.msg.split(" ",1)[1])


    async def magnetize(self) -> None:
        r"""
        ## Magnetize
        Junta ou distancia duas pessoas, mantendo elas sempre juntas ou afastadas.

        ### Comando: `~magnetiza tipo @pessoa1 @pessoa2`
        :class:`str` tipo: attract/a ou repulse/r
        :class:`member` @pessoa1/2: membros que vai ser magnetizado; A pessoa 2 segue/afasta da pessoa 1.
        """
        # Pega as informações do comando
        relation:str = ""
        try:                                        # Tenta pegar as informações
            msg:str = self.msg.split()
            relation = msg[1].lower()
            userA:int = self.getUserId(msg[2])
            userB:int = self.getUserId(msg[3])
        except:                                     # Erro no comando que foi digitado
            await self.message.channel.send("Você é burro e não sabe escrever.\nO comando certo é: ~magnetize attract/repulse @pessoa1 @pessoa2")
            return
        finally:                                    # Verifica se está correto
            if (relation not in ["attract", "a", "repulse", "r"]):
                await self.message.channel.send(f"{relation} está escrito errado. (Certo: attract/a ou repulse/r)")
                return

        # Procura os usuários nos canais de voz.
        cont:int = 0
        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                if (member.id == userA):   
                    userA = member
                    cont += 1
                elif (member.id == userB): 
                    userB = member
                    cont += 1

                if (cont == 2): break
            else: continue
            break

        # Não encontrou os usuários.
        if (cont != 2):
            await self.message.channel.send("Usuário não foi marcado corretamente.")
            return

        await self.magnetizeAct(userA, userB, self.message.guild, relation)

        relation = msg = userA = userB = cont = None
        del relation, msg, userA, userB, cont
        
        
    async def magnetizeAct(self, userA_:Member, userB_:Member, server_:Guild, tipo_:str) -> None:
        r"""
        ## Ação do magnetize
        Fução auxiliar que faz a ação deixar sempre duas pessoas juntas (attract) ou afastadas (repulse).

        ### Comando: `~demagnetize`
        Cancela a atração, outra alternativa seria sair do servidor.
        """
        await self.message.channel.send(f"{tipo_.capitalize()} ligado.")
        try:
            while (not self.msg.startswith("~demagnetize")):
                if (tipo_ in ["attract", "a"]):
                    await userB_.move_to(channel=userA_.voice.channel)
                else:
                    await userA_.move_to(server_.voice_channels[0])
                    await userB_.move_to(server_.voice_channels[-1])
        finally:
            await self.message.channel.send(f"{tipo_.capitalize()} cancelado.")
    

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

    async def safe_zone(self) -> None:

        safe_channel:discord.VoiceChannel = self.message.author.voice.channel

        if safe_channel == None:
            return

        for channel in self.message.guild.voice_channels:
            for member in channel.members:
                if member.voice.channel == safe_channel:
                    continue
                await member.move_to(None)

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
            - help: mostra uma lista dos arquivos disponíveis.
        """

        try:                                                        # Caso tenha recebido um index por parâmetro
            index:str = self.msg.split(' ', 1)[1]
            if (index == "help"): 
                await self.options("Copypastas", self.copypastas)
                index = None
                del index
                return
            else:
                index = int(index)
        except: 
            index:int = randint(0, len(self.copypastas)-1)		# Pega um arquivo aleatório
    
        path:str = "copypastas/" + self.copypastas[index]
        
        doc = open(path,"rb")
        while True:
            linha:str = doc.readline().decode('UTF-8')
            if (linha == ""): break
            if (linha.strip() == "\n"): continue
            try:
                await self.message.channel.send(linha)
                sleep(0.55)
            except:	continue
        doc.close()

        index = path = doc = linha = None
        del index, path, doc, linha


    async def roll(self) -> None:
        r"""
        ## Roll
        Aleatóriamente disconecta um usuário no mesmo canal de voz que o usuário responsável por digitar o comando.

        ### Comando: `~roullette`
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
        if (self.message.author.voice.deaf and self.message.author.voice.mute): return

        for member in self.message.guild.members:
            if self.userId == member.id:
                await member.edit(deafen=b_)
                await member.edit(mute=b_)
                break

        
    async def listCommands(self) -> None:
        r"""
        ## Help
        Mostra uma lista de todos os comando que o bot faz.

        ### Comando: `~help`
        """
        embedVar:Embed = Embed(title="~help para ter os comandos", description="Para voce infernizar seus amigos", colour=Colour.from_rgb(255, 102, 102))
        
        comandos:list = list(allComands.keys())
        for x in range(len(allComands.keys())):
            cmd = comandos[x]
            embedVar.add_field(name=cmd, value=allComands[cmd], inline=False)

        await self.message.channel.send(embed=embedVar)

        embedVar = comandos = cmd = None
        del embedVar, comandos, cmd

 
    async def playSound(self):
        r"""
        ## Playsound
        Reproduz um áudio pronto (já salvo no banco de dados) e reproduz no mesmo canal de voz que o usuário\
        responsável pelo comando difitado

        ### Comando: `~shout file`
        :class:`str` file: nome do arquivo com o seu tipo de áudio (.mp3 ou .mp4)
            - help: mostra uma lista dos arquivos disponíveis.
        """
        file:str = self.msg.split(" ", 1)[1]

        if (file == "help"): await self.options("Áudios", self.sounds)    
        else:
            try: file = self.sounds[int(file.strip())-1]
            finally:
                if (file[-4:] in [".mp3", ".mp4"]):
                    voice_channel = self.message.author.voice.channel
                    path:str = f"audios/{file}"
                    try: 
                        if (file[-4:] == ".mp3"): tam:int = MP3(path).info.length
                        else:                     tam:int = MP4(path).info.length
                    except: return
                        
                    if voice_channel != None:
                        vc = await voice_channel.connect()
                        vc.play(FFmpegPCMAudio(path, executable="Arquivos/ffmpeg.exe"))

                        sleep(tam+0.5)
                        for member in self.message.guild.members:
                            if member.id == self.botId:
                                await member.move_to(None)
                                break
                
                        vc = None
                        del vc
                    else:
                        await self.message.channel.send('Usuário não está em um canal de voz')

                    voice_channel = path = tam = None
                    del voice_channel, path,  tam
                else:
                    await self.message.channel.send('Esse arquivo não existe. \nDigite "~shout help" para ver os áudios disponiveis.')
        file = None
        del file
    

    async def barricade(self, b_:bool) -> None:
        r"""
        ## Barreira
        Limita o canal de voz, que o usuário responsável por ter digitado o comando está, pela quantidade de pessoas 
        que estão nele. Assim, somente administradores podem entrar no canal ou quando houver um espaço.

        ## Parâmetros

        > :class:`bool` b_: ativa ou desativa a barreira.
            - True: ativa.
            - False: desativa.

        ### Comando: `~barricade`
        """
        for channel in self.message.guild.voice_channels:
            if (self.message.author in channel.members):
                if (b_):
                    await channel.edit(user_limit=len(channel.members))
                    await self.message.channel.send('Barreira ativada')
                else:
                    await channel.edit(user_limit=0)
                    await self.message.channel.send('Barreira desativada')
                return

        await self.message.channel.send('Usuário não está em um canal de voz')
        

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