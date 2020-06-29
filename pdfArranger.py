import PyPDF2
from tkinter import Tk, Frame, Canvas, Label
from PIL import Image, ImageTk


class IMGViewer(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master

        c_width = 250
        c_height = 250

        self.current_image = Image.open('rpLab/2.jpg')
        self.current_image_tk = ImageTk.PhotoImage(self.current_image)
        self.preview_canvas = Canvas(self, width=c_width, height=c_height)

        self.init()
        self.pack()

    def init(self):
        self.preview_canvas.grid(row=0, column=0, rowspan=5, columnspan=2)
        self.update_preview()

        Label(self, text='test1').grid(row=0, column=2)
        Label(self, text='test1').grid(row=1, column=2)
        Label(self, text='test1').grid(row=2, column=2)

    def update_preview(self):
        self.preview_canvas.create_image(0, 0, anchor='nw', image=self.current_image_tk)


root = Tk()
nope = IMGViewer(root)

nope.mainloop()
