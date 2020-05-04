import pygame, threading
import time
import numpy as np
import random
import math



class Pygame():
    # Создаём игровое поле
    def __init__(self):
        pygame.init()
        info=pygame.display.Info()
        self.razmerX=int(info.current_w)
        self.razmerY=int(info.current_h)
        print(info.current_w)
        print(info.current_h)
        self.gameScreen = pygame.display.set_mode((self.razmerX, self.razmerY), pygame.FULLSCREEN | pygame.NOFRAME)
        self.gameScreen.fill((0,0,0)) 
        self.VerhRok=-20
        self.LevRok=-5
        self.RighRok=5
        self.NizRok=0
        self.LeftFlame=-3
        self.RightFlame=3
        self.RandomX=0
        self.RandomY=0
        self.o=0;    
        self.l=False
        self.r=False
        self.n=False
        self.w=False


    # Обновляем экран
    def Update(self):
        pygame.display.flip()

    def Random(self):
        self.RandomX=random.randint(-1,1)
        self.RandomY=random.randint(-1,1)

    def line(self,tm1,tm2,tm3,tm4,color,rotate,xpos,ypos):

        pygame.draw.line(self.gameScreen, color, [xpos+(((tm1)-xpos) * math.cos(math.radians(rotate)) + ((tm2)-ypos) * math.sin(math.radians(rotate))), ypos+(((tm2)-ypos) * math.cos(math.radians(rotate)) - ((tm1)-xpos) * math.sin(math.radians(rotate)))],[xpos+(((tm3)-xpos) * math.cos(math.radians(rotate)) + ((tm4)-ypos) * math.sin(math.radians(rotate))), ypos+(((tm4)-ypos) * math.cos(math.radians(rotate)) - ((tm3)-xpos) * math.sin(math.radians(rotate)))])
            

    def DrawRocket(self, x, y, rotate, flame, color=(255, 255, 255)):
        tmp1=x
        tmp2=y+self.VerhRok
        tmp3=x+self.LevRok
        tmp4=y+self.NizRok
        self.line(tmp1,tmp2,tmp3,tmp4,color,rotate,x,y)
        tmp1=x     
        tmp2=y+self.VerhRok     
        tmp3=x+self.RighRok      
        tmp4=y+self.NizRok
        self.line(tmp1,tmp2,tmp3,tmp4,color,rotate,x,y)
        tmp1=x+self.LevRok
        tmp2=y+self.NizRok     
        tmp3=x+self.RighRok      
        tmp4=y+self.NizRok
        self.line(tmp1,tmp2,tmp3,tmp4,color,rotate,x,y)
        tmp1=x+self.LeftFlame
        tmp2=y+self.NizRok 
        tmp3=x+self.RandomX  
        tmp4=y+flame+self.RandomY
        self.line(tmp1,tmp2,tmp3,tmp4,color,rotate,x,y)
        tmp1=x+self.RightFlame
        tmp2=y+self.NizRok 
        tmp3=x+self.RandomX  
        tmp4=y+flame+self.RandomY
        self.line(tmp1,tmp2,tmp3,tmp4,color,rotate,x,y)
         
    def DrawPlanet(self,mas):
        for i in range(len(mas)-1):
            
            pygame.draw.line(self.gameScreen, (255,255,255),[i*(self.razmerX/28),self.razmerY-(mas[i]*(self.razmerY/28))],[(i+1)*(self.razmerX/28),self.razmerY-(mas[i+1]*(self.razmerY/28))])


    def demon(self):


        #while run:
        
        for event in pygame.event.get():
            #print("   a")

            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    self.l=1
                    print("1")
                else:
                    self.l=0
                if event.key == pygame.K_RIGHT:
                  self.r=1
                  print("2")
                else:
                    self.r=0                  
                if event.key == pygame.K_UP:
                  self.w=1
                  print("3")
                else:
                    self.w=0                  
                if event.key == pygame.K_DOWN:
                  self.n=1
                  print("3")
                else:
                    self.n=0                  
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            else:
                self.l=0 
                self.r=0             
                self.n=0 
                self.w=0 

    def R(self):
        
        return self.r

    def W(self):
        
        return self.w    
    def L(self):
        
        return self.l

    def N(self):
        
        return self.n  

    def q(self):
        pygame.quit()


class Rocket():
    def __init__(self):
        self.X=300
        self.Y=300
        self.rotate=0
        self.flame=0
        self.speedX=0
        self.speedY=0

    def Fizics(self,r,l,w,n):
        self.rotate+=(-1*r)+l
        self.flame+=((-1*n)+w)
        if(self.flame>20):
            self.flame=20
        if(self.flame<0):
            self.flame=0

        self.speedX+=(self.flame/50000)*math.sin(math.radians((-1*self.rotate)%360))
        self.speedY-=(self.flame/50000)*math.cos(math.radians((-1*self.rotate)%360))-(1.8/10000)
        self.X+=self.speedX
        self.Y+=self.speedY


class Neyro(Rocket):
    def __init__(self, neyroVhod, neyroSkrut, neyroVuh):
        super().__init__()
        self.neyroVhod = neyroVhod + 1
        self.neyroSkrut = neyroSkrut
        self.neyroVuh = neyroVuh

        self.Vhodmass = np.array([1.0 for i in range(self.neyroVhod)])
        self.Skrutmass = np.array([1.0 for i in range(self.neyroSkrut)])
        self.Vuhmass = np.array([1.0 for i in range(self.neyroVuh)]) 
        
        #self.wi = makeMatrix(self.ni, self.nh)
        #self.wo = makeMatrix(self.nh, self.no)
        self.coofIn = np.ones((self.neyroVhod, self.neyroSkrut))
        self.coofOut = np.ones((self.neyroSkrut, self.neyroVuh))

        for i in range(self.neyroVhod):
            for j in range(self.neyroSkrut):
                self.coofIn[i][j] = (random.random()-0.5)*2

        for i in range(self.neyroSkrut):
            for j in range(self.neyroVuh):
                self.coofOut[i][j] = (random.random()-0.5)*2 

    def sigmoid(self,x):
        return math.tanh(x)

    def update(self, inputs):
        for i in range(self.neyroVhod):
            #self.Vhodmass[i] = self.sigmoid(inputs[i])
            self.Vhodmass[i] = inputs[i]

        print(self.Vhodmass)
        for j in range(self.neyroSkrut):
            sum = 0.0
            for i in range(self.neyroVhod):
                sum = sum + self.Vhodmass[i] * self.coofIn[i][j]
            self.Skrutmass[j] = self.sigmoid(sum)
        print(self.Skrutmass)

        for k in range(self.neyroVuh):
            sum = 0.0
            for j in range(self.neyroSkrut):
                sum = sum + self.Skrutmass[j] * self.coofOut[j][k]
            self.Vuhmass[k] = self.sigmoid(sum)
        print(self.Vuhmass)

        return self.Vuhmass





class Planet():
    def __init__(self):
        self.p = np.array([1 for i in range(28)])
        for i in range(28):
            self.p[i]=random.randint(3,10)
    
    def Exit(self,X,Y,Rotate,Speed,razmerX,razmerY):
        if(Y>=int(razmerY-self.p[int(X/(razmerX/28))]*(razmerY/28)) and abs(Speed)<100 and abs((Rotate%360)-math.degrees(math.atan2((razmerY-int(self.p[int(X/(razmerX/28)+1)]*(razmerY/28)))-(razmerY-int(self.p[int(X/(razmerX/28))]*(razmerY/28))), int((X/(razmerX/28)+1)*razmerX/28)-int((X/(razmerX/28))*razmerX/28))))<30):
            return 1
        elif(Y>=int(razmerY-self.p[int(X/(razmerX/28))]*(razmerY/28))):
            return 2
        else:
            return 0



r=0
pyg=Pygame()
rock=Rocket()
plan=Planet()
ney=Neyro(8,5,4)
ney.update([1.0,0.0,-1.0,0.31,1.0,-0.4,-0.8,-1.0,0.0])
plam=0
while(True):
    pyg.DrawRocket(rock.X,rock.Y,rock.rotate,rock.flame)
    pyg.DrawPlanet(plan.p)
    pyg.Update()
    pyg.DrawRocket(rock.X,rock.Y,rock.rotate,rock.flame,(0,0,0))
    pyg.Random()
    pyg.demon()
    rock.Fizics(pyg.r,pyg.l,pyg.w,pyg.n)
    if(plan.Exit(rock.X,rock.Y,rock.rotate,rock.speedY,pyg.razmerX,pyg.razmerY)==1):
        print("OK")
        rock.X=700
        rock.Y=300
    elif(plan.Exit(rock.X,rock.Y,rock.rotate,rock.speedY,pyg.razmerX,pyg.razmerY)==2):
        rock.X=300
        rock.Y=300


    
    
























































# ((xdlina / 2) + (((zvezdu[i][0] - xroc) + (xdlina / 2)) * Math.cos(Math.toRadians(ugol)) +((zvezdu[i][1] - yroc) + (ydlina / 2)) * Math.sin(Math.toRadians(ugol)))), (int) ((ydlina / 2) +
#                                        (((zvezdu[i][1] - yroc) + (ydlina / 2)) * Math.cos(Math.toRadians(ugol)) - ((zvezdu[i][0] - xroc) +
#                                        (xdlina / 2)) * Math.sin(Math.toRadians(ugol))))












