import arcpy
from arcpy import env
env.workspace=r"C:\Users\afars083\Downloads\Module8_data\Module8_data\OTTAWA.gdb\ottawadata"
fclist=arcpy.ListFeatureClasses()

import jj
for fc in fclist:
    print(jj.get_nomber(fc))