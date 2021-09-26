import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from level_org import Level_Org
import rh_toolbox as rt
import py_toolbox as pt



def SortSrfVrt(surface,rev=0):
    
    obj=rs.coercesurface(surface) 
    # From trimmed to untrimmed
    dpob=rg.BrepFace.DuplicateFace(obj,0)
    wires= rg.Brep.GetWireframe(dpob,0)
    edges=[]
    srfpts=[]
    vctrs= []

    for h,i in enumerate(dpob.Vertices):
        srfpts.append(i.Location)

    shifted=pt.listrotate(srfpts)
    
    edgpoints=[(rs.CurveMidPoint(i)) for i in wires] 
    
    param=rt.srf_edge_param_ord(obj,srfpts,edgpoints)

    sortedpoints=pt.sorting(param,srfpts,rev)[0]
    sortedkeys=pt.sorting(param,srfpts,rev)[1]

    #print sortedkeys

    return (sortedpoints)



# if __name__ == '__main__': 
#     SortSrfEdges(surface)


panels=Level_Org()[1]

for i,j in enumerate(panels):
    print ("Level"+" "+str(i))
    for k,l in enumerate(j):
        print ("panel"+" "+str(k))
        #print rs.coercesurface(l)

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

