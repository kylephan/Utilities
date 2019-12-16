
'''
Author - Kyle Phan
Version - 0.4
Date - 08/1/2019
Description - Bake texture sequences. Idea based on Kiel Gneba script released on 2010
'''

import maya.cmds as mc

## get range
def SwitchToOpacity(*args):
    for i in textureFile:       
        path = mc.getAttr(i + '.fileTextureName')  
        newPath = path.replace('diffuse','opacity')  
        mc.setAttr(i + '.fileTextureName', newPath, type = 'string')
    
def SwitchToDiffuse(*args):
    for i in textureFile:
        path = mc.getAttr(i + '.fileTextureName')  
        newPath = path.replace('opacity','diffuse')
        mc.setAttr(i + '.fileTextureName', newPath, type = 'string')
    
def LoadShader(*args):
    global shader
    shader = mc.ls(sl=True, sn = True)
    for s in shader:      
        shaderText = mc.textScrollList('shaderTextTextField', append = str(s) , edit = True)
    
def LoadGeo(*args):
    global geo
    geo = mc.ls(sl=True, sn = True)
    for g in geo:      
        geoText = mc.textScrollList('geoTextTextField', append = str(g) , edit = True)

def LoadTexture(*args):
    global textureFile
    textureFile = mc.ls(sl=True, sn = True)
    for t in textureFile:      
        textureText = mc.textScrollList('textureTextTextField', append = str(t) , edit = True)
       
def GetFrameRange(*args):
    global currentMin,currentMax
    currentMin = int(mc.playbackOptions(query = True, min = True))
    currentMax = int(mc.playbackOptions(query = True, max = True))
    textMin = mc.textField('textMinTextField', text = str(currentMin), edit = True)
    textMax = mc.textField('textMaxTextField', text = str(currentMax), edit = True)
    
def ChangeShaderName ( item ):
    global shaderName
    global subSubFolder
    shaderName = str(item)
    subSubFolder = str(item)
    if str(item) == 'diffuse':
        SwitchToDiffuse(textureFile)
    if str(item) == 'opacity':
        SwitchToOpacity(textureFile)
    
def ChangeObjectName ( item ):   
    global objectName
    global subFolder 
    global bakeGeo
    global bakeShader
    objectName = str(item)
    subFolder = str(item)
    
    if str(item) == 'l_eye':
        bakeGeo = geo[0]
        bakeShader = shader[0]
    elif str(item) == 'r_eye':
        bakeGeo = geo[2]
        bakeShader = shader[2]
    else:
        bakeGeo = geo[1]
        bakeShader = shader[1]
       
def BakeTexture(*args):
    
    ### get output path and correct it
    outputOrig = mc.textField('outputTextField', query = True, text = True)
    outputStr = str(outputOrig)
    outputDir = outputStr.replace('\\', '/')
    ### other settings
    padding = 4
    resX = 1024
    resY = 1024
    fileFormat = 'jpg'
    geo = mc.ls(sl=True)
       
    for t in range(currentMin,currentMax+1,1):
    ## get padding
        numberExt = ''
        mc.currentTime(t, e=1)
        currentFrame = t
        currentFramePad = len(str(currentFrame))          
            
        if currentFramePad < padding:
            pad = padding-currentFramePad
            i = 1
            while i <= pad:
                numberExt += '0'
                i+=1
                
        numberExt += str(t)  
        ## bake starts here                
        imageName = (objectName + '_' + shaderName + '.' + numberExt + '.' + fileFormat)
        imageDir = (outputDir + '/' + subFolder + '/' + subSubFolder + '/' + imageName)
        file = mc.convertSolidTx(bakeShader, bakeGeo, antiAlias=0, bm=1, fts=1, sp=0, sh=0, alpha=0, doubleSided=0, componentRange=0, resolutionX=resX, resolutionY=resY, fileFormat=fileFormat, fileImageName=imageDir)
        mc.delete(file)
        
        
        
## UI starts here
windowID = 'bakeTextureSequences'

if mc.window( windowID, exists = True):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Bake Texture Sequences UI' )
mc.rowColumnLayout( numberOfColumns=3 )

mc.text( label = '' )
mc.button( label = '1.Get Frame Range', command = GetFrameRange )
mc.text( label = '' )

mc.text(label = 'Min:')
mc.textField('textMinTextField', en = False)
mc.text( label = '' )


mc.text(label = 'Max:')
mc.textField('textMaxTextField', en = False)
mc.text( label = '' )

mc.button( label = '2. Load geo', command = LoadGeo )
mc.button( label = '3. Load texture files', command = LoadTexture )
mc.button( label = '4. Load shader', command = LoadShader )


mc.textScrollList('geoTextTextField', en = False)
mc.textScrollList('textureTextTextField', en = False)
mc.textScrollList('shaderTextTextField', en = False)

mc.text( label = 'Choose object name:' )
mc.optionMenu('nameTextField', changeCommand=ChangeObjectName)
mc.menuItem( label = '5.Select name' )
mc.menuItem( label = 'l_eye' )
mc.menuItem( label = 'r_eye' )
mc.menuItem( label = 'mouth' )
mc.text( label = '' )

mc.text( label = 'Choose shader name:' )
mc.optionMenu('shaderNameTextField', changeCommand=ChangeShaderName)
mc.menuItem( label = '6.Select name' )
mc.menuItem( label = 'diffuse' )
mc.menuItem( label = 'opacity' )
mc.text( label = '' )

mc.text( label = 'Output Directory:')
mc.textField('outputTextField')
mc.text( label = '' )

mc.text( label = '' )
mc.button( label = '5.Bake', command = BakeTexture )
mc.text( label = '' )

mc.showWindow()
