'''
Author - Kyle Phan
Version - 0.1
Date - 08/11/2018
Description - UI to name nodes with prefixes, suffixes, and integers for unique names
'''

import maya.cmds as mc

## function starts here

def nameStuff(*args):
    
    ## get user data 
    prefix = mc.textField('prefixTextField',query = True, text = True)
    suffix = mc.textField('suffixTextField',query = True, text = True)
    ## name function
    objects = mc.ls( sl = True )    
    for obj in objects:
        num = objects.index(obj) + 1
        tempName = prefix + '_' + str (num) + '_' + suffix
        realName = mc.rename( obj , tempName )

## UI starts here
windowID = 'namingUI'

if mc.window( windowID, exists = True ):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Naming with Suffix and Prefix UI' )
mc.columnLayout()
mc.text(label = 'Type in suffix and prefix')
mc.rowColumnLayout( numberOfColumns=2 )

mc.text( label = 'Prefix:')
mc.textField('prefixTextField')

mc.text( label = 'Suffix:')
mc.textField('suffixTextField')

mc.text( label = '')
mc.text( label = '')

mc.columnLayout()
mc.text(label = 'Choose objects and press Button')
mc.button( label = 'Name It', command = nameStuff)

mc.showWindow()


