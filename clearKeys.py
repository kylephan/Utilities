import maya.cmds as mc

def letsClear(*args):
    
    obj = mc.ls(sl=True)
    if all == True:
        for o in obj:    
            clearTX(o)
            clearTY(o)
            clearTZ(o)
            clearRX(o)
            clearRY(o)
            clearRZ(o)            
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
def changeAttr(item):
    
    global type
    type = ''
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
          
def clear(o, type):
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
        
def clearTX(o):
    count = mc.keyframe(o, query=True,attribute='translateX', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='translateX') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'translateX', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'translateX', index = indexRange)        

def clearTY(o):
    count = mc.keyframe(o, query=True,attribute='translateY', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='translateY') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'translateY', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'translateY', index = indexRange)   
def clearTZ(o):
    count = mc.keyframe(o, query=True,attribute='translateZ', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='translateZ') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'translateZ', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'translateZ', index = indexRange)
        
def clearRX(o):
    count = mc.keyframe(o, query=True,attribute='rotateX', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='rotateX') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'rotateX', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'rotateX', index = indexRange)        
        
def clearRY(o):
    count = mc.keyframe(o, query=True,attribute='rotateY', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='rotateY') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'rotateY', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'rotateY', index = indexRange)        
        
def clearRZ(o):
    count = mc.keyframe(o, query=True,attribute='rotateZ', keyframeCount = True)
    transX = mc.keyframe(o, query=True,attribute='rotateZ') 
    c = 0    
    emptyList = []    
    while c < count:
        test = 0
        up = c + 1
        down = c - 1
        
        value = mc.keyframe(o, query=True,attribute = 'rotateZ', valueChange=True)                     
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
        mc.cutKey(o, option = 'keys', attribute = 'rotateZ', index = indexRange)
                   
windowID = 'deleteKeys'       
        
if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Delete Key' )
mc.rowColumnLayout(numberOfColumns=3)
opt = mc.optionMenu( changeCommand = changeAttr)
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
        