# encoding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import lxml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from funcoes import encontrarPrimeiroParagrafo,acharSinopsedoArco,acharProximoArco,clicarNoProximoArco
from funcoes import PATH,driver

# Funcionalidades do webdriver e definições iniciais
driver.get("https://onepiece.fandom.com/pt/wiki/Arco_Romance_Dawn")
numeroDeArcos = 3

# O XPATH da primeira página é diferente do restante
XPath1 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td/a'
XPath2 = '/html/body/div[3]/section/div[2]/article/div/div[1]/div[2]/aside/section[2]/table/tbody/tr/td[2]/a'

def escreverLink ():
    arquivo = open("links.txt", "a")
    arquivo.write(driver.current_url + "\n")

for arco in range(numeroDeArcos):
    try:
        print("Este é o arco " + str(arco + 1))
        print(driver.title)
        escreverLink()
        
        if(arco < numeroDeArcos - 1):
            clicarNoProximoArco(arco,XPath1,XPath2,driver)
    except:
        print("Ocorreu um erro")

driver.quit()
