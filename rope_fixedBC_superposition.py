#animation of wave reflection at a boundary as superposition of two waves - fixed BC
#Author - Bhaskar Kamble

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



fig = plt.figure()
#plt.axis("off")
xleft  = -20.0
xright = -xleft
Amp = 3.0 #amplitude of wave form
yup    =   Amp + 0.4
ydn = -yup
ax = plt.axes(xlim=(xleft,xright),ylim=(ydn,yup))
ax.set_aspect("equal")
ax.axis("off")



lines = []
line1=ax.plot([],[],lw=1,color="blue",linestyle="dotted")[0]  #virtual wave form from left
lines.append(line1)

line2=ax.plot([],[],lw=1,color="green",linestyle="dotted")[0]  #virtual wave form from right
lines.append(line2)

line3=ax.plot([],[],lw=1,color="red")[0]  #real wave
lines.append(line3)

line4=ax.plot([],[],lw=2,color="black")[0]#boundary wall
lines.append(line4)

line5=ax.plot([],[],linestyle="none",marker="o",markersize=5,color="black")[0]
lines.append(line5)




def init():
    for line in lines:
        line.set_data([],[])
    return lines


x=np.linspace(xleft,xright,501)
v = 1.0 #wave speed
tmin = -15.0
tmax = 15.0
time = np.linspace(tmin,tmax,300)
lmbda = 3.0
bias = 0.2 #for better visibility

def animate(i):
    for lnum,line in enumerate(lines):
        y1 = Amp*np.exp(-((x-v*time[i])/lmbda)**2)
        y2 = -Amp*np.exp(-((x+v*time[i])/lmbda)**2)
        y3 = y1 + y2
        if lnum==0:
            line.set_data(x,y1+bias)
        if lnum==1:
            line.set_data(x,y2-bias)
        if lnum==2:
            line.set_data(x[0:x.size/2],y3[0:x.size/2])
        if lnum==3:
            line.set_data([0,0],[ydn,yup])
        if lnum==4:
            line.set_data([0,0],[0,0])
    return lines    
nzt = time.size-1
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=nzt, interval=5, blit=True)
#anim.save("rope_fixedBC_superposition.gif",dpi=80,writer='imagemagick')
plt.show()
