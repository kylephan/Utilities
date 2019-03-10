## Author : Kyle Phan
## Version: 1.0
## Date: 10/03/2019
## Description: Personal use for special group to creat offset groups for controls,joints and locators.

import maya.cmds as mc

def masterOn(*args):
    global masterOn
    masterOn = True
    mc.intField(numGroups, e = True, enable =False)
def masterOff(*args):
    global masterOn
    masterOn = False
    mc.intField(numGroups, e = True, enable =True)
    
    
def typeChange(item):
    global type
    
    
    if (item == 'Controls'):
        type = 'ctrl'
    if (item == 'Joints'):
        type = 'jnt'
    if (item == 'Locators'):
        type = 'loc'
        
def letsGroup(*args):
    
    objects = mc.ls( sl = True, o = True, sn = True )
    num = mc.intField(numGroups, query = True, value =True)

    for obj in objects:
        i = 0
        if (num == 0):
            return
        else:
            if masterOn:
                tempName = type + '_grp_offset'
                if (mc.listRelatives(obj, parent = 1) == None):    
                    grp = mc.group(em=True, name = obj.replace(type, tempName))
                
                    pos = mc.xform(obj, q=1, ws=1, t=1)
                    rot = mc.xform(obj, q=1, ws=1, ro=1)  
            
                    mc.xform(grp, ws=1, t=pos)
                    mc.xform(grp, ws=1, ro=rot)
                    
                    mc.parent(obj, grp)
                else:
                    tempName = type + '_grp_offset'
                        
                    par = mc.listRelatives(obj, parent = 1)[0]
                    grp = mc.group(em=True, name = obj.replace(type, tempName))
                
                    pos = mc.xform(obj, q=1, ws=1, t=1)
                    rot = mc.xform(obj, q=1, ws=1, ro=1)  
            
                    mc.xform(grp, ws=1, t=pos)
                    mc.xform(grp, ws=1, ro=rot)
                    
                    mc.parent(grp, par)
                    mc.parent(obj, grp)
                    
            else:
                while i < num:
                    if (mc.listRelatives(obj, parent = 1) == None):
                        tempName = type + '_grp_' + str(i)
                        grp = mc.group(em=True, name = obj.replace(type, tempName))
                    
                        pos = mc.xform(obj, q=1, ws=1, t=1)
                        rot = mc.xform(obj, q=1, ws=1, ro=1)  
                
                        mc.xform(grp, ws=1, t=pos)
                        mc.xform(grp, ws=1, ro=rot)
                        
                        mc.parent(obj, grp)
                        
                    else:
                        tempName = type+ '_grp_' + str(i)
                        
                        par = mc.listRelatives(obj, parent = 1)[0]
                        grp = mc.group(em=True, name = obj.replace(type, tempName))
                    
                        pos = mc.xform(obj, q=1, ws=1, t=1)
                        rot = mc.xform(obj, q=1, ws=1, ro=1)  
                
                        mc.xform(grp, ws=1, t=pos)
                        mc.xform(grp, ws=1, ro=rot)
                        
                        mc.parent(grp, par)
                        mc.parent(obj, grp)
                        
                    i = i +1

windowID = 'groupSpecial'

if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Group special' )
mc.rowColumnLayout(numberOfColumns=3)
mc.optionMenu(changeCommand = typeChange)
mc.menuItem(label = 'Controls')
mc.menuItem(label = 'Joints')
mc.menuItem(label = 'Locators')
mc.text(label='')
mc.text(label='')
mc.text(label = 'How many offset groups do you wants?')
numGroups = mc.intField()
mc.text(label='')
mc.button(label = 'Lets group', command = letsGroup)
mc.checkBox(label = 'Master Offset', onCommand = masterOn, offCommand = masterOff)
mc.showWindow()
