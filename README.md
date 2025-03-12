Scripts and higher-level functionality for finite-difference time-domain (FDTD)
calculations using MEEP (https://meep.readthedocs.io/en/latest/).

To install dependencies, run
```bash
pip install h5py matplotlib meep numpy pandas 
```

sim_management.py, flux.py, and sources.py provide functionality for calculating spectra of
materials in shapes designated via geom.py. 

Material fitting provides parameterization from and raw data to the Lorentz-Drude model. Some fitting
has been done in RefFIT, https://doi.org/10.1063/1.1979470.

Crosshatch geometries designed to extend the work in
Knipper, Richard, et al. "Observation of giant infrared circular dichroism in plasmonic
2D-metamaterial arrays." Acs Photonics 5.4 (2018): 1176-1180.
doi https://doi.org/10.1021/acsphotonics.7b01477

<figure>
<img src=https://github.com/andrewsalij/FDTD/blob/main/Nanoarrays/Results/CD_5nmres_50nm_slit.png alt="Circular dichroism from 2D chiral gold plasmonic thin film." width = "300px"/>
<figcaption align = "center">Circular dichroism from 2D chiral gold plasmonic thin film. Note: This was created to check if near infrared material parameterization gave reasonable results in visible region, which it does above ~400 nm. This figure is a prototype and should not be used as (converged) data.</figcaption>
</figure>

Code is provided on an "as is" basis and the user assumes responsibility for its use.

