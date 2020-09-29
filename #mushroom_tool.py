from functools import partial

#Window
cmds.window("Mushroom Tool V.02", sizeable=True, resizeToFitChildren=True) 
cmds.columnLayout( adjustableColumn=True )                                             

#Text
cmds.separator(h=20)
cmds.text("Adjust Parameters of the Mushroom")
cmds.separator(h=20)

#Stem Funcations
def adjustStemRadius(sliderRadius, *args, **kwargs):
    """
    sliderRadius: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    stemName = getName("stem")
    cmds.select(stemName, r=True)
    cmds.polyCylinder(stemName, edit=True, r=valRadius, **kwargs)  

def adjustStemHeight(sliderHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the height radius value
        
    Adjusts the stem height of the stem based on the slider value. Also adjusts the hieght of the cap based on the height of the stem.
    """
    
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    stemName = getName("stem")
    cmds.select(stemName, r=True)
    cmds.polyCylinder(stemName, edit=True, h=valHeight, **kwargs) 
    cmds.move(0, valHeight/2, 0, stemName)
    
    #adjusting the cap height based on the new stem height
    capName = getName("cap")
    cmds.move(0, valHeight, 0, capName)     

def stemSubX(sliderX, *args, **kwargs):
    """
    sliderX: intSliderGrp object holding the stem subdivisions x value
        
    Adjusts the subdivisions x of the stem based on the slider value
    """
    
    valSX = cmds.intSliderGrp(sliderX, q=True, value=True)
    stemName = getName("stem")
    cmds.select(stemName, r=True)
    cmds.polyCylinder(stemName, edit=True, sx=valSX, **kwargs)     
     
def stemSubY(sliderY, *args, **kwargs):
    """
    sliderY: intSliderGrp object holding the stem subdivisions y value
        
    Adjusts the subdivisions y of the stem based on the slider value
    """
    
    valSY = cmds.intSliderGrp(sliderY, q=True, value=True)
    stemName = getName("stem")
    cmds.select(stemName, r=True)
    cmds.polyCylinder(stemName, edit=True, sy=valSY, **kwargs)  

#Cap Funcations
def adjustCapRadius(sliderRadius, *args, **kwargs):
    """
    sliderRadius: floatSliderGrp object holding the cap radius value
        
    Adjusts the cap radius of the stem based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    capName = getName("cap")
    capNumber = getNumStr("cap")
    cmds.select(capName, r=True)
    cmds.setAttr('polySphere' + capNumber+ '.radius', valRadius, **kwargs)  

def capSubX(sliderX, *args, **kwargs):
    """
    sliderX: intSliderGrp object holding the cap subdivisions x value
        
    Adjusts the subdivisions x of the cap based on the slider value
    """
    
    capName = getName("cap")
    cmds.delete(capName)
    cap()    
     
def capSubY(sliderY, *args, **kwargs):
    """
    sliderY: intSliderGrp object holding the cap subdivisions y value
        
    Adjusts the subdivisions y of the cap based on the slider value
    """
    
    capName = getName("cap")
    cmds.delete(capName)
    cap()

def capScaleY(sliderScaleY, *args, **kwargs):
    """
    sliderScaleY: floatSliderGrp object holding the cap scale y value
        
    Adjusts the scale in y of the cap based on the slider value
    """
    
    valScaleY = cmds.floatSliderGrp(sliderScaleY, q=True, value=True)
    capName = getName("cap")
    cmds.select(capName, r=True)
    cmds.setAttr(capName + '.scaleY', valScaleY, **kwargs)  
                         
#Sliders Stem
stemRadius_Slider = cmds.floatSliderGrp(label='Stem Radius', columnAlign= (1,'right'), field=True, min=0.3, max=3, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(stemRadius_Slider,  e=True, dc = partial(adjustStemRadius, stemRadius_Slider))

stemHieght_Slider = cmds.floatSliderGrp(label='Stem Height', columnAlign= (1,'right'), field=True, min=1, max=3, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(stemHieght_Slider, e=True, dc = partial(adjustStemHeight, stemHieght_Slider))

stemSubX_Slider = cmds.intSliderGrp(label='Stem Density', columnAlign= (1,'right'), field=True, min=5, max=20, value=0, step=1, dc = 'empty')
cmds.intSliderGrp(stemSubX_Slider, e=True, dc = partial(stemSubX, stemSubX_Slider))

stemSubY_Slider = cmds.intSliderGrp(label='Stem Sections', columnAlign= (1,'right'), field=True, min=5, max=20, value=0, step=1, dc = 'empty')
cmds.intSliderGrp(stemSubY_Slider, e=True, dc = partial(stemSubY, stemSubY_Slider))

#Sliders Cap
capRadius_Slider = cmds.floatSliderGrp(label='Cap Radius', columnAlign= (1,'right'), field=True, min=0.5, max=3, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(capRadius_Slider,  e=True, dc = partial(adjustCapRadius, capRadius_Slider))

capSubX_Slider = cmds.intSliderGrp(label='Cap Density', columnAlign= (1,'right'), field=True, min=3, max=20, value=3, step=1, dc = 'empty')
cmds.intSliderGrp(capSubX_Slider, e=True, dc = partial(capSubX, capSubX_Slider))

capSubY_Slider = cmds.intSliderGrp(label='Cap Sections', columnAlign= (1,'right'), field=True, min=4, max=20, value=4, step=1, dc = 'empty')
cmds.intSliderGrp(capSubY_Slider, e=True, dc = partial(capSubY, capSubY_Slider))

capScaleY_Slider = cmds.floatSliderGrp(label='Cap Stretch/Compress', columnAlign= (1,'right'), field=True, min=0, max=2, value=1, step=0.1, dc = 'empty')
cmds.floatSliderGrp(capScaleY_Slider, e=True, dc = partial(capScaleY, capScaleY_Slider))

#Button
cmds.button(l = "Create Mushroom",  c = "mushroom()")
cmds.separator(h=20)
cmds.showWindow()


def mushroom():
    """
    Constructing a mushroom model based on user input on a variety of parameters
    """
    stemRadius = cmds.floatSliderGrp(stemRadius_Slider, q=True, value=True)
    stemHieght = cmds.floatSliderGrp(stemHieght_Slider, q=True, value=True)
    stemSubX = cmds.intSliderGrp(stemSubX_Slider, q=True, value=True)
    stemSubY = cmds.intSliderGrp(stemSubY_Slider, q=True, value=True)
    
    capRadius = cmds.floatSliderGrp(capRadius_Slider, q=True, value=True)
    capSubX = cmds.intSliderGrp(capSubX_Slider, q=True, value=True)
    capSubY = cmds.intSliderGrp(capSubY_Slider, q=True, value=True)
   
    #making stem of mushroom 
    finalStem = cmds.polyCylinder(n='stem#', r=stemRadius, h=stemHieght, sx=stemSubX, sy=stemSubY)
    
    #moving stem
    stemls = cmds.ls('stem*', long=True)
    stemName = stemls[len(stemls)-1][1:6]
    cmds.move(0, stemHieght/2, 0, stemName)
    
    #creating a group and adding the stem to it
    #mushroom = cmds.group(empty = True, name ="mushroom#")
    #cmds.parent(stemName, mushroom) 
    
    #making cap of mushroom 
    cap()
     
    
def cap():
    """
    Constructing the cap of the mushroom model based on user input on a variety of parameters. Also called when cap parameters are updated.
    """
    stemHieght = cmds.floatSliderGrp(stemHieght_Slider, q=True, value=True)
    capRadius = cmds.floatSliderGrp(capRadius_Slider, q=True, value=True)
    capSubX = cmds.intSliderGrp(capSubX_Slider, q=True, value=True)
    capSubY = cmds.intSliderGrp(capSubY_Slider, q=True, value=True)
    capScaleY = cmds.floatSliderGrp(capScaleY_Slider, q=True, value=True)
    
    #forcing capSubY to always be even because polySpheres with an odd # of SubdivisionsY can't be divided in half evenly 
    if capSubY%2 == 1:
        capSubY = capSubY + 1
    
    #quadedSphere() does this calculation, so it needs to be repeated here so the numbers align 
    if capSubX%2 == 1:
        capSubX = capSubX + 1
    
    finalCap = quadedSphere('cap#', capRadius, capSubX, capSubY)
    
    #making a polySphere into a semi-polySphere
    total_faces = capSubX * (capSubY-1)
    print(total_faces)
    
    #selecting the end and start of the facets to delete
    delStarta = 0
    delEnda = capSubX * ((capSubY/2)-1) - 1
    
    delStartb = total_faces - capSubX
    delEndb = delStartb + (capSubX/2) - 1
    print(delStartb)
    print(delEndb)
    
        
    delStarta = int(delStarta)
    delEnda = int(delEnda)
    delStartb = int(delStartb)
    delEndb = int(delEndb)
    
    capName = getName("cap")
    
    stemName = getName("stem")
  
    #deleting half of the polySphere to make a semi-polySphere mushroom cap
    cmds.delete(capName +  '.f[' + str(delStarta) + ':' +  str(delEnda)+ ']', capName + '.f[' + str(delStartb) + ':' +  str(delEndb)+ ']')
    #cmds.select(capName + '.e[0]', r=True)
    #cmds.polyExtrudeEdge( capName + '.e[0]', kft=True, ltz=2, ls=(.5, .5, 0) )
    #cmds.polyCloseBorder() 
    #cmds.select(capName, r=True)
    
    #moving cap to form a mushroom!
    cmds.move(0, stemHieght, 0, capName)
    
    #scaling cap in Y
    cmds.select(capName, r=True)
    cmds.setAttr(capName + '.scaleY', capScaleY) 
    
    #adding the cap to the mushroom group
    #mushroomls = cmds.ls('mushroom*', long=True)
    #mushroomName = mushroomls[len(mushroomls)-1][1:9]
    #cmds.parent(capName, mushroomName)  
    
def quadedSphere(name, radius, subx, suby):
    sphereRadius = radius
    sphereSubX = subx
    sphereSubY = suby
    
    #forcing capSubX to always be even because polySpheres with an odd # of SubdivisionsX can't be quaded with this method of deleting edges
    if sphereSubX%2 == 1:
        sphereSubX = sphereSubX + 1
    
    #calculating the start and end edges to delete
    totalEdges = sphereSubX*(2*sphereSubY-1)-1  
    startEdgesDelete = totalEdges - ((sphereSubX-1)*2)
    
    #creating sphere
    sphere = cmds.polySphere(n=name, r=sphereRadius, sx=sphereSubX, sy=sphereSubY, ch=True)
    sphereName = getName("cap")
    
    #iterating over the edges to delete and filling the edgeDeleteList
    edgeDeleteList = []
    for edgeNum in range(startEdgesDelete, totalEdges+1, 2): 
        edgeString = sphereName + '.e[' + str(edgeNum) + ']'
        edgeDeleteList.append(edgeString)
    cmds.delete(edgeDeleteList)
    
def getName(objPrefix):
    """
    objPrefix: string prefix of object
    
    Returns full name of object
    """
    
    objNumberStr = getNumStr(objPrefix)
    objName = objPrefix + objNumberStr
    
    return objName
    
def getNumStr(objPrefix):
    """
    objPrefix: string prefix of object
    
    Returns instance number of object
    """
    
    objls = cmds.ls(objPrefix + '*', long=True)
    objNumber = len(objls)/2
    objNumberStr = str(objNumber)
    
    return objNumberStr
   
   