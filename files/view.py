from tkinter import Tk

class View:
    def __init__(self,title):
        self.controller = None
        self.root = self.__create_root(title)

    def __create_root(self,title):
        root = Tk()
        root.geometry('400x600+50+10')
        root.iconbitmap('assets/icon.ico')
        root.title(title)
        root.config(bg='#2E2E2E')
        root.resizable(False,False)
        root.bind_all('<Control-q>', lambda e : root.destroy())
        return root

    def set_controller(self,controller):
        self.controller = controller