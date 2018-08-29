  import maya.cmds as mc

locator = mc.ls(sl=True)
lower = mc.ls(sl=True)
upper = mc.ls(sl=True)
length = [0,1,2,3,4,5,6,7,8]
driver = 'jaw_ctrl'

for i in length:
    if i == 0 or i == 8:
        mc.parentConstraint( locator[i], lower[i], sr=['x','y','z'] )
        mc.setKeyframe( lower[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( lower[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 1 )
        mc.setAttr( lower[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        mc.parentConstraint( locator[i], upper[i], sr=['x','y','z'] )
        mc.setKeyframe( upper[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( upper[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 1 )
        mc.setAttr( upper[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
    elif i == 1 or i == 7:
        mc.parentConstraint( locator[i], lower[i], sr=['x','y','z'] )
        mc.setKeyframe( lower[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( lower[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 2.5 )
        mc.setAttr( lower[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        mc.parentConstraint( locator[i], upper[i], sr=['x','y','z'] )
        mc.setKeyframe( upper[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( upper[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 2.5 )
        mc.setAttr( upper[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
    elif i == 2 or i == 6:
        mc.parentConstraint( locator[i], lower[i], sr=['x','y','z'] )
        mc.setKeyframe( lower[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( lower[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 5 )
        mc.setAttr( lower[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        mc.parentConstraint( locator[i], upper[i], sr=['x','y','z'] )
        mc.setKeyframe( upper[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( upper[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 5 )
        mc.setAttr( upper[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
    elif i == 3 or i == 5:
        mc.parentConstraint( locator[i], lower[i], sr=['x','y','z'] )
        mc.setKeyframe( lower[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( lower[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 7.5 )
        mc.setAttr( lower[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        mc.parentConstraint( locator[i], upper[i], sr=['x','y','z'] )
        mc.setKeyframe( upper[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( upper[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 7.5 )
        mc.setAttr( upper[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
    else:
        mc.parentConstraint( locator[i], lower[i], sr=['x','y','z'] )
        mc.setKeyframe( lower[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( lower[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 10 )
        mc.setAttr( lower[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( lower[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        mc.parentConstraint( locator[i], upper[i], sr=['x','y','z'] )
        mc.setKeyframe( upper[i], at ='translate', v = 0)
        mc.setAttr( driver + '.stickyLip', 0 )
        mc.setAttr( upper[i] + '.blendParent1', 0 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        mc.setAttr( driver + '.stickyLip', 10 )
        mc.setAttr( upper[i] + '.blendParent1', 1 )
        mc.setDrivenKeyframe( upper[i] + '.blendParent1', cd = driver + '.stickyLip' )
        
        
        