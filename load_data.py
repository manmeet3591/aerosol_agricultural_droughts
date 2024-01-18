import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
from datetime import datetime, timedelta
import cartopy.crs as ccrs
from matplotlib.axes import Axes
from cartopy.mpl.geoaxes import GeoAxes
import cartopy.io.shapereader as shpreader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
# GeoAxes._pcolormesh_patched = Axes.pcolormesh
# fname = '/lus/dal/cccr_rnd/manmeet/iccp/data/INDIA.shp'
# adm1_shapes = list(shpreader.Reader(fname).geometries())

############################################################
###############piClim-control###############################

#pr
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-control/pr/'

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-control_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_control_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_control_IPSL_CM6A_LR_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-control_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r2i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-control_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r3i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-control_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r4i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-control_r5i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r5i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR-INCA_piClim-control_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_control_IPSL_CM6A_LR_INCA_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-control_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-control_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r11i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-MM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_MM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-control_r1i1p2f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p2f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-control_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-control_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f2_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-control_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_control_GISS_E2_r1i1p3f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_UKESM1-0-LL_piClim-control_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_control_UKESM_r1i1p1f4_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MPI-ESM-1-2-HAM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_MPIESM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_CNRM-ESM2-1_piClim-control_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_control_CNRMESM_r1i1p1f2_pr = xr.open_dataset(file_)
#mrsos
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-control/mrsos/'

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-control_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_control_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_control_IPSL_CM6A_LR_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-control_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r2i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-control_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r3i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-control_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r4i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-control_r5i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r5i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR-INCA_piClim-control_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_control_IPSL_CM6A_LR_INCA_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-control_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-control_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r11i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-MM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_MM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-control_r1i1p2f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p2f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-control_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-control_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f2_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-control_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_control_GISS_E2_r1i1p3f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_UKESM1-0-LL_piClim-control_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_control_UKESM_r1i1p1f4_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MPI-ESM-1-2-HAM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_MPIESM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_CNRM-ESM2-1_piClim-control_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_control_CNRMESM_r1i1p1f2_mrsos = xr.open_dataset(file_)
#hfls
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-control/hfls/'

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-control_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_control_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_control_IPSL_CM6A_LR_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-control_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r2i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-control_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r3i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-control_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r4i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-control_r5i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r5i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR-INCA_piClim-control_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_control_IPSL_CM6A_LR_INCA_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-control_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-control_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r11i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-MM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_MM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-control_r1i1p2f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p2f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-control_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-control_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f2_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-control_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_control_GISS_E2_r1i1p3f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_UKESM1-0-LL_piClim-control_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_control_UKESM_r1i1p1f4_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MPI-ESM-1-2-HAM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_MPIESM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_CNRM-ESM2-1_piClim-control_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_control_CNRMESM_r1i1p1f2_hfls = xr.open_dataset(file_)

#hfss
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-control/hfss/'

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-control_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_control_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_control_IPSL_CM6A_LR_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-control_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r2i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-control_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r3i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-control_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r4i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-control_r5i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r5i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR-INCA_piClim-control_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_control_IPSL_CM6A_LR_INCA_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-control_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-control_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r11i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-MM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_MM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-control_r1i1p2f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p2f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-control_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-control_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_control_GISS_E2_r1i1p1f2_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-control_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_control_GISS_E2_r1i1p3f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_UKESM1-0-LL_piClim-control_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_control_UKESM_r1i1p1f4_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MPI-ESM-1-2-HAM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_MPIESM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_CNRM-ESM2-1_piClim-control_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_control_CNRMESM_r1i1p1f2_hfss = xr.open_dataset(file_)
#od550aer
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-control/od550aer/'

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-control_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_control_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_control_IPSL_CM6A_LR_r1i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-control_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r2i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-control_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r3i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-control_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r4i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-control_r5i1p1f1_gr_201401-204312.nc'
ds_piClim_control_IPSL_CM6A_LR_r5i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR-INCA_piClim-control_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_control_IPSL_CM6A_LR_INCA_r1i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-control_r1i1p1f1_gn_185001-187912.nc'
#ds_piClim_control_MIROC6_r1i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-control_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_control_MIROC6_r11i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_NorESM2-MM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_NorESM2_MM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-control_r1i1p2f1_gn_*.nc'
ds_piClim_control_NorESM2_LM_r1i1p2f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

# file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-control_r1i1p1f1_gn_195001-198012.nc'
# ds_piClim_control_GISS_E2_r1i1p1f1_od550aer = xr.open_dataset(file_)

# file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-control_r1i1p1f2_gn_195001-198012.nc'
# ds_piClim_control_GISS_E2_r1i1p1f2_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-control_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_control_GISS_E2_r1i1p3f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_UKESM1-0-LL_piClim-control_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_control_UKESM_r1i1p1f4_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MPI-ESM-1-2-HAM_piClim-control_r1i1p1f1_gn_*.nc'
ds_piClim_control_MPIESM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

# one ensemble of MIROC and two of GISS missing, so we can use the AOD from one only
# or another option would be to limit the other variables as well to the realizations available for od550aer

file_ = data_dir+'od550aer_AERmon_CNRM-ESM2-1_piClim-control_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_control_CNRMESM_r1i1p1f2_od550aer = xr.open_dataset(file_)

############################################################
###############piClim-aer###############################

#pr
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-aer/pr/'

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-aer_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_aer_IPSL_CM6A_LR_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-aer_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r2i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-aer_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r3i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-aer_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r4i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-aer_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL_CM6A_LR_r5i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR-INCA_piClim-aer_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_aer_IPSL_CM6A_LR_INCA_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-aer_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-aer_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r11i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-MM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_MM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-aer_r1i1p2f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p2f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f2_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-aer_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_aer_GISS_E2_r1i1p3f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_UKESM1-0-LL_piClim-aer_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_aer_UKESM_r1i1p1f4_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MPI-ESM-1-2-HAM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_MPIESM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_CNRM-ESM2-1_piClim-aer_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_aer_CNRMESM_r1i1p1f2_pr = xr.open_dataset(file_)

#mrsos
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-aer/mrsos/'

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-aer_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_aer_IPSL_CM6A_LR_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-aer_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r2i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-aer_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r3i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-aer_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r4i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-aer_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL_CM6A_LR_r5i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR-INCA_piClim-aer_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_aer_IPSL_CM6A_LR_INCA_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-aer_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-aer_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r11i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-MM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_MM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-aer_r1i1p2f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p2f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-aer_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-aer_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f2_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-aer_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_aer_GISS_E2_r1i1p3f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_UKESM1-0-LL_piClim-aer_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_aer_UKESM_r1i1p1f4_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MPI-ESM-1-2-HAM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_MPIESM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_CNRM-ESM2-1_piClim-aer_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_aer_CNRMESM_r1i1p1f2_mrsos = xr.open_dataset(file_)

#hfls
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-aer/hfls/'

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-aer_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_aer_IPSL_CM6A_LR_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-aer_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r2i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-aer_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r3i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-aer_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r4i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-aer_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL_CM6A_LR_r5i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR-INCA_piClim-aer_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_aer_IPSL_CM6A_LR_INCA_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-aer_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-aer_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r11i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-MM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_MM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-aer_r1i1p2f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p2f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f2_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-aer_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_aer_GISS_E2_r1i1p3f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_UKESM1-0-LL_piClim-aer_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_aer_UKESM_r1i1p1f4_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MPI-ESM-1-2-HAM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_MPIESM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_CNRM-ESM2-1_piClim-aer_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_aer_CNRMESM_r1i1p1f2_hfls = xr.open_dataset(file_)

#hfss
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-aer/hfss/'

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-aer_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_aer_IPSL_CM6A_LR_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-aer_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r2i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-aer_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r3i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-aer_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r4i1p1f1_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-aer_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL_CM6A_LR_r5i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR-INCA_piClim-aer_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_aer_IPSL_CM6A_LR_INCA_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-aer_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-aer_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r11i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-MM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_NorESM2_MM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-aer_r1i1p2f1_gn_*.nc'
ds_piClim_aer_NorESM2_LM_r1i1p2f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f1_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-aer_r1i1p1f2_gn_195001-198012.nc'
ds_piClim_aer_GISS_E2_r1i1p1f2_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-aer_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_aer_GISS_E2_r1i1p3f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_UKESM1-0-LL_piClim-aer_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_aer_UKESM_r1i1p1f4_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MPI-ESM-1-2-HAM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_MPIESM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_CNRM-ESM2-1_piClim-aer_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_aer_CNRMESM_r1i1p1f2_hfss = xr.open_dataset(file_)

#od550aer
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-aer/od550aer/'

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-aer_r1i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
ds_piClim_aer_IPSL_CM6A_LR_r1i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-aer_r2i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r2i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-aer_r3i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r3i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-aer_r4i1p1f1_gr_201401-204312.nc'
ds_piClim_aer_IPSL_CM6A_LR_r4i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-aer_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_aer_IPSL_CM6A_LR_r5i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR-INCA_piClim-aer_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_aer_IPSL_CM6A_LR_INCA_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-aer_r1i1p1f1_gn_185001-187912.nc'
#ds_piClim_aer_MIROC6_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-aer_r11i1p1f1_gn_185001-187912.nc'
ds_piClim_aer_MIROC6_r11i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-aer_r1i1p1f1_gn_*.nc'
#ds_piClim_aer_NorESM2_LM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')
#
#file_ = data_dir+'od550aer_AERmon_NorESM2-MM_piClim-aer_r1i1p1f1_gn_*.nc'
#ds_piClim_aer_NorESM2_MM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')
#
#file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-aer_r1i1p2f1_gn_*.nc'
#ds_piClim_aer_NorESM2_LM_r1i1p2f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-aer_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_aer_GISS_E2_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-aer_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_aer_GISS_E2_r1i1p1f2_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-aer_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_aer_GISS_E2_r1i1p3f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_UKESM1-0-LL_piClim-aer_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_aer_UKESM_r1i1p1f4_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MPI-ESM-1-2-HAM_piClim-aer_r1i1p1f1_gn_*.nc'
ds_piClim_aer_MPIESM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_CNRM-ESM2-1_piClim-aer_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_aer_CNRMESM_r1i1p1f2_od550aer = xr.open_dataset(file_)

############################################################
###############piClim-2xdust###############################

#pr
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-2xdust/pr/'

#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-2xdust_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_2xdust_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_2xdust_IPSL_CM6A_LR_r1i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-2xdust_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r2i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-2xdust_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r3i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-2xdust_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r4i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-2xdust_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r5i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_IPSL-CM6A-LR-INCA_piClim-2xdust_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_2xdust_IPSL_CM6A_LR_INCA_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-2xdust_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_2xdust_MIROC6_r1i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_MIROC6_piClim-2xdust_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_2xdust_MIROC6_r11i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

##file_ = data_dir+'pr_Amon_NorESM2-MM_piClim-2xdust_r1i1p1f1_gn_*.nc'
##ds_piClim_2xdust_NorESM2_MM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-2xdust_r1i1p2f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p2f1_pr = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f2_pr = xr.open_dataset(file_)
#
file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_2xdust_GISS_E2_r1i1p3f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_UKESM1-0-LL_piClim-2xdust_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_2xdust_UKESM_r1i1p1f4_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MPI-ESM-1-2-HAM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_MPIESM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_CNRM-ESM2-1_piClim-2xdust_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_2xdust_CNRMESM_r1i1p1f2_pr = xr.open_dataset(file_)

#mrsos
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-2xdust/mrsos/'

#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-2xdust_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_2xdust_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_2xdust_IPSL_CM6A_LR_r1i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-2xdust_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r2i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-2xdust_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r3i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-2xdust_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r4i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-2xdust_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r5i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR-INCA_piClim-2xdust_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_2xdust_IPSL_CM6A_LR_INCA_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-2xdust_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_2xdust_MIROC6_r1i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-2xdust_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_2xdust_MIROC6_r11i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'mrsos_Lmon_NorESM2-MM_piClim-2xdust_r1i1p1f1_gn_*.nc'
#ds_piClim_2xdust_NorESM2_MM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-2xdust_r1i1p2f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p2f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-2xdust_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-2xdust_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f2_mrsos = xr.open_dataset(file_)
#
file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-2xdust_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_2xdust_GISS_E2_r1i1p3f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_UKESM1-0-LL_piClim-2xdust_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_2xdust_UKESM_r1i1p1f4_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MPI-ESM-1-2-HAM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_MPIESM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_CNRM-ESM2-1_piClim-2xdust_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_2xdust_CNRMESM_r1i1p1f2_mrsos = xr.open_dataset(file_)

#hfls
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-2xdust/hfls/'

#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-2xdust_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_2xdust_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_2xdust_IPSL_CM6A_LR_r1i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-2xdust_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r2i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-2xdust_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r3i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-2xdust_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r4i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-2xdust_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r5i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR-INCA_piClim-2xdust_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_2xdust_IPSL_CM6A_LR_INCA_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-2xdust_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_2xdust_MIROC6_r1i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_MIROC6_piClim-2xdust_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_2xdust_MIROC6_r11i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfls_Amon_NorESM2-MM_piClim-2xdust_r1i1p1f1_gn_*.nc'
#ds_piClim_2xdust_NorESM2_MM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-2xdust_r1i1p2f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p2f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f2_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_2xdust_GISS_E2_r1i1p3f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_UKESM1-0-LL_piClim-2xdust_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_2xdust_UKESM_r1i1p1f4_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MPI-ESM-1-2-HAM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_MPIESM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_CNRM-ESM2-1_piClim-2xdust_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_2xdust_CNRMESM_r1i1p1f2_hfls = xr.open_dataset(file_)

#hfss
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-2xdust/hfss/'

#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-2xdust_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_2xdust_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_2xdust_IPSL_CM6A_LR_r1i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-2xdust_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r2i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-2xdust_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r3i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-2xdust_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r4i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-2xdust_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r5i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR-INCA_piClim-2xdust_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_2xdust_IPSL_CM6A_LR_INCA_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-2xdust_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_2xdust_MIROC6_r1i1p1f1_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_MIROC6_piClim-2xdust_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_2xdust_MIROC6_r11i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfss_Amon_NorESM2-MM_piClim-2xdust_r1i1p1f1_gn_*.nc'
#ds_piClim_2xdust_NorESM2_MM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-2xdust_r1i1p2f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p2f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f2_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-2xdust_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_2xdust_GISS_E2_r1i1p3f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_UKESM1-0-LL_piClim-2xdust_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_2xdust_UKESM_r1i1p1f4_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MPI-ESM-1-2-HAM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_MPIESM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_CNRM-ESM2-1_piClim-2xdust_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_2xdust_CNRMESM_r1i1p1f2_hfss = xr.open_dataset(file_)

#od550aer
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-2xdust/od550aer/'

#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-2xdust_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_2xdust_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_2xdust_IPSL_CM6A_LR_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-2xdust_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r2i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-2xdust_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r3i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-2xdust_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r4i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-2xdust_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_2xdust_IPSL_CM6A_LR_r5i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR-INCA_piClim-2xdust_r1i1p1f1_gr_185001-187912.nc'
ds_piClim_2xdust_IPSL_CM6A_LR_INCA_r1i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-2xdust_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_2xdust_MIROC6_r1i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-2xdust_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_2xdust_MIROC6_r11i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'od550aer_AERmon_NorESM2-MM_piClim-2xdust_r1i1p1f1_gn_*.nc'
#ds_piClim_2xdust_NorESM2_MM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-2xdust_r1i1p2f1_gn_*.nc'
ds_piClim_2xdust_NorESM2_LM_r1i1p2f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-2xdust_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-2xdust_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_2xdust_GISS_E2_r1i1p1f2_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-2xdust_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_2xdust_GISS_E2_r1i1p3f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_UKESM1-0-LL_piClim-2xdust_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_2xdust_UKESM_r1i1p1f4_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MPI-ESM-1-2-HAM_piClim-2xdust_r1i1p1f1_gn_*.nc'
ds_piClim_2xdust_MPIESM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_CNRM-ESM2-1_piClim-2xdust_r1i1p1f2_gr_185001-187912.nc'
ds_piClim_2xdust_CNRMESM_r1i1p1f2_od550aer = xr.open_dataset(file_)

############################################################
###############piClim-NTCF###############################

#pr
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-NTCF/pr/'

#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-NTCF_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_NTCF_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_NTCF_IPSL_CM6A_LR_r1i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-NTCF_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r2i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-NTCF_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r3i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-NTCF_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r4i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR_piClim-NTCF_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r5i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_IPSL-CM6A-LR-INCA_piClim-NTCF_r1i1p1f1_gr_185001-187912.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_INCA_r1i1p1f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_MIROC6_piClim-NTCF_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_NTCF_MIROC6_r1i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_MIROC6_piClim-NTCF_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_NTCF_MIROC6_r11i1p1f1_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_LM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'pr_Amon_NorESM2-MM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_MM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'pr_Amon_NorESM2-LM_piClim-NTCF_r1i1p2f1_gn_*.nc'
ds_piClim_NTCF_NorESM2_LM_r1i1p2f1_pr = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f1_pr = xr.open_dataset(file_)
#
#file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f2_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_NTCF_GISS_E2_r1i1p3f1_pr = xr.open_dataset(file_)

file_ = data_dir+'pr_Amon_UKESM1-0-LL_piClim-NTCF_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_NTCF_UKESM_r1i1p1f4_pr = xr.open_dataset(file_)

#file_ = data_dir+'pr_Amon_MPI-ESM-1-2-HAM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_MPIESM_r1i1p1f1_pr = xr.open_mfdataset(file_, combine='by_coords')

#mrsos
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-NTCF/mrsos/'

#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-NTCF_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_NTCF_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_NTCF_IPSL_CM6A_LR_r1i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-NTCF_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r2i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-NTCF_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r3i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-NTCF_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r4i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR_piClim-NTCF_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r5i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_IPSL-CM6A-LR-INCA_piClim-NTCF_r1i1p1f1_gr_185001-187912.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_INCA_r1i1p1f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-NTCF_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_NTCF_MIROC6_r1i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_MIROC6_piClim-NTCF_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_NTCF_MIROC6_r11i1p1f1_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_LM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'mrsos_Lmon_NorESM2-MM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_MM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'mrsos_Lmon_NorESM2-LM_piClim-NTCF_r1i1p2f1_gn_*.nc'
ds_piClim_NTCF_NorESM2_LM_r1i1p2f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-NTCF_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f1_mrsos = xr.open_dataset(file_)
#
#file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-NTCF_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f2_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_GISS-E2-1-G_piClim-NTCF_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_NTCF_GISS_E2_r1i1p3f1_mrsos = xr.open_dataset(file_)

file_ = data_dir+'mrsos_Lmon_UKESM1-0-LL_piClim-NTCF_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_NTCF_UKESM_r1i1p1f4_mrsos = xr.open_dataset(file_)

#file_ = data_dir+'mrsos_Lmon_MPI-ESM-1-2-HAM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_MPIESM_r1i1p1f1_mrsos = xr.open_mfdataset(file_, combine='by_coords')

#hfls
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-NTCF/hfls/'

#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-NTCF_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_NTCF_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_NTCF_IPSL_CM6A_LR_r1i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-NTCF_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r2i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-NTCF_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r3i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-NTCF_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r4i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR_piClim-NTCF_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r5i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_IPSL-CM6A-LR-INCA_piClim-NTCF_r1i1p1f1_gr_185001-187912.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_INCA_r1i1p1f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_MIROC6_piClim-NTCF_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_NTCF_MIROC6_r1i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_MIROC6_piClim-NTCF_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_NTCF_MIROC6_r11i1p1f1_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_LM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfls_Amon_NorESM2-MM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_MM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfls_Amon_NorESM2-LM_piClim-NTCF_r1i1p2f1_gn_*.nc'
ds_piClim_NTCF_NorESM2_LM_r1i1p2f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f1_hfls = xr.open_dataset(file_)
#
#file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f2_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_NTCF_GISS_E2_r1i1p3f1_hfls = xr.open_dataset(file_)

file_ = data_dir+'hfls_Amon_UKESM1-0-LL_piClim-NTCF_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_NTCF_UKESM_r1i1p1f4_hfls = xr.open_dataset(file_)

#file_ = data_dir+'hfls_Amon_MPI-ESM-1-2-HAM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_MPIESM_r1i1p1f1_hfls = xr.open_mfdataset(file_, combine='by_coords')

#hfss
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-NTCF/hfss/'

#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-NTCF_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_NTCF_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_NTCF_IPSL_CM6A_LR_r1i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-NTCF_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r2i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-NTCF_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r3i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-NTCF_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r4i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR_piClim-NTCF_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r5i1p1f1_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_IPSL-CM6A-LR-INCA_piClim-NTCF_r1i1p1f1_gr_185001-187912.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_INCA_r1i1p1f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_MIROC6_piClim-NTCF_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_NTCF_MIROC6_r1i1p1f1_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_MIROC6_piClim-NTCF_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_NTCF_MIROC6_r11i1p1f1_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_LM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfss_Amon_NorESM2-MM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_MM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'hfss_Amon_NorESM2-LM_piClim-NTCF_r1i1p2f1_gn_*.nc'
ds_piClim_NTCF_NorESM2_LM_r1i1p2f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f1_hfss = xr.open_dataset(file_)
#
#file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f2_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_GISS-E2-1-G_piClim-NTCF_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_NTCF_GISS_E2_r1i1p3f1_hfss = xr.open_dataset(file_)

file_ = data_dir+'hfss_Amon_UKESM1-0-LL_piClim-NTCF_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_NTCF_UKESM_r1i1p1f4_hfss = xr.open_dataset(file_)

#file_ = data_dir+'hfss_Amon_MPI-ESM-1-2-HAM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_MPIESM_r1i1p1f1_hfss = xr.open_mfdataset(file_, combine='by_coords')

#od550aer
data_dir = '/lus/dal/cccr_rnd/manmeet/AI_IITM/WeatherBench/data/dataserv.ub.tum.de/AerChemMIP/piClim-NTCF/od550aer/'

#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-NTCF_r1i1p1f1_gr_201401-204312.nc'
##ds_piClim_NTCF_IPSL-CM6A-LR_r1i1p1f1 = xr.open_mfdataset(data_dir+, combine='by_coords')
#ds_piClim_NTCF_IPSL_CM6A_LR_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-NTCF_r2i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r2i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-NTCF_r3i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r3i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-NTCF_r4i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r4i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR_piClim-NTCF_r5i1p1f1_gr_201401-204312.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_r5i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_IPSL-CM6A-LR-INCA_piClim-NTCF_r1i1p1f1_gr_185001-187912.nc'
#ds_piClim_NTCF_IPSL_CM6A_LR_INCA_r1i1p1f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-NTCF_r1i1p1f1_gn_185001-187912.nc'
ds_piClim_NTCF_MIROC6_r1i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_MIROC6_piClim-NTCF_r11i1p1f1_gn_185001-187912.nc'
#ds_piClim_NTCF_MIROC6_r11i1p1f1_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_LM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'od550aer_AERmon_NorESM2-MM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_NorESM2_MM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

file_ = data_dir+'od550aer_AERmon_NorESM2-LM_piClim-NTCF_r1i1p2f1_gn_*.nc'
ds_piClim_NTCF_NorESM2_LM_r1i1p2f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')

#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-NTCF_r1i1p1f1_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f1_od550aer = xr.open_dataset(file_)
#
#file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-NTCF_r1i1p1f2_gn_195001-198012.nc'
#ds_piClim_NTCF_GISS_E2_r1i1p1f2_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_GISS-E2-1-G_piClim-NTCF_r1i1p3f1_gn_195001-199012.nc'
ds_piClim_NTCF_GISS_E2_r1i1p3f1_od550aer = xr.open_dataset(file_)

file_ = data_dir+'od550aer_AERmon_UKESM1-0-LL_piClim-NTCF_r1i1p1f4_gn_185001-189412.nc'
ds_piClim_NTCF_UKESM_r1i1p1f4_od550aer = xr.open_dataset(file_)

#file_ = data_dir+'od550aer_AERmon_MPI-ESM-1-2-HAM_piClim-NTCF_r1i1p1f1_gn_*.nc'
#ds_piClim_NTCF_MPIESM_r1i1p1f1_od550aer = xr.open_mfdataset(file_, combine='by_coords')


