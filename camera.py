import numpy as np
import pygame
from matrices import *

class Camera():
    def __init__(self, render, pos, hfov = 60, near = 0.1, far = 10, speed = 0.02, sensitivity = 0.002):
        self.render = render
        self.position = np.array([*pos, 1])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

        self.hfov = hfov
        self.vfov = hfov * (render.HEIGHT / render.WIDTH)

        self.near = near
        self.far = far

        self.speed = speed
        self.sensitivity = sensitivity

    def control(self):
        key = pygame.key.get_pressed()
        # Movement aswd
        if key[pygame.K_a]:
            self.position -= self.right * self.speed
        if key[pygame.K_d]:
            self.position += self.right * self.speed
        if key[pygame.K_w]:
            self.position += self.forward * self.speed
        if key[pygame.K_s]:
            self.position -= self.forward * self.speed

        # Fly and land
        if key[pygame.K_SPACE]:
            self.position += self.up * self.speed
        if key[pygame.K_LSHIFT]:
            self.position -= self.up * self.speed

        # Rotate camera
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

        mouse_dx, mouse_dy = pygame.mouse.get_rel()  # Get mouse movement

        self.camera_yaw(mouse_dx * self.sensitivity)
        self.camera_pitch(mouse_dy * self.sensitivity)
        
        

    def camera_yaw(self, a):
        rotate = rotate_y(a)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate
     
    def camera_pitch(self, a):
        rotate = rotate_x(a)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate
    
        

    def translate_matrix(self):
        dx, dy, dz, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-dx, -dy, -dz, 1]
        ])
    
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up

        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
    
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()