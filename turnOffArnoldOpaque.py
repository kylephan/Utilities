import maya.cmds as mc

objects = mc.ls( sl = True )

for obj in objects:
    a = mc.listRelatives(obj)[0]
    mc.setAttr(a + '.aiOpaque' , 0 )