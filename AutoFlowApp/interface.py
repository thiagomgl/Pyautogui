import threading
import tkinter as tk
from tkinter import messagebox, ttk
from automacao import executar_automacao
from gerar_exemplo_dados import gerar_exemplo_clientes


def iniciar_interface():
    janela = tk.Tk()
    janela.title('AutoFlow - Automação de Cadastro')
    janela.geometry('620x420')
    janela.configure(bg='#1e1e1e')
    janela.resizable(False, False)

    titulo = tk.Label(
        janela,
        text='AutoFlow - Sistema de Automação de Cadastro',
        font=('Arial', 16, 'bold'),
        fg='white',
        bg='#1e1e1e'
    )
    titulo.pack(pady=20)

    status_label = tk.Label(
        janela,
        text='Pronto para iniciar.',
        font=('Arial', 11),
        fg='white',
        bg='#1e1e1e'
    )
    status_label.pack(pady=10)

    progress_var = tk.DoubleVar(value=0)
    barra_progresso = ttk.Progressbar(
        janela,
        maximum=100,
        length=520,
        variable=progress_var
    )
    barra_progresso.pack(pady=10)

    descricao = tk.Label(
        janela,
        text='1. Ajuste as coordenadas em automacao.py\n'
             '2. Use o botão de exemplo ou crie dados/clientes.xlsx\n'
             '3. Abra o formulário no navegador\n'
             '4. Clique em Iniciar e não mova o mouse durante a execução',
        font=('Arial', 10),
        fg='white',
        bg='#1e1e1e',
        justify='left'
    )
    descricao.pack(padx=20, pady=10)

    botao_exemplo = tk.Button(
        janela,
        text='GERAR EXEMPLO DE DADOS',
        font=('Arial', 12, 'bold'),
        bg='#2196F3',
        fg='white',
        padx=20,
        pady=10,
        state='normal'
    )
    botao_exemplo.pack(pady=8)

    botao_inicio = tk.Button(
        janela,
        text='INICIAR AUTOMAÇÃO',
        font=('Arial', 14, 'bold'),
        bg='#4CAF50',
        fg='white',
        padx=20,
        pady=10,
        state='normal'
    )
    botao_inicio.pack(pady=10)

    def atualiza_status(texto):
        status_label.config(text=texto)
        janela.update_idletasks()

    def atualizar_progresso(valor):
        progress_var.set(valor)
        barra_progresso.update_idletasks()

    def gerar_exemplo():
        botao_exemplo.config(state='disabled')
        atualiza_status('Gerando arquivo de exemplo...')
        try:
            caminho = gerar_exemplo_clientes()
            messagebox.showinfo('AutoFlow', f'Arquivo de exemplo criado em:\n{caminho}')
            atualiza_status('Arquivo de exemplo criado com sucesso.')
        except Exception as erro:
            messagebox.showerror('AutoFlow', f'Falha ao gerar dados de exemplo:\n{erro}')
            atualiza_status('Falha ao gerar dados de exemplo.')
        finally:
            botao_exemplo.config(state='normal')

    def executar():
        botao_inicio.config(state='disabled')
        atualiza_status('Iniciando automação...')

        def callback(progresso):
            janela.after(0, lambda: [atualiza_status(f'Progresso: {progresso}%'), atualizar_progresso(progresso)])

        def worker():
            sucesso = executar_automacao(callback)
            mensagem = 'Automação finalizada com sucesso.' if sucesso else 'A automação falhou. Verifique logs.'

            def finalizar():
                atualiza_status(mensagem)
                botao_inicio.config(state='normal')
                if sucesso:
                    messagebox.showinfo('AutoFlow', mensagem)
                else:
                    messagebox.showerror('AutoFlow', mensagem)

            janela.after(0, finalizar)

        threading.Thread(target=worker, daemon=True).start()

    botao_exemplo.config(command=gerar_exemplo)
    botao_inicio.config(command=executar)
    janela.mainloop()
