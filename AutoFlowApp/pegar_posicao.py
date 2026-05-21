import time
import pyautogui


def main():
    print('Aguarde 5 segundos e posicione o mouse sobre o campo desejado...')
    time.sleep(5)
    x, y = pyautogui.position()
    print(f'Posição capturada: ({x}, {y})')
    print('Copie esses valores para o arquivo automacao.py.')


if __name__ == '__main__':
    main()
