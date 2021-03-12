import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
dt = 0.002; #sec - chosen in order to have 1000 time steps over the fasted time constant
N = round(11/dt + 1);

t = np.zeros(N);
x1 = np.zeros(N);
x2 = np.zeros(N);
x2dot = np.zeros(N);

#Setting up inital conditions
t[0] = 0;
x1[0] = 0;
x2[0] = 0; 

#Now to do forward euler

for n in range(1,N):
    x2dot[n] = np.cos(2*t[n-1]) - 2*x2[n-1] - 2*x1[n-1];
    t[n] = t[n-1] + dt;
    x2[n] = x2[n-1] + x2dot[n]*dt;
    x1[n] = x1[n-1] + x2[n]*dt;

end = time.time()
print('Time for code run (not including the plot):',end-start, 'sec')
plt.plot(t,x1)
plt.xlabel('Time [s]');
plt.title('Solution to ODE');
