import numpy as np
import pygame
from matrices import *

class Object3D:
    def __init__(self, render, vertices, faces):
        self.render = render
        self.vertices = vertices
        self.faces = faces

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        # transfer object vertices into camera space
        vertices = self.vertices @ self.render.camera.camera_matrix()

        # transfer to clip space
        vertices = vertices @ self.render.projection.projection_matrix

        # normalize the coordinate
        vertices[vertices[:, -1] == 0, -1] = 1
        vertices /= vertices[:, -1].reshape(-1, 1)

        #remove unnecessary coordinate
        vertices[(vertices > 1) | (vertices < -1)] = 0

        vertices = vertices @ self.render.projection.to_screen_matrix

        vertices = vertices[:,:2]

        for face in self.faces:
            polygon = vertices[face]
            if not np.any((polygon == self.render.WIDTH/2) | (polygon == self.render.HEIGHT/2)):
                pygame.draw.polygon(self.render.screen, pygame.Color('red'), polygon, 3)

        for vertice in vertices:
            if not np.any((vertice == self.render.WIDTH/2) | (vertice == self.render.HEIGHT/2)):
                pygame.draw.circle(self.render.screen, pygame.Color('black'), vertice, 6)


    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, n):
        self.vertices = self.vertices @ scale(n)

    def rotate_x(self, a):
        self.vertices = self.vertices @ rotate_x(a)
    
    def rotate_y(self, a):
        self.vertices = self.vertices @ rotate_y(a)

    def rotate_z(self, a):
        self.vertices = self.vertices @ rotate_z(a)


class Cube(Object3D):
    def __init__(self, render):
        vertices = np.array([
            (0, 0, 0, 1), 
            (0, 0, 1, 1),
            (1, 0, 1, 1),
            (1, 0, 0, 1),
            (0, 1, 0, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
            (1, 1, 0, 1)
        ])
        
        faces = np.array([
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 4, 5, 1),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4)
        ])

        super().__init__(render, vertices, faces)