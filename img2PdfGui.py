from tkinter import Tk, Frame, StringVar, BooleanVar, Label, Entry, Button, Checkbutton, filedialog
from img2Pdf import gen_pdf


class ITP(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.source_folder = StringVar()
        self.out_folder = StringVar()

        self.quality = StringVar()
        self.quality.set('80')

        self.optimize = BooleanVar()
        self.optimize.set(True)

        self.init()
        self.pack()

    def gen_pdf(self):
        o = self.out_folder.get()
        print(o, len(o))
        oo = None if len(o.strip()) == 0 else o
        gen_pdf(self.source_folder.get(), int(
            self.quality.get()), self.optimize.get(), oo)

    def get_source_dir(self):
        self.source_folder.set(filedialog.askdirectory(
            title='Select folder containing the images', initialdir='./'))

    def get_out_file(self):
        self.out_folder.set(filedialog.asksaveasfilename(
            title='Save to pdf', initialdir='./'))

    def init(self):

        Label(self, text='Folder root:').grid(row=0, column=0, sticky='E')
        sf = Entry(self, textvariable=self.source_folder)
        sf.bind('<Return>', self.gen_pdf)
        sf.grid(row=0, column=1, columnspan=2, sticky='EW')
        sf.focus_set()

        Button(self, text='...', command=self.get_source_dir).grid(row=0, column=3)

        Label(self, text='Output (same folder if empty):').grid(row=1, column=0, sticky='E')
        of = Entry(self, textvariable=self.out_folder)
        of.bind('<Return>', self.gen_pdf)
        of.grid(row=1, column=1, columnspan=2, sticky='EW')

        Button(self, text='...', command=self.get_out_file).grid(row=1, column=3)

        Label(self, text='Quality:').grid(row=2, column=0, sticky='E')
        qf = Entry(self, textvariable=self.quality)
        qf.bind('<Return>', self.gen_pdf)
        qf.grid(row=2, column=1)

        Label(self, text='Optimize:').grid(row=2, column=2, sticky='E')
        pf = Checkbutton(self, variable=self.optimize)
        pf.grid(row=2, column=3)

        gb = Button(self, text='Generate', command=self.gen_pdf)
        gb.bind('<Return>', self.gen_pdf)
        gb.grid(row=3, column=0, columnspan=4, sticky='EW')


root = Tk()
app = ITP(root)

root.mainloop()
