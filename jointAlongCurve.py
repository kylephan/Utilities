'''
Author - Kyle Phan
Version - 0.1
Date - 08/11/2018
Description - Distribute joints evenly along a curve
'''

import maya.cmds as mc

crvShape = 'l_upperEyelid_crvShape' ## pass curveShape name in here

groups = mc.ls( sl=True )

for grp in groups:
    u = 1.0 - (1.0 / ( len(groups) - 1.0 ) ) * groups.index(grp)
    jointAlongCurve( crvShape,grp,u )
    
## define function
def jointAlongCurve( crvShape,grp,u ):
    mPath = mc.createNode('motionPath')
    
    mc.setAttr( mPath + '.fractionMode', 1)
    
    mc.connectAttr( crvShape + '.worldSpace', mPath + '.geometryPath' )
    mc.connectAttr( mPath + '.rotateOrder', grp + '.rotateOrder' )
    mc.connectAttr( mPath + '.message', grp + '.specifiedManipLocation' )
    
    mc.connectAttr( mPath + '.rotateX', grp + '.rotateX' )
    mc.connectAttr( mPath + '.rotateY', grp + '.rotateY' )
    mc.connectAttr( mPath + '.rotateZ', grp + '.rotateZ' )
    
    doubleLinearX = mc.createNode('addDoubleLinear')
    mc.connectAttr( grp + '.transMinusRotatePivotX', doubleLinearX + '.input1' )
    mc.connectAttr( mPath + '.xCoordinate', doubleLinearX + '.input2' )
    mc.connectAttr( doubleLinearX + '.output', grp + '.translateX' ) 
    
    doubleLinearY = mc.createNode('addDoubleLinear')
    mc.connectAttr( grp + '.transMinusRotatePivotY', doubleLinearY + '.input1' )
    mc.connectAttr( mPath + '.yCoordinate', doubleLinearY + '.input2' )
    mc.connectAttr( doubleLinearY + '.output', grp + '.translateY' ) 
    
    doubleLinearZ = mc.createNode('addDoubleLinear')
    mc.connectAttr( grp + '.transMinusRotatePivotZ', doubleLinearZ + '.input1' )
    mc.connectAttr( mPath + '.zCoordinate', doubleLinearZ + '.input2' )
    mc.connectAttr( doubleLinearZ + '.output', grp + '.translateZ' ) 
    
    mc.setAttr( mPath + '.uValue', u )
