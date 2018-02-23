import pickle
import pandas
from time import time
import sys
from mpi4py import MPI
import numpy as np
import os
sys.path.append('./Python3')
import OpenEphys


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

folderpath = 'F:/OpenEphysRecordings/170803/Experiment1_2017-08-03_15-27-18'

files = os.listdir(folderpath)


num_files = 0
for i, f in enumerate(files):
	if '.continuous' in f:
		num_files += 1
print(num_files)
local_file_poses = []
st_val = np.floor(rank*num_files/size)


print(np.arange(1, 10))

if rank == size-1:
	last_val = num_files-1
else:
	last_val = np.floor((rank+1)*num_files/size)

print(rank, st_val, last_val)



#data = OpenEphys.loadFolder('D:/Open_ephys_testing_ground_data')

#df = pandas.DataFrame(data)

#df.to_hdf('./trialhdf', 'trial')

