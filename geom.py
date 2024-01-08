from __future__ import division
import meep as mp
import numpy as np
import matplotlib.pyplot as plt
import sys, os
mod_directory = '~Documents/GitHub/FDTD'
sys.path.append(mod_directory)
mod_directory = '/home/ahs1068/FDTD'
sys.path.append(mod_directory)
import mat_params

def load_film_materials(type = "ir"):
    au = mat_params.au_ir
    sio2 = mat_params.sio2_ir
    sin = mat_params.sinx_ir
    return au, sio2, sin

def create_cell(size_array = np.array([1,1.8,20]),dpml = 4,boundaries = "periodic"):
    cell = mp.Vector3(size_array[0],size_array[1],size_array[2])
    # in meep, pml goes into the cell as opposed to lumerical, where it is outside the cell
    pml_layers = [mp.PML(dpml, direction=mp.Z)]
    if boundaries == "periodic":
        k_point = mp.Vector3(0,0,0)
    return cell, pml_layers,k_point

def z_values_from_wavelength(max_lambda,film_thickness):
    sz = 2*max_lambda+film_thickness
    dpml = max_lambda/2
    ref_z = sz/2-dpml*1.1
    source_z = sz/2-dpml*1.2
    trans_z = sz/2+dpml*1.1
    return sz, dpml,ref_z,source_z,trans_z


#for knipper films, mat1 = sio2, mat2 = au, mat3 = sin
def create_multilayer_film(cell,mat1,mat2,mat3,z_offset = 0,mat1_z = 0.15,mat2_z = .05,mat3_z= .15):
    sx,sy = cell.x, cell.y

    etch_thickness = mat1_z+mat2_z+mat3_z
    film_center = z_offset+(mat1_z+mat2_z-mat3_z)/2

    layer1 =  mp.Block(mp.Vector3(sx,sy,mat1_z),center= mp.Vector3(0,0,mat2_z+mat1_z/2+z_offset),material=mat1)
    layer2 = mp.Block(mp.Vector3(sx,sy,mat2_z),center= mp.Vector3(0,0,mat2_z/2+z_offset),material=mat2)
    layer3 =  mp.Block(mp.Vector3(sx,sy,mat3_z),center= mp.Vector3(0,0,-mat3_z/2+z_offset),material=mat3)

    geometry = [layer1,layer2,layer3]
    return geometry,etch_thickness,film_center

def cartesian_basis_vectors():
    return mp.Vector3(1,0,0),mp.Vector3(0,1,0),mp.Vector3(0,0,1)
#offset  is from y axis
def cartesian_basis_rotation(theta,axis = mp.Vector3(0,0,1)):
    e1,e2,e3 = cartesian_basis_vectors()
    e1 = e1.rotate(axis,theta)
    e2 = e2.rotate(axis,theta)
    e3 = e3.rotate(axis,theta)
    return e1,e2,e3

#dx, dy refer to slit geometry, not the parameters going into the block object
#theta refers to rotational offset from y-axis, in keeping with Knipper's convention
def create_etch(geometry,etch_thickness,film_center,dx = 0.05,dy = 1.7,theta = 0):
    e1,e2,e3 = cartesian_basis_rotation(theta)
    slit= mp.Block(mp.Vector3(dx,dy,etch_thickness),e1 = e1,e2 = e2, e3= e3,center = mp.Vector3(0,0,film_center))
    geometry.append(slit)

def create_crosshatch(geometry,etch_thickness,film_center,dx,dy1,dy2,theta1,theta2):
    create_etch(geometry,etch_thickness,film_center,dx,dy1,theta1)
    create_etch(geometry,etch_thickness,film_center,dx,dy2,theta2)


