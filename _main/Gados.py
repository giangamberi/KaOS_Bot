from discord import Client
from Commands import Commands
from time import sleep

class Gados(Commands):
    idPatrick:int = 559820831564496896
    idCassio:int = 350757556081393666
    botLua:int = 799059659649449985

    def __init__(self, c_:Client) -> None:
        super().__init__(c_)

    async def patrick(self) -> None:
        for member in self.message.guild.members:
            if member.id == self.idPatrick:
                for i in range(30):
                    try: await member.edit(mute=True)
                    except: pass
                    sleep(1)    
                await member.edit(mute=False)
                break

    async def cassio(self) -> None:
        for member in self.message.guild.members:
            if member.id == self.idCassio:
                for i in range (30):
                    try: await member.move_to(None)
                    except: pass
                    sleep(1)
                await member.move_to(None)
                break

    # Tira as permissões ou kicka o bot do lua
    async def bigIron(self, extrem_:bool = False) -> None:
        for member in self.message.guild.members:
            if member.id == self.botLua:
                if (extrem_): await member.kick()
                else: await member.edit(roles=[])