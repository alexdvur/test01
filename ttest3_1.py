from graphics import *
from math import *
#win = GraphWin("MyWin", 1600, 1280)
b_height = 1280
b_width = 1600
win = GraphWin("MyWin", b_width, b_height)
def draw_all(win,color_grass, color_sky, b_height, b_width, color_sun,x ,y, k, bool_truba, bool_smoke, color_roof, color_door, color_door1, color_house, color_truba1, color_truba2, color_window, color_door_hand,
	x_cloud, y_cloud, k_cloud, color_cloud, x_tree, y_tree, k_tree, color_tree, x_man, y_man, k_man, color_man):
	draw_back(win,color_grass, color_sky,  b_height, b_width)
	draw_sun(win, b_height, b_width, color_sun)
	c1,c2,c3 = draw_cloud(win, x_cloud, y_cloud, k_cloud, color_cloud)
	draw_tree(win, x_tree, y_tree, k_tree, color_tree)
	draw_house(win,x,y,k, bool_truba, bool_smoke, color_roof, color_door, color_door1, color_house, color_truba1, color_truba2, color_window, color_door_hand)
	draw_house(win,x = 1200, y = 490, k = 3, bool_truba = True, bool_smoke = False, color_roof = "blue", color_door = "grey", color_door1 = '#F09838',
	color_house = "yellow", color_truba1 = "#8A551C", color_truba2 = "#8A551C", color_window = "#4294F7", color_door_hand = "yellow")
	draw_man(win, x_man, y_man, k_man, color_man)
#	c1,c2,c3 = draw_cloud(win, x_cloud, y_cloud, k_cloud, color_cloud)
	return(c1,c2,c3)

"""
b_height = 1280
b_width = 1600
color_sky = "#368EFF"
color_grass = 'green'
color_sun = 'yellow'
color_roof = "#D33D25"
color_door = "#89551B"
color_door1 = 'brown'
color_house = "#F09838"
color_truba1 = "#8A551C"
color_window = "#4294F7"
color_door_hand = "yellow"
"""

def draw_tree(win, x_tree, y_tree, k_tree, color_tree):
	trunk = Polygon(Point(x_tree, y_tree), Point(x_tree-20/k_tree,y_tree+260/k_tree), Point(x_tree+20/k_tree,y_tree+260/k_tree))
	leaves = Circle(Point(x_tree,y_tree), 150/k_tree)
	trunk.setFill('brown')
	leaves.setFill(color_tree)
	trunk.draw(win)
	leaves.draw(win)

def draw_man(win, x_man, y_man, k_man, color_man):
	body = Oval(Point(x_man-30/k_man, y_man), Point(x_man+30/k_man, y_man+180/k_man))
	l_hand = Line(Point(x_man, y_man), Point(x_man-90/k_man, y_man+90/k_man))
	r_hand = Line(Point(x_man, y_man), Point(x_man+90/k_man, y_man+90/k_man))
	l_leg = Line(Point(x_man, y_man+160/k_man), Point(x_man-30/k_man, y_man+270/k_man))
	r_leg = Line(Point(x_man, y_man+160/k_man), Point(x_man+30/k_man, y_man+270/k_man))
	head = Circle(Point(x_man, y_man-30/k_man), 30/k_man)

	body.setFill(color_man)
	l_hand.setFill(color_man)
	r_hand.setFill(color_man)
	l_leg.setFill(color_man)
	r_leg.setFill(color_man)
	head.setFill(color_man)

	l_hand.setWidth(16/k_man)
	r_hand.setWidth(16/k_man)
	l_leg.setWidth(16/k_man)
	r_leg.setWidth(16/k_man)

	body.draw(win)
	l_hand.draw(win)
	r_hand.draw(win)
	l_leg.draw(win)
	r_leg.draw(win)
	head.draw(win)



def draw_cloud(win, x_cloud, y_cloud, k_cloud, color_cloud):
	cloud1 = Circle(Point(x_cloud,y_cloud), 50/k_cloud)
	cloud2 = Circle(Point(x_cloud+70/k_cloud, y_cloud), 65/k_cloud)
	cloud3 = Circle(Point(x_cloud+140/k_cloud, y_cloud), 50/k_cloud)

	cloud1.setFill(color_cloud)
	cloud2.setFill(color_cloud)
	cloud3.setFill(color_cloud)
	cloud1.setOutline(color_cloud)
	cloud2.setOutline(color_cloud)
	cloud3.setOutline(color_cloud)

	cloud1.draw(win)
	cloud2.draw(win)
	cloud3.draw(win)
	return(cloud1, cloud2, cloud3)

def draw_back(win, color_grass, color_sky, b_height, b_width):
	#win = GraphWin("MyWin", b_width, b_height)
	win.setBackground(color_sky)
	kover2 = Rectangle(Point(0, 0.5*b_height), Point(b_width, b_height))
	kover2.setFill(color_grass)
	kover2.draw(win)
	
def draw_house(win,x,y,k, bool_truba, bool_smoke, color_roof, color_door, color_door1, color_house, color_truba1, color_truba2, color_window, color_door_hand):
	Roof = Polygon(Point(x, y), Point(x+520/k, y-150/k), Point(x + 1040/k, y))
	house = Rectangle(Point(x+40/k, y), Point(x+1000/k, y+550/k))
	door = Rectangle(Point(x+150/k, y+150/k), Point(x+350/k, y+550/k))
	truba1 = Rectangle(Point(x+700/k, y-50/k), Point(x+800/k, y-150/k))
	truba2 = Rectangle(Point(x+680/k, y-150/k), Point(x+820/k, y-175/k))
	door1 = Rectangle(Point(x+160/k, y+160/k), Point(x+240/k, y+240/k))
	door2 = Rectangle(Point(x+160/k, y+260/k), Point(x+240/k, y+300/k))
	door3 = Rectangle(Point(x+160/k, y+320/k), Point(x+240/k, y+530/k))
	door4 = Rectangle(Point(x+260/k, y+160/k), Point(x+340/k, y+240/k))
	door5 = Rectangle(Point(x+260/k, y+260/k), Point(x+340/k, y+300/k))
	door6 = Rectangle(Point(x+260/k, y+320/k), Point(x+340/k, y+530/k))
	l1 = Line(Point(x+250/k, y+150/k), Point(x+250/k, y+550/k))
	l2 = Line(Point(x+150/k, y+250/k), Point(x+350/k, y+250/k))
	window =  Rectangle(Point(x+650/k, y+150/k), Point(x+900/k, y+350/k))
	l3 = Line(Point(x+650/k, y+250/k), Point(x+900/k, y+250/k))
	l4 = Line(Point(x+775/k, y+150/k), Point(x+775/k, y+350/k))
	win_cher = Oval(Point(x+465/k, y-100/k), Point(x+575/k, y-30/k))
	l5 = Line(Point(x+520/k, y-100/k), Point(x+520/k, y-30/k))
	l6 = Line(Point(x+465/k, y-65/k), Point(x+575/k, y-65/k))
	door_hand = Oval(Point(x+330/k, y+335/k), Point(x+310/k, y+350/k))
	smoke1 = Circle(Point(x+750/k, y-200/k), 35/k)
	smoke2 = Circle(Point(x+770/k, y-230/k), 35/k)
	smoke3 = Circle(Point(x+790/k, y-260/k), 30/k)
	smoke4 = Circle(Point(x+810/k, y-290/k), 26/k)

	Roof.setFill(color_roof)
	house.setFill(color_house)
	door.setFill(color_door)
	truba1.setFill(color_truba1)
	truba2.setFill(color_truba2)
	door1.setFill(color_door1)
	door2.setFill(color_door1)
	door3.setFill(color_door1)
	door4.setFill(color_door1)
	door5.setFill(color_door1)
	door6.setFill(color_door1)
	window.setFill(color_window)
	win_cher.setFill(color_window)
	door_hand.setFill(color_door_hand)
	smoke1.setFill('grey')
	smoke2.setFill('grey')
	smoke3.setFill('grey')
	smoke4.setFill('grey')
	smoke1.setOutline('grey')
	smoke2.setOutline('grey')
	smoke3.setOutline('grey')
	smoke4.setOutline('grey')


	if bool_smoke:
		smoke1.draw(win)
		smoke2.draw(win)
		smoke3.draw(win)
		smoke4.draw(win)
	if bool_truba:
		truba1.draw(win)
		truba2.draw(win)
	Roof.draw(win)
	house.draw(win)
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
	door_hand.draw(win)


	

def draw_sun(win, b_height, b_width, color_sun):
	sun = Circle(Point(0.875*b_width, 0.125*b_height), 0.06*b_height )
	sun.setFill(color_sun)
	sun.draw(win)
#	point0 = Circle(Point(200,413), 20)
#	point0.setFill('white')
#	point0.draw(win)

#################################

def check_coords(cl2_x, cl2_y, vx, vy):
	alpha = 0.28
	if cl2_y > 0.29*cl2_x + 121.1-73.5 and cl2_x > 740 and cl2_x < 1240:
		vt = vx * sin(alpha)-vy * cos(alpha)
		vz = vx * cos(alpha) + vy * sin(alpha)
		vx = (-vt * sin(alpha) + vz * cos(alpha))
		vy = (vt * cos(alpha) + vz * sin(alpha))
	
	if cl2_y > -0.29*cl2_x + 545-73.5 and cl2_x > 230 and cl2_x < 740:
		vt = vx * cos(alpha)-vy * sin(alpha)
		vz = -vx * sin(alpha) - vy * cos(alpha)
		vx = vt * cos(alpha) + vz * sin(alpha)
		vy = -vt * sin(alpha) + vz * cos(alpha)
	
	if cl2_y > 0.29*cl2_x + 45.5-73.5 and cl2_x > 1373 and cl2_x < 1550:
		vt = vx * sin(alpha)-vy * cos(alpha)
		vz = vx * cos(alpha) + vy * sin(alpha)
		vx = (-vt * sin(alpha) + vz * cos(alpha))
		vy = (vt * cos(alpha) + vz * sin(alpha))
	
	if cl2_y > -0.29*cl2_x + 836.8-73.5 and cl2_x > 1200 and cl2_x < 1373:
		vt = vx * cos(alpha)-vy * sin(alpha)
		vz = -vx * sin(alpha) - vy * cos(alpha)
		vx = vt * cos(alpha) + vz * sin(alpha)
		vy = -vt * sin(alpha) + vz * cos(alpha)
	

	if cl2_x > 370.7-141.2 and cl2_y > 450 and cl2_x < 400-141.2:
		vx = -vx

	if cl2_x > 400 - 141.2 and cl2_x < 1110+141.2 and cl2_y > 450:
		vx = -vx

	if cl2_x < 141.2 or cl2_x > b_width-141.2:
		vx = -vx
	if cl2_y < 76.5 or cl2_y > 0.5*b_height-76.5:
		vy = -vy
	return(vx,vy)

def open_umbrella(win, x_man, y_man):
	x_um = x_man - 90
	y_um = y_man + 100
	handle = Line(Point(x_um, y_um), Point(x_um, y_um - 250))
	handle.setWidth(10)
	handle.setFill('grey')
#	handle.draw(win)
	umbrella = Polygon(Point(x_um, y_um-250), Point(x_um - 160, y_um - 250+50), Point(x_um + 160, y_um -250+50))
	umbrella.setFill('grey')
	return umbrella, handle
#	umbrella.draw(win)
################################

cl1,cl2,cl3 = draw_all(win,color_grass = '#28A642', color_sky = "#83CDFE", b_height = 1280, b_width = 1600, color_sun = 'yellow', x = 340, y = 450, k = 1.3, bool_truba = True, bool_smoke = True, color_roof = "#D33D25", color_door = "#89551B", color_door1 = 'brown',
	color_house = "#F09838", color_truba1 = "#8A551C", color_truba2 = "#8A551C", color_window = "#4294F7", color_door_hand = "yellow", x_cloud = 1000, y_cloud = 150, k_cloud = 0.85, color_cloud = 'white',
	x_tree = 170, y_tree = 560, k_tree = 1.7, color_tree = 'green', x_man = 350, y_man = 750, k_man = 1, color_man = 'white')

#draw_house(win,x = 1200, y = 490, k = 3, bool_truba = True, bool_smoke = False, color_roof = "blue", color_door = "grey", color_door1 = '#F09838',
#	color_house = "yellow", color_truba1 = "#8A551C", color_truba2 = "#8A551C", color_window = "#4294F7", color_door_hand = "yellow")
#point0 = Circle(Point(300,800), 4)
#point0.setFill('white')
#point0.draw(win)


vx = -1.1
vy = 0.5
umbrella_bool = 0
umbrella, handle = open_umbrella(win, 350, 750)
while True:
	center_point = cl2.getCenter()
	vx, vy = check_coords(center_point.x, center_point.y, vx, vy)
	if center_point.x >200 and center_point.x < 500 and umbrella_bool == 0:
		umbrella.draw(win)
		handle.draw(win)
		umbrella_bool = 1
	if (center_point.x < 200 or center_point.x > 500) and umbrella_bool == 1:
		umbrella.undraw()
		handle.undraw()
		umbrella_bool = 0
	cl1.move(vx,vy)
	cl2.move(vx,vy)
	cl3.move(vx,vy)
	time.sleep(0.002)



win.getMouse()
win.close()



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
