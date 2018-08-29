import maya.cmds as mc

objects = mc.ls(sl=True)
prefix = 'leaves_'
suffix = '_geo'

for obj in objects:
    num = objects.index(obj) + 1
    tempName = prefix + str (num) + suffix
    print tempName
    tempName = mc.rename( obj , tempName )