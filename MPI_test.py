from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print('hello world', rank, comm.Get_size())
'''
if rank ==0:
	data = np.arrange(1000, dtype='i')
	comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank==1:
	data = np.empty(1000, dtype=1)
	comm.Recv([data, MPI.INT], source=0, tag=77)

if rank==0:
	data = np.arrange(100, dtype=np.float64)
	comm.Send(data, dest=1, tag=13)
elif rank==1:
	data = np.empty(100, dtype=np.float64)
	comm.Recv(data, source=0, tag=13)
'''