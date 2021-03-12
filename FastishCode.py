import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
#import cProfile
#import pstats
#profiler = cProfile.Profile()
#profiler.enable()


start2 = time.time()

def dU_dx(U, x):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], -2*U[1] - 2*U[0] + np.cos(2*x)]
U0 = [0, 0]
xs = np.linspace(0, 10, 200)
Us = odeint(dU_dx, U0, xs)
ys = Us[:,0]

end2 = time.time()
print('Time for code run (not including the plot):',end2-start2, 'sec')

#profiler.disable()
#stats = pstats.Stats(profiler).sort_stats('cumtime')
#stats.print_stats()
#stats.dump_stats('results.prof')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped harmonic oscillator")
plt.plot(xs,ys);
