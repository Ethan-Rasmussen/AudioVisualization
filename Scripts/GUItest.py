from tkinter import * 
#from matplotlib.figure import Figure
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
#NavigationToolbar2Tk)
import matplotlib.pyplot as plt

vert = [5, -4.2, 6.2, 2.1, 3.2]
horiz = [-5, 2.2, 3.4, 6.1, 1]

window = Tk()
C = Canvas(window, height = 400, width = 400, bg = 'white')

def plot(): #create scatter plot - not very good for our purposes
    plt.scatter(vert, horiz)
    plt.title("Sound Locations")
    plt.show()

def point():
      xval = inputtxtX.get(1.0, "end-1c") #get val from x box
      yval = inputtxtY.get(1.0, "end-1c") #get val from y box

      #to hoop up to main program assign xval and yval to correct *ADJUSTED* values from regression results

      point = C.create_oval(float(xval),float(yval),float(xval)+5.0,float(yval)+5.0, fill = 'red')

#*INFORMATION FOR ADJUSTMENTS FORMULA*

#400 by 400 canvas - (0,0 is top left corner)
#actual origin is located at (200,200) so equation to convert to pixels needs to include an offset of +200x and +200y to start at the origin
#positive values need to become negative to be in top half
#negative values are positive to be in bottom half i.e 245 = -45 pixels, 160 = +40 pixels
#every box is 40x40 (= 1 foot? 40/12 = 3.33 pixels per inch)
#graph covers 5 feet in any direction

C = Canvas(window, height = 400, width = 400, bg = 'white')
xaxis = C.create_line(200,0, 200,400, fill='black')
yaxis = C.create_line(0,200, 400,200, fill='black')
xline1 = C.create_line(160,0, 160,400, fill='grey')
yline1 = C.create_line(0,160, 400,160, fill='grey')
xline2 = C.create_line(120,0, 120,400, fill='grey')
yline2 = C.create_line(0,120, 400,120, fill='grey')
xline3 = C.create_line(80,0, 80,400, fill='grey')
yline3 = C.create_line(0,80, 400,80, fill='grey')
xline4 = C.create_line(40,0, 40,400, fill='grey')
yline4 = C.create_line(0,40, 400,40, fill='grey')
xline5 = C.create_line(0,0, 0,400, fill='grey')
yline5 = C.create_line(0,0, 400,0, fill='grey')
xline6 = C.create_line(240,0, 240,400, fill='grey')
yline6 = C.create_line(0,240, 400,240, fill='grey')
xline7 = C.create_line(280,0, 280,400, fill='grey')
yline7 = C.create_line(0,280, 400,280, fill='grey')
xline8 = C.create_line(320,0, 320,400, fill='grey')
yline8 = C.create_line(0,320, 400,320, fill='grey')
xline9 = C.create_line(360,0, 360,400, fill='grey')
yline9 = C.create_line(0,360, 400,360, fill='grey')
xline10 = C.create_line(400,0, 400,400, fill='grey')
yline10 = C.create_line(0,400, 400,400, fill='grey')
C.pack()

window['bg'] = 'light blue'
window.title('Audio Visualization Program')

window_width = 800
window_height = 600

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{25}')

inputtxtX = Text(window,
                   height = 5,
                   width = 20,
                   bg = 'pink'
                   )
  
inputtxtX.pack()

inputtxtY = Text(window,
                   height = 5,
                   width = 20,
                   bg = 'white')
  
inputtxtY.pack()

infoTxt = Label(window, text= "Pink is X value, White is Y value.(in pixels)", bg = 'white', fg = 'black').place(x = 40, y = 450)





point_button = Button(master = window,
                      command = point,
                      height = 2,
                      width = 10,
                      text = "Plot Point")

point_button.pack()

window.mainloop()