import matplotlib.pyplot as plt
import numpy as np


def plot_fluxes(freqs,flux_set,label_set,x_label,y_label,figure = None,axis = None,
                color_set = ["green","blue","red","black"] ):
    if (figure is None):
        figure, axis = plt.subplots()
    n_flux = np.size(flux_set,axis = 0)
    for i in range(0,n_flux):
        axis.plot(freqs,flux_set[i,:],label = label_set[i],color = color_set[i])
    axis.set_xlabel(x_label)
    axis.set_ylabel(y_label)
    figure.legend()
    figure.show()




