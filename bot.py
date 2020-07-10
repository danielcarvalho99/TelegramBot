# encoding: utf-8
from bs4 import BeautifulSoup
import telepot
from telepot.loop import MessageLoop
import requests
import lxml
from funcoes import encontrarPrimeiroParagrafo,acharSinopsedoArco

arquivo = open("links.txt","r")
linhas = arquivo.readlines()
api = "Insira sua API do Telegram"
bot = telepot.Bot(api)
textoInicial = "Olá, este é o OnePieceWikiPtBot! Digite um número e receberá a sinopse desse arco."

def exibirMensagemInicial(msg):
    _id = msg['from']['id']
    if(msg['text'] == "/help"):
        bot.sendMessage(_id,textoInicial)

def encontrarLinkdoArco(arco):
    linkDoArco = linhas[arco - 1]
    linkCorreto = linkDoArco[:-1]
    return linkCorreto

def exibirDados(msg):
    try:
        print(msg['from']['first_name'] + msg['from']['last_name'])
    except:
        print(msg['from']['first_name']) 

    print(msg['from']['id'])
    print(msg['text'])
    print(msg['message_id'])

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

bot.message_loop(receberMensagem)

while True:
    pass
