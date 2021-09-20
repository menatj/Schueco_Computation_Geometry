import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
from level_org import Level_Org
#mport scipy as sp
#import matplotlib as plt


def Int_Ang(surfaces):
    int_ang=[]
    for i,j in enumerate(surfaces):
        if type(j) == list:
            int_ang.append([])
            print ("Level"+" "+str(i))
            for k,l in enumerate(j):
                int_ang[i].append([])
                srf=rs.coercebrep(l)
                print ("panel" +" "+ str(k))
                for p,q in enumerate(srf.Vertices):
                    pt= (q.Location)
                    uv=rs.SurfaceClosestPoint(l,pt)
                    #int_ang[i][k].append(rs.SurfaceFrame(l,uv))
                    cir=rs.AddCircle(rs.SurfaceFrame(l,uv),100)
                    cir_srf=rs.AddPlanarSrf(cir)
                    int_curv=rs.IntersectBreps(cir_srf,l)
                    rs.DeleteObject(cir)
                    rs.DeleteObject(cir_srf)
                    #print int_curv
                    print int_curv
                    #print
    #             n=rs.SurfaceNormal(l,[0.5,0.5])
    #             rg.Surface.
    #             rs.AddCircle()
    #     else:
    #         n=rs.SurfaceNormal(i,[0.5,0.5])
    #         va=rs.VectorAngle(n,rs.VectorCreate((0,0,0),(0,0,1)))
    #         inc.append(90-va)

    return (int_ang)

# if __name__=='__main__':
#     inclination()

ang=Int_Ang(Level_Org()[1])
for i in Level_Org()[0]:
    for j,k in enumerate(i):
        rs.AddTextDot(str(j),k)
#print ang
