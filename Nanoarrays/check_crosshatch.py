import meep as mp
import sys, os
import numpy as np
mod_directory = '/home/andrew/Documents/GitHub/FDTD'
sys.path.append(mod_directory)
mod_directory = '/home/ahs1068/FDTD'
sys.path.append(mod_directory)
import geom
import sim_management
import sources
import math

resolution = 100# int
polarization = "x" # x y r l , str
sx, sy = 1, 1.8
dx, dy1, dy2, theta = .05,1.7,1,math.pi/4
au, sio2, sin = mp.Medium(epsilon=2),mp.Medium(epsilon=3),mp.Medium(epsilon = 4)
freq_center, freq_width = .275,.175
cell, pml_layers, k_point = geom.create_cell(size_array=np.array([sx, sy, 20]))
geometry, etch_thickness, film_center = geom.create_multilayer_film(cell, sio2, au, sin)
geom.create_crosshatch(geometry, etch_thickness, film_center, dx, dy1, dy2, 0, theta)
source = []
sim = sim_management.create_sim(cell, pml_layers, geometry, source, resolution, k_point)
sim.init_sim()

