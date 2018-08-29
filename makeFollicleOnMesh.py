import maya.cmds as mc

meshShp = 'body_geoShape' # change the name to your surface shape
joints = mc.ls ( os=True )

for jnt in joints:
    
    p = mc.xform( jnt, q=True, t=True, ws=True )
    cpom = mc.createNode( 'closestPointOnMesh' )
    
    mc.setAttr( cpom + '.inPositionX', p[0] )
    mc.setAttr( cpom + '.inPositionY', p[1] )
    mc.setAttr( cpom + '.inPositionZ', p[2] )
    
    mc.connectAttr( meshShp + '.outMesh', cpom + '.inMesh' )
    
    u = mc.getAttr ( cpom + '.parameterU' )
    v = mc.getAttr ( cpom + '.parameterV' )
    
    mc.delete(cpom)
    
    tnsfm = makeFollicleOnMesh( meshShp, jnt, u, v )
    tnsfm = mc.rename( tnsfm, jnt.replace( '_loc', '_follicle' ) )
    
    mc.parent( jnt, tnsfm )
    
def makeFollicleOnMesh( meshShp, jnt, u, v ):
    
    follicle = mc.createNode( 'follicle', name = jnt.replace( '_loc', '_follicleShape' ) )
    mc.connectAttr( meshShp + '.outMesh', follicle + '.inputMesh' )
    mc.connectAttr( meshShp + '.worldMatrix', follicle + '.inputWorldMatrix' )
    #connect u and v
    mc.setAttr( follicle + '.parameterU' , u )
    mc.setAttr( follicle + '.parameterV' , v )
    #get transform node and connect outT and outR into T and R
    follicleTnsfm = mc.listRelatives( follicle, parent = True )[0]
    
    mc.connectAttr( follicle + '.outTranslate', follicleTnsfm + '.t' )
    mc.connectAttr( follicle + '.outRotate', follicleTnsfm + '.r' )

    return follicleTnsfm