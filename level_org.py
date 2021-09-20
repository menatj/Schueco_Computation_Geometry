import rhinoscriptsyntax as rs
import Rhino.Geometry as rg


def Level_Org():

    # select all surfaces

    srf=rs.ObjectsByType(8)

    # Create bounding boxes for each surface
    # +
    # Calculating bounding boxes centroid

    cnt=[]
    for s in srf:
        if  rs.IsVisibleInView(s) and rs.ObjectType(s) == 8:
            #rint rs.ObjectType(s)
         #and rs.ObjectType(s) == 8:
            c=(rs.BoundingBox(s))
            cnt.append((rg.BoundingBox(c)).Center)
    
    # Creating set of levels

    set_=[]
    
    for i in cnt:
        z=round((i[2])/100)
        
        if (z) not in set_:
            set_.append(z)

        # Organizing Surfaces per level

    srfL=[]
    cntL=[]
    for i,j in enumerate(sorted(set_)):
        srfL.append([])
        cntL.append([])
        for k,l in enumerate(cnt):
            if j == round((l[2])/100):
                srfL[i].append(srf[k])
                cntL[i].append(l)

  
    # Sorting surfaces with curve

    bboxsL=[]
    intLines=[]
    polyLM=[]
    midpts=[]
    midpts_0=[]
    midpts_srt=[]
    srfL_0=[]


    for i in srfL:
        # Create bounding box per level

        b=rs.BoundingBox(i)

            # Get the lower points

        blp=b[:4]
            # Get bounding box centroid

        bboxcenter= rg.BoundingBox(b).Center

            # Create surface from bbo lower points 

        poly=(rs.AddPolyline(blp))
        line=rs.AddLine(blp[-1],blp[0])
        clspoly=rs.JoinCurves([poly,line],True)
        plSrf=rs.AddPlanarSrf(clspoly)
        
            # create vector from centroid

        vect=rs.VectorCreate((bboxcenter),rs.SurfaceAreaCentroid(plSrf)[0])

            # move surface with vector

        bboxsL.append(rs.MoveObject(plSrf,vect))
        #rs.sc
        clspoly=rs.MoveObject(clspoly,vect)
        polyLM.append(clspoly)
        
            # intersect Planar Surfaces with surfaces

        intLines.append([])

        for j,k in enumerate(i):
            
            intLines[srfL.index(i)].append(rs.IntersectBreps(bboxsL[srfL.index(i)],k)[0])
            a=intLines[srfL.index(i)][i.index(k)]

        rs.DeleteObject(plSrf)

            #Sort curves midpoints wuth poly line from bounding box
            
        dom=rg.Interval(0,1)
        c=rs.coercecurve(polyLM[srfL.index(i)])
        rg.Curve.Domain.SetValue(c,dom)
        midpts_0.append([])
        midpts.append([])

        for k,j in enumerate (intLines[srfL.index(i)]):
            #print j
            midpts_0[srfL.index(i)].append(rs.CurveMidPoint(j))


        # for k,j in enumerate(srfL[srfL.index(i)]):
        #     evpt=rs.SurfaceClosestPoint(j,midpts_0[srfL.index(i)][k])
        #     distpt=rs.EvaluateSurface(j,evpt[0],evpt[1])
        #     dist=round(rs.Distance(distpt,midpts_0[srfL.index(i)][k]))
        #     if  dist > 0:
        #         print rs.SelectObject(j)
                      

        for k,j in enumerate (intLines[srfL.index(i)]):
            midpts[srfL.index(i)].append(rs.CurveClosestPoint(c,rs.CurveMidPoint(j)))
            

        srfL_0.append([])
        midpts_srt.append([])

        for k,j in enumerate(sorted(midpts[srfL.index(i)])):
            if j in midpts[srfL.index(i)]:   
                srfL_0[srfL.index(i)].insert(k, srfL[srfL.index(i)][midpts[srfL.index(i)].index(j)])
                midpts_srt[srfL.index(i)].insert(k, midpts_0[srfL.index(i)][midpts[srfL.index(i)].index(j)])
    
    rs.DeleteObjects(rs.ObjectsByType(4))
    rs.DeleteObjects(rs.ObjectsByType(1))
    rs.DeleteObjects(rs.ObjectsByType(16))


    return (midpts_srt,srfL_0)


if __name__ == '__main__':
    Level_Org()



#print rs.Area(srfL[0][1]),rs.Area(srfL[0][0])
#'text dots
# for i in Level_Org()[0]:
#     for j,k in enumerate(i):
#         rs.AddTextDot(str(j),k)
#         #td=rg.TextDot(str(j),k)
#         #td.Display.DrawDot(k,str(j))
# print Level_Org()[0]  






