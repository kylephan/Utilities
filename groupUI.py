'''
Author - Kyle Phan
Version - 0.1
Date - 08/11/2018
Description - Creat empty group to act as a holder for objects
'''

import maya.cmds as mc

## for controls
def groupControls(*args):
    objects = mc.ls( sl = True, o = True, sn = True )
    
    for obj in objects:  
        grp = mc.group ( em = True , name = obj.replace('_ctrl','_ctrl_grp') )
    
        mc.setAttr( grp + '.translateX' , 0 )
        mc.setAttr( grp + '.translateY' , 0 )
        mc.setAttr( grp + '.translateZ' , 0 )
        
        mc.setAttr( grp + '.rotateX' , 0 )
        mc.setAttr( grp + '.rotateY' , 0 )
        mc.setAttr( grp + '.rotateZ' , 0 )
        
        mc.parent( obj , grp )

## for joints
def groupJoints(*args):
    objects = mc.ls( sl = True, o = True, sn = True )
    
    for obj in objects:  
        grp = mc.group ( em = True , name = obj.replace('_jnt','_jnt_grp') )
    
        mc.setAttr( grp + '.translateX' , 0 )
        mc.setAttr( grp + '.translateY' , 0 )
        mc.setAttr( grp + '.translateZ' , 0 )
        
        mc.setAttr( grp + '.rotateX' , 0 )
        mc.setAttr( grp + '.rotateY' , 0 )
        mc.setAttr( grp + '.rotateZ' , 0 )
        
        mc.parent( obj , grp )

## UI starts here
windowID = 'groupUtilityUI'

if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Group Util UI' )
mc.rowLayout(numberOfColumns=2)
mc.button( label = 'Group Joints', command = groupJoints )
mc.button( label = 'Group Controls', command = groupControls )
mc.showWindow()
