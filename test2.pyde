partList = []
numbers = 200
noiseScale = 800 #噪声规模，放在分母的参数调整噪声函数的读取
noiseStrenth = 10#噪声强度，调整噪声值变化剧烈程度（因为noise返回值为0-1）

def setup():
    size(500,500)
    pixelDensity(2)
    noStroke()
    fill(22,221,220)
    # blendMode(ADD)
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
        print("Hello")
        
def mousePressed():
    newParticles()
        
#----------------------------------------

class Particle:
    pos = PVector(0,0)
    angle = 0
    
    def __init__(self):
        self.pos = PVector(random(width),random(height))
        
    def move(self):
        self.angle = noise(self.pos.x/noiseScale , self.pos.y/noiseScale )*noiseStrenth
        self.pos.x += cos(self.angle)
        self.pos.y += sin(self.angle)
        
        
    def show(self):
        circle(self.pos.x, self.pos.y, 1)
    
    
        
