from Tkinter import *
from math import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
l = Label(root, bg='black', fg='white', width=800)
l.pack()
canv.pack(fill=BOTH,expand=1)
'''
exp_1 = 0
exp_2 = 0
'''
exp_3 = 0

colors = ['red','orange','yellow','green','blue']

'''
koord_x = rnd(100,700)
koord_y = rnd(100,500) 
dx = rnd(-3,3)
dy = rnd(-3,3)
'''

radius = rnd(30,50)

koord_x_1 = rnd(100,700)
koord_y_1 = rnd(100,500)
koord_x_2 = rnd(100,700)
koord_y_2 = rnd(100,500)
koord_x_3 = rnd(100,700)
koord_y_3 = rnd(100,500)
dx_1 = rnd(-3,3)
dy_1 = rnd(-3,3)
dx_2 = rnd(-3,3)
dy_2 = rnd(-3,3)
dx_3 = rnd(-3,3)
dy_3 = rnd(-3,3)


'''
def new_ball_1():
	global koord_x_1, koord_y_1, radius, dx_1, dy_1
	canv.delete(ALL)
	if ((koord_x_1 - radius < 3) or (koord_x_1 + radius > 797)): dx_1 = -dx_1
	if ((koord_y_1 - radius < 3) or (koord_y_1 + radius > 577)): dy_1 = -dy_1
	c1 = canv.create_oval(koord_x_1-radius,koord_y_1-radius,koord_x_1+radius,koord_y_1+radius,fill = choice(colors), width=0)
	koord_x_1 = koord_x_1 + dx_1
	koord_y_1 = koord_y_1 + dy_1
	root.after(10, new_ball_1)





def new_ball_2():
	global koord_x_1,koord_x_2,koord_y_1,koord_y_2,radius, dx_1, dx_2, dy_1, dy_2
	canv.delete(ALL)
	if ((koord_x_1 - radius < 3) or (koord_x_1 + radius > 797)): dx_1 = -dx_1
	if ((koord_y_1 - radius < 3) or (koord_y_1 + radius > 577)): dy_1 = -dy_1
	if ((koord_x_2 - radius < 3) or (koord_x_2 + radius > 797)): dx_2 = -dx_2
	if ((koord_y_2 - radius < 3) or (koord_y_2 + radius > 577)): dy_2 = -dy_2
	c1 = canv.create_oval(koord_x_1-radius,koord_y_1-radius,koord_x_1+radius,koord_y_1+radius,fill = choice(colors), width=0)
	c2 = canv.create_oval(koord_x_2-radius,koord_y_2-radius,koord_x_2+radius,koord_y_2+radius,fill = choice(colors), width=0)
	koord_x_1 = koord_x_1 + dx_1
	koord_y_1 = koord_y_1 + dy_1
	koord_x_2 = koord_x_2 + dx_2
	koord_y_2 = koord_y_2 + dy_2
	root.after(10,new_ball_2)

'''

def new_ball_3():
	global koord_x_1,koord_x_2,koord_y_1,koord_y_2,koord_x_3,koord_y_3,radius, dx_1, dx_2, dy_1, dy_2, dx_3, dy_3
	canv.delete(ALL)
	if ((koord_x_1 - radius < 3) or (koord_x_1 + radius > 797)): dx_1 = -dx_1
	if ((koord_y_1 - radius < 3) or (koord_y_1 + radius > 577)): dy_1 = -dy_1
	if ((koord_x_2 - radius < 3) or (koord_x_2 + radius > 797)): dx_2 = -dx_2
	if ((koord_y_2 - radius < 3) or (koord_y_2 + radius > 577)): dy_2 = -dy_2
	if ((koord_x_3 - radius < 3) or (koord_x_3 + radius > 797)): dx_3 = -dx_3
	if ((koord_y_3 - radius < 3) or (koord_y_3 + radius > 577)): dy_3 = -dy_3
	c1 = canv.create_oval(koord_x_1-radius,koord_y_1-radius,koord_x_1+radius,koord_y_1+radius,fill = choice(colors), width=0)
	c2 = canv.create_oval(koord_x_2-radius,koord_y_2-radius,koord_x_2+radius,koord_y_2+radius,fill = choice(colors), width=0)
	c3 = canv.create_oval(koord_x_3-radius,koord_y_3-radius,koord_x_3+radius,koord_y_3+radius,fill = choice(colors), width=0)
	koord_x_1 = koord_x_1 + dx_1
	koord_y_1 = koord_y_1 + dy_1
	koord_x_2 = koord_x_2 + dx_2
	koord_y_2 = koord_y_2 + dy_2
	koord_x_3 = koord_x_3 + dx_3
	koord_y_3 = koord_y_3 + dy_3
	root.after(10,new_ball_3)

'''
def click_1(event):
	global x,y,r, exp_1
	x = event.x
	y = event.y
	r = sqrt((koord_x - x)**2 + (koord_y - y)**2)
	if ( r <= radius / 2):
		exp_1 += 10
		l['text'] = exp_1
	elif ( r <= radius ):
		exp_1 += 5
		l['text'] = exp_1
	else:
		l['text'] = exp_1

def click_2(event):
	global x,y,r, exp_2
	x = event.x
	y = event.y
	r1 = sqrt((koord_x_1 - x)**2 + (koord_y_1 - y)**2)
	r2 = sqrt((koord_x_2 - x)**2 + (koord_y_2 - y)**2)
	r = min(r1, r2)
	if ( r <= radius / 2):
		exp_2 += 10
		l['text'] = exp_2
	elif ( r <= radius ):
		exp_2 += 5
		l['text'] = exp_2
	else:
		l['text'] = exp_2
'''

def click_3(event):
	global x,y,r, exp_3
	x = event.x
	y = event.y
	r1 = sqrt((koord_x_1 - x)**2 + (koord_y_1 - y)**2)
	r2 = sqrt((koord_x_2 - x)**2 + (koord_y_2 - y)**2)
	r3 = sqrt((koord_x_3 - x)**2 + (koord_y_3 - y)**2)
	r = min(r1, r2, r3)
	if ( r <= radius / 2):
		exp_3 += 10
		l['text'] = exp_3
	elif ( r <= radius ):
		exp_3 += 5
		l['text'] = exp_3
	else:
		l['text'] = exp_3


new_ball_3()
canv.bind('<Button-1>', click_3)
mainloop()


