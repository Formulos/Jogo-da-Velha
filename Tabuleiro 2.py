# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:59:08 2016

@author: Paulo
"""

import tkinter as tk

class tabuleiro:
    
    def __init__(self):
    #linhas e colunas
        self.window = tk.Tk()
        self.window.geometry("500x400+350+150")
        for i in range (4):
            self.window.rowconfigure(i, weight=1)
        for j in range(3):
            self.window.columnconfigure(j, weight=1)
        self.button= []
        
    #botão
        button= self.button
        for i in range(3):
            for j in range(3):
                button.append(tk.Button(self.window))
                button[-1].numero= 3*i+j
                #button[-1].configure(command= )
                button[-1].grid(row=i, column=j,sticky="nsew")
                
    #caixa de texto      
        self.conteudo_label = tk.StringVar()
        label = tk.Label(self.window)
        label.configure(textvariable=self.conteudo_label)
        label.configure(font="Courier 20 bold")
        label.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def botão_apertado(self, x):
        print(x)
        
    def iniciar(self):
        self.window.mainloop()


app = tabuleiro()
app.iniciar()