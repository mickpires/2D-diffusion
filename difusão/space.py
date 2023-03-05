from particle import Particle
import numpy as np
import numpy.random as rnd

class Space:
    def __init__(self, Np=3, dt=1):
        self.steps = []
        self.Np = Np
        self.current_step = 0
        self.dt = dt
        self.particles = [
            Particle(id=i, velocity = np.array([1,0])) for i in range(self.Np)]
            
    def mainloop(self):
        self.steps.append(self.current_step)
        self.current_step += self.dt
        for particle in self.particles:
            self.changeVelocity(particle)
            self.euler(particle)
        return


    def euler(self, particle: Particle):
        particle.previous_position.append(particle.position)
        particle.position = particle.position + particle.velocity * self.dt
        return


    def changeVelocity(self,particle:Particle):
        particle.velocity = np.array([0,0])
        number = np.floor(rnd.uniform(0,4))

        match number:
            case 0:
                particle.velocity[0] = 1
            case 1:
                particle.velocity[0] = -1
            case 2:
                particle.velocity[1] = 1
            case 3:
                particle.velocity[1] = -1
            case _:
                return