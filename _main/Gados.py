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
from discord import Client
from time import sleep

# Arquivos locais
from Commands import Commands


class Gados(Commands):
    r"""
    Classe com todos os principais comandos do bot que podem ser usados em qualquer server que ele está conectado.

    ## Parâmetros
    :class:`discord.Client` c_: Recebe o cliente conectado ao Discord para a partir dele fazer as operações.

    ## Atributos
    
    |   Atributos   |            Descrição            |
    |:--------------|:--------------------------------|
    | idPatrick     | Id do Patrick.                  |
    | idCassio      | Id do Cássio.                   |
    | idLua         | Id do bor TryRak.               |
    |---------------|---------------------------------|
    
    ## Métodos
    
    |    Métodos    |                Descrição                |
    |:--------------|:----------------------------------------|
    | patrick       | Deixa o Patrick mutado por um minuto.   |
    | cassio        | Retorna a mensagem em string.           |  
    | bigIron       | Retorna o id do bot.                    |
    |---------------|-----------------------------------------|
    """
    idPatrick:int = 559820831564496896
    idCassio:int = 350757556081393666
    botLua:int = 799059659649449985

    def __init__(self, c_:Client) -> None:
        super().__init__(c_)
        
    async def patrick(self) -> None:
        r"""
        ## Silence Patrick
        Muta o Patrick por um minuto.

        ### Comando: `~silence patrick`
        """
        for member in self.message.guild.members:
            if member.id == self.idPatrick:
                for i in range(30):
                    try: await member.edit(mute=True)
                    except: pass
                    sleep(1)
                try: await member.edit(mute=False)
                except: break
                break

    async def cassio(self) -> None:
        r"""
        ## Cassio vítima
        Fica mudando o Cassio de canal de voz por um minuto.

        ### Comando: `#CassioVitima`
        """
        self.setUserId(self.idCassio)
        self.shake()

        # for member in self.message.guild.members:
        #     if member.id == self.idCassio:
        #         for i in range (30):
        #             try: await member.move_to(None)
        #             except: pass
        #             sleep(1)
        #         await member.move_to(None)
        #         break


    # Tira as permissões ou kicka o bot do lua
    async def BFG(self, extrem_:bool = False) -> None:
        r"""
        ## Adeus TryRak
        Tira os cargos do bot TryRak ou tira ele do server

        ## Parâmetros

        > :class:`bool` extrem_: tira a permissão ou bane do server
            - True: bane do server
            - False: tira a permissao

        ### Comando: `~BFG`
        """
        for member in self.message.guild.members:
            if member.id == self.botLua:
                if (extrem_): await member.kick()
                else: await member.edit(roles=[])