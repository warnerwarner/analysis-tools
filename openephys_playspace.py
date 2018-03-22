from Python3 import OpenEphys
import time
import pandas as pd
import sys

start = time.time()

data = OpenEphys.loadFolder("D:\\Open_ephys_testing_ground_data")
print(sys.getsizeof(data))
#f = open('D:\\Open_ephys_testing_ground_data\\100_ADC2.continuous', 'rb')
