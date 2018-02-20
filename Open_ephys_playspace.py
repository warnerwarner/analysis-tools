
import sys
import pandas
sys.path.append('../analysis_tools/Python3')
import OpenEphys



data = OpenEphys.loadFolder("/Users/warnert/OneDrive - The Francis Crick Institute/Year1/Modeling/My stuff/data")

df = pandas.DataFrame(data)

print(df.memory_usage(index=True, deep=True).sum())

