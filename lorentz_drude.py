import numpy as np



def lorentz_susp(sigma,w_n,gamma,spectrum):
    return sigma*w_n**2/(w_n**2-spectrum**2-1j*gamma*spectrum)

def drude_susp(sigma,w_n,gamma,spectrum):
    return sigma*w_n**2/(-spectrum**2-1j*gamma*spectrum)

def eV_to_um(value):
    return 1.2398/value

def um_to_eV(value):
    return 1.2398/value

def eV_to_um_inv(value):
    return 1/eV_to_um(value)

def um_inv_to_eV(value):
    return um_to_eV(1/value)

def cm_inv_to_eV(value):
    return 1.23981e-4*value

def um_inv_to_cm_inv(value):
    return 1e4*value

def susp_to_ref_index(eps_inf,susp):
    eps_total = eps_inf+susp
    n = np.sqrt(eps_total)
    return np.real(n),np.imag(n)

def freq_to_sigma(w_0,w_p):
    return w_p**2/w_0**2


