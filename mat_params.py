import numpy as np 
import meep as mp 


'''
Final chosen material parameters. ReFFit used for fitting.
Kuzmenko, A. B. (2005). Kramers–Kronig constrained variational analysis of optical spectra. Review of scientific instruments, 76(8).
https://doi.org/10.1063/1.1979470

See https://meep.readthedocs.io/en/latest/Python_Tutorials/Material_Dispersion/
 '''
def cm_inv_to_eV(value):
    return 1.23981e-4*value
def freq_to_sigma(w_0,w_p):
    return w_p**2/w_0**2
# default unit length is 1 um
um_scale = 1.0

# to convert from eV to the um units meep uses
eV_um_scale = um_scale/1.23984193

'''
SINx fits to the IR regime
Kischkat, J., Peters, S., Gruska, B., Semtsiv, M., Chashnikova, M., Klinkmüller, M., ... & Masselink, W. T. (2012). 
Mid-infrared optical properties of thin films of aluminum oxide, 
titanium dioxide, silicon dioxide, aluminum nitride, and silicon nitride. Applied optics, 51(28), 6789-6798.
https://doi.org/10.1364/AO.51.006789'''

sinx_ir_w_0 = cm_inv_to_eV(835.47)*eV_um_scale
sinx_ir_gam_0 = cm_inv_to_eV(158.64)*eV_um_scale
sinx_ir_wp_0 = cm_inv_to_eV(1042.7)*eV_um_scale
sinx_ir_sig_0 = freq_to_sigma(sinx_ir_w_0,sinx_ir_wp_0)

sinx_ir_w_1 = cm_inv_to_eV(927.56)*eV_um_scale
sinx_ir_gam_1 = cm_inv_to_eV(139.41)*eV_um_scale
sinx_ir_wp_1 = cm_inv_to_eV(823.66)*eV_um_scale
sinx_ir_sig_1 = freq_to_sigma(sinx_ir_w_1,sinx_ir_wp_1)

sinx_e_inf = 3.62

sinx_susp = [mp.LorentzianSusceptibility(frequency = sinx_ir_w_0,gamma= sinx_ir_gam_0,sigma = sinx_ir_sig_0),
             mp.LorentzianSusceptibility(frequency = sinx_ir_w_1,gamma = sinx_ir_gam_1,sigma = sinx_ir_sig_1)]

sinx_ir = mp.Medium(epsilon = sinx_e_inf,E_susceptibilities=sinx_susp)

'''
SiO2 IR fitting to lorentzian
data from refractive index database and fit to 1000-4500 cm inv region
Kischkat, J., Peters, S., Gruska, B., Semtsiv, M., Chashnikova, M., Klinkmüller, M., ... & Masselink, W. T. (2012).
 Mid-infrared optical properties of thin films of aluminum oxide, titanium dioxide, silicon dioxide, 
 aluminum nitride, and silicon nitride. Applied optics, 51(28), 6789-6798.
 https://doi.org/10.1364/AO.51.006789.'''

sio2_ir_w_0 = cm_inv_to_eV(1072.4)*eV_um_scale
sio2_ir_wp_0 = cm_inv_to_eV(239.54)*eV_um_scale
sio2_ir_gam_0 = cm_inv_to_eV(27.532)*eV_um_scale
sio2_ir_sig_0 = freq_to_sigma(sio2_ir_w_0,sio2_ir_wp_0)

sio2_ir_w_1= cm_inv_to_eV(1047.9)*eV_um_scale
sio2_ir_wp_1 = cm_inv_to_eV(864.46)*eV_um_scale
sio2_ir_gam_1 = cm_inv_to_eV(74.147)*eV_um_scale
sio2_ir_sig_1 = freq_to_sigma(sio2_ir_w_1,sio2_ir_wp_1)

sio2_ir_e_inf = 2.09

sio2_susp = [mp.LorentzianSusceptibility(frequency = sio2_ir_w_0,gamma = sio2_ir_gam_0,sigma = sio2_ir_sig_0),
             mp.LorentzianSusceptibility(frequency = sio2_ir_w_1,gamma = sio2_ir_gam_1,sigma = sio2_ir_sig_1)]

sio2_ir = mp.Medium(epsilon = sio2_ir_e_inf,E_susceptibilities= sio2_susp)

'''
 Au IR fit to 1 Lorentzian at ~.4 eV and a Drude model of Babar and Weaver (2015), 
 Babar, S., & Weaver, J. H. (2015). Optical constants of Cu, Ag, and Au revisited. Applied Optics, 54(3), 477-481.
 DOI:10.1364/AO.54.000477.
'''
au_ir_w_d = 8.5436*eV_um_scale # in eV
au_ir_gam_d = 0.021501*eV_um_scale
au_ir_sig_d = 1

au_ir_w0 = .5067*eV_um_scale
au_ir_wp_0 = .4439*eV_um_scale
au_ir_gam_0 = .15335*eV_um_scale
au_ir_sig_0 = freq_to_sigma(au_ir_w0,au_ir_wp_0)

au_ir_e_inf = 7.55

au_ir_susp = [mp.DrudeSusceptibility(frequency = au_ir_w_d,gamma = au_ir_gam_d,sigma = au_ir_sig_d),
              mp.LorentzianSusceptibility(frequency = au_ir_w0,gamma = au_ir_gam_0,sigma = au_ir_sig_0)] 

au_ir = mp.Medium(epsilon = au_ir_e_inf,E_susceptibilities = au_ir_susp) 
