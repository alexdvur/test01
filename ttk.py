from Tkinter import *
from math import *
from random import randrange as rnd, choice
import time
print('Enter your name!')
user = raw_input()
print('Well done! You are registered! Lets try to beat smbs record!')


root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
l_name = Label(root, bg='black', fg='white', width=800)
l_name.pack()
l_name['text'] = user
end = Button(text='End game!', width=30)
l = Label(root, bg='black', fg='white', width=800)
l.pack()
end.pack()
canv.pack(fill=BOTH,expand=1)




exp_3 = 0

colors = ['red','orange','yellow','green','blue']



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


def endgame():
	global exp_3, user, root
	f = open("file.txt", 'a')
	print >> f, user, ": ", exp_3, "\n"
	f.close()
	root.destroy()


def new_ball_3():
	global koord_x_1,koord_x_2,koord_y_1,koord_y_2,koord_x_3,koord_y_3,radius, dx_1, dx_2, dy_1, dy_2, dx_3, dy_3, c1, c2, c3
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



def click_3(event):
	global x,y,r, exp_3, koord_x_1, koord_y_1, koord_x_2, koord_y_2, koord_x_3, koord_y_3, c1, c2, c3, dx_1, dx_2, dx_3, dy_1, dy_2, dy_3
	x = event.x
	y = event.y
	r1 = sqrt((koord_x_1 - x)**2 + (koord_y_1 - y)**2)
	r2 = sqrt((koord_x_2 - x)**2 + (koord_y_2 - y)**2)
	r3 = sqrt((koord_x_3 - x)**2 + (koord_y_3 - y)**2)
	r = min(r1, r2, r3)
	if(r == r1):
		if ( r <= radius / 2):
			exp_3 += 10
			canv.delete(c1)
			koord_x_1 = rnd(100,700)
			koord_y_1 = rnd(100,500)
			dx_1 = rnd(-3,3)
			dy_1 = rnd(-3,3)
			c1 = canv.create_oval(koord_x_1-radius,koord_y_1-radius,koord_x_1+radius,koord_y_1+radius,fill = choice(colors), width=0)
			l['text'] = exp_3
		elif ( r <= radius ):
			canv.delete(c1)
			koord_x_1 = rnd(100,700)
			koord_y_1 = rnd(100,500)
			dx_1 = rnd(-3,3)
			dy_1 = rnd(-3,3)
			c1 = canv.create_oval(koord_x_1-radius,koord_y_1-radius,koord_x_1+radius,koord_y_1+radius,fill = choice(colors), width=0)
			exp_3 += 5
			l['text'] = exp_3
		else:
			exp_3 -= 5
			l['text'] = exp_3
	elif(r == r2):
		if ( r <= radius / 2):
			exp_3 += 10
			canv.delete(c2)
			koord_x_2 = rnd(100,700)
			koord_y_2 = rnd(100,500)
			dx_2 = rnd(-3,3)
			dy_2 = rnd(-3,3)
			c2 = canv.create_oval(koord_x_2-radius,koord_y_2-radius,koord_x_2+radius,koord_y_2+radius,fill = choice(colors), width=0)
			l['text'] = exp_3
		elif ( r <= radius ):
			canv.delete(c1)
			koord_x_2 = rnd(100,700)
			koord_y_2 = rnd(100,500)
			dx_2 = rnd(-3,3)
			dy_2 = rnd(-3,3)
			c2 = canv.create_oval(koord_x_2-radius,koord_y_2-radius,koord_x_2+radius,koord_y_2+radius,fill = choice(colors), width=0)
			exp_3 += 5
			l['text'] = exp_3
		else:
			exp_3 -= 5
			l['text'] = exp_3
	elif(r == r3):
		if ( r <= radius / 2):
			exp_3 += 10
			canv.delete(c3)
			koord_x_3 = rnd(100,700)
			koord_y_3 = rnd(100,500)
			dx_3 = rnd(-3,3)
			dy_3 = rnd(-3,3)
			c3 = canv.create_oval(koord_x_3-radius,koord_y_3-radius,koord_x_3+radius,koord_y_3+radius,fill = choice(colors), width=0)
			l['text'] = exp_3
		elif ( r <= radius ):
			canv.delete(c3)
			koord_x_3 = rnd(100,700)
			koord_y_3 = rnd(100,500)
			dx_3 = rnd(-3,3)
			dy_3 = rnd(-3,3)
			c3 = canv.create_oval(koord_x_3-radius,koord_y_3-radius,koord_x_3+radius,koord_y_3+radius,fill = choice(colors), width=0)
			exp_3 += 5
			l['text'] = exp_3
		else:
			exp_3 -= 5
			l['text'] = exp_3



new_ball_3()
canv.bind('<Button-1>', click_3)
end.config(command=endgame)

mainloop()


