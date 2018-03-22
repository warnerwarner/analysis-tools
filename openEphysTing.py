from Python3 import OpenEphys
import time

start = time.time()


data = OpenEphys.load("D:\\Open_ephys_testing_ground_data\\100_ADC1.continuous")

end = time.time()

print(end-start)

print(data['reco'])
