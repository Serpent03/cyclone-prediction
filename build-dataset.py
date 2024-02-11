# https://analyticsindiamag.com/r-cnn-vs-fast-r-cnn-vs-faster-r-cnn-a-comparative-guide/
# interesting: it looks like R-CNN region proposals are actually some kind of union-find algorithm under the hood.

# have found 0 sources for the data, LOL..
# might try using a FRCNN or a RCNN to do the ML training.

"""
* @todo Convert the frames into pictures(black)
* @todo Create XML structures with labelling
* @todo Utilize three different datasets: eastwards wind, northwards wind, and precipitation levels.
"""

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import cartopy.crs as ccrs

import utils

plt.style.use('ggplot')

ds = xr.open_dataset("wind_data_vec-110523-170523.nc")
# print(ds)
# print(ds.variables)

fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})

lons = ds['longitude']
lats = ds['latitude']
eastward_wind = ds['eastward_wind']
northward_wind = ds['northward_wind']

# eastward_wind = eastward_wind.isel(time=18)
image_e = eastward_wind.isel(time=0).plot.imshow(ax=ax[0], transform=ccrs.PlateCarree(), animated=True, cmap='gist_gray')
image_n = northward_wind.isel(time=0).plot.imshow(ax=ax[1], transform=ccrs.PlateCarree(), animated=True, cmap='gist_gray')

def update(t):
    # Update the plot for a specific time
    # print(t)
    ax[0].set_title("time = %s"%t)
    ax[1].set_title("time = %s"%t)
    image_e.set_array(eastward_wind.sel(time=t))
    image_n.set_array(northward_wind.sel(time=t))
    return image_e, image_n, 

# Run the animation, applying `update()` for each of the times in the variable
animation = anim.FuncAnimation(fig, update, frames=eastward_wind.time.values, blit=False)


# plt.contourf(lons, lats, eastward_wind, transform=ccrs.PlateCarree())
ax[0].coastlines()
ax[1].coastlines()

# animation.save('e2w-wind.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
