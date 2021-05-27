import pygame as pg

from object import Projection_3D
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *


pg.init()
display = (500, 500)
pg.display.set_caption("3D | Antichrist")
screen=pg.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)
glTranslatef(0.001, 0.02, -70)


model=Projection_3D('Skull_v3_L2.obj') #'Karambit.obj' or 'Skull_v3_L2.obj')

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    model.draw_model()
    model.control()
    pg.display.flip()
    #pg.time.wait(10)

pg.quit()
