'''
Author - Kyle Phan
Version - 0.1
Date - 08/11/2018
Description - Set driven key for specified attribute.
'''

import maya.cmds as mc

## function starts here
def setDrivenKey(*args):
    driver = mc.textField('driverTextField',query = True, text = True)
    maxZ = mc.intField('maxZIntField',query = True, value = True)
    minZ = mc.intField('minZIntField',query = True, value = True)
    ##print driver,maxZ,minZ
    
    objects = mc.ls( sl = True )
    for obj in objects:
        if len(objects):
            #set default 0
            mc.setAttr( driver + '.toeCurl', 0 )
            mc.setAttr( obj + '.rotateZ',0 )
            mc.setDrivenKeyframe( at = 'rotateZ', cd = driver + '.toeCurl' )
            
            #set max
            mc.setAttr( driver + '.toeCurl', 10 )
            mc.setAttr( obj + '.rotateZ', maxZ )
            mc.setDrivenKeyframe( at = 'rotateZ', cd = driver + '.toeCurl' )
            
            #set min
            mc.setAttr( driver + '.toeCurl', -5 )
            mc.setAttr( obj + '.rotateZ', minZ )
            mc.setDrivenKeyframe( at = 'rotateZ', cd = driver + '.toeCurl' )

## UI starts here
windowID = 'setDrivenKeyUI'

if mc.window( windowID, exists = True ):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Toe Curl & Wing Curl UI' )
mc.columnLayout()
mc.text(label = 'Type in control name, values')
mc.rowColumnLayout( numberOfColumns=2 )

mc.text( label = 'Driver:')
mc.textField('driverTextField')

mc.text( label = 'Rotate Z at Max:')
mc.intField('maxZIntField')

mc.text( label = 'Rotate Z at Min:')
mc.intField('minZIntField')

mc.text( label = '')
mc.text( label = '')

mc.columnLayout()
mc.text(label = 'Choose objects and press Button')
mc.button( label = 'Set Driven Key', command = setDrivenKey)

mc.showWindow()


