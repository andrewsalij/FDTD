import matplotlib.pyplot as plt
import numpy as np

#The runs are designed to create .npy files that contain
#freqs, refl_flux, and trans_flux

#Note that baseline normalization runs are needed for proper norming

def load_fluxes(filename):
    data=  np.load(filename)
    freqs= data[:,0]
    refl_flux = data[:,1]
    trans_flux = data[:,2]
    return freqs, refl_flux, trans_flux

def load_normed_flux(filename,norm_filename):
    freqs, refl_flux, trans_flux = load_fluxes(filename)
    freqs_n, refl_flux_n,trans_flux_n = load_fluxes(norm_filename)
    return freqs,  (trans_flux)/trans_flux_n,((-refl_flux+refl_flux_n)/trans_flux_n)

#values must be normed
def get_loss(refl,trans):
    return 1-refl-trans

#fluxes must be over same bounds
def create_flux_set(*fluxes):
    num = len(fluxes)
    flux_set = np.zeros((num,np.size(fluxes[1])))
    for i in np.arange(num):
        flux_set[i,:] = fluxes[i]
    return flux_set

