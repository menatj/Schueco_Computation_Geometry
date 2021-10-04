import rhinoscriptsyntax as rs
import Rhino as rg
from level_org import Level_Org
from sort_srf_vrt import SortSrfVrt
import sys
import csv
import json


# f=open('coords.csv','w')
# writer = csv.writer(f)




# panels = Level_Org()[1]
# csv=[]
# for i,j in enumerate(panels):
#     #print ("Level"+" "+str(i))
#     for k,l in enumerate(j):
#         #print ("panel"+" "+str(k))

#         points=SortSrfVrt(l,1)
    
#         csv.append(points)


# x='x'
# y='y'
# z='z'
# csv.insert(0,[x+y+z])

# print len(csv)
# for i in csv:
#     writer.writerows(i)
# f.close()
#j=open('panels.json','w')
panels = Level_Org()[1]
midpoints=Level_Org()[0]
csv=[]
points_dic={}


for i,j in enumerate(panels):
    points_dic["L_{}".format(i)]={}
    for k,l in enumerate(j):
        serialpts=[]
        for index, p in enumerate(SortSrfVrt(l,1)):
            x=p.X
            y=p.Y
            z=p.Z
            serialpts.append((x,y,z))
        points_dic["L_{}".format(i)]["P_#{}".format(k)]=serialpts
        
print type(points_dic)

with open('panels.json','w') as outfile:
    json.dump(points_dic,outfile)        

midpoints_dic={}
for i,j in enumerate(midpoints):
    midpoints_dic["L_{}".format(i)]={}
    for k,l in enumerate(j):
        x=l.X
        y=l.Y
        z=l.Z
    
        midpoints_dic["L_{}".format(i)]["P_#{}".format(k)]=[x,y,z]
        


with open('midpoints.json','w') as outfile:
    json.dump(midpoints_dic,outfile)      