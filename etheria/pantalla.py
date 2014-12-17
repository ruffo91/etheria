import threading
import pygame
from pygame.locals import *
import sys
import escenario
import player


class pantalla(threading.Thread):
    a=0
    # METODOS GET SET
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = str(estado)
        
    def getReloj(self):
        return self.reloj
    
    def setReloj(self, reloj):
        self.reloj = reloj
        
    def getActivo(self):
        return self.activo
    
    def setActivo(self, activo):
        self.activo = activo
        
    def getVentana(self):
        return self.ventana()
    
    def setVentana(self, ventana):
        self.ventana = ventana
        
    def getEscena(self):
        return self.escena
    
    def setEscena(self, escena):
        self.escena = escena
        
    def getPlayer(self):
        return self.player
    
    def setPlayer(self, player):
        self.player = player
    
    # METODOS
    
    def salir(self):
        pygame.quit()
        sys.exit()
        
    def renderizar(self):
        self.escena.renderizar()
        self.player.renderizar()
        pygame.display.flip()
    
    def run(self):
        #while True:
            
        """for evento in pygame.event.get():
            if evento.type == QUIT:
                self.salir()
            
            if evento.type == KEYDOWN and evento.key == K_ESCAPE and self.getEstado() == "login":
                self.salir()
        self.renderizar()
        self.reloj.tick(30)"""
        #self.run()
    
    # CONSTRUCTOR
    
    def __init__(self):
        threading.Thread.__init__(self) 
        
        maxWidth = 1024
        maxHeight = 768
        
        self.setReloj(pygame.time.Clock())
        
        pygame.init()
        self.setVentana(pygame.display.set_mode((maxWidth, maxHeight)))
        pygame.display.set_caption("Etheria")
        self.setEstado("login")
        
        datosEscena = {"textura":"images/escenario0.jpg", "x":"-500", "y":"-500", "velocidad":"5"}
        self.setEscena(escenario.escenario(datosEscena, self))
        self.getEscena().start()
        
        datosPlayer = {"nivel":"1","vida":"100", "textura":"images/pj01.png", "x":str(maxWidth/2), "y":str(maxHeight/2), "o":"0", "mapa":"0"}
        self.setPlayer(player.player(datosPlayer, self))
        self.getPlayer().start()
        
        self.stoprequest = threading.Event()
        
        while True:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    self.salir()
                
                if evento.type == KEYDOWN and evento.key == K_ESCAPE and self.getEstado() == "login":
                    self.salir()
                    
                if evento.type == KEYDOWN and (evento.key == K_DOWN or evento.key == K_s):
                    self.escena.setAndando0(True)
                if evento.type == KEYUP and (evento.key == K_DOWN or evento.key == K_s):
                    self.escena.setAndando0(False)
                    
                if evento.type == KEYDOWN and (evento.key == K_DOWN or evento.key == K_a):
                    self.escena.setAndando1(True)
                if evento.type == KEYUP and (evento.key == K_DOWN or evento.key == K_a):
                    self.escena.setAndando1(False)
                    
                if evento.type == KEYDOWN and (evento.key == K_DOWN or evento.key == K_w):
                    self.escena.setAndando2(True)
                if evento.type == KEYUP and (evento.key == K_DOWN or evento.key == K_w):
                    self.escena.setAndando2(False)
                    
                if evento.type == KEYDOWN and (evento.key == K_DOWN or evento.key == K_d):
                    self.escena.setAndando3(True)
                if evento.type == KEYUP and (evento.key == K_DOWN or evento.key == K_d):
                    self.escena.setAndando3(False)
                    
            self.renderizar()
            self.reloj.tick(30)