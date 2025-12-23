import tkinter as tk
import threading
import pyautogui
import time

tela = tk.Tk()
tela.geometry("300x200")
tela.title("Auto Cliker")

click = False
situacao = False

def auto_cliker():
    global click
    while click:
        pyautogui.leftClick()
        time.sleep(1)

def iniciar():
    global click, situacao
    if not situacao:
        click = True
        situacao = True
        atualizar_status()
        threading.Thread(target=auto_cliker, daemon=True).start()

def parar():
    global click, situacao
    click = False
    situacao = False
    atualizar_status()

def atualizar_status():
    if situacao:
        label_status.config(text="Status: LIGADO", fg="green")
    else:
        label_status.config(text="Status: DESLIGADO", fg="red")


titulo = tk.Label(tela, text="Auto Cliker\nVersão:001")
titulo.grid(row=0, column=0, columnspan=2, pady=5)

label_status = tk.Label(tela, text="Status: DESLIGADO", fg="red", font=("Arial", 12))
label_status.grid(row=1, column=0, columnspan=2, pady=5)

botao_iniciar = tk.Button(tela, text="Iniciar", command=iniciar)
botao_iniciar.grid(row=2, column=0, padx=10, pady=10)

botao_sair = tk.Button(tela, text="Sair", command=quit)
botao_sair.grid(row=2, column=1, padx=10, pady=10)

botao_parar = tk.Button(tela, text="Parar", command=parar)
botao_parar.grid(row=3, column=0, columnspan=2, pady=10)

tela.mainloop()

import tkinter as tk
import threading
from tkinter import Frame

import pyautogui
import time


tela = tk.Tk()
tela.geometry("250x200")
tela.title("Auto Cliker")

click = True
situacao = False

def auto_cliker():
    global click
    while click:
        pyautogui.leftClick()
        time.sleep(1)

def iniciar():
    global click,situacao
    if not situacao:
        click = True
        situacao = True
        atualizar_status()
        threading.Thread(target=auto_cliker,daemon=True,).start()

def parar():
    global click,situacao
    click = False
    situacao = False
    atualizar_status()

def atualizar_status():
    if situacao:
        label_status.config(text="Status: LIGADO", fg="green")
    else:
        label_status.config(text="Status: DESLIGADO", fg="red")

def parar_fora(event=None):
    if situacao:
        parar()
    else:
        iniciar()

tela.bind("<9>",parar_fora )
tela.bind('<0>',quit)


titulo = tk.Label(text="Auto Cliker\nVersão:001")
titulo.grid(row=0,column=2,pady=10,padx=10)

area1 = Frame(master=None)
area1.grid(column=2,pady=5,padx=5)

label_entrada = tk.Label(area1,text='1')
label_entrada.grid(side='left')

entrada = tk.Entry(area1)
entrada.grid()





label_status = tk.Label(text="Status: DESLIGADO", fg="red", font=("Arial", 9))
label_status.grid(row=2,column=2,pady=10,padx=10)

botao_iniciar = tk.Button(text="Iniciar",command=iniciar)
botao_iniciar.grid(row=2,column=0,pady=10,padx=10)


botao_parar = tk.Button(text="Parar",command=parar)
botao_parar.grid(row=2,column=3,pady=10,padx=5)

botao_sair = tk.Button(text="Sair",command=quit)
botao_sair.grid(row=3,column=2,pady=10,padx=10)



tela.mainloop()