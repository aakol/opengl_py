import threading
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = ()
verticies1 = ()
verticies2 = ()
print ("START")
plik = open('pliczek1')
try:
    tekst = plik.read()
finally:
    plik.close()
#print(tekst)
x = tekst.replace("("," ")
x1 = x.replace(")"," ")

x3 = str(x1)
x4 = x3.split(",") 
#print(x4)    
i=0
j=0.0
while True:
    try:
        verticies = verticies+((float(x4[i])/50,float(j),float(0)),(float(0.0),float(j),float(0)),)
        #print(float(x4[i]))
        if x4[i]=='':
            break
    except:
        break
    i=i+4
    j=j+0.8
    
ii=0
jj=0.0
while True:
    try:
        verticies1 = verticies1+((float(x4[ii])/50,float(jj),float(0)),(float(0.0),float(jj),float(0)),)
        #print(float(x4[i]))
        if x4[ii]=='':
            break
    except:
        break
    ii=ii+2
    jj=jj+0.08
#print(verticies)
print ("DANE WGRANE")


exit = 0           
xa = 0.0
ya = 0.0
za = -8.0   
            
def Dane():
    global exit
    while (exit <1):
        a = input("X= ")
        b = input("Y= ")
        c = input("Z= ")
        d = input("X= ")
        e = input("Y= ")
        f = input("Z= ")
        
        g =input("koniec 1- dalej 0 :_")
        
        exit = int(g)
        global verticies2
        
        
        verticies2 = verticies2+((float(a),float(b),float(c)), (float(d),float(e),float(f)),)

        print(verticies2)
    exit = 0
    
    return verticies2

def Cube():
    
    glBegin(GL_LINES)
    
    
    glColor3fv((0,1,0))
    glVertex3fv((0,0,0))

    glVertex3fv((3,0,0))
    glEnd()
    glBegin(GL_LINES)
    glColor3fv((1,0,0))
    glVertex3fv((0,0,0))
    glVertex3fv((0,3,0))
    glEnd()
    glBegin(GL_LINES)
    glColor3fv((0,0,1))
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,3))
    
    glEnd()
    
    glBegin(GL_LINES)
    
    for vertex in verticies:
       # print (vertex )
        glColor3fv((1,0.5,1))
        glVertex3fv(vertex)
    
    glEnd()
    
    glBegin(GL_LINES)
    
    for vertex1 in verticies1:
       # print (vertex )
        glColor3fv((1,1,0.5))
        glVertex3fv(vertex1)
    
    glEnd()
    
    glBegin(GL_LINES)
    
    for vertex2 in verticies2:
       # print (vertex )
        glColor3fv((0.5,0.5,0.5))
        glVertex3fv(vertex2)
    
    glEnd()
    


def main():
    
    pygame.init()
    pygame.display.set_caption('okno 3D')
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)

    glTranslatef(xa,ya,za)
    a= True
    
    while (a == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                     glTranslatef(1,0,0)
                if event.key == pygame.K_RIGHT:
                   
                    glTranslatef(-1,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_a:
                    glRotatef(5, 0, 0, 1)
                if event.key == pygame.K_d:
                    glRotatef(5, 0, 0, -1)
                if event.key == pygame.K_w:
                    glRotatef(5, 0, 1, 0)
                if event.key == pygame.K_s:
                    glRotatef(5, 0, -1, 0)
                if event.key == pygame.K_z:
                    glRotatef(5, 1, 0, 0)
                if event.key == pygame.K_x:
                    glRotatef(5, -1, 0, 0)
                if event.key == pygame.K_q:
                   a=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                
                    glTranslatef(0,0,-1.0)
       
        
       
        
        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            
        Cube()
        
         
        pygame.display.flip()
        pygame.time.wait(40)

t=threading.Thread(target=Dane)
t1=threading.Thread(target=main)
#threades.append(t)
#threades.append(t1)
t.start()
t1.start()      