# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:01:27 2016

@author: Alexandre Young
"""

class Jogo:
    
    def __init__(self):
        self.turno="X"
        self.turnospassados= 0
        self.tabuleiro=[]
        self.status=-1
        for i in range(9):
            self.tabuleiro.append("")
        #
        
    def muda_turno(self):
        if self.turno == "X":
            self.turno= "O"
        else:
            self.turno= "X"
    #
    
    def recebe_jogada(self, square):
        if self.tabuleiro[square] == "" and self.status == -1:
            self.tabuleiro[square]= self.turno
            self.muda_turno()
            self.turnospassados+= 1
            self.status= self.verifica_ganhador()
        elif self.status != -1:
            self.limpa_jogadas()
    #
            
    def verifica_ganhador(self):
        if self.turnospassados >= 5:
        
            tabuleiro= self.tabuleiro        
        
            for i in range(3):
                #checa horizontais
                linha=tabuleiro[i*3]+tabuleiro[i*3+1]+tabuleiro[i*3+2]
                if linha == "XXX" or linha == "OOO":
                    break
                
                #checa verticais
                linha=tabuleiro[i]+tabuleiro[i+3]+tabuleiro[i+6]
                if linha == "XXX" or linha == "OOO":
                    break
                
                if i == 2:
                    #checa diagonais
                    linha=tabuleiro[0]+tabuleiro[4]+tabuleiro[8]
                    if linha == "XXX" or linha == "OOO":
                        break
                    
                    linha=tabuleiro[2]+tabuleiro[4]+tabuleiro[6]
                #   
            #
            if linha == "XXX":
                return 1 #vitoria X
                
            if linha == "OOO":
                return 2 #vitoria O
                
            if self.turnospassados == 9:
                return 0 #empate
        #
        return -1 #nada
        
    def devolve_resultados(self):
        output=[]
        
        for i in self.tabuleiro:
            output.append(i)
        
        output.append("")
        if self.status == -1:
            output[-1]+= "Próxima jogada: "+self.turno
        elif self.status >= 1:
            self.muda_turno()
            output[-1]+= "Vitória de "+self.turno+". Parabéns!"
            self.muda_turno()
        else:
            output[-1]+="Empate!"
            
        return output
    #
        
    def limpa_jogadas(self):
        self.status= -1
        self.turnospassados= 0
        self.tabuleiro=[]
        for i in range(9):
            self.tabuleiro.append("")
        #
#