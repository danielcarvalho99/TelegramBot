# encoding: utf-8
import telepot
from telepot.loop import MessageLoop
import requests
import lxml
from auxiliar import encontrarPrimeiroParagrafo,acharSinopsedoArco,api

arquivo = open("links.txt","r")
linhas = arquivo.readlines()
bot = telepot.Bot(api)
textoInicial = "Olá, este é o OnePieceWikiPtBot! Digite um número e receberá a sinopse do arco"

def exibirMensagemInicial(msg):
    _id = msg['from']['id']
    if(msg['text'] == "/start"):
        bot.sendMessage(_id,textoInicial)

def encontrarLinkdoArco(arco):
    linkDoArco = linhas[arco - 1]
    linkCorreto = linkDoArco[:-1]
    return linkCorreto

def exibirDados(msg):
    try:
        print(msg['from']['first_name'] + " " + msg['from']['last_name'] )
    except:
        print(msg['from']['first_name'])
    
    print(msg['text'])

def mandarLinkDoArco(msg):
    _id = msg['from']['id']
    arco = int(msg['text'])
    link = encontrarLinkdoArco(arco)
    sinopse = acharSinopsedoArco(link)
    bot.sendMessage(_id,sinopse)

def receberMensagem(msg):
    exibirMensagemInicial(msg)
    exibirDados(msg)
    try:
        mandarLinkDoArco(msg)
        print("Arco " + msg['text'] + " enviado")
    except:
        pass


MessageLoop(bot,receberMensagem).run_as_thread()

while True:
    pass
