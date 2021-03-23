from Tkinter import Button, Tk
from PIL import Image, ImageTk
import os
import sys

class App(Tk):

    wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    brd = [1,2,3,4,5,6,7,8,9]
    Turnofx = True
    move_of_x = []
    move_of_o = []

    def __init__(self):
        Tk.__init__(self,None)#just a method to make the code simpler

        #the image objects
        self.img1 = Image.open(r"X.png")#adress of X.png and Y.png
        self.img2 = Image.open(r'O.png')
        self.imgx = ImageTk.PhotoImage(self.img1)
        self.imgo = ImageTk.PhotoImage(self.img2)

        #the button definitions
        self.b1 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b1,1))
        self.b1.place(x=0,y=0)
        self.b2 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b2,2))
        self.b2.place(x=74,y=0)
        self.b3 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b3,3))
        self.b3.place(x=148,y=0)
        self.b4 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b4,4))
        self.b4.place(x=0,y=74)
        self.b5 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b5,5))
        self.b5.place(x=74,y=74)
        self.b6 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b6,6))
        self.b6.place(x=148,y=74)
        self.b7 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b7,7))
        self.b7.place(x=0,y=148)
        self.b8 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b8,8))
        self.b8.place(x=74,y=148)
        self.b9 = Button(self,height = 4,width = 9,command = lambda:self.main(self.b9,9))
        self.b9.place(x=148,y=148)

        self.temp = {1:self.b1,2:self.b2,3:self.b3,4:self.b4,5:self.b5,6:self.b6,7:self.b7,8:self.b8,9:self.b9}
    
    def set_image(self,arg,args):
        if App.Turnofx:
            arg.configure(image = self.imgx,height = 66,width = 68,state = 'disabled')
            arg.image = self.imgx
            
        else:
            arg.configure(image = self.imgo,height = 66,width = 68,state = 'disabled')
            arg.image = self.imgo
            
    def check_win(self,arg):
        for i in App.wins:
            if set(i).issubset(set(arg)):
                return True
        return False
    def board(self,arg,args):
        kwarg = arg+args
        Board = [1,2,3,4,5,6,7,8,9]

        for i in kwarg:
            Board.remove(i)

        return Board
    
    def minimax(self,arg,args,turn_of_human,alpha,beta):

        #first see if anyone won or the match is draw or not
        if self.check_win(arg):                  #if the human has won
            return -1/(len(arg+args))
        elif  self.check_win(args):              #if the computer has won
            return 1/len(arg+args)
        elif(len(arg) + len(args) == 9):#if the match is draw
            return 0

        #now if the game is still on then
        if turn_of_human:
            board = self.board(arg,args)
            best_score = 2
            for i in board:
                arg.append(i)
                score = self.minimax(arg,args,False,alpha,beta)
                best_score = min(best_score,score)
                arg.remove(i)
                beta = min(beta,score)
                if beta <= alpha:
                    break
            return best_score
        else:
            board = self.board(arg,args)
            best_score = -2
            for i in board:
                args.append(i)
                score = self.minimax(arg,args,True,alpha,beta)
                best_score = max(best_score,score)
                args.remove(i)
                alpha = max(score,alpha)
                if beta <= alpha:
                    break

            return best_score
            
    #the game loop
    def main(self,arg,args):
        App.move_of_x.append(args)
        self.set_image(arg,args)
        if self.check_win(App.move_of_x):
            print("You Won!")
            python = sys.executable
            os.execl(python, python, *sys.argv)
        App.brd.remove(args)

        if not len(App.brd):
            print("Match Draw.")
            python = sys.executable
            os.execl(python, python, *sys.argv)
        App.Turnofx = False
        
        best_score = -2
        best_move = 0
        for i in App.brd:
            App.move_of_o.append(i)
            score = self.minimax(App.move_of_x,App.move_of_o,True,-2,2)
            App.move_of_o.remove(i)
            if score > best_score:
                best_score = score
                best_move = i

        App.move_of_o.append(best_move)
        print("Computer played " + str(best_move))
        self.set_image(self.temp[best_move],best_move)
        App.brd.remove(best_move)
        if self.check_win(App.move_of_o):
            print("Computer Won!")
            python = sys.executable
            os.execl(python, python, *sys.argv)

        App.Turnofx = True

        
x = App()
x.configure(height = 222, width = 222)
x.resizable(False,False)
x.mainloop()
'''
SUCCESSSSSSSSS

FINALLY

AFTER SOOOOOO MANY MONTHS
'''
