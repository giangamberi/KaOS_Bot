from discord import Intents, Client, Game, Message # Configurações do dircord
from os import getenv

from Gados import Gados

intents = Intents.default()
intents.members = True
client = Client(intents=intents)

cmds = Gados(client)

@client.event                   # registrar um evento
async def on_ready():           # eventos ja prontos, quando o bot estiver pronto:
	print(f"Bot ativado com o nome {client.user}")

	await client.change_presence(activity=Game(name="~help for commands"))

@client.event  					# Próximo evento, se bot receber uma mensagem
async def on_message(message:Message):
    cmds.setMsg(message)
    await cmds.padrao()
    msg = cmds.getMsg()

    if msg.startswith("~floodPV"): await cmds.spamPv()

    elif msg.startswith("~silence patrick"): await cmds.patrick()

    elif msg.startswith("#CassioVitima"): await cmds.cassio()

    elif msg.startswith("~flood"): await cmds.spam()

    elif msg.startswith("~mensagem"): await cmds.mensagem()

    elif msg.startswith("~status"): await cmds.status()

    elif msg.startswith("~yall"): await cmds.alerta()

    elif msg.startswith("~purge"): await cmds.purge()

    elif msg.startswith("~erradicate"): await cmds.erradicate()

    elif msg.startswith("~shake"): await cmds.shake()

    elif msg.startswith("~earthquake"): await cmds.milkshake()

    elif msg.startswith("~copypasta"): await cmds.copypasta()

    elif msg.startswith("~roullete"): await cmds.roll()

    elif msg.startswith("~ban"): await cmds.ban()

    elif msg.startswith("~deafen"): await cmds.headFone(True)        

    elif msg.startswith("~undeafen"): await cmds.headFone(False)

    elif msg.startswith("~silence"): await cmds.silence(True)

    elif msg.startswith("~unsilence"): await cmds.silence(False)

    elif msg.startswith("~help"): await cmds.listCommands()

    elif msg.startswith("~shout"): await cmds.playSound()


client.run(getenv('TOKEN'))