import keyboard
import tkinter as tk
import threading
from tkinter import Frame

import pyautogui
import time


tela = tk.Tk()
tela.geometry("280x290")
tela.title("Auto Cliker")

click = True
situacao = False

modoBranco = False

botao_esquerdo = False

def Botao_esquerda_direita(event=None):
    global botao_esquerdo
    if botao_esquerdo:
        ed_botao.config(text='Botão Esquerdo')
        botao_esquerdo = False
    elif not botao_esquerdo:
        ed_botao.config(text='Botão Direito')
        botao_esquerdo = True

def auto_cliker():
    tempo = float(entrada_tempo.get())
    global click
    if botao_esquerdo:
        while click:
            pyautogui.leftClick()
            time.sleep(tempo)
    elif not botao_esquerdo:
        while click:
            pyautogui.rightClick()
            time.sleep(tempo)


def Iniciar():
    global click,situacao
    if not situacao:
        click = True
        situacao = True
        Atualizar_status()
        threading.Thread(target=auto_cliker,daemon=True,).start()

def Parar():
    global click,situacao
    click = False
    situacao = False
    Atualizar_status()

def Atualizar_status():
    if situacao:
        label_status.config(text="Status: LIGADO", fg="light green")
    else:
        label_status.config(text="Status: DESLIGADO", fg="red")

def Parar_iniciar(event=None):
    if situacao:
        Parar()
    else:
        Iniciar()


def ModoBP(event=None):
    global modoBranco
    if modoBranco:
        tela['bg'] = 'gray94'
        area1['bg'] = 'light gray'
        titulo['bg'] = 'light gray'
        titulo['fg'] = 'black'
        label_entrada['bg'] = 'light gray'
        label_entrada['fg'] = 'black'
        entrada_tempo['bg'] = 'white'
        entrada_tempo['fg'] = 'black'
        area2['bg'] = 'gray94'
        label_status['bg'] = 'gray94'
        ed_botao['bg'] = 'gray94'
        ed_botao['fg'] = 'black'
        area3['bg'] = 'gray94'
        botao_iniciar['bg'] = 'gray94'
        botao_iniciar['fg'] = 'black'
        botao_parar['bg'] = 'gray94'
        botao_parar['fg'] = 'black'
        area4['bg'] = 'gray94'
        botao_sair['bg'] = 'gray94'
        botao_sair['fg'] = 'black'
        area5['bg'] = 'gray94'
        botao_modo['bg'] = 'gray94'
        botao_modo['fg'] = 'black'
        label_status_modo.config(text='Modo:BRANCO',bg='light gray',fg='black')
        modoBranco = False
    elif not modoBranco:
        tela['bg'] = 'gray16'
        titulo['bg'] = 'gray25'
        titulo['fg'] = 'gray86'
        area1['bg'] = 'gray25'
        label_entrada['bg'] = 'gray25'
        label_entrada['fg'] = 'gray86'
        entrada_tempo['bg'] = 'gray'
        entrada_tempo['fg'] = 'gray90'
        area2['bg'] = 'gray16'
        ed_botao['bg'] = 'gray16'
        ed_botao['fg'] = 'gray86'
        label_status['bg'] = 'gray16'
        area3['bg'] = 'gray16'
        botao_iniciar['bg'] = 'gray16'
        botao_iniciar['fg'] = 'gray86'
        botao_parar['bg'] = 'gray16'
        botao_parar['fg'] = 'gray86'
        area4['bg'] = 'gray16'
        botao_sair['bg'] = 'gray16'
        botao_sair['fg'] = 'gray86'
        area5['bg'] = 'gray16'
        botao_modo['bg'] = 'gray16'
        botao_modo['fg'] = 'gray86'
        label_status_modo.config(text='Modo:PRETO',bg='gray25',fg='gray86')
        modoBranco = True

def Sair_app(event=None):
    return tela.quit()

titulo = tk.Label(text="Auto Cliker\nVersão:001",font=("Arial", 10, "bold"),bg="light gray")
titulo['border'] = 5
titulo.pack(pady= 10,padx= 5)
# Começo da area 1
area1 = Frame()
#area1["pady"] = 3
#area1["width"] = 3
area1['bg'] = 'light gray'
area1['border'] = 5
area1.pack()
label_entrada = tk.Label(area1,text='Tempo por click:',font=("Arial",10 ),bg='light gray')
label_entrada.pack(side="left")

entrada_tempo = tk.Entry(area1)
entrada_tempo.insert(0, "0.1")  # Valor padrão de 0.1 segundos
entrada_tempo.pack()
# Fim da area 1 onde mostra, usa e lê um valor/tempo de clique

# Começo da area 2
area2 = Frame()
area2["pady"] = 5
area2["width"] = 5
area2['border'] = 1
area2.pack()
label_status = tk.Label(area2,text="Status: DESLIGADO", fg="red",font=("Arial",10 ))
label_status.pack()
ed_botao = tk.Button(text='Botão Esquerdo',command=Botao_esquerda_direita)
ed_botao.pack()
# Fim da area 2 onde mostra se o programa(Auto-Cleker) está ligado ou desligado

# Começo da area 3
area3 = Frame()
area3["pady"] = 5
area3["width"] = 5
area3['border'] = 1
area3.pack()
botao_iniciar = tk.Button(area3,text="Iniciar",command=Iniciar)
botao_iniciar.pack(pady= 5,padx= 10,side="left")
botao_parar = tk.Button(area3,text="Parar",command=Parar)
botao_parar.pack(pady= 5,padx=10,side="right")
# Fim da area 3 onde tem o botão de iniciar e de parar o programa

# Começo da area 4
area4 = Frame()
area4["pady"] = 5
area4["width"] = 5
area4['border'] = 1
area4.pack()
botao_sair = tk.Button(area4,text="Sair",command=Sair_app)
botao_sair.pack()
# Fim da area 4 onde tem o botão de Sair do programa

# Começo da area 5
area5 = Frame()
area5["pady"] = 5
area5["width"] = 5
area5['border'] = 1
area5.pack()
botao_modo = tk.Button(area5,text="Modo",command=ModoBP)
botao_modo.pack(padx=5,pady=5,side="left")
label_status_modo = tk.Label(area5,text='Modo:BRANCO',bg="light gray")
label_status_modo.pack(padx=5,pady=5,side="left")
# Fim da area 5 onde tem um botão que muda o modo de claro para escuro e vise versa

keyboard.add_hotkey("\+1", Parar_iniciar)
keyboard.add_hotkey("\+esc", Sair_app)
keyboard.add_hotkey("\+2", ModoBP)
keyboard.add_hotkey("\+3",Botao_esquerda_direita)

tela.mainloop()

# pyinstaller --onefile AutoCleker.py