import numpy as np

class Projection:
    def __init__(self, render):
        n = render.camera.near
        f = render.camera.far

        r = np.tan(np.radians(render.camera.hfov) / 2)
        l = -r

        t = np.tan(np.radians(render.camera.vfov) / 2)
        b = -t

        self.projection_matrix = np.array([
            [2 / (r - l), 0, 0, 0],
            [0, 2 / (t - b), 0, 0],
            [0, 0 , (f + n) / (f - n), 1],
            [0, 0, -2 * n * f / (f - n), 0]
        ])

        HALF_WIDTH, HALF_HEIGHT = render.WIDTH / 2, render.HEIGHT / 2
        
        self.to_screen_matrix = np.array([
            [HALF_WIDTH, 0, 0, 0],
            [0, -HALF_HEIGHT, 0, 0],
            [0, 0, 1, 0],
            [HALF_WIDTH, HALF_HEIGHT, 0, 1]
        ])
        
        