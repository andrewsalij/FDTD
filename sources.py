import numpy as np
import meep as mp

'''Creation of custom sources for meep simulations
see https://meep.readthedocs.io/en/latest/Python_Tutorials/Custom_Source/'''

def polarized_source(freq_center,freq_width,cell,z_offset= 5.8,source_type = "x"):
#has to be this terrible type checking
    sx,sy = cell.x, cell.y
    if (source_type == "x"):
        source = [mp.Source(mp.GaussianSource(freq_center,fwidth = freq_width),
                 component=mp.Ex,
                 center=mp.Vector3(0,0,z_offset),
                 size=mp.Vector3(sx,sy,0))]
    elif (source_type == "y"):
        source = [mp.Source(mp.GaussianSource(freq_center, fwidth = freq_width),
                component=mp.Ey,
                center=mp.Vector3(0, 0, z_offset),
                size=mp.Vector3(sx, sy, 0))]
    elif (source_type == "r"):
        source = [mp.Source(mp.GaussianSource(freq_center,fwidth =  freq_width),
                   component=mp.Ex,
                   center=mp.Vector3(0, 0, z_offset),
                   size=mp.Vector3(sx, sy, 0)),
                  mp.Source(mp.GaussianSource(freq_center,fwidth = freq_width),
                    component = mp.Ey,
                    center = mp.Vector3(0,0,z_offset),
                    size = mp.Vector3(sx,sy,0),
                    amplitude=1j)]
    elif (source_type == "l"):
        source = [mp.Source(mp.GaussianSource(freq_center, fwidth = freq_width),
                component=mp.Ex,
                center=mp.Vector3(0, 0, z_offset),
                size=mp.Vector3(sx, sy, 0)),
                mp.Source(mp.GaussianSource(freq_center,fwith = freq_width),
                component=mp.Ey,
                center=mp.Vector3(0, 0, z_offset),
                size=mp.Vector3(sx, sy, 0),
                amplitude=-1j)]
    return source

def create_fluxes(cell,trans_z = -5.5,refl_z = 5.9,):
    sx,sy = cell.x,cell.y
    trans_flux_center = mp.Vector3(0, 0, trans_z)
    ref_flux_center = mp.Vector3(0, 0, refl_z)
    flux_size = mp.Vector3(sx, sy, 0)
    trans_flux = mp.FluxRegion(center=trans_flux_center, size=flux_size)
    refl_flux = mp.FluxRegion(center=ref_flux_center, size=flux_size)
    return [trans_flux, refl_flux]

def add_fluxes(simulation,flux_list,freq_center,freq_width,n_freq):
    flux_values = []
    for flux in flux_list:
        flux_values.append(simulation.add_flux(freq_center, freq_width, n_freq, flux))
    return flux_values

def save_array_data(filename,data):
    np.save(filename,np.array(data))

def save_flux_values(file_header,flux_values,labels = None,save_separate = False):
    flux_freqs = mp.get_flux_freqs(flux_values[0])
    if (save_separate):
        np.save(file_header + "freqs", flux_freqs)
    if (labels is None):
        n = len(flux_values)
        labels = np.linspace(1,n,n).astype('str')
    for i in range(0,len(flux_values)):
        flux_v = flux_values[i]
        flux_data = mp.get_fluxes(flux_v)
        if (save_separate):
            np.save(file_header+labels[i],flux_data)
        else:
            if (i == 0):
                flux_data_total = np.c_[flux_freqs,flux_data]
            else:
                flux_data_total = np.c_[flux_data_total,flux_data]
    if (~save_separate):
        np.save(file_header,flux_data_total)


