#Reflection of a circular wave pulse at a single boundary as a superposition

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#1
fig = plt.figure()

ydn = -10.0
yup = -ydn
xleft = -10.0
xright = 20.0


#2
ax = plt.axes(xlim=(xleft,xright),ylim=(ydn,yup))
ax.set_aspect("equal")
ax.text(4.2,-3.5,'$\copyright$2017, Bhaskar Kamble',fontsize=8,rotation=90)
##ax.axis("off")
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
#https://stackoverflow.com/questions/2176424/hiding-axis-text-in-matplotlib-plots

#3
lines = []
line1=ax.plot([],[],lw=2,color="red")[0]
lines.append(line1)
line2=ax.plot([],[],linestyle="none",marker="o",markersize=3,color="black")[0]
lines.append(line2)
line3=ax.plot([],[],lw=2,color="black")[0]
lines.append(line3)
line4=ax.plot([],[],linestyle="none",marker="o",markersize=3,color="black")[0]
lines.append(line4)
line5=ax.plot([],[],lw=2,linestyle="dashed",color="green")[0]
lines.append(line5)


#4
def init():
    for line in lines:
        line.set_data([],[])
    return lines

ntheta = 201
ntime=101
tmin = 0.0
tmax = 10.0
v = 1.0
theta = np.linspace(0,2.0*np.pi,ntheta)
time = np.linspace(tmin,tmax,ntime)

#5
def animate(i):
    r = v*time[i]
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    #here the boundary at which reflection occurs is at x=5
    xac = x.copy()
    yac = y.copy()
    xac[x>=5.0] = -x[x>=5.0] + 10.0
    x_im = 10.0 + (r-0.1)*np.cos(theta)
    y_im = (r-0.1)*np.sin(theta)
    for lnum,line in enumerate(lines):
        if lnum==0:
            line.set_data(xac,yac)
        if lnum==1:
            line.set_data([0],[0])
        if lnum==2:
            line.set_data([5,5],[ydn,yup])
        if lnum==3:
            line.set_data([10],[0])
        if lnum==4:
            line.set_data(x_im,y_im)
    return lines    

nzt = time.size-1
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=nzt, interval=2, blit=True)
#anim.save("water_one_refl_full_2.gif",dpi=80,writer='imagemagick')
plt.show()

