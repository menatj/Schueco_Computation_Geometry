import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from level_org import Level_Org
from sort_srf_vrt import SortSrfVrt
import rh_toolbox as rt
import py_toolbox as pt



panels=Level_Org()[1]

for i,j in enumerate(panels):
    print ("Level"+" "+str(i))
    for k,l in enumerate(j):
        print ("panel"+" "+str(k))

        points=SortSrfVrt(l,1)

        vectorpA=points
        vectorpB=pt.listrotate(points,1)


        #print vectorpB
        # for h,i in enumerate(vectorpA):
        #         rs.AddTextDot(str(h),(i))
        vectors=[]

        for i,j in enumerate(vectorpA):
            vectors.append(rs.VectorCreate(j,vectorpB[i]))

        vectorRot=pt.listrotate(vectors,-1)

        for i,j in enumerate(vectors):
            ang=rs.VectorAngle(j,rs.VectorReverse(vectorRot[i]))
            rs.AddTextDot(str(ang),points[i])
            print ang

