# Tkinter-Carousel
A simple carousel in Tkinter

## Code:
First, all JPG files in the current folder are read using **glob** module and saved in a list. Then **Image Module** is used to stitch all images horizontally. Then the Image is displayed on the **Carousel(inherited from Tk.Canvas)** using **ImageTk** before which it is resized so that only the first image is visible. The Carousel is bound to **Left and Right** arrow keys. On pressing the right or the left key, both the image as well as the white indicator at the bottom is moved using **animate()** method.

## Requirements:
1. Python 3.6 or above
2. Tkinter, Ttk

## How to run it:
1. Clone the repo
2. Open CMD/Terminal and CD to the directory where the repo is cloned
3. Run command **python carousel.py**
4. After the tkinter app is open, Press **Right** or **Left** key to surf through images

# Thank You
