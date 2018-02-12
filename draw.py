from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #constants
    b=-(x1-x0)
    a=y1-y0
    x=x0
    y=y0
    if(b>0):
        draw_line(x1,y1,x0,y0,screen,color)
    #first octant:
    if(a<=-b and a>0 and b<=0):
        d=2*a+b
        while x<=x1:
            plot (screen, color,x,y)
            if(d>0):
                y+=1
                d+=2*b
            x+=1
            d+=2*a
    #Second Octant:
    if(a>=-b and a>=0 and b<=0):
        d=2*b+a
        while(y<y1):
            plot(screen,color,x,y)
            if (d<0):
                x+=1
                d+=2*a
            y+=1
            d+=2*b
    #Seventh Octant:
    if(a<=b and a<=0 and b<=0):
        d=a-2*b
        while(y>y1):
            plot(screen,color,x,y)
            if(d>0):
                x+=1
                d+=2*a
            y-=1
            d-=2*b
    #We done:
    if(a>=b and a<=0 and b<=0):
        d=2*a-b;
        while(x<x1):
            plot(screen,color,x,y)
            if(d<0):
                y-=1
                d-=2*b
            x+=1
            d+=a+a

