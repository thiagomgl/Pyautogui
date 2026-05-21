from pathlib import Path
from openpyxl import Workbook

CAMINHO = Path(__file__).resolve().parent / 'dados' / 'clientes.xlsx'
EXEMPLO = [
    ['Ana Silva', 'ana.silva@example.com', '11987654321', 'Rua das Flores, 123'],
    ['Bruno Costa', 'bruno.costa@example.com', '21999887766', 'Av. Paulista, 456'],
    ['Carla Souza', 'carla.souza@example.com', '31991445566', 'Rua do Comércio, 789'],
    ['Daniel Lima', 'daniel.lima@example.com', '41988776655', 'Rua das Acácias, 101'],
    ['Eduarda Melo', 'eduarda.melo@example.com', '51997766554', 'Alameda Santos, 202']
]

COLUNAS = ['nome', 'email', 'telefone', 'endereco']


def gerar_exemplo_clientes():
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'clientes'
    sheet.append(COLUNAS)
    for linha in EXEMPLO:
        sheet.append(linha)
    workbook.save(CAMINHO)
    return str(CAMINHO)


def main():
    caminho = gerar_exemplo_clientes()
    print(f'Arquivo de exemplo criado em: {caminho}')


if __name__ == '__main__':
    main()
