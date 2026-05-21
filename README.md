# AutoFlow — Sistema de Automação de Cadastro

AutoFlow é um sistema em Python para automatizar cadastros em formulários usando PyAutoGUI.

## Recursos

- Interface gráfica com Tkinter
- Leitura de `dados/clientes.xlsx`
- Preenchimento automático de campos
- Logs em `logs/`
- Screenshots em `screenshots/`
- Utilitário para capturar coordenadas com `pegar_posicao.py`

## Instalação

1. Abra um terminal na pasta `AutoFlowApp`
2. Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute `pegar_posicao.py` para capturar as coordenadas dos campos do formulário:

```bash
python pegar_posicao.py
```

2. Abra o arquivo `automacao.py` e ajuste as constantes de coordenadas:

- `CAMPO_NOME`
- `CAMPO_EMAIL`
- `CAMPO_TELEFONE`
- `CAMPO_ENDERECO`
- `BOTAO_ENVIAR`

3. Execute `main.py` e use o botão `GERAR EXEMPLO DE DADOS` para criar automaticamente `dados/clientes.xlsx`, ou crie o arquivo manualmente com as colunas:

- `nome`
- `email`
- `telefone`
- `endereco`

- `nome`
- `email`
- `telefone`
- `endereco`

4. Execute o projeto:

```bash
python main.py
```

## Observações

- Não mova o mouse durante a execução da automação.
- O aplicativo irá recarregar a página automaticamente após cada envio.
- Logs são registrados em `logs/autoflow.log` e screenshots em `screenshots/`.
