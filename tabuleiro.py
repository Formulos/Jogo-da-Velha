# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:59:08 2016

@author: Paulo Tozzo
"""

import tkinter as tk
from jogo import Jogo


class Tabuleiro:
    
    def __init__(self):
        self.Jogo = Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x350+350+150")
        
    #linhas e colunas
        for i in range (4):
            self.window.rowconfigure(i,minsize = 100,weight=1)
        for j in range(3):
            self.window.columnconfigure(j,minsize = 100,weight=1)
        self.button= []
        
    #label
        self.label = tk.Label(self.window)
        self.label.configure(font="Courier 14 bold")
        self.label.grid(row=3, column=0, columnspan=3, sticky="n")
        self.label.configure(text="Courier 20 bold")


    #botão
        button= self.button
        for i in range(3):
            for j in range(3):
                button.append(tk.Button(self.window))
                button[-1].numero= 3*i+j
                button[-1].configure(command= lambda numero= button[-1].numero: self.botão_apertado(numero))
                button[-1].configure(text="")
                button[-1].grid(row=i, column=j,sticky="nsew")



    def botão_apertado(self, x):
        #print(x)
        self.Jogo.recebe_jogada(x)
        lista = self.Jogo.devolve_resultados()
        #print(lista)
        #print(len(lista))
        self.button[x].configure(text=lista[x])
        print(lista[-1])
        
        self.label.config(text = lista[-1])
        
    def iniciar(self):
        self.window.mainloop()


app = Tabuleiro()
app.iniciar()