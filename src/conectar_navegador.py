from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def abrir_navegador():
    navegador = webdriver.Firefox(service=Service(), options=Options())
    navegador.maximize_window()
    return navegador