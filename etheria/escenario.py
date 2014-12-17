import pygame
import threading

class escenario(threading.Thread):
    
    # METODOS GET SET
    
    def getPantalla(self):
        return self.pantalla
    
    def setPantalla(self, pantalla):
        self.pantalla = pantalla
    
    def getTextura(self):
        return self.textura
    
    def setTextura(self, textura):
        self.textura = str(textura)
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = int(x)
        
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = int(y)
        
    def getO(self):
        return self.o
    
    def setO(self, o):
        self.o = o
    
    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = int(velocidad)
        
    def getAndando(self):
        return self.andando
        
    def setAndando(self, andando):
        self.andando = andando
        
    def getSprite(self):
        return self.sprite
    
    def setSprite(self, sprite):
        self.sprite = sprite
    
    
    # METODOS
    
    def teletransportar(self, x, y):
        self.setX(x)
        self.setY(y)
        
    def andar(self):
        if self.getAndando():
            if(self.getO() == 0):
                self.setY(self.getY() + self.getVelocidad())
            if(self.getO() == 1):
                self.setX(self.getX() + self.getVelocidad())
            if(self.getO() == 2):
                self.setY(self.getY() - self.getVelocidad())
            if(self.getO() == 3):
                self.setX(self.getX() - self.getVelocidad())
                
            self.renderizar()
            
    def cargarTextura(self):
        self.setSprite(pygame.image.load(str(self.getTextura())))
    
    def renderizar(self):
        self.pantalla.ventana.fill((0,0,0))
        self.pantalla.ventana.blit(self.sprite, (self.getX(), self.getY()))
    
    def run(self):
        
        self.andar()
        self.renderizar()
        #self.renderizar()
        #self.run()
        
        
    # CONSTRUCTOR
    
    def __init__(self, datos, pantalla):
        threading.Thread.__init__(self) 
        self.setAndando(False)
        self.setTextura(datos["textura"])
        self.cargarTextura()
        self.teletransportar(datos["x"], datos["y"])
        self.setVelocidad(datos["velocidad"])
        self.setO(0)
        self.setPantalla(pantalla)
        
        self.stoprequest = threading.Event()
        
        