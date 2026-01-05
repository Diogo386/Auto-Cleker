import tkinter as tk
import threading
from tkinter import Frame
import pyautogui
import time


tela = tk.Tk()
tela.geometry("280x200")
tela.title("Auto Cliker")

click = True
situacao = False


def auto_cliker():
    tempo = float(entrada_tempo.get())
    global click
    while click:
        pyautogui.leftClick()
        time.sleep(tempo)


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
        label_status.config(text="Status: LIGADO", fg="light green")
    else:
        label_status.config(text="Status: DESLIGADO", fg="red")

def parar_fora(event=None):
    if situacao:
        parar()
    else:
        iniciar()

tela.bind("<F2>",parar_fora )
tela.bind('<F3>',quit)


titulo = tk.Label(text="Auto Cliker\nVersão:001",font=("Arial", 10, "bold"))
titulo.pack()

area1 = Frame()
area1 ["pady"] = 5
area1["width"] = 5
area1.pack()

area2 = Frame()
area2 ["pady"] = 5
area2["width"] = 5
area2.pack()

area3 = Frame()
area3 ["pady"] = 5
area3["width"] = 5
area3.pack()

area4 = Frame()
area4 ["pady"] = 5
area4["width"] = 5
area4.pack()

label_entrada = tk.Label(area1,text='Tempo por click:',font=("Arial",10 ))
label_entrada.pack(side="left")

entrada_tempo = tk.Entry(area1)
entrada_tempo.pack()


label_status = tk.Label(area2,text="Status: DESLIGADO", fg="red",font=("Arial",10 ))
label_status.pack()

botao_iniciar = tk.Button(area3,text="Iniciar",command=iniciar)
botao_iniciar.pack(pady= 5,padx= 10,side="left")


botao_parar = tk.Button(area3,text="Parar",command=parar)
botao_parar.pack(pady= 5,padx=10,side="right")

botao_sair = tk.Button(area4,text="Sair",command=quit)
botao_sair.pack()



tela.mainloop()

# pyinstaller --onefile AutoCleker.py