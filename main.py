from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from bs4 import BeautifulSoup
from time import sleep
import urllib.parse
import urllib


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.last.fm/pt/music/+free-music-downloads')
        html = BeautifulSoup(self.driver.page_source,'html.parser')
        botoes_download = html.find_all("a", class_="chartlist-download-button")
        btndownload = self.driver.find_elements(By.LINK_TEXT,'Baixar')
        contador = 0
        for i in botoes_download:
            path = 'C:\\Users\\SOFT\\Downloads\\'
            path += i['href'].split('/')[7].replace('+', ' ')
            path = urllib.parse.unquote_plus(path)
            btndownload[contador].click()
            while True:
                if os.path.exists(path):
                    print(f'o arquivo {path} existe!')
                    contador += 1
                    break
                else:
                    print(f'não encontrei {path}')
                    sleep(5)
        self.driver.close()

app = Bot()