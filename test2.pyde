partList = [] #粒子集合
circList = [] #圆集合
partNums = 6000 #粒子数量
cirNums = 6 #圆数量
noiseScale = 800 #噪声规模，放在分母的参数调整噪声函数的读取
noiseStrenth = 90 #噪声强度，调整噪声值变化剧烈程度（因为noise返回值为0-1）
radius = 220 #中心圆半径大小
step = 0.8

def setup():
    size(1000,1000)
    # pixelDensity(2)
    blendMode(ADD)
    noStroke()
    colorMode(HSB,360,100,100,100)
    initialize()
    
def draw():
    for p in partList:
        p.move()
        p.show()
        
  
#重置粒子容器
def newParticles():
    del partList[:]#清空列表
    for i in range(partNums):#填充列表
        partList.append(Particle())
    

def newCircles():
    del circList[:]#清空列表
    count = 0
    while count < cirNums:
        judge = True
        j = Circle() #新建圆对象
        for k in circList:
            if dist(j.center.x , j.center.y , k.center.x , k.center.y) < j.r+k.r:
                judge = False
        if judge:
            circList.append(j)
        count+=1
    
    
def initialize():
    background(0)
    noiseSeed(frameCount)
    newParticles()
    newCircles()
    
def mousePressed():
    count = 1
    for k in circList:
        count += 1
    print(count)
    initialize()
    
#------------------------------------------------------------------
class Circle:
    center = PVector(0,0)
    r = 0
    
    def __init__(self):
        self.r = 100 + random(100);
        self.center = PVector(random(width),random(height))
        

class Particle:
    pos = PVector(0,0)
    angle = 0
    count = 0
    
    def __init__(self):
        self.pos = PVector(random(width),random(height))
        
    def move(self):
        if self.inCircle():
            self.angle = noise(self.pos.x/noiseScale , self.pos.y/noiseScale , self.count) * 50
        else:
            self.angle = noise(self.pos.x/noiseScale , self.pos.y/noiseScale ) * noiseStrenth
        self.pos.x += cos(self.angle) * step
        self.pos.y += sin(self.angle) * step
        if self.pos.x>width or self.pos.x<0 or self.pos.y>height or self.pos.y<0 :
            self.hitWall()
        self.count += 0.001
        
    def show(self):
        fill( map(noise(self.angle),0,1,140,360), 60 , 60 ,15)
        circle(self.pos.x, self.pos.y, 1)
    
    def hitWall(self):
        self.pos = PVector(random(width),random(height))
        
    def inCircle(self):
        ret = False
        for c in circList:
            if dist(self.pos.x , self.pos.y , c.center.x , c.center.y) < c.r :
                ret = True
        return ret
    
        # for c in circList:
        #     if( dist(self.pos.x , self.pos.y , c.center.x , c.center.y ) < c.r ):
        #         ret = False
        # return ret
