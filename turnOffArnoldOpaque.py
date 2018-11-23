'''
Author - Kyle Phan
Version - 0.1
Date - 08/11/2018
Description - Simple script just to turn off opaque
'''

import maya.cmds as mc

objects = mc.ls( sl = True )

for obj in objects:
    a = mc.listRelatives(obj)[0]
    mc.setAttr(a + '.aiOpaque' , 0 )
