import tkinter as Tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob

height = 600 # Window height
width = 1000 # Window Width

def show(event):
    print(event.x,event.y)

class App(Tk.Tk):
    def __init__(self,title):
        super().__init__()

        # App Sizing and Title
        geometry = str(width) + 'x' + str(height)
        self.geometry(geometry)
        self.title(title)
        self.resizable(0,0)

        self.bind('<Left>',moveImageLeft)
        self.bind('<Right>',moveImageRight)


class Carousel(Tk.Canvas):
    def __init__(self,master):
        super().__init__()
        self.config(width=width,height=height)
        self.pack()
        self.stitchImages()
        self.showPhoto()
        self.loadIndicator()
        self.current = 1


    def stitchImages(self):
        # Stitch Image
        images = [Image.open(file) for file in glob.glob('*.jpg')]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        self.stitched = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
          self.stitched.paste(im, (x_offset,0))
          x_offset += im.size[0]
        self.stitched = self.stitched.resize((len(images)*1000,600))
        self.length = len(images)

    def showPhoto(self):
        # Show Stitched Image
        self.stitched = ImageTk.PhotoImage(self.stitched)
        self.Photo = self.create_image((0,0),image=self.stitched,anchor='nw')


    def loadIndicator(self):
        # Indicator
        self.ind = self.create_rectangle(1,590,250,600,fill='white',outline='white')

    def moveImageRight(self):
        if self.current < 4:
            for i in range(25):
                self.after(1,self.move(self.Photo,-40,0))
                self.after(1,self.move(self.ind,10,0))
                self.update()
            self.current += 1

    def moveImageLeft(self):
        if self.current > 0:
            for i in range(25):
                self.after(1,self.move(self.Photo,40,0))
                self.after(1,self.move(self.ind,-10,0))
                self.update()
            self.current -= 1

car = None

def moveImageRight(event):
    global car
    if car.current == 4:
        pass
    else:
        car.moveImageRight()

def moveImageLeft(event):
    global car
    if car.current == 1:
        pass
    else:
        car.moveImageLeft()

def main():
    global car
    app = App('Carousel')
    car = Carousel(app)
    app.mainloop()

main()
