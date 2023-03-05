import numpy as np
import numpy.random as rnd


class Particle:
    def __init__(self, id, velocity=np.array([1, 0]), position=np.array([0, 0])):
        self.id = id
        self.velocity = velocity.copy()
        self.position = position.copy()
        self.previous_position = []  