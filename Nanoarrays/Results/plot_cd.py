import numpy as np
import matplotlib.pyplot as plt
import pandas

filename = "50nmVis"
data = pandas.read_csv(filename+".csv",index_col=0)


save_filename = "CD_Knipper_5nmres_50nm_slit.png"
data_array = data.to_numpy()

wavelength_array = data_array[:,0]

#rev is reversed/backwards, for is forwards
t_l_rev = data_array[:,1]
t_r_rev = data_array[:,2]
t_l_for = data_array[:,3]
t_r_for = data_array[:,4]

abs_r_rev = -np.log10(t_r_rev)
abs_l_rev = -np.log10(t_l_rev)
abs_r_for = -np.log10(t_r_for)
abs_l_for = -np.log10(t_l_for)



cd_for = abs_l_for-abs_r_for
cd_rev=  abs_l_rev-abs_r_rev

cd_for_check = -np.log10(t_l_for/t_r_for)

import numpy.testing as np_test
np_test.assert_array_almost_equal(cd_for,cd_for_check)

fig, ax = plt.subplots()

ax.plot(wavelength_array,cd_for,label = "Front",color = "red")
ax.plot(wavelength_array,cd_rev,label = "Back",color ="blue")
ax.set_xlabel("Wavelength (nm)",fontsize= 16)
ax.set_ylabel("CD (dim.)",fontsize = 16)
fig.legend(fontsize= 12,loc = "upper left",bbox_to_anchor = (.25,.95,0,0))

plt.tight_layout()
fig.savefig(save_filename)
fig.show()
