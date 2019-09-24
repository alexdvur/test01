from graphics import *
#win = GraphWin("MyWin", 1600, 1280)

def draw_all(color_grass, color_sky, b_height, b_width, color_sun):
	draw_back(color_grass, color_sky,  b_height, b_width)
	draw_house()
	draw_sun(b_height, b_width, color_sun)
	draw_tree()
"""
b_height = 1280
b_width = 1600
color_sky = "#368EFF"
color_grass = 'green'
color_sun = 'yellow'
"""

def draw_back(color_grass, color_sky, b_height, b_width):
	win = GraphWin("MyWin", b_width, b_height)
	win.setBackground(color_sky)
	kover2 = Rectangle(Point(0, 0.5*b_height), Point(b_width, b_height))
	kover2.setFill(color_grass)
	kover2.draw(win)
	win.getMouse()
	win.close()
def draw_house():
	pass

def draw_sun(b_height, b_width, color_sun):
	sun = Circle(Point(0.875*b_width, 0.125*b_height), 0.125*b_height )
	sun.setFill(color_sun)
	sun.draw(win)
def draw_tree():
	pass

draw_all(color_grass = 'green', color_sky = "#368EFF", b_height = 1280, b_width = 1600, color_sun = 'yellow')

"""
Roof = Polygon(Point(0, 200), Point(520, 50), Point(1040, 200))
house = Rectangle(Point(40, 200), Point(1000, 750))
door = Rectangle(Point(150, 350), Point(350, 750))
door1 = Rectangle(Point(160, 360), Point(240, 440))
door2 = Rectangle(Point(160, 460), Point(240, 500))
door3 = Rectangle(Point(160, 520), Point(240, 730))
door4 = Rectangle(Point(260, 360), Point(340, 440))
door5 = Rectangle(Point(260, 460), Point(340, 500))
door6 = Rectangle(Point(260, 520), Point(340, 730))
l1 = Line(Point(250, 350), Point(250, 750))
l2 = Line(Point(150, 450), Point(350, 450))
window =  Rectangle(Point(650, 350), Point(900, 550))
l3 = Line(Point(650, 450), Point(900, 450))
l4 = Line(Point(775, 350), Point(775, 550))
truba1 = Rectangle(Point(700, 150), Point(800, 50))
truba2 = Rectangle(Point(680, 50), Point(820, 25))
win_cher = Oval(Point(465, 100), Point(575, 170))
l5 = Line(Point(520, 100), Point(520, 170))
l6 = Line(Point(465, 135), Point(575, 135))
#l7 = Line(Point(0, 700), Point(40, 700))
#l8 = Line(Point(1000, 700), Point(1280, 700))
door_hand = Oval(Point(330, 535), Point(310, 550))
kover = Polygon(Point(0, 700), Point(40, 700), Point(40, 750), Point(1000, 750), Point(1000, 700), Point(1080, 700), Point(1080, 1280), Point(0, 1280))
sun = Oval(Point(1000, 0), Point(1280, 200))
kover2 = Rectangle(Point(0, 600), Point(1600, 1280))

#win.setBackground("#368EFF")
kover2.setFill("green")
Roof.setFill("#D33D25")
door.setFill("#89551B")
window.setFill("#4294F7")
win_cher.setFill("#4294F7")
door1.setFill("brown")
door2.setFill("brown")
door3.setFill("brown")
door4.setFill("brown")
door5.setFill("brown")
door6.setFill("brown")
door_hand.setFill("yellow")
truba1.setFill("#8A551C")
truba2.setFill("#8A551C")
house.setFill("#F09838")
#door.setWidth(4)
door.setOutline("black")
#house.setWidth(5)
#Roof.setWidth(7)
Roof.setOutline("#FE6B1C")
#l1.setWidth(3)
#l2.setWidth(3)
#l3.setWidth(7)
#l4.setWidth(7)
#l5.setWidth(7)
#l6.setWidth(7)
#l7.setWidth(5)
#l8.setWidth(5)
#win_cher.setWidth(7)
#window.setWidth(10)
#door_hand.setWidth(3)
#door_hand.setOutline("yellow")
#l7.setFill("green")
#l8.setFill("green")
#kover.setWidth(0)
#kover.setFill("green")
sun.setFill("yellow")
sun.setOutline("yellow")
"""
"""
kover2.draw(win)

truba1.draw(win)
truba2.draw(win)
house.draw(win)
Roof.draw(win)

door.draw(win)
door1.draw(win)
door2.draw(win)
door3.draw(win)
door4.draw(win)
door5.draw(win)
door6.draw(win)
l1.draw(win)
l2.draw(win)
window.draw(win)
l3.draw(win)
l4.draw(win)
win_cher.draw(win)
l5.draw(win)
l6.draw(win)
#l7.draw(win)
#l8.draw(win)
door_hand.draw(win)
sun.draw(win)

win.getMouse()
win.close()
"""
