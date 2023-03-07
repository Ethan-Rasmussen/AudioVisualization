from tkinter import * 
import time


lines = 0

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)


def saveFile():
    #connect save file function call HERE
    clickText = Label(window, text = "File Saved", bg = 'green').place(x = 10,y = 10)
def loadFile():
    #connect load file function call HERE
    clickText = Label(window, text = "File Loaded", bg = 'green').place(x = 10,y = 10)

def initCalWindow():
    #connect calibrate function calls HERE
    cal_window = Toplevel(window)
    cal_window['bg'] = 'light blue'
    cal_window.geometry("300x300")
    cal_window.title("Calibration Settings")

    inputtxt1 = Text(cal_window,
                       height = 1,
                       width = 20,
                       bg = 'pink'
                       )
    
    mic1label = Label(cal_window, text = "Microphone 1", bg = 'white').place(x = 15,y = 10)
    inputtxt1.place(x=100, y =10)

    inputtxt2 = Text(cal_window,
                       height = 1,
                       width = 20,
                       bg = 'white')
    
    mic2label = Label(cal_window, text = "Microphone 2", bg = 'white').place(x = 15,y = 40)
    inputtxt2.place(x=100, y=40)

    inputtxt3 = Text(cal_window,
                   height = 1,
                   width = 20,
                   bg = 'pink'
                   )
    
    mic3label = Label(cal_window, text = "Microphone 3", bg = 'white').place(x = 15,y = 70)
    inputtxt3.place(x=100,y=70)

    inputtxt4 = Text(cal_window,
                       height = 1,
                       width = 20,
                       bg = 'white')
    mic4label = Label(cal_window, text = "Microphone 4", bg = 'white').place(x = 15,y = 100)
    inputtxt4.place(x=100, y=100)


def point():
    global lines
    lines = lines + 1

    if(lines >= 2):
        lines = 1
        C.delete('alive')
    
    xval = inputtxtX.get(1.0, "end-1c") #get val from x box //get predicted value from regression for A
    yval = inputtxtY.get(1.0, "end-1c") #get val from y box //get predicted value from regression for B

    #convert A into pixels 40 pixels = 1 (foot?) so xval * 40 scales to # of pixels (currently max value of 5)
    convAval = (float(xval) * 40.0) + 200 #A as a pixel number
    convBval = (float(yval) * 40.0) + 200 #B as a pixel number

    #Y = -Ax / B
    # X = -By /A
    Y = (-convAval * 0) / convBval
    X = (-convBval * 0) / convAval
    #to hook up to main program assign xval and yval to correct values from regression results
    guess = C.create_line(200,200,convAval,convBval, fill = 'red', tags = 'alive')
    window.after(1000, point)

C = Canvas(window, height = 400, width = 400, bg = 'white')

menubar.add_command(label = "Save", command = saveFile, activebackground='grey')
menubar.add_command(label = "Load", command = loadFile, activebackground='grey')
menubar.add_command(label = "Calibrate", command = initCalWindow, activebackground='grey')

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
                      text = "Start Plotting")

point_button.pack()

window.mainloop()