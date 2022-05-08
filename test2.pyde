partList = []
numbers = 2000
noiseScale = 800 #噪声规模，放在分母的参数调整噪声函数的读取
noiseStrenth = 90#噪声强度，调整噪声值变化剧烈程度（因为noise返回值为0-1）
radius = 125#半径大小

def setup():
    size(500,500)
    pixelDensity(2)
    noStroke()
    blendMode(ADD)
    colorMode(HSB,360,100,100,60)
    newParticles()
    
def draw():
    for p in partList:
        p.move()
        p.show()
        
  
#重置粒子容器
def newParticles():
    background(0)
    del partList[:]#清空列表
    for i in range(numbers):#填充列表
        partList.append(Particle())
        
def mousePressed():
    newParticles()
        
#----------------------------------------

class Particle:
    pos = PVector(0,0)
    angle = 0
    count = 0
    
    def __init__(self):
        self.pos = PVector(random(width),random(height))
        
    def move(self):
        if self.inCircle():
            self.angle = noise(self.pos.x/noiseScale , self.pos.y/noiseScale , self.count) * noiseStrenth
        else:
            self.angle = noise(self.pos.x/noiseScale , self.pos.y/noiseScale ) * noiseStrenth
        self.pos.x += cos(self.angle)
        self.pos.y += sin(self.angle)
        
        if self.pos.x>width or self.pos.x<0 or self.pos.y>height or self.pos.y<0 :
            self.hitWall()
        
        self.count += 0.002
        
    def show(self):
        fill( map(noise(self.angle),0,1,140,360), 60 , 60 ,15)
        circle(self.pos.x, self.pos.y, 1)
    
    def hitWall(self):
        self.pos = PVector(random(width),random(height))
        
    def inCircle(self):
        ret = False
        if( dist(self.pos.x , self.pos.y , width/2 , height/2) < radius ):
            ret = True
        return ret
