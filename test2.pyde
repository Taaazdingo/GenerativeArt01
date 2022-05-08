partList = []
numbers = 200

def setup():
    size(500,500)
    pixelDensity(2)
    noStroke()
    blendMode(ADD)
    newParticles()
    
def draw():
    fill(22,221,220)
    for p in partList:
        p.show()
  
#重置粒子容器
def newParticles():
    background(0)
    for i in range(numbers):
        # randomSeed
        partList.append(Particle())
        
def mousePressed():
    newParticles()
        
#----------------------------------------

class Particle:
    pos = PVector(0,0)
    angle = 0
    
    def __init__(self):
        self.pos.x = random(width)
        self.pos.y = random(height)
        self.angle = random(10)
        
    def show(self):
        circle(self.pos.x, self.pos.y, 10)
