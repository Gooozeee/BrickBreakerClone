#Importing the libraries
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
import sqlite3
import pygame
import random

#Declaring the constants
#Screen size 
SCREENW, SCREENH = 1280, 720

#Level colours
LEVEL1BACKGROUND = [30,210,20]
LEVEL1BRICKCOLOUR = [200,0,25]

LEVEL2BACKGROUND = [110,200,100]
LEVEL2BRICKCOLOUR = [145,50,50]

LEVEL3BACKGROUND = [200,225,50]
LEVEL3BRICKCOLOUR = [60,65,10]

LEVEL4BACKGROUND = [240,180,50]
LEVEL4BRICKCOLOUR = [200,225,200]

LEVEL5BACKGROUND = [255,100,50]
LEVEL5BRICKCOLOUR = [110,255,100]

#Values
PADDLEOFFSET = 30
PADDLEW = 300
PADDLEH = 30
PADDLEX = SCREENW / 2 - PADDLEW / 2
PADDLEY = SCREENH - PADDLEH - PADDLEOFFSET
NoOFBRICKS = 10
BRICKW = SCREENW / NoOFBRICKS
BRICKH = BRICKW / 2

#Generic colours
WHITE = [255,255,255]
BLUE = [27,189,247]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BALLCOLOUR = [100,100,255]

#User details
FIRST = ''
LAST = ''

#Creating the menus class to manage the windows (making it inherit the Tk class)
#This class will be used as the baseline for the whole menus program
class Menus(tk.Tk):

    #Creating the initialiser
    #Always runs when you call the class, first thing that runs (it's a method)
    #Args lets you pass in an infinite amount of variables, kwwrgs is for passing through dictionaries
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Specifying a font for the labels, this is a constant
        self.TITLE_FONT = tkfont.Font(family='Cooper Std Black', size=20, weight="bold")
        self.LEADERBOARD_FONT = tkfont.Font(family='Cooper Std Black', size=20, weight="bold")
      

        #Creating the container that holds everything in the app
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Dictionary to store the different frames (menus)
        self.frames = {}

        #Looping through the dictionary to add all of the menus in
        for F in (LogIn, MainMenu, LevelSelect, LeaderBoardSelect, LeaderBoardOne, LeaderBoardTwo, LeaderBoardThree, LeaderBoardFour, LeaderBoardFive):
            PageName = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[PageName] = frame

            #Sticky nsew is North,South,East,West, allows you to move things around the window
            frame.grid(row=0, column=0, sticky="nsew")

        #Showing up the first screen as the LogIn screen
        self.ShowFrame("LogIn")

    #Defining the ShowFrame function to show the wanted menu
    def ShowFrame(self, PageName):
        frame = self.frames[PageName]

        #Raises the passed frame to the front
        frame.tkraise()

#Creating all of the menus of the game
#Creating the LogIn class which will show the LogIn menu
class LogIn(tk.Frame):

    #Creating the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        shreaker = tk.Label(self, text="SHREAKER", font=controller.TITLE_FONT, fg = 'red').pack(side="top", fill="x", pady=10)
        login = tk.Label(self, text="Please log in to continue", font=controller.TITLE_FONT, fg = 'blue').pack(side="top", fill="x", pady=10)
        login = tk.Label(self, text="Make sure the first letter of your name is a capital", font=controller.TITLE_FONT, fg = 'green').pack(side="top", fill="x", pady=10)

        #Creating the input
        firstnamelabel = tk.Label(self, text="Please input your first name here:").pack(side="top")
        firstnameentry = Entry(self)
        firstnameentry.focus_set()
        firstnameentry.pack(side="top", fill="x", pady=10)

        lastnamelabel = tk.Label(self, text="Please input your last name here:").pack(side="top")
        lastnameentry = Entry(self)
        lastnameentry.focus_set()
        lastnameentry.pack(side="top", fill="x", pady=10)
        
        #Creating the Submit and MainMenu buttons
        #The lambda allows you to pass variables through to a different function without it running as soon as the program starts
        submit = tk.Button(self, text="Submit details", fg = 'red', command=lambda: CallBack(firstnameentry, lastnameentry, controller)).pack(side="top", fill="x", pady=10)

        
#Defining the MainMenu class which will show the main menu
class MainMenu(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Creating the labels
        label = tk.Label(self, text="SHREAKER", font=controller.TITLE_FONT, width = 100, fg = 'blue').pack(side="top", fill="x", pady=10)

        #Creating the buttons
        levelselection = tk.Button(self, text="PLAY", fg = 'blue', command=lambda: controller.ShowFrame("LevelSelect")).pack(side="top", fill="x", pady=10)
        leaderboard = tk.Button(self, text="Go to the leader board selection screen", fg = 'green', command=lambda: controller.ShowFrame("LeaderBoardSelect")).pack(side="top", fill="x", pady=10)
        quitbtn = tk.Button(self, text="Quit", fg = 'red', command=lambda: quit()).pack(side="top", fill="x", pady=10)

        
#Creating the level selection class which will show the level selection menu
class LevelSelect(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #Creating the labels
        levelselection = tk.Label(self, text="Level Selection", font=controller.TITLE_FONT, width = 100).pack(side="top", fill="x", pady=10)

        #Creating the buttons
        levelone = tk.Button(self, text="Play level 1", fg = '#01bf0b', command=lambda: LevelOne()).pack(side="top", fill="x", pady=10)
        leveltwo = tk.Button(self, text="Play level 2", fg = '#69bf00', command=lambda: LevelTwo()).pack(side="top", fill="x", pady=10)
        levelthree = tk.Button(self, text="Play level 3", fg = '#b8bf00', command=lambda: LevelThree()).pack(side="top", fill="x", pady=10)
        levelfour = tk.Button(self, text="Play level 4", fg = '#bf7500', command=lambda: LevelFour()).pack(side="top", fill="x", pady=10)
        levelfive = tk.Button(self, text="Play level 5", fg = '#bf0c00', command=lambda: LevelFive()).pack(side="top", fill="x", pady=10)
        leaderboard = tk.Button(self, text="Go to the leader board selection screen", fg = 'blue', command=lambda: controller.ShowFrame("LeaderBoardSelect")).pack(side="top", fill="x", pady=10)
        goback = tk.Button(self, text="Go back", fg = 'blue', command=lambda: controller.ShowFrame("MainMenu")).pack(side="top", fill="x", pady=10)


#Creating the Leader Board selection class which will show the LeaderBoard selection menu
class LeaderBoardSelect(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        leaderboardselection = tk.Label(self, text="LeaderBoard Selection", fg = 'red', font=controller.TITLE_FONT, width = 100).pack(side="top", fill="x", pady=10)
        leadselection = tk.Label(self, text="Please choose a level", fg = 'green', font=controller.TITLE_FONT, width = 100).pack(side="top", fill="x", pady=10)

        #Creating the buttons
        levelone = tk.Button(self, text="Level 1", fg = '#01bf0b', command=lambda: controller.ShowFrame("LeaderBoardOne")).pack(side="top", fill="x", pady=10)
        leveltwo = tk.Button(self, text="Level 2", fg = '#69bf00', command=lambda: controller.ShowFrame("LeaderBoardTwo")).pack(side="top", fill="x", pady=10)
        levelthree = tk.Button(self, text="Level 3", fg = '#b8bf00', command=lambda: controller.ShowFrame("LeaderBoardThree")).pack(side="top", fill="x", pady=10)
        levelfour = tk.Button(self, text="Level 4", fg = '#bf7500', command=lambda: controller.ShowFrame("LeaderBoardFour")).pack(side="top", fill="x", pady=10)
        levelfive = tk.Button(self, text="Level 5", fg = '#bf0c00', command=lambda: controller.ShowFrame("LeaderBoardFive")).pack(side="top", fill="x", pady=10)
        goback = tk.Button(self, text="Go back", fg = 'blue', command=lambda: controller.ShowFrame("MainMenu")).pack(side="top", fill="x", pady=10)


#Creating the class that will show the leaderboard for the first level
class LeaderBoardOne(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        title = tk.Label(self, text="Level one leaderboard", fg = '#01bf0b', font=controller.TITLE_FONT, width = 100).grid()

        #Getting the needed data from the database
        conn = sqlite3.connect('LeaderBoard.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT First_Name, High_Score_1
                             FROM Users, Level_1
                             WHERE Users.UserID = Level_1.UserID
                             ORDER BY High_Score_1 DESC
                             ''')

        result = cursor.fetchall()
        conn.commit()
        conn.close()

        #Getting the tuples seperate to be able to print them seperately
        try:
            names, results = zip(*result)
        except:
            return
        
        titles = '''NAME                                                                                                                                          SCORE'''
                     
        #Label that will show the leaderboard
        leaderboardlabel = tk.Label(self,text=(titles), fg = '#01bf0b', font=controller.LEADERBOARD_FONT).grid()

        #Label that will print the names
        for i in range(len(names)):
                exec('Label%d=Label(self,text="%s", fg = "#01bf0b", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=W)' % (i,names[i],i))

        #Label thet will print the results
        for i in range(len(results)):
                exec('Label%d=Label(self,text="%s", fg = "#01bf0b", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=E, row = 2+%d)' % (i,results[i],i,i))

        #Creating the buttons
        goback = tk.Button(self, text="Go back", fg = '#01bf0b', command=lambda: controller.ShowFrame("LeaderBoardSelect")).grid()
        

#Creating the class that will show the leaderboard for the second level
class LeaderBoardTwo(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        title = tk.Label(self, text="Level two leaderboard", fg = '#69bf00', font=controller.TITLE_FONT, width = 100).grid()

        #Getting the needed data from the database
        conn = sqlite3.connect('LeaderBoard.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT First_Name, High_Score_2
                             FROM Users, Level_2
                             WHERE Users.UserID = Level_2.UserID
                             ORDER BY High_Score_2 DESC
                             ''')

        result = cursor.fetchall()
        conn.commit()
        conn.close()

        #Getting the tuples seperate to be able to print them seperately
        try:
            names, results = zip(*result)
        except:
            return
        
        titles = '''NAME                                                                                                                                          SCORE'''
                     
        #Label that will show the leaderboard
        leaderboardlabel = tk.Label(self,text=(titles), fg = '#69bf00', font=controller.LEADERBOARD_FONT).grid()

        #Label that will print the names
        for i in range(len(names)):
                exec('Label%d=Label(self,text="%s", fg = "#69bf00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=W)' % (i,names[i],i))

        #Label thet will print the results
        for i in range(len(results)):
                exec('Label%d=Label(self,text="%s", fg = "#69bf00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=E, row = 2+%d)' % (i,results[i],i,i))

        #Creating the buttons
        goback = tk.Button(self, text="Go back", fg = '#69bf00', command=lambda: controller.ShowFrame("LeaderBoardSelect")).grid()


#Creating the class that will show the leaderboard for the third level
class LeaderBoardThree(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        title = tk.Label(self, text="Level three leaderboard", fg = '#b8bf00', font=controller.TITLE_FONT, width = 100).grid()

        #Getting the needed data from the database
        conn = sqlite3.connect('LeaderBoard.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT First_Name, High_Score_3
                             FROM Users, Level_3
                             WHERE Users.UserID = Level_3.UserID
                             ORDER BY High_Score_3 DESC
                             ''')

        result = cursor.fetchall()
        conn.commit()
        conn.close()

        #Getting the tuples seperate to be able to print them seperately
        try:
            names, results = zip(*result)
        except:
            return
        
        titles = '''NAME                                                                                                                                          SCORE'''
                     
        #Label that will show the leaderboard
        leaderboardlabel = tk.Label(self,text=(titles), fg = '#b8bf00', font=controller.LEADERBOARD_FONT).grid()

        #Label that will print the names
        for i in range(len(names)):
                exec('Label%d=Label(self,text="%s", fg = "#b8bf00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=W)' % (i,names[i],i))

        #Label thet will print the results
        for i in range(len(results)):
                exec('Label%d=Label(self,text="%s", fg = "#b8bf00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=E, row = 2+%d)' % (i,results[i],i,i))

        #Creating the buttons
        goback = tk.Button(self, text="Go back", fg = '#b8bf00', command=lambda: controller.ShowFrame("LeaderBoardSelect")).grid()


#Creating the class that will show the leaderboard for the fourth level
class LeaderBoardFour(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        title = tk.Label(self, text="Level four leaderboard", fg = '#bf7500', font=controller.TITLE_FONT, width = 100).grid()

        #Getting the needed data from the database
        conn = sqlite3.connect('LeaderBoard.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT First_Name, High_Score_4
                             FROM Users, Level_4
                             WHERE Users.UserID = Level_4.UserID
                             ORDER BY High_Score_4 DESC
                             ''')

        result = cursor.fetchall()
        conn.commit()
        conn.close()

        #Getting the tuples seperate to be able to print them seperately
        try:
            names, results = zip(*result)
        except:
            return
        
        titles = '''NAME                                                                                                                                          SCORE'''
                     
        #Label that will show the leaderboard
        leaderboardlabel = tk.Label(self,text=(titles), fg = '#bf7500', font=controller.LEADERBOARD_FONT).grid()

        #Label that will print the names
        for i in range(len(names)):
                exec('Label%d=Label(self,text="%s", fg = "#bf7500", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=W)' % (i,names[i],i))

        #Label thet will print the results
        for i in range(len(results)):
                exec('Label%d=Label(self,text="%s", fg = "#bf7500", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=E, row = 2+%d)' % (i,results[i],i,i))

        #Creating the buttons
        goback = tk.Button(self, text="Go back", fg = '#bf7500', command=lambda: controller.ShowFrame("LeaderBoardSelect")).grid()


#Creating the class that will show the leaderboard for the fifth level
class LeaderBoardFive(tk.Frame):

    #Defining the initialiser of this class
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Creating the labels
        title = tk.Label(self, text="Level five leaderboard", fg = '#bf0c00', font=controller.TITLE_FONT, width = 100).grid()

        #Getting the needed data from the database
        conn = sqlite3.connect('LeaderBoard.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT First_Name, High_Score_5
                             FROM Users, Level_5
                             WHERE Users.UserID = Level_5.UserID
                             ORDER BY High_Score_5 DESC
                             ''')

        result = cursor.fetchall()
        conn.commit()
        conn.close()

        #Getting the tuples seperate to be able to print them seperately
        try:
            names, results = zip(*result)
        except:
            return
        
        titles = '''NAME                                                                                                                                          SCORE'''
                     
        #Label that will show the leaderboard
        leaderboardlabel = tk.Label(self,text=(titles), fg = '#bf0c00', font=controller.LEADERBOARD_FONT).grid()

        #Label that will print the names
        for i in range(len(names)):
                exec('Label%d=Label(self,text="%s", fg = "#bf0c00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=W)' % (i,names[i],i))

        #Label thet will print the results
        for i in range(len(results)):
                exec('Label%d=Label(self,text="%s", fg = "#bf0c00", font=controller.LEADERBOARD_FONT)\nLabel%d.grid(sticky=E, row = 2+%d)' % (i,results[i],i,i))

        #Creating the buttons
        goback = tk.Button(self, text="Go back", fg = '#bf0c00', command=lambda: controller.ShowFrame("LeaderBoardSelect")).grid()



#Creating the game objects
#Creating the boss class
class Boss:
    #Defining the initialiser
    def __init__(self, posx, posy, width, height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = 4

        #Hitbox for the boss object
        self.rect = pygame.Rect(self.posx,self.posy,self.width,self.height)

        #Giving the boss an amount of health points
        self.hp = self.width
        self.barheight = 10


    #Function that draws the boss
    def draw(self,Display):
        image = pygame.image.load('Ufo.png')                        
        Display.blit(image,(self.rect))
        

    #Function to move the boss    
    def move(self, mousex):
        paddleplace = mousex-self.width / 2
        if self.posx > paddleplace:
            self.posx -= self.speed
        if self.posx < paddleplace:
            self.posx += self.speed

        #Updating the hitbox
        self.rect = (self.posx,self.posy,self.width,self.height)

    #Draws the hp bars above the enemy in level 5
    def drawhpbar(self,Display):
        pygame.draw.rect(Display, RED, [self.posx-10,self.posy-15,self.width,self.barheight])
        pygame.draw.rect(Display, GREEN, [self.posx-10,self.posy-15,self.hp,self.barheight])


#Creating the powerups
class PowerUps():
    #Defining the initialiser of this class
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy + 255
        self.width = 50
        self.height = 63
        self.speed = 4

        #Creating a hitbox around the object
        self.rect = pygame.Rect(self.posx,self.posy,self.width,self.height)

        #Boolean flaf for when a power up hits the bomb
        self.hit = False

    #This function draws the bomb powerup
    def drawbomb(self, Display):
        image = pygame.image.load('Bomb.png')
        Display.blit(image,(self.rect))

    #This function draws the arrow powerup
    def drawarrows(self, Display):
        image = pygame.image.load('Arrow.png')
        Display.blit(image,(self.rect))

    #This function draws the + powerup
    def drawplus(self, Display):
        image = pygame.image.load('Plus.png')
        Display.blit(image,(self.rect))

    #This function moves the powerup down
    def updatepowerup(self,paddle,spawnbomb,spawnplus,spawnarrow,boss):
        self.posy += self.speed
        self.rect = pygame.Rect(self.posx,self.posy,self.width,self.height)

        #If the bomb is spawned you lose when the powerup hits the paddle
        if spawnbomb:
            if self.rect.colliderect(paddle.rect):
                self.hit = True

        #If the plus is spawned the boss gets more hp
        if spawnplus:
            if self.rect.colliderect(paddle.rect):
                if boss.hp < 155:
                    boss.hp += 1

                if boss.hp > 155:
                    boss.hp = 155

        #If the arrows are spawned the paddle gets smaller
        if spawnarrow:
            if self.rect.colliderect(paddle.rect):
                if paddle.width > 0:
                    paddle.width -= 4
                    paddle.rect = pygame.Rect(paddle.posx,paddle.posy,paddle.width,paddle.height)
                if paddle.width <= 0:
                    paddle.width -= 4
                    newwidth = paddle.width * -1
                    paddle.rect = pygame.Rect(paddle.posx,paddle.posy,newwidth,paddle.height)
            
        
#Creating the paddle class
class Paddle():
    #Defining the initialiser
    def __init__(self,posx,posy,width,height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

        #Creating a hitbox around the paddle        
        self.rect = pygame.Rect(self.posx,self.posy,self.width,self.height)
      
    #Defining the function that will draw the paddle
    def draw(self, Display): #Display lets it know where to draw
        pygame.draw.rect(Display, WHITE, [self.posx, self.posy, self.width, self.height])
            
    #Making the paddle move
    def move(self, mousex):
        self.posx = mousex - self.width / 2
        self.rect.center = (self.posx+self.width/2,self.posy+18)
            

#Defining the circle class
class Circle():
    #Defining a constructor(Creates the object)
    def __init__(self,SCREENW,SCREENH,posx,posy,width,height,speedx,speedy):
        self.screensize = (SCREENW, SCREENH)
        #Defining the size of the object
        self.posx = 640
        self.posy = 650
        self.radius = 15
        #Creating the hitbox around the object
        self.rect = pygame.Rect(self.posx-self.radius,self.posy-self.radius,self.radius*2, self.radius*2)
            
        #Gives the colour
        self.colour = BALLCOLOUR
        #Gives the direction of the ball, x then y
        self.direction = [1,-1]
        #Gives the speed of the ball
        self.speedx = speedx
        self.speedy = speedy


        #Boolean flag for hitting the edge of the game
        self.hit_bottom = False

    def update(self, paddle, rectarray, bricks):
        #Creating the function that gives the ball movement
        self.posx += self.direction[0]*self.speedx
        self.posy += self.direction[1]*self.speedy

        #Creating the collision for when the ball goes past the paddle and you lose
        self.rect.center = (self.posx, self.posy)

        #Collision for top and bottom
        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= 719:
            self.hit_bottom = True

        #Collision for sides
        if self.rect.right >= 1279:
            self.direction[0] = -1
        elif self.rect.left <= 0:
            self.direction[0] = 1

        #Collision for the paddle
        if self.rect.colliderect(paddle.rect):
            
            #Plays sound when ball collides
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Paddle.wav'), maxtime=600)
            
            self.direction[1] = -1
            self.direction[0] = int(random.randrange(-2,3))

        #Collision for the bricks
        for i in rectarray:
            if self.rect.colliderect(i):
                
                #Plays sound when ball collides
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Hit.wav'), maxtime=600)
                
                self.direction[1] = int(random.randrange(1,2))
                indexofhit = rectarray.index(i)
                del rectarray[indexofhit]
                del bricks[indexofhit]

    def updatenewbrick(self,rectarrayone,bricksone):
        #Creating the collision for the new set of bricks
        for i in rectarrayone:
            if self.rect.colliderect(i):
                
                #Plays sound when ball collides
                pygame.mixer.Channel(0).play(pygame.mixer.Sound('Hit.wav'), maxtime=600)
                
                self.direction[1] = int(random.randrange(1,2))
                indexofhit = rectarrayone.index(i)
                del rectarrayone[indexofhit]
                del bricksone[indexofhit]

    def updateboss(self,boss):
        #Collision for the boss
        if self.rect.colliderect(boss.rect):
            #Plays sound when ball collides
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Boss.wav'), maxtime=2000)
            
            self.direction[1] = int(random.randrange(2,4))
            boss.hp -= 1
                
    #Function to render the circle
    def render(self, Display):
        pygame.draw.circle(Display, self.colour, (self.posx, self.posy), self.radius, 0)
        pygame.draw.circle(Display, BLACK, (self.posx, self.posy), self.radius, 5)


#Creating the brick class
class Brick():
    #Defining the initialiser
    def __init__(self, posx, posy, width, height, colour):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.colour = colour

        #Hitbox for the bricks
        self.rect = pygame.Rect(self.posx,self.posy,self.width,self.height)
                
    def draw(self,Display):
        pygame.draw.rect(Display,self.colour, [self.posx, self.posy, self.width, self.height])
       
        
#Creating the game loops        
def LevelOne():
        
    #Initilaises the PyGame module
    pygame.init()
    
    #Sets the parameters of the window
    pygame.display.set_caption("Shreaker")
    display = pygame.display.set_mode([SCREENW,SCREENH])
    display.fill(LEVEL1BACKGROUND)
    clock = pygame.time.Clock()

    #Plays background music
    pygame.mixer.music.load('Background.wav')
    pygame.mixer.music.play(-1)

    #Declaring the speed of the ball
    speedx = 5
    speedy = 5
    
    #Creating the rect object array
    columns = 2
    rectarray = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarray.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))
    
    #Creating the circle object
    pong = Circle(SCREENW,SCREENH,PADDLEX,PADDLEY,PADDLEW,PADDLEH,speedx,speedy)
    
    #Creating the paddle object
    paddle = Paddle(PADDLEX, PADDLEY, PADDLEW, PADDLEH)

    #Creating the brick objects
    bricks = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricks.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10, LEVEL1BRICKCOLOUR))

    #Creating the font for text objects
    font = pygame.font.SysFont('Arial', 50, bold=True, italic=False)
    counter = 15000
    
    #Creating the PyGame loop, making sure the window stays open
    GameOver = False

    while not GameOver:
        #FPS limit
        clock.tick(64)
        for event in pygame.event.get():

            #When the user presses X on the window, the loop stops
            if event.type == pygame.QUIT:
                GameOver = True

        #Updating the value of the score counter
        counter -= 1
        
        #Updating the ball
        pong.update(paddle, rectarray, bricks)

        #If the ball hits the bottom this happens
        if pong.hit_bottom:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard1(score)
            
            #Stops the loop
            GameOver = True

        #If all the bricks disappear this happens
        if not rectarray:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = str(counter)
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU WON! :)", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard1(score)
            
            #Stops the loop
            GameOver = True

        if counter <= 0:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU RAN OUT OF TIME! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard1(score)
            
            #Stops the loop
            GameOver = True
            

        #Creating the counter object
        countertext = font.render(str(counter), True, BLACK)
        helptext = font.render("Don't let the counter get to zero!", True, BLACK)
        
        #Changing the background colour
        display.fill(LEVEL1BACKGROUND)
            
        #Drawing the paddle
        paddle.draw(display)
            
        #Getting the mouse position
        mousex = pygame.mouse.get_pos()[0]

        #Making the paddle move
        paddle.move(mousex)

        #Drawing the bricks
        for i in range(len(bricks)):
                    bricks[i].draw(display)

        #Updating the ball
        pong.render(display)

        #Puts the text on the screen
        display.blit(countertext,(10,10))
        display.blit(helptext, (350,10))

        #The display will update itself because of this
        pygame.display.flip()
        pygame.display.update()

    #Quits the game            
    pygame.quit()


def LevelTwo():

    #Initilaises the PyGame module
    pygame.init()

    #Sets the parameters of the window
    pygame.display.set_caption("Shreaker")
    display = pygame.display.set_mode([SCREENW,SCREENH])
    display.fill(LEVEL2BACKGROUND)
    clock = pygame.time.Clock()

    #Plays background music
    pygame.mixer.music.load('Background.wav')
    pygame.mixer.music.play(-1)

    #Declaring the speed of the ball
    speedx = 6
    speedy = 6

    #Creating the rect object array
    columns = 3
    rectarray = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarray.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))
    
    #Creating the circle object
    pong = Circle(SCREENW,SCREENH,PADDLEX,PADDLEY,PADDLEW,PADDLEH,speedx,speedy)
    pongtwo = Circle(SCREENW,SCREENH,PADDLEX,PADDLEY,PADDLEW,PADDLEH,speedx,speedy)
    
    #Creating the paddle object
    paddle = Paddle(PADDLEX, PADDLEY, PADDLEW, PADDLEH)

    #Creating the brick objects
    bricks = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricks.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10,LEVEL2BRICKCOLOUR))

    #Creating the font for the counter object
    font = pygame.font.SysFont('Arial', 50, bold=True, italic=False)
    counter = 15000
    
    #Creating the PyGame loop, making sure the window stays open
    GameOver = False

    while not GameOver:
        #FPS limit
        clock.tick(64)
        
        for event in pygame.event.get():

            #When the user presses X on the window, the loop stops
            if event.type == pygame.QUIT:
                GameOver = True

        #Updating the value of the score counter
        counter -= 1
        
        #Updating the balls
        pong.update(paddle, rectarray, bricks)
        if counter <= 13500:
            pongtwo.update(paddle, rectarray, bricks)

        #If the ball hits the bottom this happens
        if pong.hit_bottom or pongtwo.hit_bottom:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard2(score)
            
            #Stops the loop
            GameOver = True

        #If all the bricks disappear this happens
        if not rectarray:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = str(counter)
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU WON! :)", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard2(score)
            
            #Stops the loop
            GameOver = True

        if counter <= 0:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU RAN OUT OF TIME! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard2(score)
            
            #Stops the loop
            GameOver = True
            

        #Creating the counter object
        countertext = font.render(str(counter), True, BLACK)
        helptext = font.render("Don't let the counter get to zero!", True, BLACK)
            
        #Changing the background colour
        display.fill(LEVEL2BACKGROUND)
            
        #Drawing the paddle
        paddle.draw(display)
            
        #Getting the mouse position
        mousex = pygame.mouse.get_pos()[0]

        #Making the paddle move
        paddle.move(mousex)

        #Drawing the bricks
        for i in range(len(bricks)):
                    bricks[i].draw(display)

        #Updating the ball
        pong.render(display)
        if counter <= 13500:
            pongtwo.render(display)

        #Puts the text on the screen
        display.blit(countertext,(10,10))
        display.blit(helptext, (350,10))   
                
        #The display will update itself because of this
        pygame.display.flip()
        pygame.display.update()

    #Quits the game            
    pygame.quit()

    
def LevelThree():

    #Initilaises the PyGame module
    pygame.init()

    #Sets the parameters of the window
    pygame.display.set_caption("Shreaker")
    display = pygame.display.set_mode([SCREENW,SCREENH])
    display.fill(LEVEL3BACKGROUND)
    clock = pygame.time.Clock()

    #Plays background music
    pygame.mixer.music.load('Background.wav')
    pygame.mixer.music.play(-1)

    #Declaring the speed of the ball
    speedx = 6
    speedy = 6
    speedx2 = 5
    speedy2 = 5

    #Creating the rect object array
    columns = 4
    rectarray = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarray.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))

    #Creating the font for the counter object
    font = pygame.font.SysFont('Arial', 50, bold=True, italic=False)
    counter = 15000
    
    #Creating the circle object
    pong = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx, speedy)
    pongtwo = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx2, speedy2)
    
    #Creating the paddle object
    paddle = Paddle(PADDLEX, PADDLEY, PADDLEW, PADDLEH)

    #Creating the brick objects
    bricks = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricks.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10, LEVEL3BRICKCOLOUR))
    
    #Creating the PyGame loop, making sure the window stays open
    GameOver = False

    while not GameOver:
        #FPS limit
        clock.tick(64)
        
        for event in pygame.event.get():

            #When the user presses X on the window, the loop stops
            if event.type == pygame.QUIT:
                GameOver = True

        #Updating the value of the score counter
        counter -= 1
        
        #Updating the ball
        pong.update(paddle, rectarray, bricks)
        pongtwo.update(paddle, rectarray, bricks)

        #If the ball hits the bottom this happens
        if pong.hit_bottom or pongtwo.hit_bottom:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard3(score)
            
            #Stops the loop
            GameOver = True

        #If all the bricks disappear this happens
        if not rectarray:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = str(counter)
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU WON! :)", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard3(score)
            
            #Stops the loop
            GameOver = True

        if counter <= 0:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU RAN OUT OF TIME! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard3(score)
            
            #Stops the loop
            GameOver = True

            
        #Creating the counter object
        countertext = font.render(str(counter), True, BLACK)
        helptext = font.render("Don't let the counter get to zero!", True, BLACK)

        #Changing the background colour
        display.fill(LEVEL3BACKGROUND)
            
        #Drawing the paddle
        paddle.draw(display)
            
        #Getting the mouse position
        mousex = pygame.mouse.get_pos()[0]

        #Making the paddle move
        paddle.move(mousex)

        #Drawing the bricks
        for i in range(len(bricks)):
                    bricks[i].draw(display)

        #Updating the ball
        pong.render(display)
        pongtwo.render(display)

        #Puts the text on the screen
        display.blit(countertext,(10,10))
        display.blit(helptext, (350,10))   
                
        #The display will update itself because of this
        pygame.display.flip()
        pygame.display.update()

    #Quits the game            
    pygame.quit()

def LevelFour():


    #Initilaises the PyGame module
    pygame.init()

    #Sets the parameters of the window
    pygame.display.set_caption("Shreaker")
    display = pygame.display.set_mode([SCREENW,SCREENH])
    display.fill(LEVEL4BACKGROUND)
    clock = pygame.time.Clock()

    #Plays background music
    pygame.mixer.music.load('Background.wav')
    pygame.mixer.music.play(-1)

    #Declaring the speed of the ball
    speedx = 6
    speedy = 6
    speedx2 = 5
    speedy2 = 5

    #Creating the rect object array
    columns = 5
    rectarray = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarray.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))

    
    #Creating the circle object
    pong = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx, speedy)
    pongtwo = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx2, speedy2)
    pongthree = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx2, speedy2)
    
    #Creating the paddle object
    paddle = Paddle(PADDLEX, PADDLEY, PADDLEW, PADDLEH)

    #Creating the brick objects
    bricks = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricks.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10, LEVEL4BRICKCOLOUR))

    #Creating the font for the counter object
    font = pygame.font.SysFont('Arial', 50, bold=True, italic=False)
    counter = 15000

    #Creates the hitboxes for the new bricks
    rectarrayone = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarrayone.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))

    #Creates the objects for the new bricks            
    bricksone = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricksone.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10, LEVEL4BRICKCOLOUR))
    
    #Creating the PyGame loop, making sure the window stays open
    GameOver = False

    #Boolean flag for when the second set of bricks appear
    bricksgone = False

    while not GameOver:
        #FPS limit
        clock.tick(64)
        
        for event in pygame.event.get():

            #When the user presses X on the window, the loop stops
            if event.type == pygame.QUIT:
                GameOver = True

        #Updating the value of the score counter
        counter -= 1
        
        #Updating the ball
        pong.update(paddle, rectarray, bricks)
        pongtwo.update(paddle, rectarray, bricks)
        if counter <= 13500:
            pongthree.update(paddle, rectarray, bricks)
        

        #If the ball hits the bottom this happens
        if pong.hit_bottom or pongtwo.hit_bottom or pongthree.hit_bottom:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard4(score)
            
            #Stops the loop
            GameOver = True

        #If all the bricks disappear this happens
        if not rectarray:

            #Sets the boolean flag to true to draw the new bricks
            bricksgone = True

            #This function checks for collision between the balls and the new set of bricks
            pong.updatenewbrick(rectarrayone,bricksone)
            pongtwo.updatenewbrick(rectarrayone,bricksone)
            if counter <= 13500:
                pongthree.updatenewbrick(rectarrayone,bricksone)
                
            #Once the second set of bricks disappears then this happens
            if not rectarrayone:
                
                #Declares font
                labelfont = ('Arial', 100, 'bold')

                #Gets the final value of the counter
                score = str(counter)
                text = "Your score was ",score
                
                #Opens a window to tell the user they lost and their score
                root = Tk()
                label = tk.Label(root, text="YOU WON! :)", font=labelfont).pack(side="top", fill="x", pady=10)
                label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

                #Updates the high score in the leaderboard
                UpdateLeaderBoard4(score)
                
                #Stops the loop
                GameOver = True

        if counter <= 0:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU RAN OUT OF TIME! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard4(score)
            
            #Stops the loop
            GameOver = True

        #Creating the counter object
        countertext = font.render(str(counter), True, BLACK)
        helptext = font.render("Don't let the counter get to zero!", True, BLACK)
        
        #Changing the background colour
        display.fill(LEVEL4BACKGROUND)
            
        #Drawing the paddle
        paddle.draw(display)
            
        #Getting the mouse position
        mousex = pygame.mouse.get_pos()[0]

        #Making the paddle move
        paddle.move(mousex)

        #Drawing the bricks
        for i in range(len(bricks)):
                    bricks[i].draw(display)

        if bricksgone:
            for i in range(len(bricksone)):
                        bricksone[i].draw(display)

        #Updating the ball
        pong.render(display)
        pongtwo.render(display)
        if counter <= 13500:
            pongthree.render(display)

        #Puts the text on the screen
        display.blit(countertext,(10,10))
        display.blit(helptext, (350,10))   
                
        #The display will update itself because of this
        pygame.display.flip()
        pygame.display.update()

    #Quits the game            
    pygame.quit()

def LevelFive():


    #Initilaises the PyGame module
    pygame.init()

    #Sets the parameters of the window
    pygame.display.set_caption("Shreaker")
    display = pygame.display.set_mode([SCREENW,SCREENH])
    display.fill(LEVEL5BACKGROUND)
    clock = pygame.time.Clock()

    #Plays background music
    pygame.mixer.music.load('Background.wav')
    pygame.mixer.music.play(-1)

    #Declaring the speed of the ball
    speedx = 6
    speedy = 6
    speedx2 = 5
    speedy2 = 5

    #Creating the rect object array
    columns = 5
    rectarray = []
    for y in range(columns):
            for i in range(0, int(SCREENW-1), int(BRICKW)):
                rectarray.append(pygame.Rect(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10))

            
    #Creating the circle object
    pong = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx, speedy)
    pongtwo = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx2, speedy2)
    pongthree = Circle(SCREENW,SCREENH, PADDLEX, PADDLEY, PADDLEW, PADDLEH, speedx2, speedy2)
    
    #Creating boss object
    boss = Boss(800,100,155,230)
    
    #Creating the paddle object
    paddle = Paddle(PADDLEX, PADDLEY, PADDLEW, PADDLEH)

    #Creating the powerup object
    powerup = PowerUps(boss.posx,boss.posy)

    #Creating the brick objects
    bricks = []
    for y in range(columns):
        for i in range(0, int(SCREENW), int(BRICKW)):
            bricks.append(Brick(i + 10, BRICKH * (y+1) + 10 , BRICKW - 10, BRICKH - 10, LEVEL5BRICKCOLOUR))

    #Creating the font for the counter object
    font = pygame.font.SysFont('Arial', 50, bold=True, italic=False)
    counter = 15000
    
    #Creating the PyGame loop, making sure the window stays open
    GameOver = False

    #Creating a boolean flag for when the bricks disappear
    bricksgone = False
    #Declares the boolean flag for spawning the powerups
    spawnpowerup = False
    spawnbomb = False
    spawnplus = False
    spawnarrow = False

    while not GameOver:
        #FPS limit
        clock.tick(64)
        
        for event in pygame.event.get():

            #When the user presses X on the window, the loop stops
            if event.type == pygame.QUIT:
                GameOver = True

        #Updating the value of the score counter
        counter -= 1
        
        #Updating the objects
        pong.update(paddle, rectarray, bricks)
        pongtwo.update(paddle, rectarray, bricks)
        pongthree.update(paddle, rectarray, bricks)
        if bricksgone:
            pong.updateboss(boss)
            pongtwo.updateboss(boss)
            pongthree.updateboss(boss)
            boss.move(mousex)
            if spawnpowerup:
                powerup.updatepowerup(paddle,spawnbomb,spawnplus,spawnarrow,boss)


        #If the ball hits the bottom this happens
        if pong.hit_bottom or pongtwo.hit_bottom or pongthree.hit_bottom:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard5(score)
            
            #Stops the loop
            GameOver = True


        #If all the bricks disappear this happens
        if not rectarray:

            #Sets the boolean flag to true
            bricksgone = True
            
            #Creates the random spawning of the powerups
            num = int(random.randrange(0,300))
            if num == 50:
                #Chooses between a random powerup
                if not spawnpowerup:
                    choice = int(random.randrange(1,4))

                #Makes the update powerup function run
                spawnpowerup = True
    
                #Draws the bomb
                if choice == 1:
                    spawnbomb = True
                    
                    if powerup.posy > paddle.posy:
                        spawnpowerup = False
                        spawnbomb = False
                        del powerup
                        powerup = PowerUps(boss.posx,boss.posy)
                        
                #Draws the plus
                elif choice == 2:
                    spawnplus = True

                    if powerup.posy > paddle.posy:
                        spawnpowerup = False
                        spawnplus = False
                        del powerup
                        powerup = PowerUps(boss.posx,boss.posy)

                #Draws the arrow
                elif choice == 3:
                    spawnarrow = True

                    if powerup.posy > paddle.posy:
                        spawnpowerup = False
                        spawnarrow = False
                        del powerup
                        powerup = PowerUps(boss.posx,boss.posy)       
                    
                
            if boss.hp <= 0:
                #Declares font
                labelfont = ('Arial', 100, 'bold')

                #Gets the final value of the counter
                score = str(counter)
                text = "Your score was ",score
                
                #Opens a window to tell the user they lost and their score
                root = Tk()
                label = tk.Label(root, text="YOU WON! :)", font=labelfont).pack(side="top", fill="x", pady=10)
                label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

                #Updates the high score in the leaderboard
                UpdateLeaderBoard5(score)
                
                #Stops the loop
                GameOver = True
                
            if powerup.hit:
                #Declares font
                labelfont = ('Arial', 100, 'bold')

                #Gets the final value of the counter
                score = '0'
                text = "Your score was ",score
                
                #Opens a window to tell the user they lost and their score
                root = Tk()
                label = tk.Label(root, text="YOU LOST! :(", font=labelfont).pack(side="top", fill="x", pady=10)
                label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

                #Updates the high score in the leaderboard
                UpdateLeaderBoard5(score)
                
                #Stops the loop
                GameOver = True
            

        if counter <= 0:
            #Declares font
            labelfont = ('Arial', 100, 'bold')

            #Gets the final value of the counter
            score = '0'
            text = "Your score was ",score
            
            #Opens a window to tell the user they lost and their score
            root = Tk()
            label = tk.Label(root, text="YOU RAN OUT OF TIME! :(", font=labelfont).pack(side="top", fill="x", pady=10)
            label1 = tk.Label(root, text=text, font=labelfont).pack(side="top", fill="x", pady=10)

            #Updates the high score in the leaderboard
            UpdateLeaderBoard5(score)
            
            #Stops the loop
            GameOver = True
            
            
        #Creating the counter object
        countertext = font.render(str(counter), True, BLACK)
        helptext = font.render("Don't let the counter get to zero!", True, BLACK)

        #Changing the background colour
        display.fill(LEVEL5BACKGROUND)
            
        #Getting the mouse position
        mousex = pygame.mouse.get_pos()[0]

        #Making the paddle move
        paddle.move(mousex)

        #Drawing the paddle
        paddle.draw(display)

        #Drawing the boss and the hp bar
        if bricksgone:
            boss.draw(display)
            boss.drawhpbar(display)

            #Drawing the bomb on the screen
            if spawnbomb:
                powerup.drawbomb(display)

            #Draws the plus powerup
            if spawnplus:
                powerup.drawplus(display)

            #Draws the arrow powerup
            if spawnarrow:
                powerup.drawarrows(display)
                

        #Drawing the bricks
        for i in range(len(bricks)):
                    bricks[i].draw(display)
            
        #Updating the ball
        pong.render(display)
        pongtwo.render(display)
        pongthree.render(display)

        #Puts the text on the screen
        display.blit(countertext,(10,10))
        display.blit(helptext, (350,10))    
                
        #The display will update itself because of this
        pygame.display.flip()
        pygame.display.update()

    #Quits the game            
    pygame.quit()


#All the functions that work behind the menus
#Making the function to get the names into the database
def CallBack(firstnameentry, lastnameentry, controller):

    #Sets the size of the font for the labels in this function
    Font = tkfont.Font(size = 100, weight="bold")
    
    #This gets the input from the entries and puts them into variables    
    first = firstnameentry.get()
    last = lastnameentry.get()
    

    #Tries this chunk of code first to try and find the name in the database, if it doesn't find it, it goes to the exception
    try:

        #Creates a connection with the leaderboard so I can check if the input is already in it
        conn = sqlite3.connect('LeaderBoard.db')

        #Creates a cursor object
        cursor = conn.cursor()

        #Executes the SQL query which checks for the first and last names
        cursor.execute(''' SELECT First_Name, Last_Name FROM Users
                           WHERE First_Name=? AND Last_Name=?''',
                           (first,last))

        #If it exists it puts it into a tuple called result
        result = cursor.fetchall()

        #Changes the tuple into a string and splits it where there is a break
        for i in result:
            strresult =  " ".join(i)
        words = strresult.split(' ')

        #Creates a list and appends the values to the list so they're seperate
        list_result = []
        for i in words:
            list_result.append(i)

        #Commits to the connection
        conn.commit()
        conn.close()
        #If the name is already in the database, it will open a new window and tell the user to go to the main menu
        if list_result[0] == first and list_result[1] == last:
            gui = Tk()
            gui.geometry("800x200")
            label = tk.Label(gui, text="Welcome back", font = Font).pack()
            controller.ShowFrame("MainMenu")

    #If it doesn't find that name in the database it runs this code to put this new user into the database
    except:

        #If the entry has been left blank then the user will be asked to input something
        if len(first) == 0 or len(last) == 0:
            gui = Tk()
            gui.geometry("800x200")
            label = tk.Label(gui, text="Please try again, you haven't put in a name", font = Font).pack()

        #This bit of code checks to see if the last character is blank or not
        elif first[-1] == ' ' or last[-1] == ' ':
            gui = Tk()
            gui.geometry("800x200")
            label = tk.Label(gui, text="Please try again, the last character of your name is blank", font = Font).pack()

        
        elif first.isdigit() or last.isdigit():
            gui = Tk()
            gui.geometry("800x200")
            label = tk.Label(gui, text="Please try again, you have a number in your name", font = Font).pack()
                    
           
        #If they've actually typed in a name, it will add them to the database
        else:
            #Creates a connection with the leaderboard so I can check if the input is already in it
            conn = sqlite3.connect('LeaderBoard.db')

            #Creates a cursor object
            cursor = conn.cursor()

            #Adds the person to the database
            cursor.execute(''' INSERT INTO Users(First_Name,Last_Name) VALUES(?,?)''', (first,last))
            conn.commit()

            #Opens a window and tells the user to go to the main menu
            gui = Tk()
            gui.geometry("800x200")
            label = tk.Label(gui, text="You have been added to the database, have fun!", font = Font).pack()
            controller.ShowFrame("MainMenu")

    StoreDetails(first,last)
    

#Getting the details of the user playing the game            
def StoreDetails(first,last):
    global FIRST
    FIRST = first
    global LAST
    LAST = last

    
#Creating the function that will update the database when the user finishes with level 1
def UpdateLeaderBoard1(score):
    #Creates a connection with the leaderboard so that I can update the data in it
    conn = sqlite3.connect('LeaderBoard.db')
    #Creates a cursor object
    cursor = conn.cursor()

    #Gets the ID of the user to be able to update their score in the other table
    cursor.execute(''' SELECT UserID FROM Users
                       WHERE First_Name=? AND Last_Name=?''',
                       (FIRST,LAST))
    conn.commit()
    
    #Getting the ID of the user into a variable
    userid = cursor.fetchone()
    for i in userid:
        userid = i

    #Checking if this score is better than their previous high score, if there isn't a score it'll just add it
    try:
        cursor.execute('''SELECT High_Score_1 FROM Level_1
                              WHERE UserID=?''',
                              (str(userid)))
        conn.commit()
        oldscore = cursor.fetchone()
        for i in oldscore:
            oldscore = i
        if oldscore > int(score):
            return 1
        else:
            #Replacing the old score with the new score
            cursor.execute(''' REPLACE INTO Level_1(High_Score_1,UserID)
                                   VALUES(?,?)''',
                                   (score,str(userid)))
            conn.commit()
            conn.close()
            
    #If the user hasn't set a score in this level this will happen    
    except:
            #Adding this score into the leaderboard
            cursor.execute(''' REPLACE INTO Level_1(High_Score_1,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()


#Creating the function that will update the database when the user finishes with level 2
def UpdateLeaderBoard2(score):
    #Creates a connection with the leaderboard so that I can update the data in it
    conn = sqlite3.connect('LeaderBoard.db')
    #Creates a cursor object
    cursor = conn.cursor()

    #Gets the ID of the user to be able to update their score in the other table
    cursor.execute(''' SELECT UserID FROM Users
                       WHERE First_Name=? AND Last_Name=?''',                       (FIRST,LAST))
    conn.commit()
    
    #Getting the ID of the user into a variable
    userid = cursor.fetchone()
    for i in userid:
        userid = i

    #Checking if this score is better than their previous high score, if there isn't a score it'll just add it
    try:
        cursor.execute('''SELECT High_Score_2 FROM Level_2
                          WHERE UserID=?''',
                          (str(userid)))
        conn.commit()
        oldscore = cursor.fetchone()
        for i in oldscore:
            oldscore = i
        if oldscore > int(score):
            return 1
        else:
            #Replacing the old score with the new score
            cursor.execute(''' REPLACE INTO Level_2(High_Score_2,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()
            
    #If the user hasn't set a score in this level this will happen    
    except:
            #Adding this score into the leaderboard
            cursor.execute(''' REPLACE INTO Level_2(High_Score_2,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()


#Creating the function that will update the database when the user finishes with level 3
def UpdateLeaderBoard3(score):
    #Creates a connection with the leaderboard so that I can update the data in it
    conn = sqlite3.connect('LeaderBoard.db')
    #Creates a cursor object
    cursor = conn.cursor()

    #Gets the ID of the user to be able to update their score in the other table
    cursor.execute(''' SELECT UserID FROM Users
                       WHERE First_Name=? AND Last_Name=?''',
                       (FIRST,LAST))
    conn.commit()
    
    #Getting the ID of the user into a variable
    userid = cursor.fetchone()
    for i in userid:
        userid = i

    #Checking if this score is better than their previous high score, if there isn't a score it'll just add it
    try:
        cursor.execute('''SELECT High_Score_3 FROM Level_3
                          WHERE UserID=?''',
                          (str(userid)))
        conn.commit()
        oldscore = cursor.fetchone()
        for i in oldscore:
            oldscore = i
        if oldscore > int(score):
            return 1
        else:
            #Replacing the old score with the new score
            cursor.execute(''' REPLACE INTO Level_3(High_Score_3,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()
            
    #If the user hasn't set a score in this level this will happen    
    except:
            #Adding this score into the leaderboard
            cursor.execute(''' REPLACE INTO Level_3(High_Score_3,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()


#Creating the function that will update the database when the user finishes with level 4
def UpdateLeaderBoard4(score):
    #Creates a connection with the leaderboard so that I can update the data in it
    conn = sqlite3.connect('LeaderBoard.db')
    #Creates a cursor object
    cursor = conn.cursor()

    #Gets the ID of the user to be able to update their score in the other table
    cursor.execute(''' SELECT UserID FROM Users
                       WHERE First_Name=? AND Last_Name=?''',
                       (FIRST,LAST))
    conn.commit()
    
    #Getting the ID of the user into a variable
    userid = cursor.fetchone()
    for i in userid:
        userid = i

    #Checking if this score is better than their previous high score, if there isn't a score it'll just add it
    try:
        cursor.execute('''SELECT High_Score_4 FROM Level_4
                          WHERE UserID=?''',
                          (str(userid)))
        conn.commit()
        oldscore = cursor.fetchone()
        for i in oldscore:
            oldscore = i
        if oldscore > int(score):
            return 1
        else:
            #Replacing the old score with the new score
            cursor.execute(''' REPLACE INTO Level_4(High_Score_4,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()
            
    #If the user hasn't set a score in this level this will happen    
    except:
            #Adding this score into the leaderboard
            cursor.execute(''' REPLACE INTO Level_4(High_Score_4,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()


#Creating the function that will update the database when the user finishes with level 5
def UpdateLeaderBoard5(score):
    #Creates a connection with the leaderboard so that I can update the data in it
    conn = sqlite3.connect('LeaderBoard.db')
    #Creates a cursor object
    cursor = conn.cursor()

    #Gets the ID of the user to be able to update their score in the other table
    cursor.execute(''' SELECT UserID FROM Users
                       WHERE First_Name=? AND Last_Name=?''',
                       (FIRST,LAST))
    conn.commit()
    
    #Getting the ID of the user into a variable
    userid = cursor.fetchone()
    for i in userid:
        userid = i

    #Checking if this score is better than their previous high score, if there isn't a score it'll just add it
    try:
        cursor.execute('''SELECT High_Score_5 FROM Level_5
                          WHERE UserID=?''',
                          (str(userid)))
        conn.commit()
        oldscore = cursor.fetchone()
        for i in oldscore:
            oldscore = i
        if oldscore > int(score):
            return 1
        else:
            #Replacing the old score with the new score
            cursor.execute(''' REPLACE INTO Level_5(High_Score_5,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()
            
    #If the user hasn't set a score in this level this will happen    
    except:
            #Adding this score into the leaderboard
            cursor.execute(''' REPLACE INTO Level_5(High_Score_5,UserID)
                               VALUES(?,?)''',
                               (score,str(userid)))
            conn.commit()
            conn.close()


#Calling the menus function to start the game
app = Menus()
app.mainloop()


