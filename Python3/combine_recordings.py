import sys
sys.path.append('/home/camp/warnert/analysis-tools/Python3')
import openephys as oe



folder_paths = ['/home/camp/warnert/working/Recordings/binary_pulses/200320/2020-03-20_15-19-47',
				'/home/camp/warnert/working/Recordings/binary_pulses/200320/2020-03-20_17-30-11']

oe.packMultiFolderFast(folder_paths)
