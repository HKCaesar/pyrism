# At first we will run the PROSPECT model. To do this we import the prism package.
import prism

# After that we specify the sensing geometry we want to simulate
iza = 35  # Incidence zenith angle
vza = 30  # Viewing zenith angle
raa = 50  # Relative azimuth angle

prospect = prism.PROSPECT(N=1.5,
                          Cab=35,
                          Cxc=5,
                          Cbr=0.15,
                          Cw=0.003,
                          Cm=0.0055)

# To access the attributes there are to ways. Firstly, we can access the whole spectrum with prospect.ks
# (scattering coefficient), prospect.ka (absorption coefficient), prospect.kt (transmittance coefficient),
# prospect.ke (extinction coefficient) and prospect.om (the division of ks through ke). Moreover, you can
# select the coefficient values for the specific bands of ASTER (B1 - B9) or LANDSAT8 (B2 - B7). To access these bands
# type prospect.L8.Bx (x = 2, 3, ..., 7) for Landsat 8 or prospect.ASTER.Bx (x = 1, 2, ..., 9) for ASTER.


# To calculate the PROSAIL model we must call SAIL and specify the scattering and transmittance coefficients with these from PROSPECT like:
prosail = prism.SAIL(iza=iza, vza=vza, raa=raa, ks=prospect.ks, kt=prospect.kt, lidf_type='campbell',
                     lai=3, hotspot=0.25, soil_reflectance=3.14 / 4, soil_moisture=0.15)

# The accessibility of the attributes are the same as the PROSPECT model.
