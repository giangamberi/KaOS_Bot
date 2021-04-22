# KaOS_Bot
[![Versão](https://img.shields.io/badge/version-v1.0-orange)](https://github.com/giangamberi/KaOS_Bot/releases/tag/v1.0)
![Plataforma](https://img.shields.io/badge/plataforma-Windows-lightgrey?logo=windows)
[![Versão python](https://img.shields.io/badge/python-v3.8.5-blue?logo=python)](https://www.python.org/downloads/release/python-385/)
[![Licença](https://img.shields.io/badge/license-MIT-brightgreen?)](https://github.com/giangamberi/KaOS_Bot/blob/main/LICENSE)

![capa](https://github.com/giangamberi/KaOS_Bot/blob/main/Arquivos/Imagens/Logo/Logo-retangulo.jpg)

Um bot *MUITO* caótico do discord.

1. [Comandos](#comandos)
2. [Código](#código)
3. [Requerimentos](#requerimentos)
4. [Documentação](#documentação)
5. [Licença](#licença)
6. [Autores](#autores)

## Comandos
|                      Comandos                         |                                              Descrição                                            |
|-------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|~help 							|Mostrar comandos do bot.|
|~mensagem 						|Manda uma mensagem aleatória inpiradora.|
|~flood (n) (mensagem)					|Spamar uma mensagem n vezes no servidor. |
|~floodPV (n) (@pessoa) (mensagem)			|Spamar uma mensagem n vezes no privado de alguém de forma anônima.|
|~status (ogo, musica ou filme) (mensagem)		|Alterar status do bot.|
|~erase (n) 						|Apaga n mensagens do canal além do próprio comando.|
|~copypasta (opcional: index da copypasta)		|Envia uma copypasta retirado diretamente do nosso incrível banco de dados.|
|~magnetize <attract ou repulse> @pessoa1 @pessoa2 	|Magnetiza duas pessoas, deixando elas juntas ou distantes nos canais de voz do servidor.|
|"~demagnetize"                                         |Cancela toda magnetização do server.|
|~yall (mensagem)					|Envia uma mensagem de alerta marcando todo mundo, em todos os canais do server.|
|~roullette						|Brinque de roleta russa e remova alguém aleatoriamente do canal.|
|~purge							|Diversão! Manda todo mundo que tá na call pro caralho.|
|~erradicate						|MAIS DIVERSÃO! Disconecta TODO MUNDO de TODAS AS CALLS.|
|~deafen (@pessoa)					|Tira os 5 sentidos da pessoa na call.|
|~undeafen (@pessoa)					|Volta o som e o mic da pessoa. Booooo.|
|~silence						|Cala a boca de todo mundo.|
|~unsilence						|!Silence.|
|~ban (@pessoa)						|Desconecta a pessoa do canal de voz.|
|~earthquake						|Mistura todos os integrantes em todas as salas e os embaralha. Show!|
|~shake (@pessoa)					|Você amaldiçoou a pessoa a ficar trocando entre os canais de voz a cada segundo. Por 1 minuto.|
|~shout (nomedoaudio).mp3				|Reproduz um áudio prestativo e inspirador.|


## Código
Baixando a pasta [_main](https://github.com/giangamberi/KaOS_Bot/tree/main/_main) você consegue ter acesso ao código. Os pré-requisitos para rodar estão declaradas na parte de [Requerimentos](#requerimentos). Para executar o programa basta rodar o arquivo ```main.py```.

## Requerimentos
1. O programa usa algumas biblioteca externas:
	- [Discord](https://pypi.org/project/discord.py/): uso da [api](https://discordpy.readthedocs.io/en/latest/api.html) do discord para suporte com python.

			pip install discord

	- [Mutagen](https://pypi.org/project/mutagen/): suporte para áudio.

			pip install mutagen

	- [PyNaCl](https://pypi.org/project/PyNaCl/): suporte para remoção de pessoas e saída de som do bot.

			pip install PyNaCl

2. Token: no aquivo [.env](https://github.com/giangamberi/KaOS_Bot/blob/main/_main/.env) precisa colocar o token do bot.
	
    	TOKEN="CódigoDoToken"

## Documentação
Em breve uma documentação será criada na [wiki](https://github.com/giangamberi/KaOS_Bot/wiki) do repositório.

## Licença
Este projeto é licenciado por [MIT License](https://github.com/giangamberi/KaOS_Bot/blob/main/LICENSE).

## Autores
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/giangamberi">
                <img src="https://avatars.githubusercontent.com/u/54535336" width="100px;" alt="Foto do Gian no GitHub"/><br>
                <sub><b>Gian Gamberi</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Gui25Reis">
                <img src="https://avatars1.githubusercontent.com/u/48360732" width="100px;" alt="Foto do Gui Reis no GitHub"/><br>
                <sub><b>Gui Reis</b></sub>
            </a>
        </td>
		<td align="center">
            <a href="https://github.com/REXDES">
                <img src="https://avatars.githubusercontent.com/u/49534119" width="100px;" alt="Foto do Rone no GitHub"/><br>
                <sub><b>Rone Filho</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/marcelotakayama">
                <img src="https://avatars.githubusercontent.com/u/47531526" width="100px;" alt="Foto do Marcelo Takayama no GitHub"/><br>
                <sub><b>Marcelo Takayama</b></sub>
            </a>
        </td>
    </tr>
</table>
