# Animates the reflection of a wave pulse traveling on a rope fixed to a wall.
# Author - Bhaskar Kamble

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



fig = plt.figure()
#plt.axis("off")
xleft  = -20.0
xright =   -xleft
Amp = 3.0 #amplitude of wave form
yup    =   Amp + 0.2
ydn = -yup
ax = plt.axes(xlim=(xleft,xright),ylim=(ydn,yup))
ax.set_aspect("equal")
ax.axis("off")
lines = []
line1=ax.plot([],[],color="red",linestyle="none",marker="o",markersize=2)[0]  #wave form
lines.append(line1)
line2=ax.plot([],[],lw=2,color="black")[0]#boundary wall
lines.append(line2)
line3=ax.plot([],[],linestyle="none",marker="o",markersize=5,color="black")[0]
lines.append(line3)


def init():
    for line in lines:
        line.set_data([],[])
    return lines


x=np.linspace(xleft,0.0,41) #was 501
v = 1.0 #wave speed
tmin = -15.0
tmax = 15.0
time = np.linspace(tmin,tmax,300)
lmbda = 3.0

def animate(i):
    for lnum,line in enumerate(lines):
        y = Amp*np.exp(-((x-v*time[i])/lmbda)**2) - Amp*np.exp(-((x+v*time[i])/lmbda)**2)
        if lnum==0:
            line.set_data(x,y)
        if lnum==1:
            line.set_data([0,0],[ydn,yup])
        if lnum==2:
            line.set_data([0,0],[0,0])
    return lines    
nzt = time.size-1
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=nzt, interval=5, blit=True)
#anim.save("rope_fixedBC.gif",dpi=80,writer='imagemagick')
plt.show()
