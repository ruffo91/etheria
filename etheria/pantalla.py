import threading
import pygame
from pygame.locals import *
import sys
import escenario


class pantalla(threading.Thread):
    
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
    
    # METODOS
    
    def salir(self):
        pygame.quit()
        sys.exit()
        
    def renderizar(self):
        self.escena.renderizar()
        pygame.display.flip()
    
    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    self.salir()
                
                if evento.type == KEYDOWN and evento.key == K_ESCAPE and self.getEstado() == "login":
                    self.salir()
            
            self.renderizar()
            self.reloj.tick(30)
        #self.run()
    
    # CONSTRUCTOR
    
    def __init__(self):
        threading.Thread.__init__(self) 
        
        self.setReloj(pygame.time.Clock())
        self.setActivo(False)
        
        pygame.init()
        self.setVentana(pygame.display.set_mode((1024, 768)))
        pygame.display.set_caption("Etheria")
        self.setEstado("login")
        
        datosEscena = {"textura":"images/escenario0.jpg", "x":"-500", "y":"-500", "velocidad":"5"}
        self.setEscena(escenario.escenario(datosEscena, self))
        self.getEscena().start()
        
        self.stoprequest = threading.Event()