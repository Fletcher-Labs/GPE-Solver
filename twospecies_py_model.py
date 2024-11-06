"""Spectral method for evolving GPE for BEC's"""

import numpy as np
from numpy.fft import fft2, ifft2, fftshift
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
import math
import scipy as sp

# %matplotlib inline
matplotlib.rcParams['figure.dpi'] = 200
plt.rcParams["animation.html"] = "jshtml"


### Initialize wavefunction(s)
# Decide num components, system size, discretization
params = {    'a1': 7,
              'm1': 12,
              'mu1': 1,
              'a2': 10,
              'm2': 1,
              'mu2': 2,
              'a12': 15,
              'wx1': 3,
              'wy1': 3,
              'wz1': 0.3,
              'wx2': 10,
              'wy2': 10,
              'wz2': 1,
              'T': 0.0625,
              'xmax':1.0,
              'N':32
              }

### Evolve via whatever terms
# Evolve wavefunction in real space for contact and potential interactions
# Evolve in k-space for kinetic and dipolar interactions
# Allow for imaginary time evolution
class Simulation:
    """Simulation to step wavefunction forward in time from the given parameters
xmax : maximum extent of boundary
N    : number of spatial points
init : initial wavefunction
nonlinearity : factor in front of |psi^2| term
"""
    def __init__(self, params):
        self.params = params

        # set up spatial dimensions
        xmax = params['xmax']
        self.xmax = xmax
        N = params['N']
        v = np.linspace(-xmax, xmax, N)
        self.dx = v[1] - v[0]
        self.x, self.y, self.z = np.meshgrid(v, v, v)

        # spectral space
        kmax = 2*np.pi / self.dx
        dk = kmax / N
        self.k = fftshift((np.arange(N)-N/2) * dk)
        kx, ky, kz = np.meshgrid(self.k, self.k, self.k)

        # time
        self.time = 0
        self.dt = self.dx**2 / 4
        self.steps = int(params['T']/self.dt)

        # wavefunction
        m1 = params['m1']
        m2 = params['m2']
        wx1 = params['wx1']
        wx2 = params['wx2']
        wy1 = params['wy1']
        wy2 = params['wy2']
        wz1 = params['wz1']
        wz2 = params['wz2']
        a1 = params['a1']
        a2 = params['a2']
        a12 = params['a12']
        self.wf1 = np.exp(-(m1*wx1*(self.x-0.125)**2 + m1*wy1*(self.y-0)**2 + m1*wz1*(self.z-0.625)**2))#normalized 3D gaussian based on trap
        self.wf2 = np.exp(-(m2*wx2*(self.x+0)**2 + m2*wy2*(self.y+0)**2 + m2*wz2*(self.z+0)**2))#normalized 3D gaussian based on trap

        # Hamiltonian operators
        self.T1 = np.exp(-1j * (kx**2 + ky**2 + kz**2)/2/m1 * self.dt / 2)
        self.T2 = np.exp(-1j * (kx**2 + ky**2 + kz**2)/2/m2 * self.dt / 2)
        self.V1 = np.exp(-1j * (wx1**2*self.x**2 + wy1**2*self.y**2 + wz1**2*self.z**2)/2 * self.dt / 2)
        self.V2 = np.exp(-1j * (wx2**2*self.x**2 + wy2**2*self.y**2 + wz2**2*self.z**2)/2 * self.dt / 2)
        self.I1 = np.exp(-1j * (a1*abs(self.wf1)**2 + a12*abs(self.wf2)**2) * self.dt / 2)
        self.I2 = np.exp(-1j * (a2*abs(self.wf2)**2 + a12*abs(self.wf1)**2) * self.dt / 2)
        self.D11 = 0
        self.D22 = 0
        self.D12 = 0
        self.LHY1 = 0
        self.LHY2 = 0


    def evolve(self, time):
        """Evolve the wavefunction to the given time in the future"""
        steps = int(time / self.dt)
        if steps == 0:
            steps = 1 # guarantee at least 1 step

        for _ in range(steps):
            self.pos_step()
            self.k_step()

        self.update_time(steps)

        
    def pos_step(self):
        """Make one pos step dt forward in time"""
        # nonlinear
        self.wf1 = self.I1*self.wf1
        self.wf2 = self.I2*self.wf2

        # potential
        self.wf1 = self.V1*self.wf1
        self.wf2 = self.V2*self.wf2

        # LHY


    def k_step(self):
        """Make one nonlinear step dt forward in time"""

        # kinetic and dipolar
        self.wf1[:] = fft2(ifft2(self.wf1) * self.T1)
        self.wf2[:] = fft2(ifft2(self.wf2) * self.T2)


    def update_time(self, steps):
        """Increment time by steps taken"""
        self.steps += steps
        self.time = self.steps * self.dt

    def norm1(self):
        return (np.abs(self.wf1)**2)[:,:,int(self.params['N']/2)]#xz cut of wf1

    def norm2(self):
        return (np.abs(self.wf2)**2)[:,:,int(self.params['N']/2)]#xz cut of wf2

    def show(self):
        """Show the current norm of the wavefunction"""
        fig, ax = plt.subplots()
        ax.imshow(self.norm(), cmap=plt.cm.hot)
        plt.show()


# Animate
def animate(simulation, interval=100):
    """Display an animation of the simulation"""
    fig, ax = plt.subplots(1,2)
    L = simulation.xmax
    norm1 = ax[0].imshow(simulation.norm1(), extent=(-L, L, -L, L), cmap=plt.cm.hot)
    ax[0].set_title('psi1^2, T = '+str(sim.time))
    norm2 = ax[1].imshow(simulation.norm2(), extent=(-L, L, -L, L), cmap=plt.cm.hot)
    ax[1].set_title('psi2^2, T = '+str(sim.time))

    def update(i):
        sim.evolve(0.0625)
        norm1 = ax[0].imshow(simulation.norm1(), extent=(-L, L, -L, L), cmap=plt.cm.hot)
        ax[0].set_title('psi1^2, T = '+str(np.round(sim.time,4)))
        norm2 = ax[1].imshow(simulation.norm2(), extent=(-L, L, -L, L), cmap=plt.cm.hot)
        ax[1].set_title('psi2^2, T = '+str(np.round(sim.time,4)))
        
    anim = animation.FuncAnimation(fig, update, interval=10, frames = 10, cache_frame_data=False)
    plt.show()



# Run
sim = Simulation(params)
animate(sim)
