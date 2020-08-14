# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:42:10 2019

@author: vidhi
"""

#FROM 112 course website https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#installingModules
from cmu_112_graphics import * 
from tkinter import *
import random
import math

class MarioGame(ModalApp):
    def appStarted(app):
        app.GameMode=GameMode()
        app.GameOver=GameOver()
        app.NewLevel=NewLevelMode()
        app.Win=WinMode()
        app.splashScreenMode = SplashScreenMode()
        app.setActiveMode(app.splashScreenMode)        
        app.lives=3

class WinMode(Mode):
    def keyPressed(mode,event):
        if event.key=="P":            
            mode.app.setActiveMode(mode.app.GameMode)       
        if(event.key=="N"):
            mode.app.setActiveMode(mode.app.NewLevel)  
        if(event.key=="W"):
            mode.app.setActiveMode(mode.app.Win)  
        if(event.key=="L"):
            mode.app.setActiveMode(mode.app.GameOver)  
            
    def redrawAll(mode, canvas):
        font = 'Arial 16 bold'
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="Pink")
        canvas.create_text(mode.width/2, 150, text="Yay Princess!", font=font)
        canvas.create_text(mode.width/2, 250, text='You have Saved the Prince!', font=font)
        canvas.create_text(mode.width/2, 350, text='Congratulations!!', font=font)
    
class NewLevelMode(Mode):
    def appStarted(mode):        
        mode.size=random.randint(20,70) 
        mode.scrollX=0    
        mode.Cloud=Cloud1(mode)
        mode.Girl=Girl1(mode)
        mode.Wall=Wall1(mode)   
        mode.Blocks=Blocks1(mode) 
        mode.Enemy=Enemy1(mode)
        mode.Castle=Castle1(mode)
        mode.Obstacle=Obstacle1(mode)
        mode.RotatingObstacle=RotatingObstacle1(mode)
        mode.Enemy=Enemy1(mode)
        mode.Coins=Coins1(mode)
        mode.cx=0
        mode.cy=0
        mode.GameOver=0
        mode.scores=0     
    
    def timerFired(mode):      
        mode.Obstacle.Obstacletime()
        mode.RotatingObstacle.Rotatingtime()
        mode.Enemy.EnemyTime()
        mode.Girl.MoveTime()
        
    def keyPressed(mode,event):
        if(event.key=="P"):
            mode.app.setActiveMode(mode.app.GameMode)  
        if(event.key=="W"):
            mode.app.setActiveMode(mode.app.Win)  
        if(event.key=="L"):
            mode.app.setActiveMode(mode.app.GameOver)  
        
        if(mode.app.lives>0 and mode.GameOver==1 ):
            mode.app.lives-=1       
            mode.appStarted()
        elif (mode.scores==50):
              mode.app.lives+=1  
              mode.scores+=15
        elif (mode.app.lives==0 ): mode.app.setActiveMode(mode.app.GameOver)
        
        else:
            mode.Girl.move(event.key)
            mode.Obstacle.move(event.key) 
            mode.Blocks.move(event.key)
            mode.Wall.move(event.key)
            mode.Cloud.move(event.key)
            mode.Enemy.move(event.key)
            mode.Castle.move(event.key)            
            mode.RotatingObstacle.move(event.key) 
            mode.Coins.move(event.key)
                       
    def keyReleased(mode,event):        
        mode.Girl.released(event.key)  
      
    def redrawAll(mode,canvas):           
        canvas.create_rectangle(mode.cx,mode.cy,mode.width,mode.height,fill="Black") 
        mode.Cloud.draw(canvas)     
        mode.Obstacle.draw(canvas)
        mode.Wall.draw(canvas)   
        mode.Blocks.draw(canvas) 
        mode.Castle.draw(canvas)       
        mode.RotatingObstacle.draw(canvas) 
        mode.Girl.draw(canvas) 
        mode.Coins.draw(canvas)
        mode.Enemy.draw(canvas)
        canvas.create_rectangle(mode.width/2-150,10,mode.width/2+50,40,fill="RED") 
        canvas.create_text(mode.width/2-50,30, text=f'LIVES LEFT: {mode.app.lives}',
                               font='Arial 20 bold')
        canvas.create_rectangle(mode.width/2+100,10,mode.width/2+300,40,fill="RED") 
        canvas.create_text(mode.width/2+200,30, text=f'SCORES: {mode.scores}',
                               font='Arial 20 bold')


       
class Cloud1(object):      
    def __init__(self,mode): 
        self.mode=mode             
        self.color='white'
        self.cx=10
        self.cy=50
        self.speed=-10
        self.x=0
        self.dimension=900
            
    def move(self,direction):
        """
        if self.mode.Girl.cx>=self.mode.Castle.cx-250:
            self.speed=0   
            """
               
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed      
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed
                     
    def draw(self,canvas):                 
        self.x = self.cx
        for i in range(3): 
            #1st Cloud
            canvas.create_oval(self.x,self.cy,self.x+90,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40,self.cy,self.x+190,self.cy+70, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+90,self.cy,self.x+290,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40,self.cy-40,self.x+190,self.cy+50, fill=self.color,outline=self.color)
        
            #2nd Cloud
            canvas.create_oval(self.x+40+510,self.cy-30,self.x+140+600,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+550,self.cy,self.x+140+750,self.cy+80, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+600,self.cy,self.x+140+800,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+550,self.cy-40,self.x+140+700,self.cy+50, fill=self.color,outline=self.color)
            
            #3rd Cloud
            canvas.create_oval(self.x+260-50,self.cy+20+50,self.x+590-50,100+100, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+340-50,self.cy+10+100,self.x+690-50,100+120, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+290-50,self.cy+150,self.x+540-50,150+100, fill=self.color,outline=self.color)
            self.x=self.x+self.dimension+100
      
               
class Castle1(object):    
    def __init__(self,mode):
        self.mode=mode     
        self.cx=3750
        self.cy=500
        self.speed=-10
        self.x=0
        self.cx1=550
        url = 'https://i.imgur.com/iFiJzsR.png'#Source of Image: https://in.pinterest.com/pin/540291286539732441/
        url1="https://i.imgur.com/WNPCGyX.jpg?1"#Source of Image: https://pixelboom.it/shop/green-screen/energy-explosions-fire-destructions/floor-lava-3d-model-animated/ 
        self.lava=self.mode.loadImage(url1)       
        self.castle1 = self.mode.loadImage(url)
        self.castle=self.mode.scaleImage(self.castle1,2.5)
   
         
    def move(self,direction):
      
        if self.mode.Girl.cx>=self.cx-5:
            self.speed=0  
        
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed
                 self.cx1+=self.speed
        if self.cx1<50:
            self.cx1=550
        
                        
    def draw(self,canvas):
        sprite=self.castle        
        drawX=self.cx 
        drawY=self.cy                
        canvas.create_image(drawX-5, drawY-110, image=ImageTk.PhotoImage(sprite))  
        canvas.create_image(self.cx1,780, image=ImageTk.PhotoImage(self.lava)) 
       
class Girl1(object):
    def __init__(self,mode):       
        self.mode=mode
        self.cx=50
        self.cy=0.75*self.mode.height          
        self.speed=10
        self.dimension=10
        self.scrollMargin=50
        self.high_jump=1
        self.ballX=-10
        self.ballY=-10

        # Spritesheet made by using code in https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        url = 'https://i.imgur.com/s6bTY5K.png?2' #Source of image: https://www.pngtube.com/viewm/moxhwh_sprite-sheet-running-girl/
        spritestrip = self.mode.loadImage(url)
        self.sprites = [ ]
        for i in range(5):
            sprite = spritestrip.crop((10 + 110 * i, 0, 120 + 110 * i, 135))
            self.sprites.append(sprite)
        self.spriteCounter = 0       
        self.goToNextLevel=0
        self.go=0
        
    def move(self,direction):
        if direction=='Up':
            while(self.high_jump):
                 self.cy-=60
                 self.high_jump=0
               
        if direction=='Space':
            while(self.high_jump and self.cx<=850):
                 self.cx+=150
                 self.cy-=150
                 self.high_jump=0
                 
        if direction=='Enter':
                 while(self.high_jump and self.cx>=150):
                     self.cx-=150
                     self.cy-=150
                     self.high_jump=0    
               
                                 
        if self.cx<self.mode.width/2:
             if direction=='Right':                 
                     self.cx+=self.speed                       
                     
            
        if self.cx>100:
             if direction=='Left':
                 self.cx-=self.speed 
                                 
        if direction=="B":
            self.ballX=self.cx-5
            self.ballY=self.cy+30
        self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)
               
    def released(self,direction):
         if direction=='Up':
             self.cy+=60
             self.high_jump=1
         if direction=='Down':
             self.high_jump=1
         if direction=='Space':
             if self.high_jump==0:                 
                 self.cy+=150
                 self.high_jump=1
         if direction=='Enter':
              if self.high_jump==0:
                  self.cy+=150
                  self.high_jump=1     
            
    def MoveTime(self):
        if self.ballX>0:
            self.ballX+=10
        if self.ballX>self.cx+200:

            self.ballX=-1
            self.ballY=-1
                       
         
    def draw(self,canvas): 
              
        drawX=self.cx #-self.mode.scrollX
        drawY=self.cy
        
        sprite = self.sprites[self.spriteCounter]     
        #canvas.create_rectangle(drawX-45, drawY-80, drawX+10,drawY+50)  
        canvas.create_image(drawX-5, drawY-20, image=ImageTk.PhotoImage(sprite))      
        canvas.create_oval(self.ballX-10, self.ballY-10,self.ballX+10,self.ballY+10,fill="yellow")  
      
                     
class Obstacle1(object):    
     def __init__(self,mode):
        self.mode=mode
        self.cx1=500
        self.cx2=2300
        self.cx3=4100
        self.cy1=0.2*self.mode.height     
        self.cy2=0.4*self.mode.height 
        self.cy3=0.6*self.mode.height 
        self.cy4=0.8*self.mode.height 
        self.cy5=self.mode.height
        self.color='RED'
        self.dimension=100
        self.speed=-10
        self.scrollX=0
        self.x=0
        
     def Obstacletime(self):
         if self.cy1+10<0:
             self.cy1=self.mode.height
         if self.cy2+10<0:
             self.cy2=self.mode.height
         if self.cy3+10<0:
             self.cy3=self.mode.height
         if self.cy4+10<0:
             self.cy4=self.mode.height
         if self.cy5+10<0:
             self.cy5=self.mode.height
         
         self.cy1-=10
         self.cy2-=10
         self.cy3-=10
         self.cy4-=10
         self.cy5-=10
        
         
     def move(self,direction):      
                                                  
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx1+=self.speed
                 self.cx2+=self.speed
                 self.cx3+=self.speed
                 
        
        elif  self.x>=0 and self.cx1>=self.x:
            if direction=='Left':
                 self.cx1-=self.speed 
                 self.cx2-=self.speed 
                 self.cx3-=self.speed 

     def __hash__(self):
        return hash((self.cx,self.cy))
    
     def __eq__(self,other):
        return (isinstance(other, Obstacle) and (self.cx == other.cx) and (self.cy == other.cy) )
    
     def draw(self,canvas):  
          #1ST STAIRS
                       
          canvas.create_rectangle(self.cx1,self.cy1,self.cx1+self.dimension,self.cy1-20,fill=self.color)
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy5-50 and self.mode.Girl.cy<=self.cy1-50):
                  self.mode.Girl.cy=self.cy1-60
                  self.mode.Girl.high_jump=1 
                  
          if self.mode.Girl.cy==self.cy1-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):  
                  self.mode.Girl.cy=0.75*self.mode.height    
  
          canvas.create_rectangle(self.cx1,self.cy2,self.cx1+self.dimension,self.cy2-20,fill=self.color)  
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy1-50 and self.mode.Girl.cy<=self.cy2-50):
                  self.mode.Girl.cy=self.cy2-60
                  self.mode.Girl.high_jump=1  
                  
          if self.mode.Girl.cy==self.cy2-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10): 
                  self.mode.Girl.cy=0.75*self.mode.height    
           
          canvas.create_rectangle(self.cx1,self.cy3,self.cx1+self.dimension,self.cy3-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy2-50  and self.mode.Girl.cy<=self.cy3-50):
                  self.mode.Girl.cy=self.cy3-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy3-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):  
                  self.mode.Girl.cy=0.75*self.mode.height    
       
          canvas.create_rectangle(self.cx1,self.cy4,self.cx1+self.dimension,self.cy4-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy3-50 and self.mode.Girl.cy<=self.cy4-50):
                  self.mode.Girl.cy=self.cy4-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy4-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):
                  self.mode.Girl.cy=0.75*self.mode.height    
         
          canvas.create_rectangle(self.cx1,self.cy5,self.cx1+self.dimension,self.cy5-20,fill=self.color) 
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy4-50 and self.mode.Girl.cy<=self.cy5-50):
                  self.mode.Girl.cy=self.cy5-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy5-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10): 
                  self.mode.Girl.cy=0.75*self.mode.height              
                 
          #2ND STAIRS
     
          canvas.create_rectangle(self.cx2,self.cy1,self.cx2+self.dimension,self.cy1-20,fill=self.color)
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy5-50 and self.mode.Girl.cy<=self.cy1-50):
              
                  self.mode.Girl.cy=self.cy1-60
                  self.mode.Girl.high_jump=1             
          
       
          canvas.create_rectangle(self.cx2,self.cy2,self.cx2+self.dimension,self.cy2-20,fill=self.color)  
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy1-50 and self.mode.Girl.cy<=self.cy2-50):
                  self.mode.Girl.cy=self.cy2-60
                  self.mode.Girl.high_jump=1  
         
            
          canvas.create_rectangle(self.cx2,self.cy3,self.cx2+self.dimension,self.cy3-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy2-50 and self.mode.Girl.cy<=self.cy3-50):
                  self.mode.Girl.cy=self.cy3-60
                  self.mode.Girl.high_jump=1 
          
        
          canvas.create_rectangle(self.cx2,self.cy4,self.cx2+self.dimension,self.cy4-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy3-50 and self.mode.Girl.cy<=self.cy4-50):
                  self.mode.Girl.cy=self.cy4-60
                  self.mode.Girl.high_jump=1 
          
            
          canvas.create_rectangle(self.cx2,self.cy5,self.cx2+self.dimension,self.cy5-20,fill=self.color) 
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy4-50 and self.mode.Girl.cy<=self.cy5-50):
                  self.mode.Girl.cy=self.cy5-60
                  self.mode.Girl.high_jump=1 
          
        
           
class RotatingObstacle1(object):
    
    def __init__(self,mode):
        self.mode=mode
        self.centre1=[1150,0.8*self.mode.height]  
        self.centre2=[2950,0.8*self.mode.height]
        self.centre3=[4750,0.8*self.mode.height]
        self.end_x1=1200
        self.end_y1=0.8*self.mode.height
        self.end_x2=3000
        self.end_y2=0.8*self.mode.height
        self.end_x3=4800
        self.end_y3=0.8*self.mode.height
        self.angle_degrees=0
        self.speed=-10
        self.x=0
        self.color="white"
        self.m1=(self.centre1[1]-self.end_y1)/(self.centre1[0]-self.end_x1)
        self.m2=(self.centre2[1]-self.end_y2)/(self.centre2[0]-self.end_x2)
        self.m3=(self.centre3[1]-self.end_y3)/(self.centre3[0]-self.end_x3)
        
    def move(self,direction):        
       
        if self.mode.Girl.cx>50:
            if direction=='Right':                 
                 self.centre1[0]+=self.speed 
                 self.end_x1+=self.speed
                 self.centre2[0]+=self.speed 
                 self.end_x2+=self.speed
                 self.centre3[0]+=self.speed 
                 self.end_x3+=self.speed
        
        elif direction=='Left': 
            self.centre1[0]-=self.speed 
            self.end_x1-=self.speed
            self.centre2[0]-=self.speed 
            self.end_x2-=self.speed
            self.centre3[0]-=self.speed 
            self.end_x3-=self.speed
                             
     
    def Rotatingtime(self):
        self.angle_degrees+=5
        angle_rad = self.angle_degrees * math.pi / 180
        line_length =100
        self.end_x1 = self.centre1[0] + line_length * math.cos(angle_rad)
        self.end_y1 = self.centre1[1]+line_length * math.sin(angle_rad)
        self.end_x2 = self.centre2[0] + line_length * math.cos(angle_rad)
        self.end_y2 = self.centre2[1]+line_length * math.sin(angle_rad)
        self.end_x3 = self.centre3[0] + line_length * math.cos(angle_rad)
        self.end_y3 = self.centre3[1]+line_length * math.sin(angle_rad)

    def draw(self,canvas):  
        canvas.create_line(self.centre1,self.end_x1,self.end_y1,width=5,fill=self.color)
        canvas.create_line(self.centre2,self.end_x2,self.end_y2,width=5,fill=self.color)
        canvas.create_line(self.centre3,self.end_x3,self.end_y3,width=5,fill=self.color)
        
        if self.mode.Girl.cx>self.end_x1-69.5 and  self.mode.Girl.cx<self.end_x1+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y1==self.m1*(x-self.end_x1)):
                        self.mode.GameOver=1
        
        if self.mode.Girl.cx>self.end_x2-69.5 and  self.mode.Girl.cx<self.end_x2+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y2==self.m2*(x-self.end_x2)):
                        self.mode.GameOver=1
            
        if self.mode.Girl.cx>self.end_x3-69.5 and  self.mode.Girl.cx<self.end_x3+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y3==self.m3*(x-self.end_x3)):
                        self.mode.GameOver=1      
    
class Wall1(object):   
        
    def __init__(self,mode):
        self.mode=mode
        self.cx=0
        self.cy=0.8*self.mode.height     
        self.color='IndianRed1'
        self.dimension=500 
        self.speed=-10
        self.scrollX=0
        self.x=0
        self.win=0
                  
    def move(self,direction):
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed
        
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed     
        
        if self.win==1:
            self.mode.app.setActiveMode(self.mode.app.Win)
       
    def __hash__(self):
        return hash((self.cx,self.cy))
    
    def __eq__(self,other):
        return (isinstance(other, Wall) and (self.cx == other.cx) and (self.cy == other.cy) )
    
    def draw(self,canvas):  
       # drawX=self.cx   #-self.mode.scrollX
        #drawY=self.cy     
      
        self.x = self.cx - self.scrollX           
        
        for i in range(5):     
           
            canvas.create_rectangle(self.x,self.cy,self.x+self.dimension,0.9*self.mode.height,fill='wheat2')
            
            
            #if (self.mode.Girl.cx<self.x-self.dimension and self.mode.Girl.cx<self.x+self.dimension+100 and self.mode.Girl.cy<0.75*self.mode.height):     
            """
            if (self.mode.Girl.cy<self.cy-300):
                self.mode.Girl.cy=0.75*self.mode.height
                self.mode.Girl.high_jump=1              
            """ 
         
            if (self.mode.Girl.cx>self.x+self.dimension and self.mode.Girl.cx<self.x+self.dimension+100 and self.mode.Girl.cy==0.75*self.mode.height):                
                if(self.mode.Girl.cx>self.mode.Obstacle.cx1+100 and self.mode.Girl.cx not in range(self.mode.Obstacle.cx2,self.mode.Obstacle.cx2+100) and 
                   self.mode.Girl.cx not in range(self.mode.Obstacle.cx3,self.mode.Obstacle.cx3+100)):
                    self.mode.Girl.cy=self.mode.height
                    
                    self.mode.GameOver=1                                  
            self.x=self.x+self.dimension+100
        canvas.create_rectangle(self.x-100,self.cy,self.x+1500,0.9*self.mode.height,fill='wheat2')
        if self.mode.Girl.cx>=self.mode.Castle.cx-5:
            self.win=1

class Coins1(object):  
    
    def __init__(self,mode): 
        self.mode=mode
        self.circleCenters = [ ]
        self.speed=10
        self.scrollX=0
        X=50
        Y=0.5*800
        self.r=20
        self.x=0
        url1="https://i.imgur.com/o1cjyNC.png?1"  #Source of Image: http://www.mariouniverse.com/wp-content/img/sprites/nes/smb/items.png  
        self.sprites1 = self.mode.loadImage(url1)
        self.coins = self.mode.scaleImage(self.sprites1, 2)
        for i in range (17):
            x=random.randint(X,X+100)
            y=random.randint(Y,Y+100)
            X=X+150            
            self.circleCenters.append((x,y))
      
                 
    def move(self,direction):
        if self.mode.Girl.cx>50:
            if direction=='Right':
                self.scrollX += 10
        
        elif  self.x>=0:
            if direction=='Left':
                 self.scrollX -= 10                         
                                        
    def draw(self,canvas):
        # draw the circles        
                
        for circleCenter in self.circleCenters:
            
            (cx, cy) = circleCenter   
            cx-=self.scrollX
            
            if (cx<=self.mode.Girl.cx+10 and  cx>=self.mode.Girl.cx-45 and cy<=self.mode.Girl.cy+50 and cy>=self.mode.Girl.cy-80) :
                self.circleCenters.remove(circleCenter)
                self.mode.scores+=10
                                    
            canvas.create_oval(cx-self.r, cy-self.r, cx+self.r, cy+self.r, fill='cyan')
            #canvas.create_image(cx,cy, image=ImageTk.PhotoImage(self.coins)) 
    
        
class Enemy1(object):
    
    def __init__(self,mode):       
        self.mode=mode
        self.cx1=300
        self.cx2=600
        self.cx3=900
        self.cy=0.815*self.mode.height         
        self.speed=-10
        self.dimension=10
        self.scrollMargin=50
        self.x=0
        # Spritesheet made by using code in https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        url1 = 'https://i.imgur.com/qYbGiM8.png?1' #Source: https://in.pinterest.com/pin/475692779361182825/
        url2="https://i.imgur.com/eLeTdC9.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url3="https://i.imgur.com/5kDSjYS.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url4="https://i.imgur.com/JVF2Bvr.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url5="https://i.imgur.com/duMkixt.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url6="https://i.imgur.com/sWBsNRl.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        
        self.sprites1 = self.mode.loadImage(url1)
        self.image1 = self.mode.scaleImage(self.sprites1, 2)
        self.sprites2=self.mode.loadImage(url2)
        self.image2 = self.mode.scaleImage(self.sprites2, 2)
        self.sprites3=self.mode.loadImage(url3)
        self.image3 = self.mode.scaleImage(self.sprites3, 2)
        self.sprites4=self.mode.loadImage(url4)
        self.image4 = self.mode.scaleImage(self.sprites4, 2)
        self.sprites5=self.mode.loadImage(url5)
        self.image5 = self.mode.scaleImage(self.sprites5, 2)
        self.sprites6=self.mode.loadImage(url6)
        self.image6 = self.mode.scaleImage(self.sprites6, 2)
        self.enemy1=self.image1
        self.enemy2=self.image2
        self.enemy3=self.image5
        self.ScoreGiven1=0
        self.ScoreGiven2=0     
        self.ScoreGiven3=0
      
    
    def EnemyTime(self):
       
        self.cx1-=10
        self.cx2-=10
        self.cx3-=10
        if self.cx1<0:
            self.cx1=1000
        if self.cx2<0:
            self.cx2=1000  
        if self.cx3<0:
            self.cx3=1000
                              
   
    def move(self,direction):
                         
        if self.mode.Girl.cx>50:
             if direction=='Right':
                 self.cx1+=self.speed     
                 self.cx2+=self.speed
                 self.cx3+=self.speed  
                       
                              
    def draw(self,canvas):       
                      
            if (self.cx1<=self.mode.Girl.cx+10 and  self.cx1>=self.mode.Girl.cx-45 and self.cy<=self.mode.Girl.cy+50+25 and self.cy>=self.mode.Girl.cy-80+25 and self.enemy1==self.image1) :
                self.mode.GameOver=1
                
            if (self.cx2<=self.mode.Girl.cx+10 and  self.cx2>=self.mode.Girl.cx-45 and self.cy<=self.mode.Girl.cy+50+25 and self.cy>=self.mode.Girl.cy-80+25 and self.enemy2==self.image2) :
                self.mode.GameOver=1
                
            if (self.cx3<=self.mode.Girl.cx+10 and  self.cx3>=self.mode.Girl.cx-45 and self.cy<=self.mode.Girl.cy+50+25 and self.cy>=self.mode.Girl.cy-80+25 and self.enemy3==self.image5) :
                self.mode.GameOver=1
                
            if self.cx1==1000:
                self.enemy1=self.image1
                self.ScoreGiven1=0
            if self.cx2==1000:
                self.enemy2=self.image2
                self.ScoreGiven2=0
                
            if self.cx3==1000:
                self.enemy3=self.image5
                self.ScoreGiven3=0     
                
            if (self.mode.Girl.ballX>=self.cx1-15 and  self.mode.Girl.ballX<self.cx1+15 and self.mode.Girl.ballY==0.75*self.mode.height+30) :               
                self.enemy1=self.image4
                self.mode.Girl.ballX=-10
                self.mode.Girl.ballY=-10
                
                if self.ScoreGiven1==0:
                    self.ScoreGiven1=1
                    self.mode.scores+=10
                
            if (self.mode.Girl.ballX>=self.cx2-15 and self.mode.Girl.ballX<self.cx2+15 and self.mode.Girl.ballY==0.75*self.mode.height+30) :
                self.enemy2=self.image3  
                self.mode.Girl.ballX=-10
                self.mode.Girl.ballY=-10
                
                if self.ScoreGiven2==0:
                    self.ScoreGiven2=1
                    self.mode.scores+=10
           
            if (self.mode.Girl.ballX>=self.cx3-15 and self.mode.Girl.ballX<self.cx3+15 and self.mode.Girl.ballY==0.75*self.mode.height+30) :
                self.enemy3=self.image6  
                self.mode.Girl.ballX=-10
                self.mode.Girl.ballY=-10
                
                if self.ScoreGiven3==0:
                    self.ScoreGiven3=1
                    self.mode.scores+=10
                                  
            canvas.create_image(self.cx1,self.cy-25, image=ImageTk.PhotoImage(self.enemy1))    
            canvas.create_image(self.cx2, self.cy-25, image=ImageTk.PhotoImage(self.enemy2))  
            canvas.create_image(self.cx3, self.cy-25, image=ImageTk.PhotoImage(self.enemy3))
                            
        
class Blocks1(object):           
    def __init__(self,mode,cx=150,cy=0.63*800,color='goldenrod2',dimension=250):
        self.mode=mode
        self.cx=cx
        self.cy=cy
        self.color=color
        self.dimension=dimension   
        self.scrollX=0
        self.speed=-10
        self.x=0
        
    def move(self,direction):
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed                            
                 
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed
                  
        
    def __hash__(self):
        return hash((self.cx,self.cy))
    
    def __eq__(self,other):
        return (isinstance(other, Wall) and (self.cx == other.cx) and (self.cy == other.cy) )
    
    def draw(self,canvas):              
        self.x = self.cx
            
        if ( self.mode.Girl.cx>self.x-self.dimension-400 and 
                self.mode.Girl.cx<self.x and 
                self.mode.Girl.cy==self.cy-45):   
                self.mode.Girl.cy=0.75*self.mode.height 
       
        for i in range(4): 
            
            canvas.create_rectangle(self.x,self.cy,self.x+self.dimension,self.cy+50,fill=self.color)
            if (self.mode.Girl.cx>=self.x and self.mode.Girl.cx<=self.x+self.dimension and self.mode.Girl.cy<self.cy):
                self.mode.Girl.cy=self.cy-45
                self.mode.Girl.high_jump=1 
                
            if ( self.mode.Girl.cx>self.x+self.dimension and 
                self.mode.Girl.cx<self.x+self.dimension+400 and 
                self.mode.Girl.cy==self.cy-45):   
                     self.mode.Girl.cy=0.75*self.mode.height     
                     
            if (self.mode.Girl.cx>=self.x and self.mode.Girl.cx<=self.x+self.dimension and self.mode.Girl.cy==self.cy-45+60):
                self.mode.Girl.cy=self.cy-45

            self.x=self.x+self.dimension+400   

class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 16 bold'
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="cyan")
        canvas.create_text(mode.width/2, 150, text="Welcome Dear Princess!", font=font)
        canvas.create_text(mode.width/2, 250, text='You have got to Save the Prince!', font=font)
        canvas.create_text(mode.width/2, 350, text='Press "S" for the game!', font=font)
        canvas.create_text(mode.width/2, 450, text='Use keys Up/Left/Right for movements !', font=font)
        canvas.create_text(mode.width/2, 550, text='Use keys Space/Enter to jump and move forward or backwards', font=font)
        canvas.create_text(mode.width/2, 650, text='Use key "Down" to navigate inside the tunnel', font=font)
        canvas.create_text(mode.width/2, 750, text='Press key "B" to hit the enemy', font=font)

    def keyPressed(mode, event):
        if event.key=="S":            
            mode.app.setActiveMode(mode.app.GameMode)       
        if(event.key=="N"):
            mode.app.setActiveMode(mode.app.NewLevel)  
        if(event.key=="W"):
            mode.app.setActiveMode(mode.app.Win)  
        if(event.key=="L"):
            mode.app.setActiveMode(mode.app.GameOver)  
        
        
class GameMode(Mode):
    def appStarted(mode):        
        mode.size=random.randint(20,70) 
        mode.scrollX=0    
        mode.Cloud=Cloud(mode)
        mode.Girl=Girl(mode)
        mode.Wall=Wall(mode)   
        mode.Blocks=Blocks(mode) 
        mode.Enemy=Enemy(mode)        
        mode.Obstacle=Obstacle(mode)
        mode.RotatingObstacle=RotatingObstacle(mode)
        mode.Enemy=Enemy(mode)
        mode.Coins=Coins(mode)
        mode.cx=0
        mode.cy=0
        mode.GameOver=0
        mode.scores=0
     
    
    def timerFired(mode):
      
        mode.Obstacle.Obstacletime()
        mode.RotatingObstacle.Rotatingtime()
        mode.Enemy.EnemyTime()
        mode.Girl.MoveTime()
        
    def keyPressed(mode,event):             
        if(event.key=="N"):
            mode.app.setActiveMode(mode.app.NewLevel)  
        if(event.key=="W"):
            mode.app.setActiveMode(mode.app.Win)  
        if(event.key=="L"):
            mode.app.setActiveMode(mode.app.GameOver)  
        
        if(mode.app.lives>0 and mode.GameOver==1 ):
            mode.app.lives-=1       
            mode.appStarted()
        elif (mode.scores==50):
              mode.app.lives+=1  
              mode.scores+=15
        elif (mode.app.lives==0 ): mode.app.setActiveMode(mode.app.GameOver)
        
        else:
           
            mode.Girl.move(event.key)
            mode.Obstacle.move(event.key) 
            mode.Blocks.move(event.key)
            mode.Wall.move(event.key)
            mode.Cloud.move(event.key)
            mode.Enemy.move(event.key)                     
            mode.RotatingObstacle.move(event.key) 
            mode.Coins.move(event.key)
                       
    def keyReleased(mode,event):
        
        mode.Girl.released(event.key)  
      
    def redrawAll(mode,canvas):           
        canvas.create_rectangle(mode.cx,mode.cy,mode.width,mode.height,fill="DeepSkyBlue2") 
        mode.Cloud.draw(canvas)     
        mode.Obstacle.draw(canvas)
        mode.Wall.draw(canvas)   
        mode.Blocks.draw(canvas)             
        mode.RotatingObstacle.draw(canvas) 
        mode.Girl.draw(canvas) 
        mode.Wall.draw(canvas)  
        mode.Coins.draw(canvas)
        mode.Enemy.draw(canvas)
        canvas.create_rectangle(mode.width/2-150,10,mode.width/2+50,40,fill="RED") 
        canvas.create_text(mode.width/2-50,30, text=f'LIVES LEFT: {mode.app.lives}',
                               font='Arial 20 bold')
        canvas.create_rectangle(mode.width/2+100,10,mode.width/2+300,40,fill="RED") 
        canvas.create_text(mode.width/2+200,30, text=f'SCORES: {mode.scores}',
                               font='Arial 20 bold')

       
class Cloud(object):      
    def __init__(self,mode): 
        self.mode=mode             
        self.color='white'
        self.cx=10
        self.cy=50
        self.speed=-10
        self.x=0
        self.dimension=900
            
    def move(self,direction):
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
            
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed      
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed
                                
                   
    def draw(self,canvas):                 
        self.x = self.cx
        for i in range(18): 
            #1st Cloud
            canvas.create_oval(self.x,self.cy,self.x+90,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40,self.cy,self.x+190,self.cy+70, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+90,self.cy,self.x+290,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40,self.cy-40,self.x+190,self.cy+50, fill=self.color,outline=self.color)
        
            #2nd Cloud
            canvas.create_oval(self.x+40+510,self.cy-30,self.x+140+600,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+550,self.cy,self.x+140+750,self.cy+80, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+600,self.cy,self.x+140+800,self.cy+50, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+40+550,self.cy-40,self.x+140+700,self.cy+50, fill=self.color,outline=self.color)
            
            #3rd Cloud
            canvas.create_oval(self.x+260-50,self.cy+20+50,self.x+590-50,100+100, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+340-50,self.cy+10+100,self.x+690-50,100+120, fill=self.color,outline=self.color)
            canvas.create_oval(self.x+290-50,self.cy+150,self.x+540-50,150+100, fill=self.color,outline=self.color)
            self.x=self.x+self.dimension+100
      
       
class Girl(object):
    def __init__(self,mode):       
        self.mode=mode
        self.cx=50
        self.cy=0.75*self.mode.height          
        self.speed=10
        self.dimension=10
        self.scrollMargin=50
        self.high_jump=1
        self.ballX=-10
        self.ballY=-10
        self.TunnelUpX=3100
        self.TunnelUpY=0.8*self.mode.height-75-25
        self.TunnelDownX=3125
        self.TunnelDownY=0.8*self.mode.height-75
        # Spritesheet made by using code in https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        url = 'https://i.imgur.com/s6bTY5K.png?2' #Source of image: https://www.pngtube.com/viewm/moxhwh_sprite-sheet-running-girl/
        spritestrip = self.mode.loadImage(url)
        self.sprites = [ ]
        for i in range(5):
            sprite = spritestrip.crop((10 + 110 * i, 0, 120 + 110 * i, 135))
            self.sprites.append(sprite)
        self.spriteCounter = 0       
        self.goToNextLevel=0
        self.go=0
        self.way=0
        
    def move(self,direction):
        if direction=='Up':
            while(self.high_jump):
                 self.cy-=60
                 self.high_jump=0
               
        if direction=='Space':
            while(self.high_jump and self.cx<=850):
                 self.cx+=150
                 self.cy-=150
                 self.high_jump=0
                 
        if direction=='Enter':
                 while(self.high_jump and self.cx>=150):
                     self.cx-=150
                     self.cy-=150
                     self.high_jump=0    
        
        if direction=='Down':   
            if (self.cx>=self.TunnelDownX and self.cx<=self.TunnelDownX+50 ):
                if self.way==0:
                    self.cy-=60
                    self.way=1
                else:
                    self.cy+=20
                self.high_jump=0   
                    
                
        if self.goToNextLevel==1:                       
            self.mode.app.setActiveMode(self.mode.app.NewLevel)   
            
        if self.cx>=self.TunnelUpX+150:
            self.speed=0
        else:self.speed=10
                        
        if self.cx<self.mode.width/2:
             if direction=='Right':                 
                     self.cx+=self.speed                       
        if self.TunnelUpX+150<self.mode.width and self.cx<self.mode.width:
             if direction=='Right':                 
                     self.cx+=self.speed                
            
        if self.cx>100:
             if direction=='Left':
                 self.cx-=self.speed                 
                 
        if direction=="B":
            self.ballX=self.cx-5
            self.ballY=self.cy+30
        self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)
               
    def released(self,direction):
         if direction=='Up':
             self.cy+=60
             self.high_jump=1
         if direction=='Down':
             self.cy+=60
             self.high_jump=1
         if direction=='Space':
             if self.high_jump==0:                 
                 self.cy+=150
                 self.high_jump=1
         if direction=='Enter':
              if self.high_jump==0:
                  self.cy+=150
                  self.high_jump=1     
            
    def MoveTime(self):
        if self.ballX>0:
            self.ballX+=10
        if self.ballX>self.cx+200:

            self.ballX=-1
            self.ballY=-1
                     
         
    def draw(self,canvas): 
               
        if self.cy>=700 and self.cx>=self.TunnelUpX and self.cx<=self.TunnelUpX+100:            
            self.goToNextLevel=1
                 
        if ( self.cx>self.TunnelUpX-100 and self.cx<self.TunnelUpX and self.cy==self.TunnelUpY-45):   
            self.cy=0.75*self.mode.height 
  
            
        if (self.cx>=self.TunnelUpX and self.cx<=self.TunnelUpX+100 and self.cy<self.TunnelUpY):
            self.cy=self.TunnelUpY-45
            self.mode.Girl.high_jump=1 
          
                
        if ( self.cx>self.TunnelUpX+100 and self.cx<self.TunnelUpX+200 and self.cy==self.TunnelUpY-45):   
            self.cy=0.75*self.mode.height    
        
             
        drawX=self.cx #-self.mode.scrollX
        drawY=self.cy
        
        sprite = self.sprites[self.spriteCounter]     
        #canvas.create_rectangle(drawX-45, drawY-80, drawX+10,drawY+50)  
        canvas.create_image(drawX-5, drawY-20, image=ImageTk.PhotoImage(sprite))      
        canvas.create_oval(self.ballX-10, self.ballY-10,self.ballX+10,self.ballY+10,fill="yellow")          
        canvas.create_rectangle(self.TunnelUpX,self.TunnelUpY,self.TunnelUpX+100,self.TunnelUpY+25,fill="Green") 
        canvas.create_rectangle(self.TunnelDownX,self.TunnelDownY,self.TunnelDownX+50,self.TunnelDownY+75,fill="Green") 
                   
           
class Obstacle(object):    
     def __init__(self,mode):
        self.mode=mode
        self.cx1=500
        self.cx2=2300
        self.cx3=4100
        self.cy1=0.2*self.mode.height     
        self.cy2=0.4*self.mode.height 
        self.cy3=0.6*self.mode.height 
        self.cy4=0.8*self.mode.height 
        self.cy5=self.mode.height
        self.color='GREEN'
        self.dimension=100
        self.speed=-10
        self.scrollX=0
        self.x=0
        
     def Obstacletime(self):
         if self.cy1+10<0:
             self.cy1=self.mode.height
         if self.cy2+10<0:
             self.cy2=self.mode.height
         if self.cy3+10<0:
             self.cy3=self.mode.height
         if self.cy4+10<0:
             self.cy4=self.mode.height
         if self.cy5+10<0:
             self.cy5=self.mode.height
         
         self.cy1-=10
         self.cy2-=10
         self.cy3-=10
         self.cy4-=10
         self.cy5-=10
        
         
     def move(self,direction):            
                                           
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
            
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx1+=self.speed
                 self.cx2+=self.speed
                 self.cx3+=self.speed
                 self.mode.Girl.TunnelUpX+=self.speed
                 self.mode.Girl.TunnelDownX+=self.speed
        
        elif  self.x>=0 and self.cx1>=self.x:
            if direction=='Left':
                 self.cx1-=self.speed 
                 self.cx2-=self.speed 
                 self.cx3-=self.speed 
                 self.mode.Girl.TunnelUpX-=self.speed
                 self.mode.Girl.TunnelDownX-=self.speed
                                       
     def __hash__(self):
        return hash((self.cx,self.cy))
    
     def __eq__(self,other):
        return (isinstance(other, Obstacle) and (self.cx == other.cx) and (self.cy == other.cy) )
    
     def draw(self,canvas):  
          #1ST STAIRS               
          canvas.create_rectangle(self.cx1,self.cy1,self.cx1+self.dimension,self.cy1-20,fill=self.color)
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy5-50 and self.mode.Girl.cy<=self.cy1-50):
                  self.mode.Girl.cy=self.cy1-60
                  self.mode.Girl.high_jump=1 
                  
          if self.mode.Girl.cy==self.cy1-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):  
                  self.mode.Girl.cy=0.75*self.mode.height    
  
          canvas.create_rectangle(self.cx1,self.cy2,self.cx1+self.dimension,self.cy2-20,fill=self.color)  
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy1-50 and self.mode.Girl.cy<=self.cy2-50):
                  self.mode.Girl.cy=self.cy2-60
                  self.mode.Girl.high_jump=1  
                  
          if self.mode.Girl.cy==self.cy2-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10): 
                  self.mode.Girl.cy=0.75*self.mode.height    
           
          canvas.create_rectangle(self.cx1,self.cy3,self.cx1+self.dimension,self.cy3-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy2-50  and self.mode.Girl.cy<=self.cy3-50):
                  self.mode.Girl.cy=self.cy3-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy3-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):  
                  self.mode.Girl.cy=0.75*self.mode.height    
       
          canvas.create_rectangle(self.cx1,self.cy4,self.cx1+self.dimension,self.cy4-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy3-50 and self.mode.Girl.cy<=self.cy4-50):
                  self.mode.Girl.cy=self.cy4-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy4-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10):
                  self.mode.Girl.cy=0.75*self.mode.height    
         
          canvas.create_rectangle(self.cx1,self.cy5,self.cx1+self.dimension,self.cy5-20,fill=self.color) 
          if (self.mode.Girl.cx>=self.cx1 and self.mode.Girl.cx<=self.cx1+self.dimension and self.mode.Girl.cy>self.cy4-50 and self.mode.Girl.cy<=self.cy5-50):
                  self.mode.Girl.cy=self.cy5-60
                  self.mode.Girl.high_jump=1 
          if self.mode.Girl.cy==self.cy5-60 and self.mode.Girl.cx not in range(self.cx1+5,self.cx1+self.dimension+10) and self.mode.Girl.cx not in range(self.cx2+5,self.cx2+self.dimension+10) and self.mode.Girl.cx not in range(self.cx3+5,self.cx3+self.dimension+10): 
                  self.mode.Girl.cy=0.75*self.mode.height              
                 
          #2ND STAIRS
     
          canvas.create_rectangle(self.cx2,self.cy1,self.cx2+self.dimension,self.cy1-20,fill=self.color)
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy5-50 and self.mode.Girl.cy<=self.cy1-50):
              
                  self.mode.Girl.cy=self.cy1-60
                  self.mode.Girl.high_jump=1             
          
       
          canvas.create_rectangle(self.cx2,self.cy2,self.cx2+self.dimension,self.cy2-20,fill=self.color)  
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy1-50 and self.mode.Girl.cy<=self.cy2-50):
                  self.mode.Girl.cy=self.cy2-60
                  self.mode.Girl.high_jump=1  
         
            
          canvas.create_rectangle(self.cx2,self.cy3,self.cx2+self.dimension,self.cy3-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy2-50 and self.mode.Girl.cy<=self.cy3-50):
                  self.mode.Girl.cy=self.cy3-60
                  self.mode.Girl.high_jump=1 
          
        
          canvas.create_rectangle(self.cx2,self.cy4,self.cx2+self.dimension,self.cy4-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy3-50 and self.mode.Girl.cy<=self.cy4-50):
                  self.mode.Girl.cy=self.cy4-60
                  self.mode.Girl.high_jump=1 
          
            
          canvas.create_rectangle(self.cx2,self.cy5,self.cx2+self.dimension,self.cy5-20,fill=self.color) 
          if (self.mode.Girl.cx>=self.cx2 and self.mode.Girl.cx<=self.cx2+self.dimension and self.mode.Girl.cy>self.cy4-50 and self.mode.Girl.cy<=self.cy5-50):
                  self.mode.Girl.cy=self.cy5-60
                  self.mode.Girl.high_jump=1 
          
          
          #3RD STAIRS
          canvas.create_rectangle(self.cx3,self.cy1,self.cx3+self.dimension,self.cy1-20,fill=self.color)
          if (self.mode.Girl.cx>=self.cx3 and self.mode.Girl.cx<=self.cx3+self.dimension and self.mode.Girl.cy>self.cy5-50 and self.mode.Girl.cy<=self.cy1-50):
                  self.mode.Girl.cy=self.cy1-60
                  self.mode.Girl.high_jump=1 
          

       
          canvas.create_rectangle(self.cx3,self.cy2,self.cx3+self.dimension,self.cy2-20,fill=self.color)  
          if (self.mode.Girl.cx>=self.cx3 and self.mode.Girl.cx<=self.cx3+self.dimension and self.mode.Girl.cy>self.cy1-50 and self.mode.Girl.cy<=self.cy2-50):
                  self.mode.Girl.cy=self.cy2-60
                  self.mode.Girl.high_jump=1  
            
          canvas.create_rectangle(self.cx3,self.cy3,self.cx3+self.dimension,self.cy3-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx3 and self.mode.Girl.cx<=self.cx3+self.dimension and self.mode.Girl.cy>self.cy2-50 and self.mode.Girl.cy<=self.cy3-50):
                  self.mode.Girl.cy=self.cy3-60
                  self.mode.Girl.high_jump=1 
         
                  
          canvas.create_rectangle(self.cx3,self.cy4,self.cx3+self.dimension,self.cy4-20,fill=self.color)   
          if (self.mode.Girl.cx>=self.cx3 and self.mode.Girl.cx<=self.cx3+self.dimension and self.mode.Girl.cy>self.cy3-50 and self.mode.Girl.cy<=self.cy4-50):
                  self.mode.Girl.cy=self.cy4-60
                  self.mode.Girl.high_jump=1 
          
            
          canvas.create_rectangle(self.cx3,self.cy5,self.cx3+self.dimension,self.cy5-20,fill=self.color) 
          if (self.mode.Girl.cx>=self.cx3 and self.mode.Girl.cx<=self.cx3+self.dimension and self.mode.Girl.cy>self.cy4-50 and self.mode.Girl.cy<=self.cy5-50):
                  self.mode.Girl.cy=self.cy5-60
                  self.mode.Girl.high_jump=1    
         
            
class RotatingObstacle(object):
    
    def __init__(self,mode):
        self.mode=mode
        self.centre1=[1150,0.8*self.mode.height]  
        self.centre2=[2950,0.8*self.mode.height]
        self.centre3=[4750,0.8*self.mode.height]
        self.end_x1=1200
        self.end_y1=0.8*self.mode.height
        self.end_x2=3000
        self.end_y2=0.8*self.mode.height
        self.end_x3=4800
        self.end_y3=0.8*self.mode.height
        self.angle_degrees=0
        self.speed=-10
        self.x=0
        self.m1=(self.centre1[1]-self.end_y1)/(self.centre1[0]-self.end_x1)
        self.m2=(self.centre2[1]-self.end_y2)/(self.centre2[0]-self.end_x2)
        self.m3=(self.centre3[1]-self.end_y3)/(self.centre3[0]-self.end_x3)
        
    def move(self,direction):   
        
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
            
        if self.mode.Girl.cx>50:
            if direction=='Right':                 
                 self.centre1[0]+=self.speed 
                 self.end_x1+=self.speed
                 self.centre2[0]+=self.speed 
                 self.end_x2+=self.speed
                 self.centre3[0]+=self.speed 
                 self.end_x3+=self.speed
        
        elif direction=='Left': 
            self.centre1[0]-=self.speed 
            self.end_x1-=self.speed
            self.centre2[0]-=self.speed 
            self.end_x2-=self.speed
            self.centre3[0]-=self.speed 
            self.end_x3-=self.speed
                             
     
    def Rotatingtime(self):
        self.angle_degrees+=5
        angle_rad = self.angle_degrees * math.pi / 180
        line_length =100
        self.end_x1 = self.centre1[0] + line_length * math.cos(angle_rad)
        self.end_y1 = self.centre1[1]+line_length * math.sin(angle_rad)
        self.end_x2 = self.centre2[0] + line_length * math.cos(angle_rad)
        self.end_y2 = self.centre2[1]+line_length * math.sin(angle_rad)
        self.end_x3 = self.centre3[0] + line_length * math.cos(angle_rad)
        self.end_y3 = self.centre3[1]+line_length * math.sin(angle_rad)

    def draw(self,canvas):  
        canvas.create_line(self.centre1,self.end_x1,self.end_y1,width=5)        
        canvas.create_line(self.centre2,self.end_x2,self.end_y2,width=5)
        canvas.create_line(self.centre3,self.end_x3,self.end_y3,width=5)
        
        
        if self.mode.Girl.cx>self.end_x1-69.5 and  self.mode.Girl.cx<self.end_x1+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y1==self.m1*(x-self.end_x1)):
                        self.mode.GameOver=1
        
        if self.mode.Girl.cx>self.end_x2-69.5 and  self.mode.Girl.cx<self.end_x2+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y2==self.m2*(x-self.end_x2)):
                        self.mode.GameOver=1
            
        if self.mode.Girl.cx>self.end_x3-69.5 and  self.mode.Girl.cx<self.end_x3+69.5:
            for x in range(self.mode.Girl.cx-45,self.mode.Girl.cx+10):
                for y in range(int(self.mode.Girl.cy-55),int(self.mode.Girl.cy+75)):
                    if (y-self.end_y3==self.m3*(x-self.end_x3)):
                        self.mode.GameOver=1        
    
class Wall(object):           
    def __init__(self,mode):
        self.mode=mode
        self.cx=0
        self.cy=0.8*self.mode.height     
        self.color='OrangeRed4'
        self.dimension=500 
        self.speed=-10
        self.scrollX=0
        self.x=0
                  
    def move(self,direction):
        
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
            
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed
        
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed        
       
    def __hash__(self):
        return hash((self.cx,self.cy))
    
    def __eq__(self,other):
        return (isinstance(other, Wall) and (self.cx == other.cx) and (self.cy == other.cy) )
    
    def draw(self,canvas):  
       # drawX=self.cx   #-self.mode.scrollX
        #drawY=self.cy     
      
        self.x = self.cx - self.scrollX           
        
        for i in range(20):     
           
            canvas.create_rectangle(self.x,self.cy,self.x+self.dimension,self.mode.height,fill=self.color)
            
            #if (self.mode.Girl.cx<self.x-self.dimension and self.mode.Girl.cx<self.x+self.dimension+100 and self.mode.Girl.cy<0.75*self.mode.height):     
            """
            if (self.mode.Girl.cy<self.cy-300):
                self.mode.Girl.cy=0.75*self.mode.height
                self.mode.Girl.high_jump=1              
            """ 

            if (self.mode.Girl.cx>self.x+self.dimension and self.mode.Girl.cx<self.x+self.dimension+100 and self.mode.Girl.cy==0.75*self.mode.height):                
                if(self.mode.Girl.cx>self.mode.Obstacle.cx1+100 and self.mode.Girl.cx not in range(self.mode.Obstacle.cx2,self.mode.Obstacle.cx2+100) and 
                   self.mode.Girl.cx not in range(self.mode.Obstacle.cx3,self.mode.Obstacle.cx3+100)):
                    self.mode.Girl.cy=self.mode.height
                    self.mode.GameOver=1                                  
            self.x=self.x+self.dimension+100


class Coins(object):  
    def __init__(self,mode): 
        self.mode=mode
        self.circleCenters = [ ]
        self.speed=-10
        self.scrollX=0
        X=50
        Y=0.5*800
        self.r=20
        self.x=0
        url1="https://i.imgur.com/bdumuyA.png?1"  #Source of Image: http://www.mariouniverse.com/wp-content/img/sprites/nes/smb/items.png 
       
        self.sprites1 = self.mode.loadImage(url1)
        self.coins = self.mode.scaleImage(self.sprites1, 2)
        for i in range (100):
            x=random.randint(X,X+100)
            y=random.randint(Y,Y+100)
            X=X+150            
            self.circleCenters.append((x,y))
      
                 
    def move(self,direction):
        
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
                                 
                        
        if self.mode.Girl.cx>50:
            if direction=='Right':
                if self.mode.Girl.TunnelUpX+200 <self.mode.width:
                    self.srollX=0
                else:
                    self.scrollX += 10
        
        elif  self.x>=0:
            if direction=='Left':
                 self.scrollX -= 10
                 
                                        
    def draw(self,canvas):
        # draw the circles        
        
        
        for circleCenter in self.circleCenters:
           
            (cx, cy) = circleCenter   
            cx-=self.scrollX
            
            if (cx<=self.mode.Girl.cx+10 and  cx>=self.mode.Girl.cx-45 and cy<=self.mode.Girl.cy+50 and cy>=self.mode.Girl.cy-80) :
                self.circleCenters.remove(circleCenter)
                self.mode.scores+=10
                                    
          
            canvas.create_image(cx,cy, image=ImageTk.PhotoImage(self.coins))  
            
class Enemy(object):
    
    def __init__(self,mode):       
        self.mode=mode
        self.cx1=1000
        self.cx2=500
        self.cy=0.815*self.mode.height         
        self.speed=-10
        self.dimension=10
        self.scrollMargin=50
        self.x=0
        # Spritesheet made by using code in https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        url1 = 'https://i.imgur.com/i4hwTdT.png' #Source: https://in.pinterest.com/pin/475692779361182825/
        url2="https://i.imgur.com/8OAynOr.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url3="https://i.imgur.com/TiYdVx1.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/
        url4="https://i.imgur.com/qc4NgJ4.png?1"  #Source: https://in.pinterest.com/pin/475692779361182825/        
       
        self.sprites1 = self.mode.loadImage(url1)
        self.image1 = self.mode.scaleImage(self.sprites1, 2)
        self.sprites2=self.mode.loadImage(url2)
        self.image2 = self.mode.scaleImage(self.sprites2, 2)
        self.sprites3=self.mode.loadImage(url3)
        self.image3 = self.mode.scaleImage(self.sprites3, 2)
        self.sprites4=self.mode.loadImage(url4)
        self.image4 = self.mode.scaleImage(self.sprites4, 2)
        self.enemy1=self.image1
       
        self.enemy2=self.image2
        self.ScoreGiven1=0
        self.ScoreGiven2=0       
        
    
    def EnemyTime(self):
       
        self.cx1-=10
        self.cx2-=10
        if self.cx1<0:
            self.cx1=1000
        if self.cx2<0:
            self.cx2=1000  
                              
   
    def move(self,direction):
                         
        if self.mode.Girl.cx>50:
             if direction=='Right':
                 self.cx1+=self.speed
                          
        if self.mode.Girl.cx>50:
             if direction=='Right':
                 self.cx2+=self.speed                         
                              
    def draw(self,canvas):       
                      
            if (self.cx1<=self.mode.Girl.cx+10 and  self.cx1>=self.mode.Girl.cx-45 and self.cy<=self.mode.Girl.cy+50+25 and self.cy>=self.mode.Girl.cy-80+25 and self.enemy1==self.image1) :
                self.mode.GameOver=1
                
            if (self.cx2<=self.mode.Girl.cx+10 and  self.cx2>=self.mode.Girl.cx-45 and self.cy<=self.mode.Girl.cy+50+25 and self.cy>=self.mode.Girl.cy-80+25 and self.enemy2==self.image2) :
                self.mode.GameOver=1
                
            if self.cx1==1000:
                self.enemy1=self.image1
                self.ScoreGiven1=0
            if self.cx2==1000:
                self.enemy2=self.image2
                self.ScoreGiven2=0          
                
            if (self.mode.Girl.ballX>=self.cx1-15 and  self.mode.Girl.ballX<self.cx1+15 and self.mode.Girl.ballY==0.75*self.mode.height+30) :               
                self.enemy1=self.image4
                self.mode.Girl.ballX=-10
                self.mode.Girl.ballY=-10
                
                if self.ScoreGiven1==0:
                    self.ScoreGiven1=1
                    self.mode.scores+=10
                
            if (self.mode.Girl.ballX>=self.cx2-15 and self.mode.Girl.ballX<self.cx2+15 and self.mode.Girl.ballY==0.75*self.mode.height+30) :
                self.enemy2=self.image3  
                self.mode.Girl.ballX=-10
                self.mode.Girl.ballY=-10
                
                if self.ScoreGiven2==0:
                    self.ScoreGiven2=1
                    self.mode.scores+=10           
                                  
            canvas.create_image(self.cx1,self.cy-25, image=ImageTk.PhotoImage(self.enemy1))    
            canvas.create_image(self.cx2, self.cy-25, image=ImageTk.PhotoImage(self.enemy2))  
            #drawX=drawX+1000                 
        
class Blocks(object):           
    def __init__(self,mode,cx=150,cy=0.63*800,color='goldenrod2',dimension=250):
        self.mode=mode
        self.cx=cx
        self.cy=cy
        self.color=color
        self.dimension=dimension   
        self.scrollX=0
        self.speed=-10
        self.x=0
        
    def move(self,direction):
        if self.mode.Girl.cx>=self.mode.Girl.TunnelUpX+150:
            self.speed=0
            
        if self.mode.Girl.cx>50:
            if direction=='Right':
                 self.cx+=self.speed                            
                 
        elif  self.x>=0 and self.cx>=self.x:
            if direction=='Left':
                 self.cx-=self.speed
        
                  
        
    def __hash__(self):
        return hash((self.cx,self.cy))
    
    def __eq__(self,other):
        return (isinstance(other, Wall) and (self.cx == other.cx) and (self.cy == other.cy) )
    
    def draw(self,canvas):              
        self.x = self.cx
           
        if ( self.mode.Girl.cx>self.x-self.dimension-400 and self.mode.Girl.cx<self.x and self.mode.Girl.cy==self.cy-45):   
                self.mode.Girl.cy=0.75*self.mode.height 
     
        for i in range(18):        
                
            canvas.create_rectangle(self.x,self.cy,self.x+self.dimension,self.cy+50,fill=self.color)
            if (self.mode.Girl.cx>=self.x and self.mode.Girl.cx<=self.x+self.dimension and self.mode.Girl.cy<self.cy):
                self.mode.Girl.cy=self.cy-45
                self.mode.Girl.high_jump=1 
                
            if ( self.mode.Girl.cx>self.x+self.dimension and 
                self.mode.Girl.cx<self.x+self.dimension+400 and 
                self.mode.Girl.cy==self.cy-45):   
                     self.mode.Girl.cy=0.75*self.mode.height  
                     
            if (self.mode.Girl.cx>=self.x and self.mode.Girl.cx<=self.x+self.dimension and self.mode.Girl.cy==self.cy-45+60):
                self.mode.Girl.cy=self.cy-45               

            self.x=self.x+self.dimension+400
   
class GameOver(Mode):
    def keyPressed(mode,event):
        if event.key=="P":            
            mode.app.setActiveMode(mode.app.GameMode)       
        if(event.key=="N"):
            mode.app.setActiveMode(mode.app.NewLevel)  
        if(event.key=="W"):
            mode.app.setActiveMode(mode.app.Win)  
        if(event.key=="L"):
            mode.app.setActiveMode(mode.app.GameOver)  
    
    def redrawAll(mode,canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height,fill="YELLOW")
        canvas.create_text(mode.width//2,150,text="You Lost", font='Arial 20 bold')
        canvas.create_text(mode.width//2,250,text="Better Luck Next Time!!!", font='Arial 20 bold')
               

def runTheGame():
    MarioGame(width=1000, height=800)

def main():
    runTheGame()

if __name__ == "__main__":
    main()