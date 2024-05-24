import numpy as np
import matplotlib.pyplot as plt
import os

from astropy.io import ascii

from astropy.coordinates import SkyCoord
from astropy.time import Time
from astroplan import FixedTarget
from astroplan.plots import plot_airmass, plot_altitude, plot_sky

import astropy.units as u
from astropy.coordinates import EarthLocation
from pytz import timezone
from astroplan import Observer
from astroplan import AltitudeConstraint
from astroplan import AtNightConstraint
from astroplan import is_observable

# Setting up location
longitude = '+79d41m04s'
latitude = '+29d21m40s'
elevation = 2424 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name='Devasthal Optical Telescope',
                    location=location,
                    relative_humidity=0.6,
                    temperature=21.5 * u.deg_C,
                    timezone=timezone('Asia/Kolkata'),
                    description='3.6m DOT, Nainithal')

# Calling the list of targets
table = ascii.read('PS_2023.11.29_05.05.54.csv')


# Setting up constraing
constraints = [AltitudeConstraint(20*u.deg, 80*u.deg)]

dates = ['08', '09', '17', '18']
i = 0

while i < len(dates):
    time = Time('2023-12-{} 18:00:00'.format(dates[i])) + np.linspace(0, 6, 10)*u.hour
    time_range = Time(["2023-12-{} 18:00:00".format(dates[i]), "2023-12-{} 23:59:59".format(dates[i])])


    possible_target = []
    plt.figure()
    dirname = '202312'+dates[i]
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    for n, host in enumerate(table['hostname']):
        ra = table['rastr'][n]
        dec = table['decstr'][n]
        coordinates = SkyCoord(ra, dec, frame='icrs')
        target = FixedTarget(name=host, coord=coordinates)
        observable = observer.target_is_up(time, target)
        observable = is_observable(constraints, observer, target, time_range=time_range)
        
        if observable[0] ==  True:
            if host not in possible_target:
                plt.figure()
                plt.title(target)
                print(host, ra, dec)
                plot_sky(target, observer, time)
                possible_target.append(host)
                plt.savefig(os.path.join(dirname,'SkyMap_202312{}_{}'.format(dates[i],host)))
    i += 1
