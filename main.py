import pygame
from camera import *
from projection import *
from objects import Cube

class Render:
    def __init__(self):
        pygame.init()
        self.RES = self.WIDTH, self.HEIGHT = 1000, 600
        self.FPS = 144

        self.screen = pygame.display.set_mode(self.RES)
        pygame.display.set_caption("3D render from scratch")

        self.clock = pygame.time.Clock()

        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.cube = Cube(self)

        self.cube.translate([0.2, 0.4, 0.2])
        

    def draw(self):
        self.screen.fill(pygame.Color('white'))
        self.cube.draw()
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
            
            self.draw()
            self.camera.control()
            
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

if __name__ == "__main__":
    render = Render()
    render.run()
