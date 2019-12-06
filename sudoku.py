import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, GameScreen,SettingsMenu, LeaderboardMenu):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.configure(bg = "#2c3c43")
        frame.tkraise()

        
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        tk.Label(self, text = "Menu", bg = "#2c3c43", fg = "#39742c",font=("Times New Roman", 20, "bold")).place(x = 370, y=50)

        Continue = tk.Button(self, text="Continue",highlightthickness = 0, width = 50, height = 3,
                            command=lambda: controller.show_frame(GameScreen))
        Continue.configure(bg = "#a7e02c")
        Continue.place(x=200,y=100)



        newGame = tk.Button(self, text="New Game",highlightthickness = 0, width = 50, height = 3,
                            command=lambda: controller.show_frame(GameScreen))
        newGame.configure(bg = "#a7e02c")
        newGame.place(x=200,y=200)



        Settings = tk.Button(self, text="Settings",highlightthickness = 0, width = 50, height = 3,
                            command=lambda: controller.show_frame(SettingsMenu))
        Settings.configure(bg = "#a7e02c")
        Settings.place(x=200,y=300)


        
        Leaderboard = tk.Button(self, text="Leaderboard",highlightthickness = 0, width = 50, height = 3,
                            command=lambda: controller.show_frame(LeaderboardMenu))
        Leaderboard.configure(bg = "#a7e02c")
        Leaderboard.place(x=200,y=400)

class GameScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        tk.Label(self, text = "HERE WILL BE STOPWATCH", bg = "#2c3c43", fg = "#39742c", font=("Times New Roman", 20, "bold")).place(x = 300, y=50)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.place(x=50,y=50)

        
class SettingsMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = "Settings", bg = "#2c3c43", fg = "#39742c",  font=("Times New Roman", 20, "bold")).place(x = 320, y=50)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.place(x=50,y=50)


class LeaderboardMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text = "Leaderboard", bg = "#2c3c43", fg = "#39742c", font=("Times New Roman", 20, "bold")).place(x = 300, y=50)

        backToMenu = tk.Button(self, text="Back to Menu",highlightthickness = 0, width = 10, height = 1,
                            command=lambda: controller.show_frame(MainMenu))
        backToMenu.configure(bg = "#a7e02c")
        backToMenu.place(x=50,y=50)




app = MainWindow()
app.geometry("800x800")
app.resizable(0,0)
app.title("Sudoku")
app.mainloop()