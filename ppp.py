from graphics import *
from math import *
win = GraphWin('MYWIN',800,400)



def home(x, y, roof_color, home_color, window_color, door_color, height, width, lines, storona_ruchki, win):
    r = Rectangle(Point(x, y), Point(x + width, y + height))
    r.setFill(home_color)

    p1 = Polygon(Point(x - width / 10, y), Point(x + width / 2, y - 4 * height / 5), Point(x + 11 * width / 10, y))
    p2 = Polygon(Point(x + width / 19, y - height / 20), Point(x + width / 2, y - 17 * height / 25), Point(x + 18 * width / 19, y - height / 20))
    p1.setFill(home_color)
    p2.setFill(roof_color)

    r1 = Rectangle(Point( x + width / 15, y + height / 6), Point(x + 5 * width / 15, y + 3 * height / 6))
    r2 = Rectangle(Point( x + 10 * width / 15, y + height / 6), Point(x + 14 * width / 15, y + 3 * height / 6))
    r3 = Rectangle(Point( x + 22 * width / 60, y + height / 3), Point(x + 38 * width / 60, y + height))


    r1.setFill(window_color)
    r2.setFill(window_color)
    r3.setFill(door_color)

    l1 = Line(Point(x + width / 15, y + 2 * height / 6), Point(x + 5 * width / 15, y + 2 * height / 6))
    l2 = Line(Point(x + 3 * width / 15, y + height / 6), Point(x + 3 * width / 15, y + 3 * height / 6))
    l3 = Line(Point(x + 10 * width / 15, y + 2 * height / 6), Point(x + 14 * width / 15, y + 2 * height / 6))
    l4 = Line(Point(x + 12 * width / 15, y + height / 6), Point(x + 12 * width / 15, y + 3 * height / 6))
    if storona_ruchki == 1 :
        l5 = Line(Point(x + 24 * width / 60, y + 2 * height / 3), Point(x + 26 * width / 60, y + 2 * height / 3))
    else :
        l5 = Line(Point(x + 34 * width / 60, y + 2 * height / 3), Point(x + 36 * width / 60, y + 2 * height / 3))


    r.draw(win)
    p1.draw(win)
    p2.draw(win)
    r1.draw(win)
    r2.draw(win)
    r3.draw(win)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    l4.draw(win)
    l5.draw(win)

    if lines == True:
        p2.setWidth(5)
        for k in range(4):
            i = 2 * k

            line = Line(Point(x + (1 + i) * width  / 19, y - 2 * i * height / 25 - height / 25), Point(x + (18 - i) * width / 19, y - 2 * i * height / 25 - height / 25))
            line.setOutline("black")
            line.draw(win)

def human(x, y, height, width, body_color, window):
    body = Oval(Point(x, y + height / 4), Point(x + width, y + 5 * height / 7))
    head = Oval(Point(x, y), Point(x + width, y + height / 4))
    leg1 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x, y + height))
    leg2 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x + width, y + height))
    arm1 = Line(Point(x + width / 8, y + 6 * height / 16), Point(x - width / 3, y + 4 * height / 7))
    arm2 = Line(Point(x + 7 * width / 8, y + 6 * height / 16), Point(x + 4 * width / 3, y + 4 * height / 7))
    eye1 = Circle(Point(x + width / 4, y + height / 16), 1)
    eye2 = Circle(Point(x + 3 * width / 4, y + height / 16), 1)
    mouth = Line(Point(x + width / 3, y + 3 * height / 16), Point(x + 2 * width / 3, y + 3 * height / 16))

    body.setFill(body_color)
    head.setFill(body_color)
    leg1.setOutline(body_color)
    leg2.setOutline(body_color)
    arm1.setOutline(body_color)
    arm2.setOutline(body_color)
    mouth.setOutline("red")
    eye1.setFill("blue")
    eye2.setFill("blue")

    arm1.setWidth(3)
    arm2.setWidth(3)
    leg1.setWidth(3)
    leg2.setWidth(3)

    head.draw(window)
    leg1.draw(window)
    leg2.draw(window)
    arm1.draw(window)
    arm2.draw(window)
    body.draw(window)
    eye2.draw(window)
    eye1.draw(window)
    mouth.draw(window)
    k = 1
    while(1==1):
        for i in range(1, 12001):
            if(i % 100 == 0):
                body.move(k, k*sin(i/30000))
                head.move(k, k*sin(i/30000))
                leg1.move(k, k*sin(i/30000))
                leg2.move(k, k*sin(i/30000))
                arm1.move(k, k*sin(i/30000))
                arm2.move(k, k*sin(i/30000))
                eye1.move(k, k*sin(i/30000))
                eye2.move(k, k*sin(i/30000))
                mouth.move(k, k*sin(i/30000))
        k = k*(-1)   

def sun(x, y, r, window):
    c = Circle(Point(x,y), r)
    c.draw(window)
    c.setFill('yellow')

def cloud(x, y, height, width, color, window):
    cloud = Oval(Point(x, y), Point(x + width, y + height))
    cloud.setWidth(2)
    cloud.setFill(color)
    cloud.draw(window)

def tree(x, y, height, width, bush_color, color, window):
    bush = Oval(Point(x, y), Point(x + width, y + 2 * height / 3))
    tree = Rectangle(Point(x + 4 * width / 10, y + height / 5),  Point(x + 6 * width / 10, y + height))
    bush.setFill(bush_color)
    tree.setFill(color)
    bush.setWidth(3)
    tree.draw(window)
    bush.draw(window)



r00 = Rectangle(Point(0,0), Point(800, 280))
r00.draw(win)
r00.setFill("#00A2E8")

r0 = Rectangle(Point(0,280), Point(800, 400))
r0.draw(win)
r0.setFill("green")


home(200, 200, "red", "grey", "#00A2E8", "#B97A57", 110, 160, True, 2, win)

sun(500, 70, 30, win)

cloud(600, 80, 40, 100, "grey", win)

tree(600, 200, 100, 100,"green", "brown", win)

human(50, 300, 80, 28, "grey", win)

while (1 < 0): 
    pravda = "Yest smisl jit"

win.getMouse()
win.close()
