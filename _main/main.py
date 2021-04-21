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
from discord import Intents, Client, Game, Message      # Configurações do dircord
from os import getenv                                   # Pega o token do bot

# Arquivos locais
from Gados import Gados

if __name__ == "__main__":
    intents = Intents.default()
    intents.members = True
    client = Client(intents=intents)

    cmds = Gados(client)

    @client.event                                       # Regstra um evento
    async def on_ready():                               # Quando o bot estiver pronto
        print(f"Bot ativado com o nome {client.user}")

        await client.change_presence(activity=Game(name="~help for commands"))

    @client.event  					                    # Próximo evento, se bot receber uma mensagem
    async def on_message(message:Message):
        cmds.setMsg(message)
        msg = cmds.getMsg()
        await cmds.padrao()

        if msg.startswith("~floodPV"):              await cmds.spamPv()
        elif msg.startswith("~silence patrick"):    await cmds.patrick()
        elif msg.startswith("#CassioVitima"):       await cmds.cassio()
        elif msg.startswith("obliterate TryRak"):   await cmds.BFG(True)
        elif msg.startswith("~flood"):              await cmds.spam()
        elif msg.startswith("~erase"):              await cmds.erase()
        elif msg.startswith("~mensagem"):           await cmds.mensagem()
        elif msg.startswith("~status"):             await cmds.status()
        elif msg.startswith("~yall"):               await cmds.alerta()
        elif msg.startswith("~purge"):              await cmds.purge()
        elif msg.startswith("~erradicate"):         await cmds.erradicate()
        elif msg.startswith("~shake"):              await cmds.shake()
        elif msg.startswith("~earthquake"):         await cmds.milkshake()
        elif msg.startswith("~copypasta"):          await cmds.copypasta()
        elif msg.startswith("~roullete"):           await cmds.roll()
        elif msg.startswith("~ban"):                await cmds.ban()
        elif msg.startswith("~deafen"):             await cmds.headFone(True)        
        elif msg.startswith("~undeafen"):           await cmds.headFone(False)
        elif msg.startswith("~silence"):            await cmds.silence(True)
        elif msg.startswith("~unsilence"):          await cmds.silence(False)
        elif msg.startswith("~help"):               await cmds.listCommands()
        elif msg.startswith("~shout"):              await cmds.playSound()
        elif msg.startswith("~magnetize"):          await cmds.magnetize()

    client.run(getenv('TOKEN'))
