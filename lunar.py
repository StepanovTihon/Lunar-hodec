import pygame, threading
import time
import numpy as np
import random
import math
import time as tm


class Pygame():
    # Создаём игровое поле
    def __init__(self):
        pygame.init()
        info=pygame.display.Info()
        self.razmerX=int(info.current_w)
        self.razmerY=int(info.current_h)
        #print(info.current_w)
        #print(info.current_h)
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
    def Update(self,tmp,top):
        font = pygame.font.Font(None, 80)
        text = font.render(str(tmp)+"\n"+str(top), True, [255, 255, 255])
        textpos = (300, 800)

        self.gameScreen.blit(text, textpos)
        pygame.display.flip()
        font = pygame.font.Font(None, 80)
        text = font.render((str(tmp)+"\n"+str(top)), True, [0, 0, 0])
        textpos = (300, 800)

        self.gameScreen.blit(text, textpos)

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

    def Drawline(self,y):
        pygame.draw.line(self.gameScreen, (255,255,255),[0,800],[1920,800])

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
                    #print("1")
                else:
                    self.l=0
                if event.key == pygame.K_RIGHT:
                  self.r=1
                  #print("2")
                else:
                    self.r=0                  
                if event.key == pygame.K_UP:
                  self.w=1
                  #print("3")
                else:
                    self.w=0                  
                if event.key == pygame.K_DOWN:
                  self.n=1
                  #print("3")
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
        self.X=1920/2+random.randint(-81,81)
        self.Y=800/2+random.randint(-40,40)
        self.rotate=0
        self.flame=0.0
        self.speedX=0
        self.speedY=0
        self.fuel=3000.0
    def Fizics(self,r,l,w,n):
        self.rotate+=((-1*r)+l) *3.0
        self.flame+=((-1*n)+w)*5
        if(self.flame>20):
            self.flame=20
        if(self.flame<0):
            self.flame=0
        self.fuel-=self.flame
        if(self.fuel<0):
            self.flame=0
        self.speedX+=(self.flame/100)*math.sin(math.radians((-1*self.rotate)%360))
        self.speedY-=(self.flame/100)*math.cos(math.radians((-1*self.rotate)%360))-(1.8/50)
        self.X+=self.speedX
        self.Y+=self.speedY


class Neyro(Rocket):
    def __init__(self, neyroVhod, neyroSkrut, neyroVuh):
        super().__init__()
        self.neyroVhod = neyroVhod + 1
        self.neyroSkrut = neyroSkrut
        self.neyroVuh = neyroVuh
        self.time=0
        self.down= np.array([1.0 for i in range(4)])
        self.dead=0
        self.otklon=0
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

        #print(self.Vhodmass)
        for j in range(self.neyroSkrut):
            sum = 0.0
            for i in range(self.neyroVhod):
                sum = sum + self.Vhodmass[i] * self.coofIn[i][j]
            self.Skrutmass[j] = self.sigmoid(sum)
        #print(self.Skrutmass)

        for k in range(self.neyroVuh):
            sum = 0.0
            for j in range(self.neyroSkrut):
                sum = sum + self.Skrutmass[j] * self.coofOut[j][k]
            self.Vuhmass[k] = self.sigmoid(sum)
        
        for i in range(4):
            if(self.Vuhmass[i]>0):
                self.down[i]=1
            else:
                self.down[i]=0

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


class Generic():
    def __init__(self,quantity,pyg):
        self.pyg=pyg
        self.pocolenie=0
        self.vhod=9
        self.skrut=28
        self.selo=0
        self.top=0
        self.vuh=4
        self.personQuantity=quantity
        self.persons = np.array([Neyro(self.vhod, self.skrut,  self.vuh) for i in range(self.personQuantity)]) 


    def check(self):
        deads=0
        while(deads<self.personQuantity):
            for i in range(self.personQuantity):
                if(self.persons[i].dead==0):
                    if(self.pocolenie%1==0 ):
                      self.pyg.Drawline(800)
                      self.pyg.DrawRocket(self.persons[i].X,self.persons[i].Y,self.persons[i].rotate,self.persons[i].flame,(0,0,0))
                      self.persons[i].update([(self.persons[i].X)/1920,(1920-self.persons[i].X)/1920,(self.persons[i].Y/800),(800-self.persons[i].Y)/800,(self.persons[i].speedX)/1920,(self.persons[i].speedY)/800,(self.persons[i].rotate%360)/360,(self.persons[i].flame)/20,(random.random()-0.5)*2,(self.persons[i].fuel)/3000])
                    self.persons[i].Fizics(self.persons[i].down[0],self.persons[i].down[1],self.persons[i].down[2],self.persons[i].down[3])
                    if(self.pocolenie%1==0):
                      self.pyg.DrawRocket(self.persons[i].X,self.persons[i].Y,self.persons[i].rotate,self.persons[i].flame)
                      self.pyg.Update(self.pocolenie,self.selo)
                    if(self.persons[i].X>1920 or self.persons[i].Y>1920 or self.persons[i].X<0 or self.persons[i].Y<0):
                        self.persons[i].dead=1
                        deads+=1
                    else:
                        #self.persons[i].otklon=abs(self.persons[i].X-(1920/2))+abs(self.persons[i].Y-800)
                        #if( self.persons[i].otklon<200):
                        #    self.persons[i].time+=1
                        self.persons[i].time+=1
                        if(abs(self.persons[i].speedX<2)):
                            self.persons[i].time+=1
                        if(abs(self.persons[i].speedY<1)):
                            self.persons[i].time+=1                        
                        if(abs(self.persons[i].Y-800<100)):
                            self.persons[i].time+=1
                    if(800-self.persons[i].Y<15 and self.persons[i].speedY<1.5 and abs(self.persons[i].rotate%360)<30):
                        self.persons[i].dead=1
                        self.selo+=1
                        deads+=1
                        self.persons[i].time*=2
                    if(self.persons[i].Y>800):
                        deads+=1
                        self.persons[i].dead=1

                    

        for i in range(self.personQuantity):
            self.pyg.DrawRocket(self.persons[i].X,self.persons[i].Y,self.persons[i].rotate,self.persons[i].flame,(0,0,0))
                                
    def sort(self):
        person_tmp=Neyro(self.vhod, self.skrut,  self.vuh)

        for i in range(self.personQuantity):
            for j in range(self.personQuantity-i-1):
                if(self.persons[j].time > self.persons[j+1].time):
                    person_tmp = self.persons[j]
                    self.persons[j]=self.persons[j+1]
                    self.persons[j+1]= person_tmp
        self.top = self.persons[self.personQuantity-1].time

    def crossing(self,person1,person2):
        tmp_person=Neyro(self.vhod, self.skrut,  self.vuh)
        for i in range(person1.neyroVhod):
            for j in range(person1.neyroSkrut):
                tmp_person.coofIn[i,j]=(person1.coofIn[i,j]+person2.coofIn[i,j])/2

        for i in range(person1.neyroSkrut):
            for j in range(person1.neyroVuh):
                tmp_person.coofOut[i,j]=(person1.coofOut[i,j]+person2.coofOut[i,j])/2

        return tmp_person

    def mutation(self,person_mutant):

        for i in range(person_mutant.neyroVhod):
            for j in range(person_mutant.neyroSkrut):
                if(random.randint(0,100)<=30):
                    person_mutant.coofIn[i,j]+=(random.random()-0.5)*2

        for i in range(person_mutant.neyroSkrut):
            for j in range(person_mutant.neyroVuh):
                if(random.randint(0,100)<=30):
                    person_mutant.coofOut[i,j]+=(random.random()-0.5)*2

        
        return person_mutant

    def evolution(self):
        #self.pyg.Update(self.pocolenie,self.top)
        self.pocolenie+=1
        next_persons = np.array([Neyro(self.vhod, self.skrut,  self.vuh) for i in range(self.personQuantity)]) 
        for i in range(self.personQuantity):
            
            next_persons[i]=self.crossing(self.persons[int(random.random()*(self.personQuantity/2)+(self.personQuantity/2))],
                                          self.persons[int(random.random()*(self.personQuantity/2)+(self.personQuantity/2))])
            next_persons[i]=self.mutation(next_persons[i])
            
        next_persons[0]=self.persons[self.personQuantity-1]
        next_persons[1]=self.persons[self.personQuantity-2]
        next_persons[0].dead=0
        next_persons[1].dead=0
        next_persons[0].X=1920/2+random.randint(-81,81)
        next_persons[1].X=1920/2+random.randint(-81,81)
        next_persons[0].Y=800/2+random.randint(-40,40)
        next_persons[1].Y=800/2+random.randint(-40,40)
        next_persons[0].rotate=0
        next_persons[1].rotate=0
        next_persons[0].speedX=0
        next_persons[1].speedX=0
        next_persons[0].speedY=0
        next_persons[1].speedY=0
        next_persons[0].time=0
        next_persons[1].time=0
        next_persons[0].fuel=3000.0
        next_persons[1].fuel=3000.0                             
        self.persons=next_persons


r=0
pyg=Pygame()
rock=Rocket()
plan=Planet()
gen=Generic(10,pyg)
#ney=Neyro(8,5,4)
#ney.update([1.0,0.0,-1.0,0.31,1.0,-0.4,-0.8,-1.0,0.0,1000.0])
plam=0
trig=1
while(True):
    
    gen.check()
    gen.sort()
    gen.evolution()
    #pyg.DrawRocket(rock.X,rock.Y,rock.rotate,rock.flame)
    #pyg.DrawPlanet(plan.p)
    #pyg.Update(0,rock.fuel)
    #pyg.DrawRocket(rock.X,rock.Y,rock.rotate,rock.flame,(0,0,0))
    #pyg.Random()
    #pyg.demon()
    #if(pyg.w==1):
    #    trig*=-1
    #rock.Fizics(pyg.r,pyg.l,pyg.w,pyg.n)

    tm.sleep(0.001)


    #if(plan.Exit(rock.X,rock.Y,rock.rotate,rock.speedY,pyg.razmerX,pyg.razmerY)==1):
    #    print("OK")
    #    rock.X=700
    #    rock.Y=300
    #elif(plan.Exit(rock.X,rock.Y,rock.rotate,rock.speedY,pyg.razmerX,pyg.razmerY)==2):
    #    rock.X=300
    #    rock.Y=300


    
    
































































