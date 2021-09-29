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



if __name__ == '__main__': 
    SortSrfVrt(surface,rev=0)


