from space import *

dt = 1
Np = 100
final_step = 1000

simulation = Space(Np=100,dt=1)

while simulation.current_step <= final_step:
    print(simulation.current_step)
    simulation.mainloop()

print(simulation.particles[0].position)