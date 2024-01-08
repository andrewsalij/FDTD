import meep as mp
import sys, os
mod_directory = '~Documents/GitHub/FDTD'
sys.path.append(mod_directory)
mod_directory = '/home/ahs1068/FDTD'
sys.path.append(mod_directory)
import geom
import sim_management
import sources

resolution = 50
au, sio2, sin = geom.load_film_materials()
freq_center,freq_width = .275, .175
cell, pml_layers,k_point = geom.create_cell()
geometry, etch_thickness, film_center = geom.create_multilayer_film(cell,au,sio2,sin)
geom.create_etch(geometry,etch_thickness,film_center)
source = sources.polarized_source(freq_center,freq_width,cell,z_offset=  5.8)
fluxes = sources.create_fluxes(cell)
sim = sim_management.create_sim(cell,pml_layers,geometry,source,resolution,k_point)
flux_values = sources.add_fluxes(sim,fluxes,freq_center,freq_width,100)
sim.init_sim()
eps_data = sim.get_epsilon()
sim.filename_prefix = "geom_test"
sim_management.run_sim(sim,mp.output_efield,1)
sources.save_flux_values("test_flux_quest",flux_values)
