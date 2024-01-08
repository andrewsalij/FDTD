
import h5py
import numpy as np
import matplotlib.pyplot as plt

def plot_array_pair(array_pair,axis = None):
    if (axis is None):
        plt.plot(array_pair[:,0],array_pair[:,1])
        plt.show()
    else:
        axis.plot(array_pair[:,0],array_pair[:,1])

def load_dset_by_label(filename,label):
    data = h5py.File(filename,'r')
    return data[label]
