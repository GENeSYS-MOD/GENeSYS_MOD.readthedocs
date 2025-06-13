GENeSYS-MOD Weather Timeseries Tool
===================================

The timeseries script  can be used to create the capacity factors for solar PV, Wind (Onshore and Offshore) and Heatpumps, as well as residential heating and cooling demand. It uses functions from `atlite <https://atlite.readthedocs.io/en/master/index.html>` and the `ERA5 weather dataset <https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview>`, which is downloaded and transformed locally. This section provides a step by step guide on how to use the script and change settings to fit a specific case study:

Requirements
-------------

**Python**: If you don’t have Python installed on your system already you can download it here: https://www.python.org/downloads/

**Jupyter Notebook**: You will need a Jupyter Notebook to run the script. You can install it in one of the following ways:
Directly install Jupyter Notebook by following the instructions here: https://jupyter.org/instal
Alternatively, you can install Jupyter via Anaconda, which provides a bundled environment manager and Jupyter Notebook setup:  https://www.anaconda.com/download

**Packages**: To use this script, you will also need to have the following packages installed:

- numpy
- matplotlib
- seaborn
- pandas
- geopandas (version v. 0.14.4 or older)
- scikit-learn
- cartopy
- xarray
- atlite

You can install all the necessary packages with the following commands:

pip install numpy matplotlib seaborn pandas scikit-learn cartopy xarray atlite

pip install geopandas==0.14.4

**API key**
In addition, in order to be able to load the ERA5 cutouts, you need an API key. To activate the API key, follow the instructions at 
https://cds.climate.copernicus.eu/how-to-api 

Set Up 
-------
The Timeseries script, along with all necessary data files and functions, can be found here:
https://github.com/GENeSYS-MOD/GENeSYS_MOD.tools/tree/main/GIS_%26_Timeseries_Tool

You can either clone the repository or download the files directly to your computer. Be sure to note the location where you save the files.
Once the files are on your system, open the file GENeSYS-MOD_RES_Tool.ipynb using Jupyter Notebook.

Change Settings
----------------
Within the file some lines need to be changed to fit your specific location:

Cell 2:


Adjust the time frame according to your case study requirement and choose a filename.Set admin= 0 if you want the data on a national level and admin = 1 for a sub-national level (regions, states, provinces). For regions, write the ISO 3166-1 alpha-2 code of your desired country (list can be found here: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). 

Cell 3:

You can adjust the tilt (pv_slope) and orientation (pv_azimuth) of the solar panel. The optimal tilt angle for your location can be calculated here: https://footprinthero.com/solar-panel-tilt-angle-calculator 
For the azimuth it is common to use 180° for the northern hemisphere (panel facing south) and 0° for the southern hemisphere (panel facing north).

Cell 4:


If needed adjust the spatial resolution of the cutout.

Alternative: Define cutout with coordinates
The steps above define a cutout based on national borders for your selected region. If you want to cover a different area—for example, to include offshore regions for analyzing wind capacity—you can specify the area using geographic coordinates.

In Cell 2, enter two coordinates representing the northwest and southeast corners of your desired rectangular cutout.

Then, in Cell 3, when defining your cutout, include these coordinates as parameters and remove the regions parameter by commenting it out.   

Run Code and Use Output
-------------------------
After adjusting the settings, run the Jupyter Notebook cell by cell from top to bottom.
.. Note:: 
    Downloading the weather data from Atlite can take a significant amount of time, depending on the size of the region and the timeframe you have selected. It is recommended to use a device with ample system memory (at least 24GB of RAM) and ensure you have a stable internet connection and uninterrupted power supply to avoid issues during the download and processing.

Once the data processing is complete, you will see time series CSV files in your output folder. Open these files and copy the columns into your desired hourly data file for further use.

Additionally, the script will display a map showing the area covered by the cutout and provide the means of all the generated factors, allowing you to check for plausibility.
