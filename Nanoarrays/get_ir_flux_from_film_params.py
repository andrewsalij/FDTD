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
import json

def main():
    resolution = int(sys.argv[1]) # int
    polarization  = sys.argv[2] #x y r l , str
    to_make_film = json.loads(sys.argv[3].lower()) #bool
    sx, sy = float(sys.argv[4]),float(sys.argv[5]) #float
    dx, dy1, dy2 , theta = float(sys.argv[6]),float(sys.argv[7]),float(sys.argv[8]),float(sys.argv[9]) #float
    au, sio2, sin = geom.load_film_materials()
    freq_center,freq_width = float(sys.argv[10]),float(sys.argv[11])
    directory = sys.argv[12]
    wavelength_max = 1/(freq_center-freq_width)
    sio2_z, au_z, sin_z = .15,.05,.15
    film_thickness = sio2_z+au_z+sin_z
    sz, dpml,refl_z,source_z,trans_z =  geom.z_values_from_wavelength(wavelength_max,film_thickness)
    cell, pml_layers,k_point = geom.create_cell(size_array = np.array([sx,sy,sz]),dpml = dpml)
    if (to_make_film):
        geometry, etch_thickness, film_center = geom.create_multilayer_film(cell,sio2,au,sin,z_offset = 0,mat1_z=sio2_z,mat2_z=au_z,mat3_z=sin_z)
        geom.create_crosshatch(geometry,etch_thickness,film_center,dx,dy1,dy2,0,theta)
    else:
        geometry = []
    source = sources.polarized_source(freq_center,freq_width,cell,z_offset=  source_z,source_type=polarization)
    fluxes = sources.create_fluxes(cell,trans_z=trans_z,refl_z=refl_z)
    sim = sim_management.create_sim(cell,pml_layers,geometry,source,resolution,k_point)

    flux_values = sources.add_fluxes(sim,fluxes,freq_center,freq_width,200)
    sim.init_sim()
    sim.filename_prefix = "film"
    refl_flux = flux_values[1]
    if (to_make_film):
        pwd = os.getcwd()
        #you have to do this terribleness of changing directories bc
        #meep only reads files correctly if you are currently in the directory of the file
        #due to adding prefixes and suffixes
        norm_path = os.path.abspath(os.path.join(directory, '..', "1"))
        # normalization runs are always saved in same directory in folder "1"
        flux_path = os.path.join(norm_path, 'refl_flux')
        os.chdir(norm_path)
        print(flux_path)
        print(flux_values[1])
        sim.load_minus_flux('refl_flux', refl_flux)
        os.chdir(pwd)
    sim_management.run_sim(sim,"decay")
    sources.save_flux_values("flux",flux_values)
    if (not to_make_film):
        sim.save_flux("refl_flux",refl_flux)
if __name__ == "__main__":
   main()