import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from level_org import Level_Org
from sort_srf_edges import SortSrfEdges

#mport scipy as sp
#import matplotlib as plt


def Int_Ang(surfaces):
    int_ang=[]
    for i,j in enumerate(surfaces):
        if type(j) == list:
            int_ang.append([])
            print ("Level"+" "+str(i))
            for k,l in enumerate(j):
                print ("Panel"+" "+ str(k))
                vectors=SortSrfEdges(l,1)[1]
                for i,j in enumerate(vectors):
                    shifted=vectors[i-1]
                    print ("angle"+ " "+ str(i) + " "+ str(rs.VectorAngle(j,shifted)))
                points=SortSrfEdges(l,1)[0]

                # for i, j in enumerate(points):
                #     rs.AddTextDot(str(i),j)

    return (int_ang)

rs.Angle()
# if __name__=='__main__':
#     inclination()
rs.SurfaceDomain
ang=Int_Ang(Level_Org()[1])
# for i in Level_Org()[0]:
#     for j,k in enumerate(i):
#         rs.AddTextDot(str(j),k)
#print ang
rs.alig