# encoding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import lxml
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/daniel/chromedriver"
driver = webdriver.Chrome(PATH)

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

def acharProximoArco (arcoAtual,XPath1,XPath2,driver):
    if (arcoAtual == 0):
        proximoArco = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, XPath1))
        )
    else:
        proximoArco = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, XPath2))
        )
    return proximoArco

def clicarNoProximoArco(arcoAtual,XPath1,XPath2,driver):
    try:
        driver.execute_script("window.scrollTo(0, 800)")
        acharProximoArco(arcoAtual,XPath1,XPath2,driver).click()
    except:
        driver.execute_script("window.scrollTo(0, 300)")
        acharProximoArco(arcoAtual,XPath1,XPath2,driver).click()

def escreverLink (driver):
    arquivo = open("links.txt", "a")
    arquivo.write(driver.current_url + "\n")
