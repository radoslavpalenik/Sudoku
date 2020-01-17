import tkinter as tk
import tkinter.ttk
import random
import mapGenerator
import boxClass
import sudokuClass as sc
import copy
import itertools
from collisionDetector import collisionDetector as cd


#   ITU, 2019, 2BIT
#   Authors: Radoslav Páleník <xpalen05@stud.fit.vutbr.cz>, Daniel Pohančaník <xpohan03@stud.fit.vutbr.cz>, Michal Řezáč <xrezac20@stud.fit.vutbr.cz>


#Hodnota, ktorou sa zadáva vstup z myši do poľa
inputVal = 1
seconds = 0
minutes = 0
sudoku = sc.Sudoku()
sdkBtn =  [[0 for x in range(11)] for x in range(11)]
lastEdited = 0
gBtn = [tk.Button]
beforeFirstGame = 1
numLeft = [None]*9 
showNumbersLeft = 0


def selectValue(val, self):
    global inputVal
    global gBtn
    inputVal = val
    
def selectKeyboardValue(val):
    global gBtn
    global inputVal
    for i in range (1,10):
        gBtn[i].configure(bg = "#2c3c43", fg = "#a7e02c" )
    val = val.char
    inputVal = int(val)
    gBtn[int(val)]['bg'] = "#a7e02c"
    gBtn[int(val)]['fg'] = "#2c3c43"
    

class TopScreenStruct:
    def __init__(self):
        self.actualScreen = 0

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
    
        self.screen = TopScreenStruct()
        global seconds
        global minutes
        seconds = 0
        minutes = 0
        self.seconds = 0
        self.minutes = 0
        # label displaying time
        self.label = tk.Label(self, text="0 s", font="Arial 30", width=20 , bg ="#2c3c43", foreground = "#a7e02c")
        self.label.pack()
        # start the timer
        self.label.after(10, self.refresh_label)

        container.pack(side="bottom",  fill = "both")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (MainMenu, GameScreen, SettingsMenu, LeaderboardMenu, backtoGameSettingsMenu, SummaryScreen, levelSelect):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu, False, False,0)

    def show_frame(self, cont, wasInGame, isNewGame, Level):

        global minutes
        global seconds
        global sudoku
        global sdkBtn
        global beforeFirstGame

        if wasInGame and (cont == SettingsMenu):
            cont = backtoGameSettingsMenu

        if isNewGame:
            seconds = 0
            minutes = 0
            beforeFirstGame = 0


            for x in range(0,9):
                for y in range (0,9):
                    sdkBtn[x][y].configure(text = "")
                    

            if Level > 0:
                sudoku.reset(Level)
                if showNumbersLeft == 1:
                    for num in range(0,9):
                        numLeft[num]["text"] = sudoku.checkMissing(num+1)



            for x in range(0,9):
                for y in range (0,9):

                    sdkBtn[x][y].configure(text = sudoku.gameBoard[x][y])
                    if(sudoku.gameBoard[x][y] != None):
                        sdkBtn[x][y].configure(state = "disabled")
                    else:
                        sdkBtn[x][y].configure(state = "normal")


        if cont == GameScreen:
            self.screen.actualScreen = 1

        elif cont == SettingsMenu or cont == backtoGameSettingsMenu:
            self.screen.actualScreen = 2

        elif cont == LeaderboardMenu:
            self.screen.actualScreen = 3

        elif cont == levelSelect:
            self.screen.actualScreen = 5

        elif cont == SummaryScreen:
            self.screen.actualScreen = 4

        else:
            self.screen.actualScreen = 0

        frame = self.frames[cont]
        frame.configure(bg = "#2c3c43")
        frame.tkraise()

    def refresh_label(self):
        global minutes
        global seconds
        self.label.configure(fg = "#a7e02c")
        self.label.configure(text="%.2i" % minutes+" : %.2i" % seconds)
        
        if self.screen.actualScreen == 1:
            self.seconds += 0.01
            seconds += 0.01
            if self.seconds >= 60.00:
                self.seconds = self.seconds-60.0
                seconds = self.seconds
                self.minutes += 1
                minutes += 1
                

        elif self.screen.actualScreen == 2:    
            self.label.configure(text = "Settings")
            

        elif self.screen.actualScreen == 3:
            self.label.configure(text = "Leaderboard")

        elif self.screen.actualScreen == 5:
            self.label.configure(text = "Choose game difficulty")

        elif self.screen.actualScreen == 4:
            self.label.configure(fg = "#2c3c43")
           

        else:
            self.label.configure(text = "Menu")
           

        self.label.after(10, self.refresh_label)

    def ManageTopBtns(self):

        if self.screen.actualScreen == 1:
            self.leftBtn.configure(text = "Menu")

        elif self.screen.actualScreen == 2:    
            self.leftBtn.configure(text = "Settings")

        elif self.screen.actualScreen == 3:
            self.leftBtn.configure(text = "Leaderboard")

        elif self.screen.actualScreen == 4:
            self.leftBtn.configure(fg = "#2c3c43")
           

        else:
            self.leftBtn.configure(text = "Menu")
           

        self.label.after(100, self.refresh_label)


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Nastavenia okna Menu 

        self.grid_columnconfigure(0, weight = 1)

        self.grid_columnconfigure(1, weight = 5)

        self.grid_columnconfigure(2, weight = 1)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 0, row =0)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 2, row =0)

        self.grid_rowconfigure(1, weight = 10)
        self.grid_rowconfigure(2, weight = 5)
        self.grid_rowconfigure(3, weight = 10)
        self.grid_rowconfigure(4, weight = 5)
        self.grid_rowconfigure(5, weight = 10)
        self.grid_rowconfigure(6, weight = 5)
        self.grid_rowconfigure(7, weight = 10)
        self.grid_rowconfigure(8, weight = 15)

        #Koniec nastaveni okna Menu

        self.Continue = tk.Button(self, text="Continue", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c", 
                            command=lambda: controller.show_frame(GameScreen, False, False,0))
        self.Continue.grid(row = 1, column = 1)
        
        self.Continue.after(10, self.checkIfContinue)

        newGame = tk.Button(self, text="New Game", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(levelSelect, False, False,0)).grid(row = 3, column = 1)

        Settings = tk.Button(self, text="Settings", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(SettingsMenu, False, False,0)).grid(row = 5, column = 1)

        Leaderboard = tk.Button(self, text="Leaderboard", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(LeaderboardMenu, False, False,0)).grid(row = 7, column = 1)

    def checkIfContinue(self):
        	global beforeFirstGame

        	if beforeFirstGame == 1:
        		self.Continue.configure(state = "disabled",bg = "#7aa719")
        	else:
        		self.Continue.configure(state = "normal",bg = "#a7e02c")

        	self.Continue.after(100, self.checkIfContinue)


class GameScreen(tk.Frame):

    

    
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Nastavenia okna Leaderboard
        self.grid_columnconfigure(0, weight = 10)

        self.grid_columnconfigure(1, weight = 80)

        self.grid_columnconfigure(2, weight = 10)

        leftBar = tk.Frame(self, width = 25,bg = "#2c3c43")
        leftBar.grid(column = 0, row =2)

        
        

        self.grid_rowconfigure(1, weight = 5)
        self.grid_rowconfigure(0, weight = 15)
        self.grid_rowconfigure(2, weight = 70)
        self.grid_rowconfigure(3, weight = 5)
        self.grid_rowconfigure(4, weight = 5)

        bottomBar = tk.Frame(self)
        bottomBar.grid(row = 3, column = 1)
    
        #btn = [tk.Button]*10
        global gBtn
        btn = [tk.Button]*10
        for i in range(1,10):
            btn[i] = tk.Button(bottomBar, text = i, fg = "#a7e02c",bg = "#2c3c43", font = ("Helvetica 18 bold"),
                highlightthickness = 0, bd = 0, pady = 20, padx = 20)
            gBtn.append(btn[i])
            btn[i].grid(column = i, row = 0)

        btn[1].configure(command = lambda: resetColor(btn[1], 1))
        btn[2].configure(command = lambda: resetColor(btn[2], 2))
        btn[3].configure(command = lambda: resetColor(btn[3], 3))
        btn[4].configure(command = lambda: resetColor(btn[4], 4))
        btn[5].configure(command = lambda: resetColor(btn[5], 5))
        btn[6].configure(command = lambda: resetColor(btn[6], 6))
        btn[7].configure(command = lambda: resetColor(btn[7], 7))
        btn[8].configure(command = lambda: resetColor(btn[8], 8))
        btn[9].configure(command = lambda: resetColor(btn[9], 9))
        

        def changeBg(self, val):
            self.configure(bg = "#a7e02c" , fg = "#2c3c43" )
            selectValue(val, self)

        def resetColor(self, val):
            for i in range(1,10):
                btn[i].configure(bg = "#2c3c43", fg = "#a7e02c" )
            changeBg(self, val)
        #Koniec nastaveni okna Leaderboard



        #Horna Navigacia
        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0,  height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(MainMenu, False, False,0)).grid(row = 0, column = 0, padx = 20)

        jumpToSettings = tk.Button(self, text="Settings",highlightthickness = 0,  height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(SettingsMenu, True, False,0)).grid(row = 0, column = 2, padx = 20)

       
 
        #Matica 9x9
        playMatrix = tk.Frame(self, bg = "#222e34")
        playMatrix.grid(column = 1, row = 2)

        

        # Game grid
        for x in range(0,9):
            playMatrix.grid_columnconfigure(x, weight = 1)
            playMatrix.grid_rowconfigure(x, weight = 1)

        for rows in range(0,11):
            for columns in range(0,11):

                if columns != 3 and columns != 7 and rows != 3 and rows != 7:
                    act_col = columns
                    act_row = rows
                    bgcol = "#2c3c43"
                    
                    #Potrebne posunutie matice pokial pride vykreslovanie na ciaru
                    if columns > 3:
                        if columns > 7:
                            act_col = act_col -1
                        act_col = act_col -1
                    if rows > 3:
                        if rows > 7:
                            act_row = act_row -1
                        act_row = act_row -1

                    #Prepinanie farieb pre lepsiu prehladnost aplikacie
                    if ((columns <= 2 or columns >= 7) and (rows <= 2 or rows >=7)) or ((columns > 2 and columns < 7 ) and (rows > 3 and rows < 8)) :
                        bgcol = "#1e292f"


                    sdkBtn[act_row][act_col] = tk.Button(playMatrix,width = 5, height = 3,
                     bg = bgcol, fg = "#7aa719", font = ('Helvetica 15 bold') ,command = lambda i=act_row, j=act_col : putValue(i, j, inputVal, controller),
                      highlightthickness = 0, bd = 0,)
                    sdkBtn[act_row][act_col].grid(row = rows, column = columns)
                    
                else:
                    if rows == 3 or rows == 7:
                        tkinter.ttk.Separator(playMatrix, orient=tk.HORIZONTAL).grid(column=columns, row=rows, columnspan=1, sticky='we')
                    else:
                        tkinter.ttk.Separator(playMatrix, orient=tk.VERTICAL).grid(column=columns, row=rows, rowspan=1, sticky='ns')

   
        global sudoku
        
        helpFrame = tk.Frame(self)
        helpFrame.grid(row = 4, column = 1)
        global numLeft

        for x in range(0,9):
        	numLeft[x] = tk.Label(helpFrame,text = "", bg = "#2c3c43", fg = "#7aa719", font = ("Helvetica 18 bold"),highlightthickness = 0,padx = 20)
        	numLeft[x].grid( row = 0, column = x)

        #controler pre zmenu vlastnosti na danej pozicii v poli
        def putValue( x, y, val, cont):
            sdkBtn[x][y].configure(text = str(val))
            sudoku.gameBoard[x][y] = val

            if(mapGenerator.checkIfSolved(sudoku.gameBoard)):
                cont.show_frame(SummaryScreen, False, False,0)

            if enableCollisionCheck.get() == 1:
                cd.markCollision(x, y, sudoku.gameBoard, sdkBtn)

            if showNumbersLeft == 1:
                for number in range(0,9):
                    numslft = sudoku.checkMissing(number+1)
                    numLeft[number]["text"] = numslft
                    if numslft < 0:
                        numLeft[number]["fg"] = "red"
                    else:
                         numLeft[number]["fg"] = "#7aa719"
        
            
        
class SettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        #Nastavenia okna Settings
        self.grid_columnconfigure(0,weight = 1)
        self.grid_columnconfigure(1,weight = 5)
        self.grid_columnconfigure(2,weight = 1)


        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1, bg = "#a7e02c",
                           command=lambda: controller.show_frame(MainMenu, False, False,0)).grid(row = 0, column = 0)
        #Moj Super CHEAT
        tk.Button(self, text="",highlightthickness = 0, width = 10, height = 1, bg = "#2c3c43", bd = 0,
                           command=lambda: controller.show_frame(SummaryScreen, False, False, 0)).grid(row = 0, column = 3)

        global enableCollisionCheck
        enableCollisionCheck = tk.IntVar()
       

        tk.Checkbutton(self, text ='Show count from each number left in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3,  font= ("Times New Roman", 15,"bold"),
                takefocus = 0, variable =  showNumbersLeft,onvalue = 1, offvalue = 0,command = self.switchShowNumbers ).grid(row = 1, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Show button to validate progress of game', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 2, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Highlight column and row on item hover', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 3, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Enable adding notes in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 4, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Enable automatic collision checking', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3,  font= ("Times New Roman", 15,"bold"),
                takefocus = 0, variable = enableCollisionCheck).grid(row = 5, column = 1,pady = 15,  sticky ="we")

    def switchShowNumbers(self):
        global showNumbersLeft
        if showNumbersLeft == 1:
            showNumbersLeft = 0
            
            for number in range(0,9):
                numLeft[number]["text"] = ""
        else:
            showNumbersLeft = 1
            for num in range(0,9):
                numLeft[num]["text"] = sudoku.checkMissing(num+1)

class backtoGameSettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        self.grid_columnconfigure(0,weight = 1)
        self.grid_columnconfigure(1,weight = 5)
        self.grid_columnconfigure(2,weight = 1)


        backToMenu = tk.Button(self, text="Back to Game",highlightthickness = 0, width = 10, height = 1, bg = "#a7e02c",
                           command=lambda: controller.show_frame(GameScreen, False, False,0)).grid(row = 0, column = 0)
        #Moj Super CHEAT
        tk.Button(self, text="",highlightthickness = 0, width = 10, height = 1, bg = "#2c3c43", bd = 0,
                           command=lambda: controller.show_frame(MainMenu, False, False,0)).grid(row = 0, column = 3)

        tk.Checkbutton(self, text ='Show count from each number left in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3,  font= ("Times New Roman", 15,"bold"),
                takefocus = 0, variable =  showNumbersLeft,onvalue = 1, offvalue = 0,command = self.switchShowNumbers ).grid(row = 1, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Show button to validate progress of game', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 2, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Highlight column and row on item hover', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 3, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Enable adding notes in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 4, column = 1,pady = 15,  sticky ="we")

    def switchShowNumbers(self):
        global showNumbersLeft
        if (showNumbersLeft == 1):

                showNumbersLeft = 0
                for number in range(0,9):
                    numLeft[number]["text"] = ""
        else:
                showNumbersLeft = 1
                for num in range(0,9):
                    numLeft[num]["text"] = sudoku.checkMissing(num+1)

class SummaryScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        global seconds
        global minutes

        tk.Label(self, text = "You did it!", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 50, "bold", "italic")).place(x = 250, y=250)
        self.timeLabel = tk.Label(self, text = "Your time: {0:02d}:{1:02d}".format(minutes, seconds), bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 30, "bold"))
        self.timeLabel.place(x = 450, y = 350)


        self.timeLabel.after(10, self.chcekTime)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(MainMenu, False, False,0)).place(x=50,y=50)

    global beforeFirstGame
    beforeFirstGame = 1
    
    def chcekTime(self):
	        global minutes
	        global seconds

	        self.timeLabel.configure(text="%.2i" % minutes+" : %.2i" % seconds)
	        self.timeLabel.after(100, self.chcekTime)

        

class LeaderboardMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        #Nastavenia okna Leaderboard
        self.grid_columnconfigure(0, weight = 1)

        self.grid_columnconfigure(1, weight = 8)

        self.grid_columnconfigure(2, weight = 1)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 0, row =0)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 2, row =0)

        self.grid_rowconfigure(0, weight = 5)
        self.grid_rowconfigure(1, weight = 15)
        self.grid_rowconfigure(2, weight = 75)
        self.grid_rowconfigure(3, weight = 5)
        #Koniec nastaveni okna Leaderboard

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu, False, False,0))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.grid(row = 1, column = 0)

        #LEADERBOARD

        table = tk.Frame(self, width = 100)
        table.grid(row = 2, column = 1)

        #Nastavenie Leaderboardu

        table.grid_columnconfigure(0,weight = 1)
        table.grid_columnconfigure(1,weight = 5)
        table.grid_columnconfigure(2,weight = 4)

        #Koniec nastaveni Leaderboardu

        #Vrchny riadok Leaderboardu

        topPosition = tk.Label(table, text = "Position", fg = "#7aa719", width = 15, height = 3, bg = "#222e34")
        topPosition.grid(column = 0, row =0)

        topTime = tk.Label(table, text = "Time", fg = "#7aa719", width = 35, height = 3, bg = "#222e34")
        topTime.grid(column = 1, row =0)

        topDate = tk.Label(table, text = "Date", fg = "#7aa719", width = 25, height = 3, bg = "#222e34")
        topDate.grid(column = 2, row =0)

        #Vykreslovanie Leaderboardu

        nth_row = 0
        bgcol = "#4a6571"

        for pos in range(1,11):

            if (nth_row % 2) :
                bgcol = "#4a6571"
            else:
                bgcol = "#7aa719"

            topRecordPosition = tk.Label(table, text = pos, width = 15, height = 3, bg = bgcol)
            topRecordPosition.grid(column = 0, row = pos)

            topRecordTime = tk.Label(table, text = "Best Time " + str(pos), width = 35, height = 3, bg = bgcol)
            topRecordTime.grid(column = 1, row = pos)

            topRecordDate = tk.Label(table, text = "Date of time", width = 25, height = 3, bg = bgcol)
            topRecordDate.grid(column = 2, row = pos)

            nth_row+=1


class levelSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        

       	self.grid_columnconfigure(0, weight = 1)

        self.grid_columnconfigure(1, weight = 5)

        self.grid_columnconfigure(2, weight = 1)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 0, row =0)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 2, row =0)

        self.grid_rowconfigure(0, weight = 20)
        self.grid_rowconfigure(1, weight = 10)
        self.grid_rowconfigure(2, weight = 5)
        self.grid_rowconfigure(3, weight = 10)
        self.grid_rowconfigure(4, weight = 5)
        self.grid_rowconfigure(5, weight = 10)
        self.grid_rowconfigure(6, weight = 40)

         

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(MainMenu, False, False,0)).place(x=50,y=50)
        

        tk.Button(self, text="Easy", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(GameScreen, False, True,1)).grid(row = 1, column = 1)

        tk.Button(self, text="Medium", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(GameScreen, False, True,2)).grid(row = 3, column = 1)

        tk.Button(self, text="Hard", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(GameScreen, False, True,3)).grid(row = 5, column = 1)

app = MainWindow()
app.minsize(800,600)
app.title("Sudoku")
app.configure(bg = "#2c3c43")
for i in range(1,10):
    app.bind(str(i), selectKeyboardValue)
app.mainloop()