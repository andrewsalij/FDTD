import geom
import sources
import meep as mp
import sys, os
mod_directory = '~Documents/GitHub/FDTD'
sys.path.append(mod_directory)
mod_directory = '/home/ahs1068/FDTD'
sys.path.append(mod_directory)

def create_sim(cell,pml_layers,geometry,source,resolution,k_point):
    return mp.Simulation(cell_size=cell,
                    geometry_center = mp.Vector3(0,0,0),
                    boundary_layers=pml_layers,
                    geometry=geometry,
                    sources=source,
                    resolution=resolution,
                    k_point = k_point)

#factor is amount to the edge that you go
def get_sim_base(sim,factor = .95):
    cen_z = sim.geometry_center.z
    edge_z = sim.cell_size.z
    layer_z = sim.boundary_layers[0].thickness
    z = (cen_z-edge_z/2+layer_z)*factor
    return z
#end_time can be number in t or, if string, other parameters
def run_sim(sim,end_time,dt=  50):
    if type(end_time) == str:
        #for now, only handles decay at base of sim
        base_z = get_sim_base(sim)
        point = mp.Vector3(0,0,base_z)
        condition = mp.stop_when_fields_decayed(dt,mp.Ex,point,1e-3)
    else:
        condition = end_time
    sim.run(until=condition)




