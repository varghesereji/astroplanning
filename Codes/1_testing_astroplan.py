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

#from datetime import tzinfo
import datetime
# Setting up location

# DOT
# longitude = '+79d41m04s'
# latitude = '+29d21m40s'
# elevation = 2424 * u.m

# HCT
longitude = '+78.9641'  # d41m04s'
latitude = '+32.77944'#29d21m40s'
elevation = 4500 * u.m


location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name='Himalayan Chandra Telescope',
                    location=location,
                    relative_humidity=0.6,
                    temperature=10 * u.deg_C,
                    timezone=timezone('Asia/Kolkata'),
                    description='3.6m DOT, Nainithal')
                    


# Setting up Target


# TOI 5688

RA = '17h49m13.28s'
Dec = '47d36m28.91s'

coordinates = SkyCoord(RA,Dec,frame='icrs')
toi5688 = FixedTarget(name='TOI-5688', coord=coordinates)
'''
#TOI 5359
RA = '03h36m15.85s'
Dec = '30d12m21.35s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
toi5359 = FixedTarget(name='TOI-5359', coord=coordinates)

#TOI 3884
RA = '12h06m17.24s'
Dec = '12d30m25.29s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
toi3884 = FixedTarget(name='TOI-3884', coord=coordinates)

# NGC 2158
# RA = '06h07m26.9s'
# Dec = '+24d05m56s'
RA = '06h11m30.09s'
Dec = '+61d32m06.40s'

coordinates = SkyCoord(RA,Dec,frame='icrs')
ngc2158 = FixedTarget(name='NGC 2158', coord=coordinates)

# lspm
RA = '20h49m27.440s'
Dec = '+33d36m50.96s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
kosh = FixedTarget(name='LSPM J2049+3336', coord=coordinates)
'''
'''
# AS 40

RA = '23h58m50.2s'
Dec = '+61d10m02s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
tirspec_observation = FixedTarget(name='LSPM J2049+3336', coord=coordinates)

# AS 31
RA = '17h44m06.8s'
Dec = '-00d24m58s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
tirspec_observation = FixedTarget(name='LSPM J2049+3336', coord=coordinates)

# AS 17
RA = '07h38m15.5s'
Dec = '+38d56m16s'
coordinates = SkyCoord(RA,Dec,frame='icrs')
tirspec_observation = FixedTarget(name='LSPM J2049+3336', coord=coordinates)
'''

time_f = Time('2024-05-23 12:30:00')
time = time_f + np.linspace(0, 10, 30)*u.hour

# print(observer.local_sidereal_time(time))
tirspec_observation = toi5688

print(observer.target_is_up(time,tirspec_observation))

plt.figure()
plot_sky(tirspec_observation, observer, time)
plt.show(block=False)

plt.figure()
plot_airmass(tirspec_observation, observer, time, brightness_shading=True, altitude_yaxis=True)
plt.show(block=False)
# plt.figure()
# plot_altitude(ngc2158, observer, time)
# plt.show(block=False)

