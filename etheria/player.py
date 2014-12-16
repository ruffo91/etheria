class player:
    
    nivel = 0;
    vida = 0;
    textura = ""
    posX = 0
    posY = 0
    posO = 0
    mapa = 0
    velocidad = 0
    
    # DEFINICION DE LOS GET SET
    
    def getVida(self):
        return self.vida
    
    def setVida(self, vida):
        self.vida = vida
        
        
    def getNivel(self):
        return self.nivel
    
    def setNivel(self, nivel):
        self.nivel = nivel
        
        
    def getTextura(self):
        return self.textura
    
    def setTextura(self, textura):
        self.textura = textura
        
        
    def getPosX(self):
        return self.posX
    
    def setPosX(self, posX):
        self.posX = posX
        
    
    def getPosY(self):
        return self.posY
    
    def setPosY(self, posY):
        self.posY = posY
        
        
    def getPosO(self):
        return self.posO
    
    def setPosO(self, posO):
        self.posO = posO
        
        
    def getMapa(self):
        return self.mapa
    
    def setMapa(self, mapa):
        self.mapa = mapa
        
        
    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
        
    
    # METODOS
    
    def mover(self, posO, velocidad):
        # MOVERSE AL SUR
        if posO == 0: 
            self.setY(self.getY() - velocidad)
        # MOVERSE AL SUROESTE
        elif posO == 1:
            self.setX(self.getX() - velocidad)
            self.setY(self.getY() - velocidad)
        # MOVERSE AL OESTE
        elif posO == 2:
            self.setX(self.getX() - velocidad)
        # MOVERSE AL NOROESTE
        elif posO == 3:
            self.setX(self.getX() - velocidad)
            self.setY(self.getY() + velocidad)
        # MOVERSE AL NORTE
        elif posO == 4:
            self.setY(self.getY() + velocidad)
        # MOVERSE AL NORESTE
        elif posO == 5:
            self.setX(self.getX() + velocidad)
            self.setY(self.getY() + velocidad)
        # MOVERSE AL ESTE
        elif posO == 6:
            self.setX(self.getX() + velocidad)
        # MOVERSE AL SUROESTE
        elif posO == 7:
            self.setX(self.getX() + velocidad)
            self.setY(self.getY() - velocidad)
            
        # ASIGNAMOS LA POSICION AL PLAYER
        self.setPosO(posO)
            
    
    def teletransportar(self, posX, posY, posO, mapa):
        self.setPosX(posX)
        self.setPosY(posY)
        self.setPosO(posO)
        self.setMapa(mapa)
        
        
    # CONSTRUCTOR
    
    def __init__(self):
        self.setNivel(1)
        self.setvida(100)
        self.setTextura("")
        self.teletransportar(0, 0, 0, 0)
        
        