## Author : Kyle Phan
## Version: 1.0
## Date: 10/03/2019
## Description: Personal use for connecting rotates/translates to user-defined attributes using animCurveUU
##

import maya.cmds as mc

def autoVariateRotOn(*args):   
 
    global onAuto    
    onAuto = True
    
def autoVariateRotOff(*args):   
 
    global onAuto    
    onAuto = False    

def selectGroups(*args):
    global groups
    groups = mc.ls(sl=True)
    mc.textScrollList(showGroups, e=True, ra = True )
    for g in groups:
        mc.textScrollList(showGroups, e=True , append = g)

def changeControlAttr(item):
    global controlAttr
    global attrName
    attrName=item
    controlAttr = '.' + item
    
    print controlAttr
            
def changeOutputAttr(item):
    global rota 
    rota = ''
    if (item == 'Rotate X'):
        rota = '.rotateX'
    if (item == 'Rotate Y'):
        rota = '.rotateY'
    if (item == 'Rotate Z'):
        rota = '.rotateZ'

def pickControl(*args):
    global ctrl
    ctrl = mc.ls(sl=True)
    mc.textScrollList(showControl, e=True, ra = True )
    mc.textScrollList(showControl, e=True , append = ctrl)
    
    attrList = mc.listAttr(ctrl, userDefined = True)
    existedItems = mc.optionMenu(attrMenu, query=1,itemListLong=1)
    if existedItems:
        mc.deleteUI(existedItems)
        for at in attrList:
            mc.menuItem(parent = attrMenu, label = at )
    else:
        for at in attrList:
            mc.menuItem(parent = attrMenu, label = at )
        
    
def setAnimCurveUU(*args):
    
    minFloat = mc.floatField('minFloat', q=1, value=1)
    maxFloat = mc.floatField('maxFloat', q=1, value=1)
    minValue = mc.floatField('minValue', q=1, value=1)
    maxValue = mc.floatField('maxValue', q=1, value=1)
    
    if onAuto:
        for grp in groups:
            
            newMinValue = minValue * ( 1 + 0.05 * groups.index(grp))
            newMaxValue = maxValue * ( 1 + 0.05 * groups.index(grp))
            
            animC = mc.createNode( 'animCurveUU', name = grp.replace('ctrl_grp', attrName ))
            
            min = mc.setKeyframe(animC, inTangentType = 'linear', outTangentType = 'linear', float= minFloat, value= newMinValue )
            max = mc.setKeyframe(animC, inTangentType = 'linear', outTangentType = 'linear', float= maxFloat, value= newMaxValue )
            
            zero = mc.setKeyframe(animC, insert=1, float=0.0 ,value=0.0)
            
            mc.connectAttr(ctrl[0] + str(controlAttr), animC + '.input')
            mc.connectAttr(animC + '.output', grp + str(rota) )
    
    else:           
        for grp in groups:
            
            animC = mc.createNode( 'animCurveUU', name = grp.replace('ctrl_grp', attrName ))
            
            min = mc.setKeyframe(animC, breakdown=1, float= minFloat, value= minValue )
            max = mc.setKeyframe(animC, breakdown=1, float= maxFloat, value= maxValue )
            
            zero = mc.setKeyframe(animC, insert=1, float=0.0 ,value=0.0)
            
            mc.connectAttr(ctrl[0] + str(controlAttr), animC + '.input')
            mc.connectAttr(animC + '.output', grp + str(rota) )

## Window starts here    
windowID = 'setAnimCurveUU'

if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Set AnimCurveUU for curl' )
mc.rowColumnLayout(numberOfColumns=5)
mc.text(label='Control&Attribute')
mc.button(label = 'Pick Control', command = pickControl)
showControl = mc.textScrollList(numberOfRows=1)
attrMenu = mc.optionMenu('optionTest',numberOfItems=3, changeCommand=changeControlAttr)
mc.text(label = '')

mc.text(label='Min Float:')
mc.floatField('minFloat')
mc.text(label='Min Value:')
mc.floatField('minValue')
mc.text(label = '')

mc.text(label='Max Float:')
mc.floatField('maxFloat')
mc.text(label='Max Value:')
mc.floatField('maxValue')
mc.text(label = '')
mc.text(label = 'Select offset groups')
mc.button(label = 'Select', command=selectGroups)
showGroups = mc.textScrollList()
mc.text(label = '')
mc.text(label = '')

mc.text(label='Atribute to be connected')
optMenu = mc.optionMenu(numberOfItems=3, changeCommand=changeOutputAttr)
mc.menuItem(label = 'Rotate X')
mc.menuItem(label = 'Rotate Y')
mc.menuItem(label = 'Rotate Z')
single = mc.checkBox(label = 'Auto Variate Rotation (For Single Finger)', onCommand=autoVariateRotOn, offCommand = autoVariateRotOff )
mc.button( label = 'Set', command = setAnimCurveUU )
mc.showWindow()
    