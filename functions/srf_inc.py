import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from level_org import Level_Org
#mport scipy as sp
#import matplotlib as plt


def inclination(surfaces):
    inc=[]

    for i,j in enumerate(surfaces):
        if type(j) == list:
            inc.append([])
            for k,l in enumerate(j):
                n=rs.SurfaceNormal(l,[0.5,0.5])
                va=rs.VectorAngle(n,rs.VectorCreate((0,0,0),(0,0,1)))
                inc[i].append(90-va)
        else:
            n=rs.SurfaceNormal(i,[0.5,0.5])
            va=rs.VectorAngle(n,rs.VectorCreate((0,0,0),(0,0,1)))
            inc.append(90-va)

    return (inc)

# if __name__=='__main__':
#     inclination()


#srf=rs.ObjectsByType(8)
#surface=Level_Org()[1]
inclinations=inclination(Level_Org()[1])

print (inclinations)
#text dots
for i in Level_Org()[0]:
    for j,k in enumerate(i):
        rs.AddTextDot(str(j),k)