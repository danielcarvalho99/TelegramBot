from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests

api = "Insira aqui a sua API"

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