from selenium.webdriver.common.by import By
from src.acoes import *
from time import sleep

def login_ecg(navegador, usuario, senha):
    navegador.get('https://ecgglass.com/ecg_glass/login/login.php')
    escrever(navegador, By.NAME, 'text_usuario', usuario)
    escrever(navegador, By.NAME, 'password_senha', senha)
    clicar(navegador, By.CSS_SELECTOR, 'html body#bg_login_full div.container div#box_login_full form div.box_input.text-right input.btn.btn-primary')

def acessar_kits(navegador):
    navegador.get('https://ecgglass.com/ecg_glass/materiais/material/cadastro.php?grupo=K')

def cadastrar_codigos_gerais(navegador, dados_kit):
    selecionar_combo_box(navegador, By.ID, "select_familia", '5')
    
    ids_itens = {
        'codigo_interno' : "text_codigo_interno",
        'tipo' : "text_tipo_kit",
        'largura' : "text_largura",
        'altura' : "text_altura",
        'descricao' : "text_descricao"
    }

    codigo_cru = dados_kit['codigo']
    tipo = f'{codigo_cru.split('.')[0].replace('X', '-')}'
    largura = (codigo_cru[:-3].split('.', 1)[1].split('X')[0].replace('.', ''))+'0'
    altura = (codigo_cru[:-3].split('.', 1)[1].split('X')[1].replace('.', ''))+'0'

    textos = {
        'codigo' : codigo_cru,
        'tipo' : tipo,
        'largura_mm' : largura,
        'altura_mm' : altura,
        'descricao' : dados_kit['produto']
        }

    for id, texto in zip(ids_itens.values(), textos.values()):
        escrever(navegador, By.ID, id, texto)

def cadastrar_marcas(navegador, dados_kit):
    clicar(navegador, By.ID, "btn-1-tab")
    marca_kit = {
        'branco' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(10) > input:nth-child(1)',
        'nat_fosco' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(22) > input:nth-child(1)',
        'bronze' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(9) > input:nth-child(1)',
        'preto' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(24) > input:nth-child(1)',
    }
    marca_temperados_cia = {
        'branco' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(10) > input:nth-child(1)',
        'nat_fosco' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(22) > input:nth-child(1)',
        'bronze' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(9) > input:nth-child(1)',
        'preto' : 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(11) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(24) > input:nth-child(1)',
    }
    selecionar_combo_box(navegador, By.ID, "select_marca_padrao", "49")
    cor = ''
    cor_kit = dados_kit['codigo'][-3:]
    if cor_kit == 'BCO':
        cor = 'branco'
    elif cor_kit == 'BZE':
        cor = 'bronze'
    elif cor_kit == 'FCO':
        cor = 'nat_fosco'
    elif cor_kit == 'PTO':
        cor = 'preto'

    neutro = 'div.tabela:nth-child(5) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > input:nth-child(1)'
    clicar(navegador, By.XPATH, "/html/body/div[3]/form/div[1]/div[2]/div[5]/table[1]/tbody/tr[4]/td[2]/div/button/span")
    clicar(navegador, By.CSS_SELECTOR, neutro)
    clicar(navegador, By.CSS_SELECTOR, marca_kit[cor])
    clicar(navegador, By.XPATH, "/html/body/div[3]/form/div[1]/div[2]/div[5]/table[1]/tbody/tr[4]/td[2]/div/button/span")

    clicar(navegador, By.XPATH, "/html/body/div[3]/form/div[1]/div[2]/div[5]/table[1]/tbody/tr[10]/td[2]/div/button/span")    
    clicar(navegador, By.CSS_SELECTOR, marca_temperados_cia[cor])
    clicar(navegador, By.XPATH, "/html/body/div[3]/form/div[1]/div[2]/div[5]/table[1]/tbody/tr[10]/td[2]/div/button/span")    

    objeto = navegador.find_element(By.CSS_SELECTOR, ".titulo_estilo_responsivo")
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", objeto)
    # clique_fora = '/html/body'
    # clicar(navegador, By.XPATH, clique_fora)

def cadastrar_valores(navegador, dados_kit):
    clicar(navegador, By.ID, "btn-3-tab")
    valor = dados_kit['valor_bruto']

    marca_kit = "text_custo_unitario_178_TODAS"
    marca_temperados_cia = "text_custo_unitario_49_TODAS"

    escrever(navegador, By.NAME, marca_kit, valor)
    escrever(navegador, By.NAME, marca_temperados_cia, valor)


def cadastrar(navegador):
    clicar(navegador, By.ID, "button_salvar")

def cadastrar_kit(navegador, dados_kit):
    acessar_kits(navegador)    
    sleep(1)
    cadastrar_codigos_gerais(navegador, dados_kit)    
    sleep(1)
    cadastrar_marcas(navegador, dados_kit)    
    sleep(1)
    cadastrar_valores(navegador, dados_kit)    
    sleep(1)
    cadastrar(navegador)
    sleep(1)


