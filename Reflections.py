import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#Nx and Ny determine the resolution of the simulation
Nx = 100
Ny = 100
pi = np.pi
eta = 0.1





#fix the lengths of the rectangular boundary
Rx = 2.0 
Ry = 1.4
# horizontal length = 2*Rx, vertical length = 2*Ry



#set up the grid of image-rectangles
NOx = 10
NOy = 10
orgx = np.linspace(-2.0*NOx*Rx,2.0*NOx*Rx,2.0*NOx+1.0) #-2Rx*NOx, -2Rx*NOx+2Rx, ....,-2Rx,0,2Rx,...2Rx*NOx-2Rx,2Rx*NOx
orgy = np.linspace(-2.0*NOy*Ry,2.0*NOy*Ry,2.0*NOy+1.0)
#the center rectangle is the object rectangle, rest are image-rectangles
#2*NOx+1 rows and 2*NOy+1 columns in the grid




#Coordinates of the source point:
ax = 0.7 # x-coordinate
ay = 0.3 # y-coordinate


#set up coordinates of the image points:
pow_x = np.arange(orgx.size) + NOx
pow_y = np.arange(orgy.size) + NOy
m1_pow_x = (-1)**pow_x
m1_pow_y = (-1)**pow_y
orgx_im = orgx + (ax*m1_pow_x)
orgy_im = orgy + (ay*m1_pow_y)
xorg,yorg=np.meshgrid(orgx_im,orgy_im)






xarr = np.linspace(-Rx,Rx,Nx+1)
yarr = np.linspace(-Ry,Ry,Ny+1)

xmesh,ymesh = np.meshgrid(xarr,yarr)
cap=eta #to avoid "blowing up" when dividing by small numbers



# ___________make the animation____________

fig = plt.figure()
plt.axis("off")




# this is just a dummy function - doesn't matter which function you actually use
def f(x,y):
    fxy = x*x+y*y
    fxy = np.imag(1.0/(fxy-1j*eta))
    return fxy


rad=np.linspace(0,40.0,2800)
im = plt.imshow(f(xmesh,ymesh), animated=True,aspect=Ry/Rx)


title_text = plt.text(4.0,96.0,'$\copyright$2017, Bhaskar Kamble',fontsize=10)

def animate(i):
    global xmesh,ymesh,rad
    radi = rad[i]
    fxy = 0
    for ix in range(2*NOx+1):
        for iy in range(2*NOy+1):
            r = np.sqrt((xmesh-orgx_im[ix])*(xmesh-orgx_im[ix])+(ymesh-orgy_im[iy])*(ymesh-orgy_im[iy]))
            ftemp = r - radi
            r_cap = r.copy()
            r_cap[r<cap] = cap
            ftemp = np.imag(1.0/((ftemp)-1j*eta)) / r_cap
            fxy = fxy + ftemp
    im.set_array(fxy)
    return im,title_text

ani = animation.FuncAnimation(fig, animate, interval=50,frames=2799, blit=True)

#ani.save('ImageMap_09_Rx2Ry1p4_ax0p7_ay0p3.mp4', fps=80, extra_args=['-vcodec', 'libx264'])

plt.show()
