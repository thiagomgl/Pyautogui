import os
import time
import logging
from datetime import datetime

import pandas as pd
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DADOS_DIR = os.path.join(BASE_DIR, 'dados')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')
EXCEL_PATH = os.path.join(DADOS_DIR, 'clientes.xlsx')

# ==========================================
# COORDENADAS DO FORMULÁRIO
# ==========================================
# Ajuste os valores abaixo usando pegar_posicao.py
CAMPO_NOME = (700, 390)
CAMPO_EMAIL = (700, 470)
CAMPO_TELEFONE = (700, 550)
CAMPO_ENDERECO = (700, 630)
BOTAO_ENVIAR = (950, 760)

# Se o seu formulário tem botão específico para atualizar, defina abaixo.
# Caso contrário, a automação usará Ctrl+R para recarregar.
BOTAO_RECARREGAR = None


def criar_pastas():
    os.makedirs(DADOS_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def configurar_logger():
    criar_pastas()
    logger = logging.getLogger('autoflow')
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    arquivo_log = os.path.join(LOGS_DIR, 'autoflow.log')
    file_handler = logging.FileHandler(arquivo_log, encoding='utf-8')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

logger = configurar_logger()


def clicar(x, y, duration=0.15):
    pyautogui.click(x, y, duration=duration)
    time.sleep(0.3)


def escrever(texto, interval=0.03):
    pyautogui.write(str(texto), interval=interval)
    time.sleep(0.2)


def screenshot(nome):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_arquivo = f'{timestamp}_{nome}'.replace(' ', '_')
    caminho = os.path.join(SCREENSHOTS_DIR, f'{nome_arquivo}.png')
    try:
        pyautogui.screenshot(caminho)
        logger.info(f'Screenshot salva em: {caminho}')
    except Exception as erro:
        logger.warning(f'Falha ao salvar screenshot: {erro}')


def abrir_formulario():
    logger.info('Verifique se o formulário está aberto e visível na tela.')
    time.sleep(2)


def ler_dados():
    if not os.path.exists(EXCEL_PATH):
        raise FileNotFoundError(f'Arquivo não encontrado: {EXCEL_PATH}')
    dados = pd.read_excel(EXCEL_PATH, engine='openpyxl')
    colunas_esperadas = ['nome', 'email', 'telefone', 'endereco']
    faltando = [col for col in colunas_esperadas if col not in dados.columns]
    if faltando:
        raise ValueError(f'Colunas faltando no Excel: {faltando}')
    return dados


def preencher_formulario(nome, email, telefone, endereco):
    clicar(*CAMPO_NOME)
    escrever(nome)

    clicar(*CAMPO_EMAIL)
    escrever(email)

    clicar(*CAMPO_TELEFONE)
    escrever(telefone)

    clicar(*CAMPO_ENDERECO)
    escrever(endereco)

    clicar(*BOTAO_ENVIAR)


def recarregar_formulario():
    if BOTAO_RECARREGAR:
        clicar(*BOTAO_RECARREGAR)
        time.sleep(3)
    else:
        pyautogui.hotkey('ctrl', 'r')
        time.sleep(3)


def executar_automacao(callback_progresso=None):
    try:
        logger.info('Iniciando automação')
        criar_pastas()
        dados = ler_dados()
        total = len(dados)

        if total == 0:
            logger.warning('Nenhum registro encontrado no arquivo Excel.')
            return False

        abrir_formulario()

        for index, linha in dados.iterrows():
            nome = linha['nome']
            email = linha['email']
            telefone = linha['telefone']
            endereco = linha['endereco']

            logger.info(f'Processando registro {index + 1}/{total}: {nome}')
            preencher_formulario(nome, email, telefone, endereco)
            screenshot(f'enviado_{index+1}')
            recarregar_formulario()

            progresso = int(((index + 1) / total) * 100)
            if callback_progresso:
                callback_progresso(progresso)

        logger.info('Automação finalizada com sucesso')
        return True

    except Exception as erro:
        logger.exception(f'Erro durante a automação: {erro}')
        screenshot('erro')
        return False
