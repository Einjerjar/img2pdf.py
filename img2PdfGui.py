from tkinter import Tk, Frame, StringVar, BooleanVar, Label, Entry, Button, Checkbutton, filedialog
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

    def getSourceDir(self):
        self.sourceFolder.set(filedialog.askdirectory(
            title='Select folder containing the images', initialdir='./'))

    def getOutFile(self):
        self.outFolder.set(filedialog.asksaveasfilename(
            title='Save to pdf', initialdir='./'))

    def init(self):
        self.sourceFolder = StringVar()
        self.outFolder = StringVar()

        self.quality = StringVar()
        self.quality.set('90')

        self.optimize = BooleanVar()
        self.optimize.set(True)

        Label(self, text='Folder root:').grid(row=0, column=0)
        sf = Entry(self, textvariable=self.sourceFolder)
        sf.bind('<Return>', self.genPDF)
        sf.grid(row=0, column=1, columnspan=2, sticky='EW')
        sf.focus_set()

        Button(self, text='...', command=self.getSourceDir).grid(row=0, column=3)

        Label(self, text='Output folder:').grid(row=1, column=0)
        of = Entry(self, textvariable=self.outFolder)
        of.bind('<Return>', self.genPDF)
        of.grid(row=1, column=1, columnspan=2, sticky='EW')

        Button(self, text='...', command=self.getOutFile).grid(row=1, column=3)

        Label(self, text='Quality').grid(row=2, column=0)
        qf = Entry(self, textvariable=self.quality)
        qf.bind('<Return>', self.genPDF)
        qf.grid(row=2, column=1)

        Label(self, text='Optimize').grid(row=2, column=2)
        pf = Checkbutton(self, variable=self.optimize)
        pf.grid(row=2, column=3)

        gb = Button(self, text='Generate', command=self.genPDF)
        gb.bind('<Return>', self.genPDF)
        gb.grid(row=3, column=0, columnspan=4, sticky='EW')


root = Tk()
app = ITP(root)

root.mainloop()
