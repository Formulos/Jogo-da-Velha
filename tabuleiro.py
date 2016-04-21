# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:59:08 2016

@author: Paulo Tozzo
"""

import tkinter as tk
from Jogo import Jogo


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
        self.conteudo_label = tk.StringVar()
        self.label.configure(textvariable=self.conteudo_label)
        self.label.configure(font='Courier 20 bold')
        self.label.configure(text= 'teste')
        self.label.grid(row=4, column=0,columnspan=3, padx=20, sticky="s")
        
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
        print(x)
        self.Jogo.recebe_jogada(x)
        lista = self.Jogo.devolve_resultados()
        #self.conteudo_label.set(self.conteudo_caixa_texto.get(lista[-1]))
        self.button[x].configure(text=lista[x])
        
    def iniciar(self):
        self.window.mainloop()


app = Tabuleiro()
app.iniciar()