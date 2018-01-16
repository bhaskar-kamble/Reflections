# Animation of multiple reflections of a wave-pulse in a square boundary as a line plot - shows a 5x5 grid with the superposition of the image waves as well
# Author - Bhaskar Kamble

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#consider a square of side 2R filled with water. 
#The center of the square lies at the origin.
# A disturbance is created at a point on the water's surface.
# We want to track the disturbance as a function of time including all the possible reflections at the surface.

rx=0.0
ry=0.0

R=1.0
px = rx*R #the point's x-coordinate
py = ry*R #the point's y-coordinate

Nx = 10
Ny = 10 # the lattice is Nx by Ny.

orgx = np.linspace(-2.0*Nx*R,2.0*Nx*R,2.0*Nx+1.0) #-2R*Nx, -2R*Nx+2R, ....,-2R,0,2R,...2R*Nx-2R,2R*Nx
orgy = np.linspace(-2.0*Ny*R,2.0*Ny*R,2.0*Ny+1.0)


xorg,yorg=np.meshgrid(orgx,orgy)

xorg = xorg.ravel()
yorg = yorg.ravel()




fig = plt.figure()
#ax = plt.axes(xlim=(-R,R),ylim=(-R,R))
ax = plt.axes(xlim=(-5.0*R,5.0*R),ylim=(-5.0*R,5.0*R))
ax.set_aspect("equal")
#ax.text(-1.0,1.02,'$\copyright$2017, Bhaskar Kamble',fontsize=12)
ax.text(-5.0,5.02,'$\copyright$2017, Bhaskar Kamble',fontsize=12)
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

lines = []
for ix in range(2*Nx+1):
    for iy in range(2*Ny+1):
        line1 = ax.plot([],[],marker="o",color="black",markersize=2)[0]
        lines.append(line1)
        line2 = ax.plot([],[],lw=2,color="red")[0]
        lines.append(line2)
#the above has generated (2*Nx+1)*(2*Ny+1) number of objects for the expanding circles
#now you have to add the boundaries
#-5R, -3R etc.
##########################################################
for ii in range(4):
    line1 = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]
    lines.append(line1)
for ii in range(4):
    line1 = ax.plot([],[],lw=1,color="black",linestyle="dotted")[0]
    lines.append(line1)
for ii in range(4):
    line1 = ax.plot([],[],lw=2,color="black")[0]
    lines.append(line1)
##########################################################


def init():
    for line in lines:
        line.set_data([],[])
    return lines

dt=0.001
v =27.0
rmax = 10.0*R
npoints = int(rmax/(v*dt))
radius= np.linspace(0,rmax,npoints)

def animate(i):
    theta = np.linspace(0,2.0*np.pi,200)
    counter = 0
    counter2 = 0
    counter3 = 0
    for lnum,line in enumerate(lines):
        if lnum%2==0 and lnum<2*(2*Nx+1)*(2*Ny+1):
            xc = xorg[counter]
            yc = yorg[counter]
            line.set_data(xc,yc)#if lnum is even, plots just the center point
        if lnum%2!=0 and lnum<2*(2*Nx+1)*(2*Ny+1):
            rad   = radius[i]
            x_rip = xc + rad*np.cos(theta)
            y_rip = yc + rad*np.sin(theta)
            line.set_data(x_rip,y_rip)#if lnum is odd, plots the ripple
            counter+=1
        if lnum>=2*(2*Nx+1)*(2*Ny+1) and lnum<2*(2*Nx+1)*(2*Ny+1)+4:
            line.set_data([(-3.0+counter2)*R,(-3.0+counter2)*R],[-5.0*R,5.0*R])
            counter2+=2
        if lnum>=2*(2*Nx+1)*(2*Ny+1)+4 and lnum<2*(2*Nx+1)*(2*Ny+1)+8:
            line.set_data([-5.0*R,5.0*R],[(-3.0+counter3)*R,(-3.0+counter3)*R])
            counter3+=2
        if lnum == 2*(2*Nx+1)*(2*Ny+1)+8:
            line.set_data([-R,R],[-R,-R])
        if lnum == 2*(2*Nx+1)*(2*Ny+1)+9:
            line.set_data([-R,R],[R,R])
        if lnum == 2*(2*Nx+1)*(2*Ny+1)+10:
            line.set_data([R,R],[-R,R])
        if lnum == 2*(2*Nx+1)*(2*Ny+1)+11:
            line.set_data([-R,-R],[-R,R])
    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=npoints-1, interval=32, blit=True)

#anim.save('Reflections03_forblog_02.mp4', fps=80, extra_args=['-vcodec', 'libx264'])
#anim.save("Reflections03_forblog_02_all.gif",dpi=80,writer='imagemagick')
#anim.save("Reflections03_forblog_02_unitcell.gif",dpi=80,writer='imagemagick')

plt.show()
