import pygame, threading
import time
import numpy as np
import random
import math
import time as tm

class Pygame():
    def __init__(self):# Создаём игровое поле
        pygame.init()
        self.startmp=0
        self.tmp=int(time.time())
        info=pygame.display.Info()
        self.razmerX=int(info.current_w)
        self.razmerY=int(info.current_h)
        self.gameScreen = pygame.display.set_mode((self.razmerX,  self.razmerY), pygame.FULLSCREEN | pygame.NOFRAME)
        self.gameScreen.fill((0, 0, 0)) 
        self.upPointRocket=-20
        self.leftPointRocket=-5
        self.rightPointRocket=5
        self.downPointRocket=0
        self.leftPointFlame=-3
        self.rightPointFlame=3
        self.RandomX=0
        self.RandomY=0
        self.o=0;    
        self.l=False
        self.r=False
        self.n=False
        self.w=False
        self.u=0
        self.tmp2=0
        self.top=0

    def Update(self, tmp, top, ):# Обновляем экран

        if(time.time()-self.startmp>=1):

            self.u=time.time()
            self.tmp2=tmp
            self.top=top
            self.startmp=time.time()
            font = pygame.font.Font(None, 30)
            h=str(   int((int(self.u) - self.tmp)/3600))
            m=str(   int(int(int((int(self.u)) - self.tmp)%3600)/60))
            s=str(int(int(self.u) - self.tmp)%60)
            if(int(h)<10):
                h="0"+h
            if(int(m)<10):
                m="0"+m
            if(int(s)<10):
                s="0"+s        
            pygame.draw.rect(self.gameScreen, (0, 0, 0), (0, 900, 1920, 1080))
            text = font.render(" Поколение: " + str(self.tmp2)+"                                                    севших:"+str(self.top)+ "                                                                   время: " + h +" : "+ m +" : "+s, True, [255,  255,  255])

            textpos = (300,  900)
            self.gameScreen.blit(text,  textpos)
            pygame.display.flip()
        else:
            pygame.display.flip()

    def Random(self):#делает динамичный огонь
        self.RandomX=random.randint(-1, 1)
        self.RandomY=random.randint(-1, 1)

    def line(self, tm1, tm2, tm3, tm4, color, rotate, xpos, ypos):#рисует линию под любым углом

        pygame.draw.line(self.gameScreen,  color,  [xpos+(((tm1)-xpos) * math.cos(math.radians(rotate)) 
        + ((tm2)-ypos) * math.sin(math.radians(rotate))),  ypos+(((tm2)-ypos) * math.cos(math.radians(rotate)) 
        - ((tm1)-xpos) * math.sin(math.radians(rotate)))], [xpos+(((tm3)-xpos) * math.cos(math.radians(rotate)) 
        + ((tm4)-ypos) * math.sin(math.radians(rotate))),  ypos+(((tm4)-ypos) * math.cos(math.radians(rotate)) 
        - ((tm3)-xpos) * math.sin(math.radians(rotate)))])
            
    
    
    def DrawRocket(self,  x,  y,  rotate,  flame,  color=(255,  255,  255)):#Рисует рокету
        tmp1=x
        tmp2=y+self.upPointRocket
        tmp3=x+self.leftPointRocket
        tmp4=y+self.downPointRocket
        self.line(tmp1, tmp2, tmp3, tmp4, color, rotate, x, y)
        tmp1=x     
        tmp2=y+self.upPointRocket     
        tmp3=x+self.rightPointRocket      
        tmp4=y+self.downPointRocket
        self.line(tmp1, tmp2, tmp3, tmp4, color, rotate, x, y)
        tmp1=x+self.leftPointRocket
        tmp2=y+self.downPointRocket     
        tmp3=x+self.rightPointRocket    
        tmp4=y+self.downPointRocket
        self.line(tmp1, tmp2, tmp3, tmp4, color, rotate, x, y)
        tmp1=x+self.leftPointFlame
        tmp2=y+self.downPointRocket 
        tmp3=x+self.RandomX  
        tmp4=y+flame+self.RandomY
        if(color==(0,0,0)):
          self.line(tmp1, tmp2, tmp3, tmp4, color, rotate, x, y)
        else:
          self.line(tmp1, tmp2, tmp3, tmp4, (255,165,0), rotate, x, y)
        tmp1=x+self.rightPointFlame
        tmp2=y+self.downPointRocket 
        tmp3=x+self.RandomX  
        tmp4=y+flame+self.RandomY
        if(color==(0,0,0)):
          self.line(tmp1, tmp2, tmp3, tmp4, color, rotate, x, y)
        else:
          self.line(tmp1, tmp2, tmp3, tmp4, (255,165,0), rotate, x, y)


    def DrawR(self):
        print("u")
        pygame.draw.rect(self.gameScreen, (0, 0, 0), (0, 0, 1920, 1080))

    def Drawline(self, x, y,rx,ry):#рисует линию по y
        pygame.draw.line(self.gameScreen,  (255, 255, 255), [x, 800+rx], [y, 800+ry])

    def DrawPlanet(self, mas):#отрисовывает планету по массиву
        for i in range(len(mas)-1): 
            pygame.draw.line(self.gameScreen,  (255, 255, 255), [i*(self.razmerX/28), self.razmerY-(mas[i]*(self.razmerY/28))], 
            [(i+1)*(self.razmerX/28), self.razmerY-(mas[i+1]*(self.razmerY/28))])

    def demon(self):#управление с клавиатуры
       
        for event in pygame.event.get():         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    self.l=1
                else:
                    self.l=0
                if event.key == pygame.K_s:
                    self.r=1
                else:
                    self.r=0                  s
                if event.key == pygame.K_UP:
                    self.w=1
                else:
                    self.w=0                  
                if event.key == pygame.K_DOWN:
                    self.n=1
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
    def __init__(self):#Создаём рокету
        self.X=1920/2#+random.randint(-41, 41)
        self.Y=800/2#+random.randint(-20, 20)
        self.rotate=0
        self.flame=0.0
        self.speedX=0
        self.speedY=0
        self.fuel=3000.0

    def Fizics(self, r, l, w, n):#отробатываем физику
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
    def __init__(self,  neyroinput,  neyrohidden, neyrohidden2,  neyroexit, moon):#Создаём нейронку
        super().__init__()
        self.moon=moon 
        self.iznach=neyroinput + 1
        self.neyroinput = neyroinput + 1 + self.moon.razmer
        self.neyrohidden = neyrohidden
        self.neyrohidden2 = neyrohidden2
        self.neyroexit = neyroexit
        self.time=0
        self.pos=0
        self.down= np.array([1.0 for i in range(4)])
        self.dead=0
        self.inputmass = np.array([1.0 for i in range(self.neyroinput)])
        self.hiddenmass = np.array([1.0 for i in range(self.neyrohidden)])
        self.hiddenmass2 = np.array([1.0 for i in range(self.neyrohidden2)])
        self.exitmass = np.array([1.0 for i in range(self.neyroexit)]) 
        self.coofIn = np.ones((self.neyroinput,  self.neyrohidden))
        self.coofCentr = np.ones((self.neyrohidden,  self.neyrohidden2))
        self.coofOut = np.ones((self.neyrohidden2,  self.neyroexit))
        for i in range(self.neyroinput):
            for j in range(self.neyrohidden): 
                self.coofIn[i][j] = (random.random()-0.5)*2
        for i in range(self.neyrohidden):
            for j in range(self.neyrohidden2):
                self.coofCentr[i][j] = (random.random()-0.5)*2 
        for i in range(self.neyrohidden2):
            for j in range(self.neyroexit):
                self.coofOut[i][j] = (random.random()-0.5)*2 

    def sigmoid(self, x):#Активация
        return math.tanh(x)

    def update(self,  inputs):#нахождение выходов
        

        for i in range(self.neyroinput):
            if(i<self.iznach):
                self.inputmass[i] = inputs[i]
            else:
                self.inputmass[i]=self.moon.surface[i-self.iznach]

        for j in range(self.neyrohidden):
            sum = 0.0
            for i in range(self.neyroinput):
                sum = sum + self.inputmass[i] * self.coofIn[i][j]
            self.hiddenmass[j] = self.sigmoid(sum)
        for j in range(self.neyrohidden2):
            sum = 0.0
            for i in range(self.neyrohidden):
                sum = sum + self.hiddenmass[i] * self.coofCentr[i][j]
            self.hiddenmass2[j] = self.sigmoid(sum)
        for k in range(self.neyroexit):
            sum = 0.0
            for j in range(self.neyrohidden2):
                sum = sum + self.hiddenmass2[j] * self.coofOut[j][k]
            self.exitmass[k] = self.sigmoid(sum)
        for i in range(4):
            if(self.exitmass[i]>0):
                self.down[i]=1
            else:
                self.down[i]=0
        return self.exitmass

class PlanetG():
    def __init__(self):#Создаём планету
        self.surface = np.array([1 for i in range(28)])
        for i in range(28):
            self.surface[i]=random.randint(3, 10)
    
    def Exit(self, X, Y, Rotate, Speed, razmerX, razmerY):#Посадка
        if(Y>=int(razmerY-self.surface[int(X/(razmerX/28))]*(razmerY/28)) and abs(Speed)<100 and
         abs((Rotate%360)-math.degrees(math.atan2((razmerY-int(self.surface[int(X/(razmerX/28)+1)]*
         (razmerY/28)))-(razmerY-int(self.surface[int(X/(razmerX/28))]*(razmerY/28))),  int((X/(razmerX/28)+1)*
         razmerX/28)-int((X/(razmerX/28))*razmerX/28))))<30):
            return 1
        elif(Y>=int(razmerY-self.surface[int(X/(razmerX/28))]*(razmerY/28))):
            return 2
        else:
            return 0

class planet():
    def __init__(self):#Создаём планету
        self.razmer=3
        self.surface = np.array([0 for i in range(self.razmer)])
        for i in range(self.razmer):
            self.surface[i]=int(random.randint(0, 1))
        self.randoms = np.array([0 for i in range(self.razmer+1)])
        for i in range(self.razmer+1):
            if(i<self.razmer):
                if(self.surface[i]==1):
                    self.randoms[i]=int(random.randint(0, 5))

        self.X = np.array([0])
        self.Y = np.array([0])


    def Sozd(self):
        starttmpX=0
        tmpX=random.randint(10,40)
        starttmpY=0
        while(tmpX<1920):

            if(self.surface[int(tmpX/(1920/self.razmer))]==1):
                tmpY=random.randint(0,2)
            else:
                tmpY=random.randint(15,50)
            
            self.X=np.append(self.X,tmpX)
            self.Y=np.append(self.Y,tmpY)
            starttmpY=tmpY
            starttmpX=tmpX
            tmpX=starttmpX+random.randint(10,40)  
            

    def Draw(self,pyg):

        for i in range(len(self.X)-1):
            

            pyg.Drawline( self.X[i], self.X[i+1],self.Y[i] , self.Y[i+1])
        print("a")
            

class Generic():
    def __init__(self, quantity, pyg, moon):#Генетический алгоритм
        self.pyg=pyg
        self.generation=0
        self.input=9
        self.hidden=40
        self.hidden2=20
        self.landing=0
        self.exit=4
    
        self.moon=moon
        self.personQuantity=quantity
        self.persons = np.array([Neyro(self.input,  self.hidden,  self.hidden2,   self.exit, self.moon) for i in range(self.personQuantity)]) 

    def Save(self,plan):
        f = open("abc", "w")
        for i in range(self.personQuantity):
            for k in range(self.persons[i].neyroinput):
                for n in range(self.persons[i].neyrohidden): 
                    f.write(str(self.persons[i].coofIn[k][n])+"\n")
            for k in range(self.persons[i].neyrohidden):
                for n in range(self.persons[i].neyrohidden2):
                    f.write(str(self.persons[i].coofCentr[k][n])+"\n")
            for k in range(self.persons[i].neyrohidden2):
                for n in range(self.persons[i].neyroexit):
                    f.write(str(self.persons[i].coofOut[k][n])+"\n")
        for i in range(len(plan)):
            f.write(str(plan[i])+"\n")
        f.write(str(time.time()-pyg.tmp)+"\n")
        f.write(str(self.landing)+"\n")
        f.write(str(self.generation)+"\n")
        

        f.close()

    def load(self,plan,pyg):
        f = open("abc", "r")#.readline()
        for i in range(self.personQuantity):
            for k in range(self.persons[i].neyroinput):
                for n in range(self.persons[i].neyrohidden): 
                    self.persons[i].coofIn[k][n]=float(f.readline())
            for k in range(self.persons[i].neyrohidden):
                for n in range(self.persons[i].neyrohidden2):
                    self.persons[i].coofCentr[k][n]=float(f.readline())
            for k in range(self.persons[i].neyrohidden2):
                for n in range(self.persons[i].neyroexit):
                    self.persons[i].coofOut[k][n]=float(f.readline())
        for i in range(len(plan)):
            plan[i]=int(f.readline())
        
        pyg.tmp-=float(f.readline())
        self.landing=int(f.readline())
        self.generation=int(f.readline())


        f.close()
    def check(self):#Отбор
        deads=0
        while(deads<self.personQuantity):
            self.pyg.demon()
            if(self.pyg.r==1):
                self.Save(self.moon.surface)

            if(self.pyg.l==1):
                #self.moon.Sozd() 
                moon.__init__()
                self.load(self.moon.surface,self.pyg)
                self.pyg.DrawR()
                self.moon.Sozd()
                self.moon.Draw(self.pyg)

            for i in range(self.personQuantity):
                if(self.persons[i].dead==0):
                    if(self.generation%1==0 ):

                      self.pyg.DrawRocket(self.persons[i].X, self.persons[i].Y, self.persons[i].rotate, self.persons[i].flame, (0, 0, 0))
                      self.persons[i].update([(self.persons[i].X)/1920, (1920-self.persons[i].X)/1920, (self.persons[i].Y/800), 
                      (800-self.persons[i].Y)/800, (self.persons[i].speedX)/1920, (self.persons[i].speedY)/800, 
                      ((self.persons[i].rotate%360)-180)/360, (self.persons[i].flame)/20, (random.random()-0.5)*2, 
                      (self.persons[i].fuel)/3000])
                    self.persons[i].Fizics(self.persons[i].down[0], self.persons[i].down[1], 
                    self.persons[i].down[2], self.persons[i].down[3])
                    if(self.generation%1==0):
                        self.pyg.DrawRocket(self.persons[i].X, self.persons[i].Y, self.persons[i].rotate, self.persons[i].flame,(255,255,255))
                        self.pyg.Update(self.generation, self.landing)
                    if(self.persons[i].X>1920 or self.persons[i].X<0 or self.persons[i].Y<0):
                        self.persons[i].dead=1
                        deads+=1
                    else:
                        if(abs(self.persons[i].speedX<3)):
                            self.persons[i].time+=1
                        if(abs(self.persons[i].speedY<1)):
                            self.persons[i].time+=1               
                        if(abs(self.persons[i].Y-800)<250):
                            self.persons[i].time+=1
                        if(self.moon.surface[int(self.persons[i].X/(1920/self.moon.razmer))]==1):
                            self.persons[i].time+=2
                        else:
                            self.persons[i].time-=1
                        if(self.moon.surface[int(self.persons[i].X/(1920/self.moon.razmer))]==1 and 800-self.persons[i].Y<15 and abs(self.persons[i].speedY)<2 and abs(self.persons[i].rotate%360)<30):                        
                            self.persons[i].dead=1
                            self.landing+=1
                            deads+=1
                            self.persons[i].pos=1
                            self.persons[i].time=abs(self.persons[i].time)*20
                        if(self.persons[i].Y>800):
                            deads+=1
                            self.persons[i].dead=1
                else:
                    if(self.persons[i].pos==0):
                        self.pyg.DrawRocket(self.persons[i].X, self.persons[i].Y, self.persons[i].rotate, self.persons[i].flame,(255,0,0))
                    else:
                        self.pyg.DrawRocket(self.persons[i].X, self.persons[i].Y, self.persons[i].rotate, self.persons[i].flame,(0,255,0))

        for i in range(self.personQuantity):
            self.pyg.DrawRocket(self.persons[i].X, self.persons[i].Y, self.persons[i].rotate, self.persons[i].flame, (0, 0, 0))
                                
    def sort(self):#сортировка
        person_tmp=Neyro(self.input,  self.hidden,   self.hidden2,  self.exit, self.moon)
        for i in range(self.personQuantity):
            for j in range(self.personQuantity-i-1):
                if(self.persons[j].time > self.persons[j+1].time):
                    person_tmp = self.persons[j]
                    self.persons[j]=self.persons[j+1]
                    self.persons[j+1]= person_tmp
    def crossing(self, person1, person2):#Скрещивание
        tmp_person=Neyro(self.input,  self.hidden,  self.hidden2,  self.exit , self.moon)
        for i in range(person1.neyroinput):
            for j in range(person1.neyrohidden):
                tmp_person.coofIn[i, j]=(person1.coofIn[i, j]+person2.coofIn[i, j])/2
        for i in range(person1.neyrohidden):
            for j in range(person1.neyrohidden2):
                tmp_person.coofCentr[i, j]=(person1.coofCentr[i, j]+person2.coofCentr[i, j])/2
        for i in range(person1.neyrohidden2):
            for j in range(person1.neyroexit):
                tmp_person.coofOut[i, j]=(person1.coofOut[i, j]+person2.coofOut[i, j])/2
        return tmp_person

    def mutation(self, person_mutant):#Мутация
        for i in range(person_mutant.neyroinput):
            for j in range(person_mutant.neyrohidden):
                if(random.randint(0, 100)<=10):
                    person_mutant.coofIn[i, j]+=(random.random()-0.5)*2
        for i in range(person_mutant.neyrohidden):
            for j in range(person_mutant.neyrohidden2):
                if(random.randint(0, 100)<=10):
                    person_mutant.coofCentr[i, j]+=(random.random()-0.5)*2
        for i in range(person_mutant.neyrohidden2):
            for j in range(person_mutant.neyroexit):
                if(random.randint(0, 100)<=10):
                    person_mutant.coofOut[i, j]+=(random.random()-0.5)*2
        return person_mutant

    def evolution(self):#Создание нового поколения
        #self.pyg.Update(self.generation, self.top)
        self.generation+=1
        next_persons = np.array([Neyro(self.input,  self.hidden,  self.hidden2,   self.exit, self.moon) for i in range(self.personQuantity)]) 
        for i in range(self.personQuantity):
            next_persons[i]=self.crossing(self.persons[int(random.random()*(self.personQuantity/2)+(self.personQuantity/2))], 
                                          self.persons[int(random.random()*(self.personQuantity/2)+(self.personQuantity/2))])
            next_persons[i]=self.mutation(next_persons[i])
        next_persons[0]=self.persons[self.personQuantity-1]
        next_persons[1]=self.persons[self.personQuantity-2]
        next_persons[0].dead=0
        next_persons[1].dead=0
        next_persons[0].X=1920/2#+random.randint(-41, 41)
        next_persons[1].X=1920/2#+random.randint(-41, 41)
        next_persons[0].Y=800/2#+random.randint(-20, 20)
        next_persons[1].Y=800/2#+random.randint(-20, 20)
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
        next_persons[0].pos=0
        next_persons[1].pos=0                                        
        self.persons=next_persons

pyg=Pygame()
rock=Rocket()
moon=planet()
moon.Sozd()
gen=Generic(10, pyg, moon)
moon.Draw(pyg)
while(True):

            


    gen.check()
    gen.sort()
    gen.evolution()
    pyg.DrawR()
    moon.Draw(pyg)
    #pyg.DrawRocket(rock.X, rock.Y, rock.rotate, rock.flame)
    pyg.DrawPlanet(moon.surface)
    #pyg.Update(0, rock.fuel)
    #pyg.DrawRocket(rock.X, rock.Y, rock.rotate, rock.flame, (0, 0, 0))
    #pyg.Random()

    #rock.Fizics(pyg.r, pyg.l, pyg.w, pyg.n)

    tm.sleep(0.0001)



    #if(moon.Exit(rock.X, rock.Y, rock.rotate, rock.speedY, pyg.razmerX, pyg.razmerY)==1):
    #    print("OK")
    #    rock.X=700
    #    rock.Y=300
    #elif(moon.Exit(rock.X, rock.Y, rock.rotate, rock.speedY, pyg.razmerX, pyg.razmerY)==2):
    #    rock.X=300
    #    rock.Y=300