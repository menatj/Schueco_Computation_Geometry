import rhinoscriptsyntax as rs
import Rhino as rg
import csv
import sys
import re

f="C:\\Dropbox\\00_TOMAS\\00_PC\\01_Work\\00_Schueco\\CORONA CRISIS_HOME OFFICE\\Bangkok\\RE__36949_Gunkzl_HQ_Bangkok\\ReferencePoints.csv"
#def csv_points(path,file):
with open(f) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',',)
    for row in csv_reader:
        x=(re.findall(r"[-+]?\d*\.\d+|\d+",row[0]))
        y=(re.findall(r"[-+]?\d*\.\d+|\d+",row[1]))
        z=(re.findall(r"[-+]?\d*\.\d+|\d+",row[2]))
        print (x, y,z)
        rs.AddPoint(float(x[0]),float(y[0]),float(z[0]))