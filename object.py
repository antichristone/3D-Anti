from OpenGL.GL import *
from OpenGL.GLU import *

import pygame as pg
import random


class Projection_3D():
    def __init__(self, file=None):
        self.speed = 1
        self.camera = -20
        self.cube_v = ( (5, 7), (1, 5), (0, 1), (7, 6), (2, 3), (4, 5), (2, 6), (0, 2), (7, 3), (6, 4), (4, 0), (3, 1) )
        self.cube = ( (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1))
        self.colors = ((1, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (1, 1, 0), (1, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (1, 1, 0))

        if file not in [None]:
            vertex, faces = [], []
            with open(file) as model:
                for line in model:
                    if line.startswith('v '):
                        vertex.append([float(i) for i in line.split()[1:]] + [1])
                    elif line.startswith('f'):
                        faces_ = line.split()[1:]
                        faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

            self.model = [], []
            for data in vertex:
                self.model[0].append((data[0], data[1], data[2]))

            for data in faces:
                self.model[1].append((data[0], data[1], data[2]))

            self.face_vector = []
            for x,y in enumerate(self.model[1]):
                if x % 2 == 0:
                    x1, x2 = self.model[1][x], self.model[1][x-1]
                    self.face_vector.append((x1[0], x1[1], x2[0], x2[1]))

        else:
            self.model = self.cube, self.cube_v
            self.face_vector = []
            for x,y in enumerate(self.model[1]):
                if x % 2 == 0:
                    x1, x2 = self.model[1][x], self.model[1][x-1]
                    self.face_vector.append((x1[0], x1[1], x2[0], x2[1]))

    def control(self):
        key = pg.key.get_pressed()

        if key[pg.K_e]:
            glRotatef(self.speed, 0, 90, 0)

        if key[pg.K_q]:
            glRotatef(self.speed, 0, -90, 0)

        if key[pg.K_d]:
            glRotatef(self.speed, 0, 0, -90)

        if key[pg.K_a]:
            glRotatef(self.speed, 0, 0, 90)

        if key[pg.K_w]:
            glRotatef(self.speed, -90, 0, 0)

        if key[pg.K_s]:
            glRotatef(self.speed, 90, 0, 0)

        if key[pg.K_SPACE]:
            self.speed *= 2

        if key[pg.K_TAB]:
            self.speed = 1


        if key[pg.K_RETURN]:
            glBegin(GL_QUADS)
            for face in self.model[1]:
                for vertex in face:
                    glColor3fv(random.choice(self.colors))
                    glVertex3fv(self.model[0][vertex])

            glEnd()


    def draw_model(self):
        glBegin(GL_LINES)
        for edge in self.model[1]:
            for vertex in edge:
                glVertex3fv(self.model[0][vertex])
        glEnd()
