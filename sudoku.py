import tkinter as tk
import tkinter.ttk
import random
import mapGenerator
import boxClass
import sudokuClass

#   ITU, 2019, 2BIT
#   Authors: Radoslav Páleník <xpalen05@stud.fit.vutbr.cz>, Daniel Pohančaník <xpohan03@stud.fit.vutbr.cz>, Michal Řezáč <xrezac20@stud.fit.vutbr.cz>


#Hodnota, ktorou sa zadáva vstup z myši do poľa
inputVal = 1

def selectValue(val):
    global inputVal
    print(str(val))
    inputVal = val

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, GameScreen,SettingsMenu, LeaderboardMenu, backtoGameSettingsMenu, SummaryScreen):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu, False)

    def show_frame(self, cont, wasInGame):

        if wasInGame and (cont == SettingsMenu):
            cont = backtoGameSettingsMenu
        

        frame = self.frames[cont]
        frame.configure(bg = "#2c3c43")
        frame.tkraise()
        
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Nastavenia okna Menu 

        self.grid_columnconfigure(0, weight = 1)

        self.grid_columnconfigure(1, weight = 5)

        self.grid_columnconfigure(2, weight = 1)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 0, row =0)

        tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 2, row =0)

        self.grid_rowconfigure(0, weight = 15)
        self.grid_rowconfigure(1, weight = 10)
        self.grid_rowconfigure(2, weight = 5)
        self.grid_rowconfigure(3, weight = 10)
        self.grid_rowconfigure(4, weight = 5)
        self.grid_rowconfigure(5, weight = 10)
        self.grid_rowconfigure(6, weight = 5)
        self.grid_rowconfigure(7, weight = 10)
        self.grid_rowconfigure(8, weight = 15)

        #Koniec nastaveni okna Menu


        tk.Label(self, text = "Menu", bg = "#2c3c43", fg = "#7aa719",font=("Times New Roman", 20, "bold")).grid(row = 0, column = 1)

        Continue = tk.Button(self, text="Continue", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#7aa719", state = "disabled",
                            command=lambda: controller.show_frame(GameScreen, False)).grid(row = 1, column = 1)

        newGame = tk.Button(self, text="New Game", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(GameScreen, False)).grid(row = 3, column = 1)

        Settings = tk.Button(self, text="Settings", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(SettingsMenu, False)).grid(row = 5, column = 1)

        Leaderboard = tk.Button(self, text="Leaderboard", font = ("Times New Roman", 12, "bold", "italic"),highlightthickness = 0,bd =0,  width = 75, height = 3,bg = "#a7e02c",
                            command=lambda: controller.show_frame(LeaderboardMenu, False)).grid(row = 7, column = 1)


class GameScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        #Nastavenia okna Leaderboard
        self.grid_columnconfigure(0, weight = 10)

        self.grid_columnconfigure(1, weight = 80)

        self.grid_columnconfigure(2, weight = 10)

        leftBar = tk.Frame(self, width = 25)
        leftBar.grid(column = 0, row =2)

        for x in range(0,9):
            tk.Button(leftBar, text = x+1, fg = "#a7e02c",bg = "#2c3c43", font = ("Helvetica 18 bold"),
             highlightthickness = 0, bd = 0, pady = 20, padx = 20,
              command = lambda val = x+1: selectValue(val)).grid(column = 0, row = x)
            

        self.grid_rowconfigure(0, weight = 5)
        self.grid_rowconfigure(1, weight = 15)
        self.grid_rowconfigure(2, weight = 70)
        self.grid_rowconfigure(3, weight = 5)
        #Koniec nastaveni okna Leaderboard

        #Horna Navigacia
        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0,  height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(MainMenu, False)).grid(row = 0, column = 0)

        jumpToSettings = tk.Button(self, text="Settings",highlightthickness = 0,  height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(SettingsMenu, True)).grid(row = 0, column = 2)
 
        #Matica 9x9
        playMatrix = tk.Frame(self, bg = "#222e34")
        playMatrix.grid(column = 1, row = 2)

        sdkBtn =  [[0 for x in range(11)] for x in range(11)]

        #Generovanie Matice 
        fullBoard = mapGenerator.make_board(3)

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
                        bgcol = "#4a6571"


                    sdkBtn[act_row][act_col] = tk.Button(playMatrix,width = 5, height = 3,
                     bg = bgcol, fg = "#7aa719", font = ('Helvetica 15 bold') ,command = lambda i=act_row, j=act_col : putValue(i, j, inputVal, controller),
                      highlightthickness = 0, bd = 0,)
                    sdkBtn[act_row][act_col].grid(row = rows, column = columns)
                else:
                    if rows == 3 or rows == 7:
                        tkinter.ttk.Separator(playMatrix, orient=tk.HORIZONTAL).grid(column=columns, row=rows, columnspan=1, sticky='we')
                    else:
                        tkinter.ttk.Separator(playMatrix, orient=tk.VERTICAL).grid(column=columns, row=rows, rowspan=1, sticky='ns')

        #Vyplnenie nahodnych cislic, tak aby boli na kazdom riadku vyplnene aspon 2 a celkovo 24 cislic v celej matici
        for x in range(0,9):
            toShowPosition = random.randint(0,8)
            sdkBtn[x][toShowPosition]['text'] = fullBoard[x][toShowPosition]
            sdkBtn[x][toShowPosition].configure(state = "disabled")
            toShowAnotherPosition = random.randint(0,8)
            while toShowAnotherPosition == toShowPosition:
                toShowAnotherPosition = random.randint(0,8)
            sdkBtn[x][toShowAnotherPosition]['text'] =  fullBoard[x][toShowAnotherPosition]
            sdkBtn[x][toShowAnotherPosition].configure(state = "disabled")
            

        numsShown = 18
        while numsShown < 25:
            randX = random.randint(0,8)
            randY = random.randint(0,8)

            while sdkBtn[randX][randY]['text']:
                randX = random.randint(0,8)
                randY = random.randint(0,8)

            sdkBtn[randX][randY]['text'] =  fullBoard[randX][randY]
            sdkBtn[randX][randY].configure(state = "disabled")
            numsShown += 1
            

        #controler pre zmenu vlastnosti na danej pozicii v poli
        def putValue( x, y, val, cont):
            print("changing value ["+str(x)+"]["+str(y)+"]")
            sdkBtn[x][y].configure(text = str(val))

            isMatrixCorrect = True

            for rows in range(0,9):
                for columns in range(0,9):
                    if not sdkBtn[rows][columns]['text']:
                        isMatrixCorrect = False
                        break;

                    if int(sdkBtn[rows][columns]['text']) != fullBoard[rows][columns]:
                        isMatrixCorrect = False
            print(str(isMatrixCorrect))
            if isMatrixCorrect:
                cont.show_frame(SummaryScreen, False)
        
class SettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        #Nastavenia okna Settings
        self.grid_columnconfigure(0,weight = 1)
        self.grid_columnconfigure(1,weight = 5)
        self.grid_columnconfigure(2,weight = 1)


        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1, bg = "#a7e02c",
                           command=lambda: controller.show_frame(MainMenu, False)).grid(row = 0, column = 0)
        #Moj Super CHEAT
        tk.Button(self, text="",highlightthickness = 0, width = 10, height = 1, bg = "#2c3c43", bd = 0,
                           command=lambda: controller.show_frame(MainMenu, False)).grid(row = 0, column = 3)

        tk.Label(self, text = "Settings", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 20, "bold"), pady = 15).grid( row = 0, column = 1)

        tk.Checkbutton(self, text ='Show count from each number left in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3,  font= ("Times New Roman", 15,"bold"),
                takefocus = 0, ).grid(row = 1, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Show button to validate progress of game', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 2, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Highlight column and row on item hover', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 3, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Enable adding notes in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 4, column = 1,pady = 15,  sticky ="we")


class backtoGameSettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        self.grid_columnconfigure(0,weight = 1)
        self.grid_columnconfigure(1,weight = 5)
        self.grid_columnconfigure(2,weight = 1)


        backToMenu = tk.Button(self, text="Back to Game",highlightthickness = 0, width = 10, height = 1, bg = "#a7e02c",
                           command=lambda: controller.show_frame(GameScreen, False)).grid(row = 0, column = 0)
        #Moj Super CHEAT
        tk.Button(self, text="",highlightthickness = 0, width = 10, height = 1, bg = "#2c3c43", bd = 0,
                           command=lambda: controller.show_frame(MainMenu, False)).grid(row = 0, column = 3)

        tk.Label(self, text = "Settings", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 20, "bold"), pady = 15).grid( row = 0, column = 1)

        tk.Checkbutton(self, text ='Show count from each number left in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3,  font= ("Times New Roman", 15,"bold"),
                takefocus = 0, ).grid(row = 1, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Show button to validate progress of game', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 2, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Highlight column and row on item hover', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 3, column = 1,pady = 15,  sticky ="we")

        tk.Checkbutton(self, text ='Enable adding notes in matrix', bg = "#a7e02c", bd = 0, highlightthickness = 0,  height = 3, font= ("Times New Roman", 15,"bold"), 
                takefocus = 0, ).grid(row = 4, column = 1,pady = 15,  sticky ="we")

class SummaryScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        tk.Label(self, text = "You did it!", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 50, "bold", "italic")).place(x = 250, y=250)
        tk.Label(self, text = "Your final time will be here", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 30, "bold")).place(x = 450, y=350)


        backToMenu = tk.Button(self, text="{0}:{1}".format(random.randint(0,3), random.randint(0,59)),highlightthickness = 0, width = 10, height = 1,bg = "#a7e02c",
                            command=lambda: controller.show_frame(MainMenu, False)).place(x=50,y=50)


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


        tk.Label(self, text = "Leaderboard", bg = "#2c3c43", fg = "#7aa719", font=("Times New Roman", 20, "bold")).grid(row = 1, column = 1)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu, False))
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

   
app = MainWindow()
app.minsize(900,700)
app.title("Sudoku")
app.mainloop()