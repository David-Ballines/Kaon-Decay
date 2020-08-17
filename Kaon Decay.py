import makedecay as md
import histogram as hb

#make and label all of the histograms
#histograms made using proffesor made histogram class
histo1=hb.histo("First Detector",150,-.9,.9)
histo1.hsetlabels("Pion X Value at Chamber 1","N")

histo2=hb.histo("Second Detector",150,-.9,.9)
histo2.hsetlabels("Pion X Value at Chamber ","N")

histo3=hb.histo("Third Detector Good Trigger",150,-.9,.9)
histo3.hsetlabels("Pion X Value at Calorimeter","N")

histo4=hb.histo("Kaon Decay Location, Z",150,0,25)
histo4.hsetlabels("Z Value of the Decay","N")

histo5=hb.histo("Kaon Decay Location for Good Triggers",150,0,25)
histo5.hsetlabels("Z Value of the Decay","N")

histo6=hb.histo("Pion Energy",150,0,60)
histo6.hsetlabels("Energy","N")

histo7=hb.histo("Pion Energy for Good Triggers",150,0,60)
histo7.hsetlabels("Energy","N")
kdg=md.Kdecay()

#function to find the position of x or y depending on the z position, z momentum, and y/x momentum
def getd(z,mmomx,pmomx,pmomz,mmomz):
    distance_minus = mmomx*z/mmomz
    distance_plus = pmomx*z/pmomz
    return(distance_minus,distance_plus)


#initialize variables to keep track of where the particles end up and
#the detector position and total kaons produced
first_detector = 38 
kaons = 100000 
inhole = 0 
wide = 0 

for i in range(kaons):
    vertex,pmu_plus,pmu_minus = kdg.getdecay()
    hole = False
    
    #locations of the detectors from decay location
    z1 = 38 - vertex[2]    
    z2 = z1 + 10
    z3 = z1 + 15
    
    #calculate the x position for the pions - then +
    xm1,xp1 = getd(z1,pmu_plus[1],pmu_minus[1],pmu_plus[3],pmu_minus[3])
    xm2,xp2 = getd(z2,pmu_plus[1],pmu_minus[1],pmu_plus[3],pmu_minus[3])
    xm3,xp3 = getd(z3,pmu_plus[1],pmu_minus[1],pmu_plus[3],pmu_minus[3])
    
    #calculate the y positions for the pions - then +
    ym1,yp1 = getd(z1,pmu_plus[2],pmu_minus[2],pmu_plus[3],pmu_minus[3])
    ym2,yp2 = getd(z2,pmu_plus[2],pmu_minus[2],pmu_plus[3],pmu_minus[3])
    ym3,yp3 = getd(z3,pmu_plus[2],pmu_minus[2],pmu_plus[3],pmu_minus[3])
    
    #check if its a good trigger or if it's wide or in the hole
    if((xm1>-.6 and xm1<.6) and (ym1>-.6 and ym1<.6)):
        if((xm2>-.7 and xm2<.7) and (ym2>-.7 and ym2<.7)):
            if((xm3>-.75 and xm3<.75) and (ym3>-.75 and ym3<.75)):
                if((xm3<-.25 or xm3>.25) or (ym3<-.25 or ym3>.25)):
                    histo3.hfill(xm3)   
                else:
                    hole=True
            else:
                wide+=1
        else:
            wide+=1
    else:
        wide+=1
                    
    if((xp1>-.6 and xp1<.6) and (yp1>-.6 and yp1<.6)):
        if((xp2>-.7 and xp2<.7) and (yp2>-.7 and yp2<.7)):
            if((xp3>-.75 and xp3<.75) and (yp3>-.75 and yp3<.75)):
                if((xp3<-.25 or xp3>.25) or (yp3<-.25 or yp3>.25)):
                    histo3.hfill(xp3)
                else:
                    hole=True
            else:
                wide+=1
        else:
            wide+=1
    else:
        wide+=1

    #check if either pion went through  the hoole
    if (hole):
        inhole+=1
    else:
        histo7.hfill(pmu_minus[0])
        histo7.hfill(pmu_plus[0])
        histo5.hfill(vertex[2])
    
    #fill the graphs that do not depend on triggering
    histo1.hfill(xm1)
    histo1.hfill(xp1)
    
    histo2.hfill(xm2)
    histo2.hfill(xp2)
    
    histo4.hfill(vertex[2])
    
    histo6.hfill(pmu_minus[0])
    histo6.hfill(pmu_plus[0])
    
#print out the graphs
histo1.hprint()
histo2.hprint()
histo3.hprint()
histo4.hprintlog()
histo5.hprintlog()
histo6.hprint()
histo7.hprint()

print("number of decays:  100000")
print("number of triggers:",kaons-inhole)
print("number of events with pion(s) in hole: ",inhole)
print("target to first tracker distance:  ",first_detector)