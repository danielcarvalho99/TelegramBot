# encoding: utf-8
import telepot
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests

api = "1305904762:AAEPaVSnU11s9tI1-yndrurrI7KROIVrInY"

bot = telepot.Bot(api)
textoInicial = "Olá, este é o OnePieceWikiPtBot! Digite um número e receberá a sinopse do arco"

def exibirDados(msg):
    try:
        print(msg['from']['first_name'] + " " + msg['from']['last_name'] )
    except:
        print(msg['from']['first_name'])
    
    print(msg['text'])

def mandarLinkDoArco(msg):
    _id = msg['from']['id']
    bot.sendMessage(_id,"Isto é um teste")

def receberMensagem(msg):
    try:
        mandarLinkDoArco(msg)
    except:
        pass



bot.message_loop(receberMensagem)

while True:
    pass