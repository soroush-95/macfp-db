#!ng/Anaconda3/2021.05/usr/bin/env python3
# DBI_twi_kal_bph
# Feb 2021
# first, make sure the macfp module directory is in your path
# if not, uncomment the lines below and replace <path to macfp-db>
# with the path (absolute or relative) to your macfp-db repository
import sys
# sys.path.append('<path to macfp-db>/macfp-db/Utilities/')
sys.path.append('../../../../../../macfp-db/Utilities/')
import macfp
import importlib
importlib.reload(macfp) # use for development (while making changes to macfp.py)
import matplotlib.pyplot as plt
macfp.dataplot(config_filename='DBI_NIST_Pool_Fires_cmp_config.csv',
               institute='DBI',
               revision='MaCFP-3, Tsukuba, 2023',
               expdir='../../../Experimental_Data/',
               cmpdir='./Output/',
               pltdir='./Plots/',
               close_figs=True,
               verbose=True,
               plot_list=['all'])
# plt.show()
