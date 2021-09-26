
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import py_toolbox as pt


def srf_edge_param_ord(srf,Vpoints,Epoints,cRad=200):
    rs.EnableRedraw(0)
    param=[]
    obj=srf
    cnt=rs.SurfaceAreaCentroid(obj)
    sclp=rs.SurfaceClosestPoint(obj,cnt[0])
    uv=rs.EvaluateSurface(obj,sclp[0],sclp[1])
    plz=rs.SurfaceNormal(obj,uv)
    plane=rs.PlaneFromNormal(cnt[0],plz)
    circ=rs.AddCircle(plane,cRad)

    
    lowerpoint=[rs.coerce3dpoint(i).Z for i in Epoints]
    lowerpoint=pt.sorting(lowerpoint,Epoints)
    
    crvstart=lowerpoint[0][0]
    rs.CurveSeam(circ,rs.CurveClosestPoint(circ,crvstart))
    #rs.AddPoint(rs.CurveStartPoint(circ))
    for i,j in enumerate(Vpoints):
        param.append(rs.CurveClosestPoint(circ, j))
    rs.DeleteObject(circ)
    rs.EnableRedraw(1)
    
    return param
    

