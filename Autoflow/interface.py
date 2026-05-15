import tkinter as tk

botao_inicio.config(state='normal')


# ==========================================
# THREAD
# ==========================================

def iniciar_thread():
    thread = threading.Thread(target=iniciar)
    thread.start()


# ==========================================
# BOTÃO
# ==========================================

botao_inicio = tk.Button(
    janela,
    text='INICIAR AUTOMAÇÃO',
    font=('Arial', 14, 'bold'),
    bg='#4CAF50',
    fg='white',
    padx=20,
    pady=10,
    command=iniciar_thread
)

botao_inicio.pack(pady=30)


# ==========================================
# INSTRUÇÕES
# ==========================================

texto = '''
1. Abra o navegador
2. Não mexa no mouse
3. Ajuste as coordenadas
4. Clique em iniciar
'''

label_info = tk.Label(
    janela,
    text=texto,
    font=('Arial', 10),
    bg='#1e1e1e',
    fg='white',
    justify='left'
)

label_info.pack(pady=10)


# ==========================================
# EXECUTAR
# ==========================================

def iniciar_interface():
    janela.mainloop()