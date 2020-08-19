from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests

api = "1305904762:AAEPaVSnU11s9tI1-yndrurrI7KROIVrInY"

def encontrarPrimeiroParagrafo(link):
    textoDaPagina = requests.get(link).text
    textoLegivel = BeautifulSoup(textoDaPagina,'lxml')
    primeiroParagrafo = textoLegivel.p
    return primeiroParagrafo

def acharSinopsedoArco(link):
    if len(encontrarPrimeiroParagrafo(link).text) < 30:
        sinopseDoArco = encontrarPrimeiroParagrafo(link).find_next('p').text
    else:
        sinopseDoArco = encontrarPrimeiroParagrafo(link).text
    return sinopseDoArco