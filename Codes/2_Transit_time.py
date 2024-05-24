import numpy as np
import matplotlib.pyplot as plt

from astropy.coordinates import SkyCoord
from astropy.time import Time
from astroplan import FixedTarget
from astroplan.plots import plot_airmass, plot_altitude, plot_sky

import astropy.units as u
from astropy.coordinates import EarthLocation
from pytz import timezone
from astroplan import Observer

from astroplan import EclipsingSystem

# Setting up location
longitude = '+79d41m04s'
latitude = '+29d21m40s'
elevation = 2424 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name='Devasthal Optical Telescope',
                    location=location,
                    relative_humidity=0.6,
                    temperature=10 * u.deg_C,
                    timezone=timezone('Asia/Kolkata'),
                    description='3.6m DOT, Nainithal')

# Transit properties.
tr_midpoint = 2459790.58344 * u.day  # 2459443.47179 * u.day

orbital_period = 0.71912603 * u.day #1.630757 * u.day 
eclipse_duration = (27.36/(60*24)) * u.day   # 0.0583 * u.day

primary_eclipse_time = Time(tr_midpoint, format='jd')

lspm = EclipsingSystem(primary_eclipse_time=primary_eclipse_time,
                          orbital_period=orbital_period, duration=eclipse_duration, name='LSPM J2049+3336')

Observing_time = Time('2023-12-17 13:30')
next_transit = lspm.next_primary_eclipse_time(Observing_time, n_eclipses=10)
for f in next_transit:
    print(f)
#print(next_transit)
