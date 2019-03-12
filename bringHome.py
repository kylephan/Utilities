import maya.cmds as mc

surfShp = 'CHR003_Model_03_surfShape'
joints = mc.ls(os=True)

for jnt in joints:
    
    p = mc.xform(jnt, q=True, ws=True, t=True)
    cpos = mc.createNode('closestPointOnSurface')
    
    mc.setAttr(cpos + '.inPositionX', p[0])
    mc.setAttr(cpos + '.inPositionY', p[1])
    mc.setAttr(cpos + '.inPositionZ', p[2])
    
    mc.connectAttr( surfShp + '.worldSpace', cpos + '.inputSurface' )
    
    u = mc.getAttr( cpos + '.parameterU' )
    v = mc.getAttr( cpos + '.parameterV' )
    
    tsnfm = makeFollicleOnSurface( surfShp, jnt, u , v )
    tsnfm = mc.rename(tsnfm, jnt.replace('_jnt', '_follicle'))
    mc.parent(jnt, tsnfm)
    
def makeFollicleOnSurface(surfShp, jnt, u, v):
    follicle = mc.createNode('follicle', name = jnt.replace('_jnt', '_follicleShape'))
    mc.connectAttr(surfShp + '.worldSpace', follicle + '.inputSurface')
    mc.connectAttr(surfShp + '.worldMatrix', follicle + '.inputWorldMatrix')
    
    follicleTnsfm = mc.listRelatives(follicle, parent = True)[0]
    
    mc.connectAttr( follicle + '.outTranslate', follicleTnsfm + '.t' )
    mc.connectAttr( follicle + '.outRotate', follicleTnsfm + '.r' )
    
    mc.setAttr(follicle + '.parameterU', u)
    mc.setAttr(follicle + '.parameterV', v)
    
    return follicleTnsfm
       
    