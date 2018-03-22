import pickle
import pandas
from time import time
import sys
from mpi4py import MPI
import numpy as np
import time
import os
sys.path.append('./Python3')
import OpenEphys


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

folderpath = 'F:/OpenEphysRecordings/170803/Experiment1_2017-08-03_15-27-18'
#folderpath = 'D:/Open_ephys_testing_ground_data'

files = os.listdir(folderpath)

continuous_files = {}
num_files = 0
for f in files:
	if '.continuous' in f:
		continuous_files[num_files] = f
		num_files += 1
local_file_poses = []
st_val = np.floor(rank*num_files/size)

print(continuous_files)


if rank == size-1:
	last_val = num_files
else:
	last_val = np.floor((rank+1)*num_files/size)

rank_vals = np.arange(st_val, last_val)
rank_vals = rank_vals.astype(int)


data = {}

for i in rank_vals:
	print('i', i)
	st = time.time()
	data[continuous_files[i].replace('.continuous', '')] = OpenEphys.load(folderpath + '/'+continuous_files[i])
	en = time.time()
	print(en-st)
	print('done')





#data = OpenEphys.loadFolder('D:/Open_ephys_testing_ground_data')

#df = pandas.DataFrame(data)

#df.to_hdf('./trialhdf', 'trial')

