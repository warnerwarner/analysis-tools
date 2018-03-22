import pickle
import sys
import pandas
import os
from mpi4py import MPI
sys.path.append('./Python3')
import OpenEphys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

folderpath = 'F:/OpenEphysRecordings/170803/Experiment1_2017-08-03_15-27-18'

filelist = os.listdir(folderpath)
data = {}
if rank==0:
	num_files = 0
	for i, f in enumerate(filelist):
		if '.continuous' in f:
			#data[f.replace('.continuous','')] = OpenEphys.loadContinuous(os.path.join(folderpath, f))
			num_files += 1
print(num_files)
#data = OpenEphys.load("F:/OpenEphysRecordings/170803/Experiment1_2017-08-03_15-27-18/100_ADC4.continuous")
local_n = num_files/size


print('Finished loaded')


#print(df.info(memory_usage='deep'))

