import random
import time
import threading
from Tkinter import *
window = Tk()
canvas = Canvas(window, width=800, height=780, bg='#cecece')
canvas.pack()

op = open('num.txt')
rd = op.read()


x = int(rd)
y=x

coords1=[]
coords2=[]
coords3=[]
coords4=[]
coords5=[]
coords6=[]
coords7=[]
coords8=[]
coords9=[]
coords10=[]
coords11=[]
coords12=[]
coords13=[]
coords14=[]
coords15=[]
coords16=[]
coords17=[]
coords18=[]
coords19=[]
coords20=[]
coords21=[]
coords22=[]
coords23=[]
coords24=[]
coords25=[]
coords26=[]
coords27=[]
coords28=[]
coords29=[]
coords30=[]
coords31=[]
coords32=[]
coords33=[]
coords34=[]
coords35=[]
coords36=[]
coords37=[]
coords38=[]
coords39=[]


for i in range(40):
    coords39.append(int(x%10))
    x = x/10

list.reverse(coords39)

for i in range(40):
    coords38.append(int(x%10))
    x = x/10

list.reverse(coords38)

for i in range(40):
    coords37.append(int(x%10))
    x = x/10

list.reverse(coords37)

for i in range(40):
    coords36.append(int(x%10))
    x = x/10

list.reverse(coords36)

for i in range(40):
    coords35.append(int(x%10))
    x = x/10

list.reverse(coords35)

for i in range(40):
    coords34.append(int(x%10))
    x = x/10

list.reverse(coords34)

for i in range(40):
    coords33.append(int(x%10))
    x = x/10

list.reverse(coords33)

for i in range(40):
    coords32.append(int(x%10))
    x = x/10

list.reverse(coords32)

for i in range(40):
    coords31.append(int(x%10))
    x = x/10

list.reverse(coords31)

for i in range(40):
    coords30.append(int(x%10))
    x = x/10

list.reverse(coords30)

for i in range(40):
    coords29.append(int(x%10))
    x = x/10

list.reverse(coords29)

for i in range(40):
    coords28.append(int(x%10))
    x = x/10

list.reverse(coords28)

for i in range(40):
    coords27.append(int(x%10))
    x = x/10

list.reverse(coords27)

for i in range(40):
    coords26.append(int(x%10))
    x = x/10

list.reverse(coords26)

for i in range(40):
    coords25.append(int(x%10))
    x = x/10

list.reverse(coords25)

for i in range(40):
    coords24.append(int(x%10))
    x = x/10

list.reverse(coords24)

for i in range(40):
    coords23.append(int(x%10))
    x = x/10

list.reverse(coords23)

for i in range(40):
    coords22.append(int(x%10))
    x = x/10

list.reverse(coords22)

for i in range(40):
    coords21.append(int(x%10))
    x = x/10

list.reverse(coords21)

for i in range(40):
    coords20.append(int(x%10))
    x = x/10

list.reverse(coords20)

for i in range(40):
    coords19.append(int(x%10))
    x = x/10

list.reverse(coords19)

for i in range(40):
    coords18.append(int(x%10))
    x = x/10

list.reverse(coords18)

for i in range(40):
    coords17.append(int(x%10))
    x = x/10

list.reverse(coords17)

for i in range(40):
    coords16.append(int(x%10))
    x = x/10

list.reverse(coords16)

for i in range(40):
    coords15.append(int(x%10))
    x = x/10

list.reverse(coords15)

for i in range(40):
    coords14.append(int(x%10))
    x = x/10

list.reverse(coords14)

for i in range(40):
    coords13.append(int(x%10))
    x = x/10

list.reverse(coords13)

for i in range(40):
    coords12.append(int(x%10))
    x = x/10

list.reverse(coords12)

for i in range(40):
    coords11.append(int(x%10))
    x = x/10

list.reverse(coords11)

for i in range(40):
    coords10.append(int(x%10))
    x = x/10

list.reverse(coords10)

for i in range(40):
    coords9.append(int(x%10))
    x = x/10

list.reverse(coords9)

for i in range(40):
    coords8.append(int(x%10))
    x = x/10

list.reverse(coords8)

for i in range(40):
    coords7.append(int(x%10))
    x = x/10

list.reverse(coords7)

for i in range(40):
    coords6.append(int(x%10))
    x = x/10

list.reverse(coords6)

for i in range(40):
    coords5.append(int(x%10))
    x = x/10

list.reverse(coords5)

for i in range(40):
    coords4.append(int(x%10))
    x = x/10

list.reverse(coords4)

for i in range(40):
    coords3.append(int(x%10))
    x = x/10

list.reverse(coords3)

for i in range(40):
    coords2.append(int(x%10))
    x = x/10

list.reverse(coords2)

for i in range(40):
    coords1.append(int(x%10))
    x = x/10

list.reverse(coords1)

matrix = [coords1, coords2, coords3, coords4, coords5, coords6, coords7, coords8, coords9, coords10, coords11, coords12, coords13, coords14, coords15, coords16, coords17, coords18, coords19, coords20, coords21, coords22, coords23, coords24, coords25, coords26, coords27, coords28, coords29, coords30, coords31, coords32, coords33, coords34, coords35, coords36, coords37, coords38, coords39]


sprite1 = PhotoImage(file = 'sprites/floorSprite.gif')
sprite2 = PhotoImage(file = 'sprites/wallSprite.gif')
sprite3 = PhotoImage(file = 'sprites/glight.gif')
sprite4 = PhotoImage(file = 'sprites/rlight.gif')
sprite5 = PhotoImage(file = 'sprites/alight.gif')
sprite6 = PhotoImage(file = 'sprites/robotSprite1.gif')

treasure1 = PhotoImage(file = 'sprites/bigTreasure1.gif')
treasure2 = PhotoImage(file = 'sprites/bigTreasure2.gif')
treasure3 = PhotoImage(file = 'sprites/bigTreasure3.gif')
treasure4 = PhotoImage(file = 'sprites/bigTreasure4.gif')
treasure5 = PhotoImage(file = 'sprites/bigTreasure5.gif')
treasure6 = PhotoImage(file = 'sprites/smallTreasure1.gif')
treasure7 = PhotoImage(file = 'sprites/smallTreasure2.gif')
treasure8 = PhotoImage(file = 'sprites/smallTreasure3.gif')
treasure9 = PhotoImage(file = 'sprites/smallTreasure4.gif')
treasure10 = PhotoImage(file = 'sprites/smallTreasure5.gif')

treasures = [treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10]
xlights = []
ylights = []
slights = []
xtreasures = []
ytreasures = []
ct = 0

for i in range(40):
    for j in range(39):
        if matrix[j][i] == 1:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite1, anchor = NW)

        if matrix[j][i] == 2:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite2, anchor = NW)

        if matrix[j][i] == 3:
            cox =i*20
            coy =j*20
            r = random.randrange(0, 10)
            canvas.create_image(cox, coy, image=sprite1, anchor = NW)

        if matrix[j][i] == 4:
            cox =i*20
            coy =j*20
            r = random.randrange(0, 10)
            canvas.create_image(cox, coy, image=treasures[r], anchor = NW)
            xtreasures.append(i)
            ytreasures.append(j)

        if matrix[j][i] == 5:
            cox =i*20
            coy =j*20
            canvas.create_image(cox, coy, image=sprite4, anchor = NW)
            xlights.append(cox)
            ylights.append(coy)
            slights.append(0)

class Robots:
   rbtCount = 0

   def __init__(self, points, xco, yco):
      self.xco = xco
      self.yco = yco
      self.points = points
      Robots.rbtCount += 1

i = 0
j = 0

while i < 40:
    while j < 39:
        if matrix[j][i] == 3:
            cox1 = i*20
            coy1 = j*20
            robot1=Robots(0, cox1, coy1)
            i = 40
            j = 39
        j = j + 1
    i = i + 1

i = cox1/10
j = coy1/10

while i < 40:
    while j < 39:
        if matrix[j][i] == 3:
            cox2 = i*20
            coy2 = j*20
            robot2=Robots(0, cox2, coy2)
            j = 39
            i = 40
        j = j + 1
    i = i + 1
            

def lights1():
    global slights
    for hr in range(len(xlights)):
        if hr % 2 == 0:
            canvas.create_image(xlights[hr], ylights[hr], image=sprite3, anchor = NW)
    ko = 1
    while ko < 400:
        for hr in range(len(xlights)):
            if hr %2 == 0:
                canvas.create_image(xlights[hr], ylights[hr], image=sprite4, anchor = NW)
                canvas.update()
                slights[hr] = 0
                time.sleep(2)
                canvas.create_image(xlights[hr], ylights[hr], image=sprite3, anchor = NW)
                canvas.update()
                slights[hr] = 1
                time.sleep(3)
                ko = ko + 1
            
def lights2():
    global slights
    for hr in range(len(xlights)):
        if hr % 2 != 0:
            canvas.create_image(xlights[hr], ylights[hr], image=sprite3, anchor = NW)
    ko = 1
    while ko < 400:
        for hr in range(len(xlights)):
            if hr %2 != 0:
                canvas.create_image(xlights[hr], ylights[hr], image=sprite4, anchor = NW)
                canvas.update()
                slights[hr] = 0
                time.sleep(1)
                canvas.create_image(xlights[hr], ylights[hr], image=sprite3, anchor = NW)
                canvas.update()
                slights[hr] = 1
                time.sleep(2)
                ko = ko + 1


bot1= canvas.create_image(cox1, coy1, image=sprite6, anchor = NW)
bot2= canvas.create_image(cox2, coy2, image=sprite6, anchor = NW)

def r1_right(finish):
    global bot1
    v = 1
    while v == 1:
        robot1.xco = robot1.xco + 1
        x1 = robot1.xco
        y1 = robot1.yco
        time.sleep(0.05)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.xco == finish:
            v = 0

def r1_left(finish):
    global bot1
    v = 1
    while v == 1:
        robot1.xco = robot1.xco - 1
        x1 = robot1.xco
        y1 = robot1.yco
        time.sleep(0.05)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.xco == finish:
            v = 0

def r1_up(finish):
    global bot1
    v = 1
    while v == 1:
        robot1.yco = robot1.yco - 1
        x1 = robot1.xco
        y1 = robot1.yco
        time.sleep(0.05)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.yco == finish:
            v = 0

def r1_down(finish):
    global bot1
    v = 1
    while v == 1:
        robot1.yco = robot1.yco + 1
        x1 = robot1.xco
        y1 = robot1.yco
        time.sleep(0.05)
        canvas.coords(bot1, robot1.xco, robot1.yco)
        canvas.update()
        if robot1.yco == finish:
            v = 0

checkpointsx=[]
checkpointsy=[]

if robot1.xco == 0:
    px = 0
else:
    px = int(robot1.xco/10-1)
if robot1.yco == 0:
    0
else:
    py = int(robot1.yco/10-1)
    
#checkpointsx.append(px)
#checkpointsy.append(py)
k = 0

possx=[]
possy=[]


def detect_right():
    global px
    global py
    global possx
    global possy
    global checkpointsx
    global checkpointsy
    global ct
    go = 1
    while go == 1:
        k = 0
        possx=[]
        possy=[]
            
            
        if (matrix[py][px+1] == 1 or matrix[py][px+1] == 5) and px < 40:
            go = 1
            px = px + 1
        else:
            go = 0
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]

        if (matrix[py+1][px] == 1 or matrix[py+1][px] == 5) and py < 39 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)

        if (matrix[py-1][px] == 1 or matrix[py-1][px] == 5) and py > 0 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)



def detect_down():
    global px
    global py
    global possx
    global possy
    global checkpointsx
    global checkpointsy
    global ct
    go = 1
    while go == 1:
        k = 0
        if (matrix[py+1][px] == 1 or matrix[py+1][px] == 5) and py < 39:
            go = 1
            py = py + 1
        else:
            go = 0
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]
            
    
        if (matrix[py][px-1] == 1 or matrix[py][px-1] == 5) and px > 0 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)
    

        if (matrix[py][px+1] == 1 or matrix[py][px+1] == 5) and px < 40 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)



def detect_up():
    global px
    global py
    global possx
    global possy
    global checkpointsx
    global checkpointsy
    global ct
    go = 1
    while go == 1:
        k = 0


        if (matrix[py-1][px] == 1 or matrix[py-1][px] == 5) and py > 0:
            go = 1
            py = py - 1
        else:
            go = 0
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]
            
    
        if (matrix[py][px-1] == 1 or matrix[py][px-1] == 5):
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)
    

        if (matrix[py][px+1] == 1 or matrix[py][px+1] == 5) and px < 40 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)

def detect_left():
    global px
    global py
    global possx
    global possy
    global checkpointsx
    global checkpointsy
    global ct
    go = 1
    while go == 1:
        k = 0

    
        if (matrix[py][px-1] == 1 or matrix[py][px-1] == 5) and px > 0:
            go = 1
            px = px - 1
        else:
            go = 0
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]

        if (matrix[py+1][px] == 1 or matrix[py+1][px] == 5) and py < 39 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)

        if (matrix[py-1][px] == 1 or matrix[py-1][px] == 5) and py > 0 and go == 1:
            g = 0
            for i in range(len(checkpointsx)):
                if px == checkpointsx[i] and py == checkpointsy[i]:
                    g = 1
            if g == 0:
                checkpointsx.append(px)
                checkpointsy.append(py)
lx = px
ly = py
go = 1
t = 0
while go < 25:
    #RIGHT------------
    
    if xtreasures[ct] > px:
        lx = px
        ly = py
        detect_right()
        #-----
        if lx == px and ly == py:
            px = checkpointsx[len(checkpointsx)-2]
            py = checkpointsy[len(checkpointsy)-2]
            checkpointsx.remove(checkpointsx[len(checkpointsx)-1])
            checkpointsy.remove(checkpointsy[len(checkpointsy)-1])
            lx == px
            ly == py
            detect_right()
            if lx == px and ly == py:
                px = checkpointsx[len(checkpointsx)-1]
                py = checkpointsy[len(checkpointsy)-1]
                lx == px
                ly == py
                detect_down()
                if lx == px and ly == py:
                    px = checkpointsx[len(checkpointsx)-1]
                    py = checkpointsy[len(checkpointsy)-1]
                    lx == px
                    ly == py
                    detect_up()
                    if lx == px and ly == py:
                        px = checkpointsx[len(checkpointsx)-1]
                        py = checkpointsy[len(checkpointsy)-1]
                        detect_left()
                    
    #DOWN-------------
    
    if ytreasures[ct] > py:
        lx = px
        ly = py
        detect_down()
        if lx == px and ly == py:
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]
            lx == px
            ly == py
            detect_down()
            if px == lx and py == ly:
                px = checkpointsx[len(checkpointsx)-1]
                py = checkpointsy[len(checkpointsy)-1]
                lx == px
                ly == py
                detect_up()
                if px == lx and py == ly:
                    px = checkpointsx[len(checkpointsx)-1]
                    py = checkpointsy[len(checkpointsy)-1]
                    lx == px
                    ly == py
                    detect_left()
                    if px == lx and py == ly:
                        px = checkpointsx[len(checkpointsx)-1]
                        py = checkpointsy[len(checkpointsy)-1]
                        detect_right()
                        
    #LEFT----------
    
    if xtreasures[ct] < px:
        lx = px
        ly = py
        detect_left()
        if px == lx and py == ly:
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]
            #checkpointsx.remove(checkpointsx[len(checkpointsx)-1])
            #checkpointsy.remove(checkpointsy[len(checkpointsy)-1])
            lx == px
            ly == py
            detect_left()
            if px == lx and py == ly:
                px = checkpointsx[len(checkpointsx)-1]
                py = checkpointsy[len(checkpointsy)-1]
                lx == px
                ly == py
                detect_right()
                if px == lx and py == ly:
                    px = checkpointsx[len(checkpointsx)-1]
                    py = checkpointsy[len(checkpointsy)-1]
                    lx == px
                    ly == py
                    detect_down()
                    if px == lx and py == ly:
                        px = checkpointsx[len(checkpointsx)-1]
                        py = checkpointsy[len(checkpointsy)-1]
                        detect_up()
                        
        
    #UP------------
    
    if ytreasures[ct] < py:
        lx = px
        ly = py
        detect_up()
        if px == lx and py == ly:
            px = checkpointsx[len(checkpointsx)-1]
            py = checkpointsy[len(checkpointsy)-1]
            lx == px
            ly == py
            detect_up()
            if px == lx and py == ly:
                px = checkpointsx[len(checkpointsx)-1]
                py = checkpointsy[len(checkpointsy)-1]
                lx == px
                ly == py
                detect_left()
                if px == lx and py == ly:
                    px = checkpointsx[len(checkpointsx)-1]
                    py = checkpointsy[len(checkpointsy)-1]
                    lx == px
                    ly == py
                    detect_right()
                    if px == lx and py == ly:
                        px = checkpointsx[len(checkpointsx)-1]
                        py = checkpointsy[len(checkpointsy)-1]
                        detect_down()
                                
        
    if xtreasures[ct] == px and ytreasures[ct] == py:
        go = 0
    lx = px
    ly = py
    go = go + 1


thread1 = threading.Thread(target=lights1)
thread2 = threading.Thread(target=lights2)

thread1.start()
thread2.start()

if robot1.xco == 0:
    rx = robot1.xco/10
else:
    rx = robot1.xco/10-1
if robot1.yco == 0:
    ry = robot1.yco/10
else:
    ry = robot1.yco/10-1

for i in range(len(checkpointsx)):
    go = 1
    if checkpointsy[i] == ry and checkpointsx[i] > rx and go ==1:
        r1_right(checkpointsx[i]*20)
        go = 0
        rx = checkpointsx[i]
        ry = checkpointsy[i]
    if checkpointsy[i] == ry and checkpointsx[i] < rx and go == 1:
        r1_left(checkpointsx[i]*20)
        go = 0
        rx = checkpointsx[i]
        ry = checkpointsy[i]
    if checkpointsx[i] == rx and checkpointsy[i] > ry and go == 1:
        r1_down(checkpointsy[i]*20)
        go = 0
        rx = checkpointsx[i]
        ry = checkpointsy[i]
    if checkpointsx[i] == rx and checkpointsy[i] < ry and go == 1:
        r1_up(checkpointsy[i]*20)
        go = 0
        rx = checkpointsx[i]
        ry = checkpointsy[i]


window.mainloop()




