import tkinter as tk

import time




class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, GameScreen,SettingsMenu, LeaderboardMenu, backtoGameSettingsMenu):

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

        self.grid_columnconfigure(1, weight = 3)

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

        Continue = tk.Button(self, text="Continue",highlightthickness = 0, width = 75, height = 3,
                            command=lambda: controller.show_frame(GameScreen, False))
        Continue.configure(bg = "#a7e02c")
        #Continue.place(x=200,y=100)
        Continue.grid(row = 1, column = 1)



        newGame = tk.Button(self, text="New Game",highlightthickness = 0, width = 75, height = 3,
                            command=lambda: controller.show_frame(GameScreen, False))
        newGame.configure(bg = "#a7e02c")
        #newGame.place(x=200,y=200)
        newGame.grid(row = 3, column = 1)


        Settings = tk.Button(self, text="Settings",highlightthickness = 0, width = 75, height = 3,
                            command=lambda: controller.show_frame(SettingsMenu, False))
        Settings.configure(bg = "#a7e02c")
        #Settings.place(x=200,y=300)
        Settings.grid(row = 5, column = 1)

        
        Leaderboard = tk.Button(self, text="Leaderboard",highlightthickness = 0, width = 75, height = 3,
                            command=lambda: controller.show_frame(LeaderboardMenu, False))
        Leaderboard.configure(bg = "#a7e02c")
        #Leaderboard.place(x=200,y=400)
        Leaderboard.grid(row = 7, column = 1)

class GameScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        #Nastavenia okna Leaderboard
        self.grid_columnconfigure(0, weight = 10)

        self.grid_columnconfigure(1, weight = 80)

        self.grid_columnconfigure(2, weight = 10)

       # tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 0, row =0)

        #tk.Label(self, bg = "#2c3c43", width = 25).grid(column = 2, row =0)

        self.grid_rowconfigure(0, weight = 5)
        self.grid_rowconfigure(1, weight = 15)
        self.grid_rowconfigure(2, weight = 70)
        self.grid_rowconfigure(3, weight = 5)
        #Koniec nastaveni okna Leaderboard


    
        tk.Label(self, text = "HERE WILL BE STOPWATCH", bg = "#2c3c43", fg = "#7aa719", font=("Times New Roman", 20, "bold")).grid(row = 1, column = 1)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0,  height = 1,
                            command=lambda: controller.show_frame(MainMenu, False))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.grid(row = 0, column = 0)

        jumpToSettings = tk.Button(self, text="Settings",highlightthickness = 0,  height = 1,
                            command=lambda: controller.show_frame(SettingsMenu, True))
        jumpToSettings.configure(bg = "#a7e02c")
        jumpToSettings.grid(row = 0, column = 2)




        playMatrix = tk.Frame(self, bg = "#222e34",   height = 600)
        playMatrix.grid(column = 1, row = 2)

        sdkBtn =  [[0 for x in range(9)] for x in range(9)]

        # Herny grid
       	for x in range(0,9):
       		playMatrix.grid_columnconfigure(x, weight = 1)
       		playMatrix.grid_rowconfigure(x, weight = 1)

       	for rows in range(0,9):
       		for columns in range(0,9):
       			sdkBtn[rows][columns] = tk.Button(playMatrix,text = str(rows)+str(columns), width = 10, height = 3, bg = "green", highlightthickness = 0,
       			 command = lambda i=rows, j=columns : colorChange(i, j) )
       			sdkBtn[rows][columns].grid(row = rows, column = columns)
       	
       	#controler pre zmenu vlastnosti na danej pozicii v poli
       	def colorChange( x ,y):
       		sdkBtn[x][y].configure(bg = "red")
       		pass
       	 


        
class SettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        tk.Label(self, text = "Settings", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 20, "bold")).place(x = 320, y=50)


       
       

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu, False))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.place(x=50,y=50)

        numbersLeft = tk.Checkbutton(self, text ='Show count of each number left', 
                     takefocus = 0, bg = "#2c3c43", activebackground = "#2c3c43", highlightthickness = 0, font=(20), fg = "#7aa719").place(x = 150, y = 150) 
        validateGame = tk.Checkbutton(self, text ='Show button to validate your progress in game', 
                     takefocus = 0, bg = "#2c3c43", activebackground = "#2c3c43", highlightthickness = 0, font=(20), fg = "#7aa719").place(x = 150, y = 200) 

class backtoGameSettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        tk.Label(self, text = "Settings", bg = "#2c3c43", fg = "#7aa719",  font=("Times New Roman", 20, "bold")).place(x = 320, y=50)


       
       

        backToMenu = tk.Button(self, text="Back to Game",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(GameScreen, False))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.place(x=50,y=50)

        numbersLeft = tk.Checkbutton(self, text ='Show count of each number left', 
                     takefocus = 0, bg = "#2c3c43", activebackground = "#2c3c43", highlightthickness = 0, font=(20), fg = "#7aa719").place(x = 150, y = 150) 
        validateGame = tk.Checkbutton(self, text ='Show button to validate your progress in game', 
                     takefocus = 0, bg = "#2c3c43", activebackground = "#2c3c43", highlightthickness = 0, font=(20), fg = "#7aa719").place(x = 150, y = 200) 



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
                            command=lambda: controller.show_frame(MainMenu))
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

        topPosition = tk.Label(table, text = "Position", fg = "#7aa719", width = 15, height = 3, bg = "#222e34")
        topPosition.grid(column = 0, row =0)

        topTime = tk.Label(table, text = "Time", fg = "#7aa719", width = 35, height = 3, bg = "#222e34")
        topTime.grid(column = 1, row =0)

        topDate = tk.Label(table, text = "Date", fg = "#7aa719", width = 25, height = 3, bg = "#222e34")
        topDate.grid(column = 2, row =0)

        nth_row = 0
        bgcol = "#4a6571"

        for pos in range(1,11):

        	if (nth_row % 2) :
        		bgcol = "#4a6571"
        	else:
        		bgcol = "#7aa719"


        	topRecordPosition = tk.Label(table, text = pos, width = 15, height = 3, bg = bgcol)
        	topRecordPosition.grid(column = 0, row =pos)

        	topRecordTime = tk.Label(table, text = "Best Time " + str(pos), width = 35, height = 3, bg = bgcol)
        	topRecordTime.grid(column = 1, row =pos)

        	topRecordDate = tk.Label(table, text = "Date of time", width = 25, height = 3, bg = bgcol)
        	topRecordDate.grid(column = 2, row =pos)

        	nth_row+=1


   

app = MainWindow()
app.minsize(800,700)
#app.resizable(0,0)
app.title("Sudoku")
app.mainloop()


