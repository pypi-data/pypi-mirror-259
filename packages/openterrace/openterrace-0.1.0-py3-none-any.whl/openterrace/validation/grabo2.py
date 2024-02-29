""" Validation using the experiments presented by Grabo et al. "Modeling and improvement of a packed bed latent heat storage filled with non-spherical encapsulated PCM-Elements", https://doi.org/10.1016/j.renene.2021.04.022 """

import openterrace
import numpy as np
import matplotlib.pyplot as plt
import os

#load grabo data
grabo_sim = np.loadtxt(os.path.dirname(os.path.realpath(__file__))+"/grabo_A.txt", dtype=float)

ot = openterrace.Simulate(t_end=60*800, dt=0.1)

fluid = ot.create_phase(n=290, type='fluid')
fluid.select_substance_on_the_fly(rho=990, cp=4179, k=0.64)
fluid.select_domain_shape(domain='cylinder_1d', D=0.79, H=1.9)
fluid.select_porosity(phi=0.65)
fluid.select_schemes(diff='central_difference_1d', conv='upwind_1d')
fluid.select_initial_conditions(T=273.15+47)
fluid.select_massflow(mdot=360/3600) #ok
fluid.select_bc(bc_type='fixed_value', parameter='T', position=(slice(None, None, None), 0), value=273.15+67)
fluid.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), -1), value=0)
fluid.select_output(times=range(0, 800*60+60, 30))

bed = ot.create_phase(n=40, n_other=290, type='bed')
bed.select_substance('ATS58')
bed.select_domain_shape(domain='hollow_sphere_1d', Rinner=0.0553, Router=0.0665, Vcapsule=0.0005253)
bed.select_schemes(diff='central_difference_1d')
bed.select_initial_conditions(T=273.15+47)
bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), 0))
bed.select_bc(bc_type='zero_gradient', parameter='T', position=(slice(None, None, None), -1))
bed.select_output(times=range(0, 800*60+60, 30))

ot.select_coupling(fluid_phase=0, bed_phase=1, h_exp='constant', h_value=70)
ot.run_simulation()

plt.plot(fluid.data.time/60,fluid.data.T[:,0,-1]-273.15,'k')
plt.plot(grabo_sim[:,0], grabo_sim[:,1],'ob')
plt.show()
plt.xlabel('Time (min)')
plt.ylabel(u'Outlet temperature (℃)')
plt.xlim([0, 800])
plt.ylim([45, 70])
plt.grid()
plt.grid(which='major', color='#DDDDDD', linewidth=1)
plt.grid(which='minor', color='#EEEEEE', linestyle=':', linewidth=0.8)
plt.minorticks_on()
plt.savefig('grabo.png')