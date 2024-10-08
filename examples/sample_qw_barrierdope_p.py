#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Input File Description:  Barrier doped AlGaAs/GaAs heterostructure.
# -------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------

# TEMPERATURE
T = 300.0 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
# 7: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson then  poisson and DD)
# 8: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD)
# 9: Schrodinger-Poisson-Drift_Diffusion (Schrodinger solved with poisson and DD) using Gummel & Newton map
computation_scheme = 9

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_h = 2
subnumber_e = 2
# APPLIED ELECTRIC FIELD
Fapplied = 0.00#/50e-9 # (V/m)
vmax= 1.4
vmin= 0.0
Each_Step=0.05# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------

# GRID
# For 1D, z-axis is choosen
gridfactor = 1 #nm
maxgridpoints = 200000 #for controlling the size
mat_type='Zincblende'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm) | Material | Alloy fraction | Doping(cm^-3) | n or p type |
# Layer 0 |      250.0     |   Si     |      0         |     1e16      |     n       |
# Layer 1 |      250.0     |   Si     |      0         |     1e16      |     p       |
#
dopp=5e17
# To input this list in Gallium, we use lists as:
material =[[ 100.0, 'AlGaAs', 0.3, 0.0, dopp, 'p','b'],
            [ 40.0, 'AlGaAs', 0.3, 0.0, dopp, 'p','b'],
            [ 20.0, 'GaAs', 0.0, 0.0, 0.0,'n','w'],
            [ 40.0, 'AlGaAs', 0.3, 0.0, dopp, 'n','b'],
            [ 100.0, 'AlGaAs', 0.3, 0.0, dopp, 'n','b']]
#---------------------------------------- 
import numpy as np
x_max = sum([layer[0] for layer in material])
n_max=int(x_max/gridfactor)
#---------------------------------------- 
dop_profile=np.zeros(n_max) 
#----------------------------------------
Quantum_Regions=False
Quantum_Regions_boundary=np.zeros((2,2))
#----------------------------------------  
surface=np.zeros(2)
#----------------------------------------
inputfilename = "sample_qw_barrierdope_p"
from os import path
if __name__ == "__main__": #this code allows you to run the input file directly
    input_obj = vars()
    import sys
    sys.path.append(path.join(path.dirname(__file__), '..'))
    import aestimo_eh
    aestimo_eh.run_aestimo(input_obj)
