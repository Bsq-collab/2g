from display import *
from draw import *
from random import randint

screen = new_screen()
color = [ 0, 255, 255 ]

draw_line(0,0,200,250,screen,color)
ctr=0
while(ctr<=500):
    color=[255,255,255]
    draw_line(0,0,500,ctr,screen,color)
    ctr+=20

ctr=0
while(ctr<=500):
    color=[0,255,255]
    draw_line(0,0,ctr,500,screen,color)
    ctr+=20

ctr=0
while(ctr<=500):
    color=[255,0,0]
    draw_line(0,ctr,500,500,screen,color)
    ctr+=20


ctr=0
while(ctr<=500):
    color=[255,255,0]
    draw_line(ctr,0,500,500,screen,color)
    ctr+=20

display(screen)
save_extension(screen, 'img.png')
