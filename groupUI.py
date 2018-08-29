import maya.cmds as mc

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
        
windowID = 'groupUtilityUI'

if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Group Util UI' )
mc.rowLayout(numberOfColumns=2)
mc.button( label = 'Group Joints', command = groupJoints )
mc.button( label = 'Group Controls', command = groupControls )
mc.showWindow()