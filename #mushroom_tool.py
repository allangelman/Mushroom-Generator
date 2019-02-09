#mushroom_tool.py
import maya.cmds as cmds
import functools

def UI(pWindowTitle, makeMushroom):
    """
    Creating the user Interface to input various paramters to create a mushroom
    """
    windowID = 'Mushroom'
    
    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)
        
    #UI window  
    cmds.window(windowID, title = pWindowTitle, sizeable=True, resizeToFitChildren=True)
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1,20), (2,200), (3,200)],
                         columnOffset = [(1,'right', 3)])
    
    #input fields
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Stem Radius: ')
    stemRadius = cmds.floatField()
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Stem Height: ')
    stemHieght = cmds.floatField()
    cmds.separator(h=10,style='none')
    
    cmds.text(label='# Stem SubdivisionsX: ')
    stemSubX = cmds.intSlider(min = 0, max = 20, value=0, step=1)
    cmds.separator(h=10,style='none')
    
    cmds.text(label='# Stem SubdivisionsY: ')
    stemSubY = cmds.intSlider(min = 0, max = 20, value=0, step=1) 
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Cap Radius: ')
    capRadius = cmds.floatField()    
    cmds.separator(h=10,style='none')
    
    cmds.text(label='# Cap SubdivisionsX: ')
    capSubX = cmds.intSlider(min = 3, max = 20, value=3, step=1)
    cmds.separator(h=10,style='none')
    
    cmds.text(label='# Cap SubdivisionsY' + '\n' + '(rounded to nearest even): ')
    capSubY = cmds.intSlider(min = 4, max = 20, value=4, step=1)
    cmds.separator(h=10,style='none')
    
    cmds.text(label='Cap ScalingY: ')
    capScaleY = cmds.floatField()
    cmds.separator(h=10,style='none')
 
    
    #apply button calls makeMushroom
    cmds.button(label='Apply', command=functools.partial(makeMushroom, stemRadius, stemHieght, stemSubX, stemSubY, 
                                                            capRadius, capSubX, capSubY, capScaleY))
    def cancelCallback(*pArgs):
        if cmds.window(windowID, exists=True):
            cmds.deleteUI(windowID)
    cmds.button(label='Cancel', command=cancelCallback)
    cmds.showWindow()

def makeMushroom(stemRadius, stemHieght, stemSubX, stemSubY, 
capRadius, capSubX, capSubY, capScaleY, *pArgs):
    
    """
    Constructing a mushroom model based on user input on a variety of parameters
    """
    
    #user input
    stemRadius = cmds.floatField(stemRadius, query=True,value = True)
    stemHieght = cmds.floatField(stemHieght, query=True,value = True)
    stemSubX = cmds.intSlider(stemSubX, query=True,value = True)
    stemSubY = cmds.intSlider(stemSubY, query=True,value = True) 
    capRadius = cmds.floatField(capRadius, query=True,value = True)
    capSubX = cmds.intSlider(capSubX, query=True,value = True)
    capSubY = cmds.intSlider(capSubY, query=True,value = True)
    capScaleY = cmds.floatField(capScaleY, query=True,value = True)
    
    #forcing capSubY to always be even
    #this is because polySpheres with an odd # of SubdivisionsY can't be divided in half evenly 
    if capSubY%2 == 1:
        capSubY = capSubY + 1
    
    #creating stem
    stem_inst = cmds.polyCylinder(n='stem', r=stemRadius, h=stemHieght, sx=stemSubX, sy=stemSubY)
   
    #creating cap
    cap_inst = cmds.polySphere(n='cap', r=capRadius, sx=capSubX, sy=capSubY)
    cmds.polyOptions(db=True)
   
    #making a polySphere into a semi-polySphere
    
    term = capSubX * ((capSubY-2)/2)
    
    #selecting the end and start of the facets to delete
    delStarta = 0
    delEnda = term - 1 
    delStartb = 0
    delEndb = 0
    
    delStartb = term * 2
    delEndb = term * 2 + (capSubX - 1)
        
    delStarta = int(delStarta)
    delEnda = int(delEnda)
    delStartb = int(delStartb)
    delEndb = int(delEndb)
    
    cap_name = cmds.ls(cap_inst[0])
    stem_name = cmds.ls(stem_inst[0])
    
    #deleting half of the polySphere to make a semi-polySphere mushroom cap
    cmds.delete(cap_name[0] +  '.f[' + str(delStarta) + ':' +  str(delEnda)+ ']', cap_name[0] + '.f[' + str(delStartb) + ':' +  str(delEndb)+ ']')
    cmds.select(cap_name[0] + '.e[0]', r=True)
    cmds.polyCloseBorder()    
    
    #scaling cap in Y
    cmds.scale(1, capScaleY, 1, cap_inst[0])
    
    #moving stem and cap to form a mushroom!
    cmds.move(0, stemHieght/2, 0, stem_inst[0])
    cmds.move(0, stemHieght, 0, cap_inst[0])
    
    #organizing the mushroom parts in a layer 
    mushroom = cmds.group(empty = True, name ="mushroom")
    cmds.parent(stem_inst, mushroom)
    cmds.parent(cap_inst, mushroom)
    
    
UI('Mushroom Input', makeMushroom)
    
