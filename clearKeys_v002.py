##Author: Kyle Phan
##Date: 19/03
##Description: Cleaning static inbetween keys on chosen/all attributes

import maya.cmds as mc

def letsClear(*args):
    
    obj = mc.ls(sl=True)
    if all == True:
        for o in obj:    
            clearTransRot(o)
            clearUserDefinedAttr(o)            
    else:
        for o in obj:    
            clear(o,type)
        
def allOn(*args):
    global all
    all = True   
    mc.optionMenu(opt, e = True, enable = False)
def allOff(*args):
    global all
    all = False
    mc.optionMenu(opt, e = True, enable = True)  
      
def letsError(item):
    global type
    type = 'error'

def changeAttr(item):
    
    global type
    type = ''
    if (item == 'Choose an attribute'):
        type = 'error'
    
    if (item == 'Rotate X'):
        type = 'rotateX'
        
    if (item == 'Rotate Y'):
        type = 'rotateY'
        
    if (item == 'Rotate Z'):
        type = 'rotateZ'
        
    if (item == 'Translate X'):
        type = 'translateX' 
           
    if (item == 'Translate Y'):
        type = 'translateY'  
        
    if (item == 'Translate Z'):
        type = 'translateZ'    

def clearUserDefinedAttr(o):
    
    attrList = mc.listAttr(o, userDefined = True, keyable=True, visible = True)
    attrCount = len(attrList)
    aC = 0
    while aC < attrCount:
        
        type = str(attrList[aC])
        
        aC = aC + 1
        
        count = mc.keyframe(o, query=True,attribute=type, keyframeCount = True)
        
        if count > 2:        
            c = 0    
            emptyList = []    
            while c < count:
                test = 0
                up = c + 1
                down = c - 1
                
                value = mc.keyframe(o, query=True,attribute = type, valueChange=True)                     
                if c == 0 or c == (len(value)-1):
                    test = test + 1
                else:
                    if value[c] == value[up] and value[c] == value[down]: 
                    
                        emptyList.append(c)
                    
                c = c + 1 
                print value  
            if len(emptyList) != 0:
                emptyList.reverse()
                indexRange=[(index,) for index in emptyList]   
                mc.cutKey(o, option = 'keys', attribute = type, index = indexRange)
          
def clear(o, type):
    if (type == 'error'):
        mc.confirmDialog(title = 'ERROR!', message='No attribute chosen. Please choose 1')
    else:
          
        count = mc.keyframe(o, query=True,attribute=type, keyframeCount = True)
        transX = mc.keyframe(o, query=True,attribute=type) 
        c = 0    
        emptyList = []    
        while c < count:
            test = 0
            up = c + 1
            down = c - 1
            
            value = mc.keyframe(o, query=True,attribute = type, valueChange=True)                     
            if c == 0 or c == (len(value)-1):
                test = test + 1
            else:
                if value[c] == value[up] and value[c] == value[down]: 
                
                    emptyList.append(c)
                
            c = c + 1 
            print value  
        if len(emptyList) != 0:
            emptyList.reverse()
            indexRange=[(index,) for index in emptyList]   
            mc.cutKey(o, option = 'keys', attribute = type, index = indexRange)
        
def clearTransRot(o):
    
    attrList = mc.listAttr(o, keyable = True, visible = True, st = ['translate*', 'rotate*'])
    attrCount = len(attrList)
    aC = 0
    while aC < attrCount:
        
        type = str(attrList[aC])
        
        aC = aC + 1
        
        count = mc.keyframe(o, query=True,attribute=type, keyframeCount = True)
        
        if count > 2:        
            c = 0    
            emptyList = []    
            while c < count:
                test = 0
                up = c + 1
                down = c - 1
                
                value = mc.keyframe(o, query=True,attribute = type, valueChange=True)                     
                if c == 0 or c == (len(value)-1):
                    test = test + 1
                else:
                    if value[c] == value[up] and value[c] == value[down]: 
                    
                        emptyList.append(c)
                    
                c = c + 1 
                print value  
            if len(emptyList) != 0:
                emptyList.reverse()
                indexRange=[(index,) for index in emptyList]   
                mc.cutKey(o, option = 'keys', attribute = type, index = indexRange)
                
                
windowID = 'deleteKeys'              
if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)
mc.window( windowID, title = 'Delete Key' )
mc.rowColumnLayout(numberOfColumns=3)
opt = mc.optionMenu( changeCommand = changeAttr, visibleChangeCommand=letsError)
mc.menuItem(label = 'Choose an attribute')
mc.menuItem(label = 'Rotate X')
mc.menuItem(label = 'Rotate Y')
mc.menuItem(label = 'Rotate Z')
mc.menuItem(label = 'Translate X')
mc.menuItem(label = 'Translate Y')
mc.menuItem(label = 'Translate Z')

mc.checkBox(label = 'All Attribute', onCommand = allOn, offCommand = allOff)

mc.button(label = 'Lets clear', command = letsClear)
mc.showWindow()
        