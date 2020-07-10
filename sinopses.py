# encoding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import lxml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Funcionalidades do webdriver e definições iniciais
PATH = "/home/daniel/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://onepiece.fandom.com/pt/wiki/Arco_Romance_Dawn")
numeroDeArcos = int(input("De quantos arcos você quer a sinopse? "))

# O XPATH da primeira página é diferente do restante
XPath1 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td/a'
XPath2 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td[2]/a'

# Funcionalidades de cada página
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

def escreverConteudoDoArco(link):
    arquivo = open("sinopses.txt", "a")
    arquivo.write("\n" + driver.title + "\n" + acharSinopsedoArco(link) + "\n")

def acharProximoArco (arcoAtual):
    if (arcoAtual == 0):
        proximoArco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPath1))
        )
    else:
        proximoArco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, XPath2))
        )
    return proximoArco

def clicarNoProximoArco(arcoAtual):
    try:
        driver.execute_script("window.scrollTo(0, 800)")
        acharProximoArco(arcoAtual).click()
    except:
        driver.execute_script("window.scrollTo(0, 300)")
        acharProximoArco(arcoAtual).click()

for arco in range(numeroDeArcos):
        
        print(f'{driver.title}\nEste é o arco {arco + 1}')
        escreverConteudoDoArco(driver.current_url)

        if (arco < numeroDeArcos - 1):
            clicarNoProximoArco(arco)

driver.quit()