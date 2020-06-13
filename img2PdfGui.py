from tkinter import Tk, Frame, StringVar, BooleanVar, Label, Entry, Button
from img2Pdf import genPDF


class ITP(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.init()
        self.pack()

    def genPDF(self, e=None):
        o = self.outFolder.get()
        print(o, len(o))
        oo = None if len(o.strip()) == 0 else o
        genPDF(self.sourceFolder.get(), int(
            self.quality.get()), self.optimize.get(), oo)

    def init(self):
        self.sourceFolder = StringVar()
        self.outFolder = StringVar()

        self.quality = StringVar()
        self.quality.set('90')

        self.optimize = BooleanVar()
        self.optimize.set(True)

        Label(self, text='Folder root').pack()
        sf = Entry(self, textvariable=self.sourceFolder)
        sf.bind('<Return>', self.genPDF)
        sf.pack()
        sf.focus_set()

        Label(self, text='Output folder [leave blank for auto]').pack()
        of = Entry(self, textvariable=self.outFolder)
        of.bind('<Return>', self.genPDF)
        of.pack()

        Label(self, text='Quality').pack()
        qf = Entry(self, textvariable=self.quality)
        qf.bind('<Return>', self.genPDF)
        qf.pack()

        Label(self, text='Optimize').pack()
        pf = Checkbutton(self, variable=self.optimize)
        pf.pack()

        gb = Button(self, text='Generate', command=self.genPDF)
        gb.bind('<Return>', self.genPDF)
        gb.pack()


root = Tk()
app = ITP(root)

root.mainloop()
