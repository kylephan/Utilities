#|############################################################################################################
#
# NAME: 
#     bakeTextureSequence
#
# AUTHOR:
#     Kiel Gnebba (ksg@kielgnebba.com)
#
# PROJECT:
#     project name
#		
# VERSION: 
#     v. 1.0
#
# DESCRIPTION: 
#     This script will...
#         -
#         -
#         -
#
# INSTALLATION:
#     Copy the script into your scripts/ directory
#     If you're unsure where that is run this in the script editor:
#         mel    == internalVar -userScriptDir;
#         python == import maya.cmds as cmds; print cmds.internalVar(userScriptDir=True)
#
# USAGE:
#     To use just run: 
#         import maya.cmds as cmds
#         scriptName = 'bakeTextureSequence'
#         scriptsDir = cmds.internalVar(userScriptDir=True)
#         execfile(scriptsDir + scriptName + '.py')
#         bakeTextureSequence() 
#        
#     Or you can call the file directly from where ever you put it
#         execfile(C:/...where_ever.../bakeTextureSequence.py)
#         bakeTextureSequence()
#
# HISTORY:
#     01/01/2010 -- v. 1.0
#         - first release
#     
#|############################################################################################################

#import
import time
import maya.cmds as cmds
import maya.mel


#*************************************************************************************************************
#*start bakeTextureSequence_browser()

def bakeTextureSequence_browser():
    proc = 'bakeTextureSequence_browser'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#output directory browser
    currentString = cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', q=1, text=1)
    newString = cmds.fileDialog2(dialogStyle=2, fileMode=3, dir=currentString, caption='Output Directory', okCaption='OK', returnFilter=0)
    if len(str(newString)) == 4:
        cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', e=1, text=currentString)
    else:
        cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', e=1, text=newString[0])

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_browser()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_outputDir()

def bakeTextureSequence_outputDir():
    proc = 'bakeTextureSequence_outputDir'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#get current sourceimage dir and auto fill the output dir path
    rootDir = cmds.workspace(q=1, rd=1)
    workspaces = cmds.workspace(q=1, fr=1)
    sourceimageDir = ''
    for i in range(len(workspaces)):
        if workspaces[i] == 'sourceImages':
            sourceimageDir = workspaces[i+1]
            break

    if sourceimageDir == 'sourceImages' or sourceimageDir == 'sourceimages':
        sourceimageDir = rootDir+sourceimageDir
        
    cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', e=1, text=sourceimageDir)
    
#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_outputDir()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_maintain()

def bakeTextureSequence_maintain():
    proc = 'bakeTextureSequence_maintain'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#if maintain is checked update res y
    maintain = cmds.checkBox('bakeTextureSequence_maintainCB', q=1, value=1)
    if maintain == 1:
        resX = cmds.intSliderGrp('bakeTextureSequence_xResFSG', q=1, value=1)    
        cmds.intSliderGrp('bakeTextureSequence_yResFSG', e=1, value=resX) 

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_maintain()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_loadGeo()

def bakeTextureSequence_loadGeo():
    proc = 'bakeTextureSequence_loadGeo'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#load only nurbs or mesh if not already loaded
    cmds.textScrollList('bakeTextureSequence_loadGeoTSL', e=1, removeAll=1)
    selection = cmds.ls(sl=1, dag=1, type='shape')
    currentList=['']
    list = cmds.textScrollList('bakeTextureSequence_loadGeoTSL', q=1, ai=1)
    if str(list)!= 'None':
        currentList+=list
    if len(selection)==0:
        cmds.warning('nothing selected...select a nurbs/mesh and load')
    else:
        for each in selection:
            nodetype = cmds.nodeType(each)
            if nodetype == 'mesh' or nodetype == 'nurbsSurface':
                contains = each in currentList
                if contains == 0:
                    cmds.textScrollList('bakeTextureSequence_loadGeoTSL', e=1, append=each)

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_loadGeo()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_loadTexture()

def bakeTextureSequence_loadTexture():
    proc = 'bakeTextureSequence_loadTexture'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#load only nurbs or mesh if not already loaded
    cmds.textScrollList('bakeTextureSequence_loadTextureTSL', e=1, removeAll=1)
    selection = cmds.ls(sl=1)
    if len(selection)==0:
        cmds.warning('nothing selected...select a texture/file/ramp/ect and load')
    elif len(selection)>1:
        cmds.warning('more then one thing selected...select a texture or file node')
    else:
        nodetype = cmds.nodeType(selection[0])
        classification = cmds.getClassification(nodetype)
        newMayaFix = classification[0].split(':')
        if newMayaFix[1] == 'texture/2d' or newMayaFix[1] == 'shader/surface' or newMayaFix[1] == 'shader/surface/utility' or newMayaFix[1] == 'utility/color' or newMayaFix[1] == 'utility/general' or newMayaFix[1] == 'connection/mentalray/shadow:rendernode/mentalray/material:shader/surface:swatch/mentalRaySwatchGen'  or newMayaFix[1] == 'connection/mentalray/photon:connection/mentalray/shadow:rendernode/mentalray/material:shader/surface:swatch/mentalRaySwatchGen':
            cmds.textScrollList('bakeTextureSequence_loadTextureTSL', e=1, append=selection[0])
           
#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_loadTexture()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_mayaOrMR()

def bakeTextureSequence_mayaOrMR():
    proc = 'bakeTextureSequence_mayaOrMR'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#update ui based on maya vs mental ray
    mayaOrMr = cmds.radioButtonGrp('bakeTextureSequence_bakeTypeRBG', q=1, select=1) 
    if mayaOrMr == 1:
        #cmds.intSliderGrp('bakeTextureSequence_paddingFSG', e=1, en=1, visible=1)
        #cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', e=1, en=1, visible=1)
        cmds.deleteUI('bakeTextureSequence_fileFormatOMG', control=1)
        cmds.optionMenuGrp('bakeTextureSequence_fileFormatOMG', label='file format: ', columnWidth=(2, 80), p='bakeTextureSequence_bakeOptionsForm')
        cmds.menuItem('bakeTextureSequence_fileFormatJpgMI', label='JEPG (jpg)')
        cmds.menuItem('bakeTextureSequence_fileFormatIffMI', label='Maya IFF (iff)')
        cmds.menuItem('bakeTextureSequence_fileFormatPsdMI', label='PSD (psd)')
        cmds.menuItem('bakeTextureSequence_fileFormatSgiMI', label='SGI (sgi)')
        cmds.menuItem('bakeTextureSequence_fileFormatTgaMI', label='Targa (tga)')
        cmds.menuItem('bakeTextureSequence_fileFormatTifMI', label='Tiff (tif)')           
    elif mayaOrMr == 2:
        #cmds.intSliderGrp('bakeTextureSequence_paddingFSG', e=1, en=0, visible=0)
        #cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', e=1, en=0, visible=0)
        cmds.deleteUI('bakeTextureSequence_fileFormatOMG', control=1)
        cmds.optionMenuGrp('bakeTextureSequence_fileFormatOMG', label='file format: ', columnWidth=(2, 80), p='bakeTextureSequence_bakeOptionsForm')
        cmds.menuItem('bakeTextureSequence_fileFormatJpgMI', label='JEPG (jpg)')
        cmds.menuItem('bakeTextureSequence_fileFormatIffMI', label='Maya IFF (iff)')
        cmds.menuItem('bakeTextureSequence_fileFormatTgaMI', label='Targa (tga)')
        cmds.menuItem('bakeTextureSequence_fileFormatTifMI', label='Tiff (tif)') 
        
    cmds.formLayout('bakeTextureSequence_bakeOptionsForm',  e=1, 
    attachForm=[
    ('bakeTextureSequence_bakeTypeRBG', 'top', 8),
    ('bakeTextureSequence_bakeTypeRBG', 'left', 0),    
    ('bakeTextureSequence_maintainCB', 'left', 95),
    ('bakeTextureSequence_xResFSG', 'left', 0),
    ('bakeTextureSequence_xResFSG', 'right', 10),
    ('bakeTextureSequence_yResFSG', 'left', 0),
    ('bakeTextureSequence_yResFSG', 'right', 10),
    ('bakeTextureSequence_fileFormatOMG', 'left', 0),
    ('bakeTextureSequence_fileFormatOMG', 'right', 10),
    ('bakeTextureSequence_browserFBG', 'left', 0),
    ('bakeTextureSequence_browserFBG', 'right', 5),
    ('bakeTextureSequence_paddingFSG', 'left', 0),
    ('bakeTextureSequence_paddingFSG', 'right', 10),
    ('bakeTextureSequence_prefixTFG', 'left', 0),
    ('bakeTextureSequence_renameCB', 'left', 95),
    ('bakeTextureSequence_renameTFG', 'left', 0)
    ],
    attachControl=[
    ('bakeTextureSequence_maintainCB', 'top', 15, 'bakeTextureSequence_bakeTypeRBG'),
    ('bakeTextureSequence_xResFSG', 'top', 3, 'bakeTextureSequence_maintainCB'),
    ('bakeTextureSequence_yResFSG', 'top', 1, 'bakeTextureSequence_xResFSG'),
    ('bakeTextureSequence_fileFormatOMG', 'top', 5, 'bakeTextureSequence_yResFSG'),
    ('bakeTextureSequence_paddingFSG', 'top', 5, 'bakeTextureSequence_fileFormatOMG'),
    ('bakeTextureSequence_renameCB', 'top', 5, 'bakeTextureSequence_paddingFSG'),     
    ('bakeTextureSequence_renameTFG', 'top', 5, 'bakeTextureSequence_renameCB'), 
    ('bakeTextureSequence_prefixTFG', 'top', 5, 'bakeTextureSequence_renameTFG'),     
    ('bakeTextureSequence_browserFBG', 'top', 5, 'bakeTextureSequence_prefixTFG') 
    ])

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_mayaOrMR()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence_bake()

def bakeTextureSequence_bake():
    proc = 'bakeTextureSequence_bake'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    startTime = time.time()
    gMainProgressBar = maya.mel.eval('$tmp = $gMainProgressBar')
    isCancelled=0
    
#-------------------------------------------------------------------------------------------------------------
#bake the texture/shader
    isThereGeo = cmds.textScrollList('bakeTextureSequence_loadGeoTSL', q=1, numberOfItems=1)
    isThereTexture = cmds.textScrollList('bakeTextureSequence_loadTextureTSL', q=1, numberOfItems=1)

    if isThereGeo == 0 or isThereTexture == 0:
        cmds.error('both geo and a texture/shader must be loaded first')

    geometry = cmds.textScrollList('bakeTextureSequence_loadGeoTSL', q=1, ai=1)
    shader = cmds.textScrollList('bakeTextureSequence_loadTextureTSL', q=1, ai=1)

    startFrame = cmds.intField('bakeTextureSequence_startIF', q=1, value=1)
    endFrame = cmds.intField('bakeTextureSequence_endIF', q=1, value=1)
    byFrame = cmds.intField('bakeTextureSequence_byFrameIF', q=1, value=1)
    currentFrameOnly = cmds.checkBox('bakeTextureSequence_currentFrameCB', q=1, value=1)

    bakeType = cmds.radioButtonGrp('bakeTextureSequence_bakeTypeRBG', q=1, select=1)    
    xRes = cmds.intSliderGrp('bakeTextureSequence_xResFSG', q=1, value=1)    
    yRes = cmds.intSliderGrp('bakeTextureSequence_yResFSG', q=1, value=1) 
    padding = cmds.intSliderGrp('bakeTextureSequence_paddingFSG', q=1, value=1) 
    prefix = cmds.textFieldGrp('bakeTextureSequence_prefixTFG', q=1, text=1)
    doRename = cmds.checkBox('bakeTextureSequence_renameCB', q=1, value=1)
    rename = cmds.textFieldGrp('bakeTextureSequence_renameTFG', q=1, text=1)    
    
    formatDic={'JEPG (jpg)':'jpg','Maya IFF (iff)':'maya', 'PSD (psd)':'psd', 'SGI (sgi)':'sgi', 'Targa (tga)':'tga', 'Tiff (tif)':'tif'}
    formatDicMR={'JEPG (jpg)':3,'Maya IFF (iff)':2, 'Targa (tga)':6, 'Tiff (tif)':1}
    fileFormats = cmds.optionMenuGrp('bakeTextureSequence_fileFormatOMG', q=1, value=1)
    fileFormat = formatDic[fileFormats]
    fileFormatMR = formatDicMR[fileFormats]

    formatExt = fileFormat
    if formatExt == 'maya':
        formatExt = 'iff'

    outputDir = cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', q=1, text=1)
 
    bakingText = 'Baking Texture/Shader...(Press ESC To Cancel)'
     
#if mr...open options ui and set bases on bake ui
    if bakeType == 2:
        bakingText = 'Baking Texture/Shader...(ESC will NOT Cancel due to mental ray process)'
        
        if cmds.window('OptionBoxWindow', exists=1)==1:
            cmds.deleteUI('OptionBoxWindow')
            
        maya.mel.eval('mrBakeToVertices 1')

        parent = cmds.formLayout('prelightMentalRayOptions')
        commandName = 'mrBake'
        callback = (commandName + 'Callback')
        command = (callback + ' ' +  parent + ' 1')

        #reset default
        maya.mel.eval("mrBakeSetup " + parent + " 1;")

        #set ui 
        cmds.optionMenuGrp('textureBakeColorModeCtrl', e=1, select=1)
        maya.mel.eval('textureBakeSetOverrideCtrlChanged("textureBakeColorMode");')

        cmds.checkBoxGrp('useBakeSetOverrideCtrl', e=1, v1=1)
        maya.mel.eval('useBakeSetOverrideChanged("' + parent + '" );')

        cmds.textFieldGrp('prefixCtrl', e=1, text=prefix)
        maya.mel.eval('textureBakeSetOverrideCtrlChanged("prefix");')

        cmds.intSliderGrp('xResolutionCtrl', e=1, value=xRes)
        maya.mel.eval('textureBakeSetOverrideCtrlChanged("xResolution");')

        cmds.intSliderGrp('yResolutionCtrl', e=1, value=yRes)
        maya.mel.eval('textureBakeSetOverrideCtrlChanged("yResolution");')

        cmds.optionMenuGrp('fileFormatCtrl', e=1, select=fileFormatMR)
        maya.mel.eval('textureBakeSetOverrideCtrlChanged("fileFormat");')

#progress bar
    progressAmount = int(endFrame-startFrame)
    if currentFrameOnly == 1:
        progressAmount=1
    cmds.progressBar('bakeTextureSequence_progBar', e=1, maxValue=progressAmount)
    cmds.text('bakeTextureSequence_cancelTxt', e=1, label=bakingText) 
    cmds.progressBar('bakeTextureSequence_progBar', e=1, progress=0)
    cmds.progressBar(gMainProgressBar, edit=1, beginProgress=1, isInterruptable=1, status='Baking Texture/Shader......', maxValue=progressAmount)
    
#current frame only
    if currentFrameOnly == 1:
        numberExt = ''
        currentFrame = int(cmds.currentTime(q=1)) 
        currentFrameSize = len(str(currentFrame))
        negative = 0
        if currentFrame < 0:
            currentFrameStr = str(currentFrame)
            currentFrameStr = currentFrameStr.replace('-', '')
            currentFrame = int(currentFrameStr)
            currentFrameSize = len(str(currentFrame))
            negative = 1
            
        if currentFrameSize < padding:
            pad = padding-currentFrameSize
            i = 1
            while i <= pad:
                numberExt += '0'
                i+=1
                
        numberExt += str(currentFrame)
        if negative == 1:
            numberExt = '-' + numberExt
            
    #maya
        if bakeType == 1:
            for eachGeo in geometry:
                geoCleanName = eachGeo.replace(':', '_')
                shaderCleanName = shader[0]
                shaderCleanName = shaderCleanName.replace(':', '_')
                
                imageName = (prefix + geoCleanName + '_' + shaderCleanName + '.' + numberExt + '.' + formatExt)
                if doRename == 1:
                    imageName = (prefix + rename + '.' + numberExt + '.' + formatExt)
                    
                imageDir = (outputDir + '/' + imageName)
                file = cmds.convertSolidTx(shader, eachGeo, antiAlias=0, bm=1, fts=1, sp=0, sh=0, alpha=0, doubleSided=0, componentRange=0, resolutionX=xRes, resolutionY=xRes, fileFormat=fileFormat, fileImageName=imageDir)
                cmds.delete(file)
    #mental ray
        else:
            for eachGeo in geometry:
                geoCleanName = eachGeo.replace(':', '_')
                shaderCleanName = shader[0]
                shaderCleanName = shaderCleanName.replace(':', '_')
                
                mrDir = maya.mel.eval('miGetRootDir')
                mrDir += 'lightMap/'
                currentFolderFiles = []
                currentFolderFiles = cmds.getFileList(folder=mrDir)
                
                cmds.select(eachGeo, shader[0], r=1)
                maya.mel.eval(command)
                cmds.undo()                

                newFolderFiles = cmds.getFileList(folder=mrDir)
                newFileSet = set(newFolderFiles) - set(currentFolderFiles)
                newFile = list(newFileSet) 
                if '.mayaSwatches' in newFile:
                    newFile.remove('.mayaSwatches') 
                    
                if len(newFile) > 0:
                    newOutputDir = mrDir + newFile[0]
                    renameNewFile = newFile[0].split('.')
                    imageName = (prefix + geoCleanName + '_' + shaderCleanName + '.' + numberExt + '.' + renameNewFile[1])
                    if doRename == 1:
                        imageName = (prefix + rename + '.' + numberExt + '.' + renameNewFile[1])
                    
                    imageDir = (outputDir + '/' + imageName)
                    folderExists = cmds.file(outputDir, q=1, ex=1)
                    if folderExists==1:
                        cmds.sysFile(newOutputDir, rename=imageDir)
                    else:
                        print(newOutputDir + ' doesnt exist')

        #progress bar    
            cmds.progressBar('bakeTextureSequence_progBar', e=1, step=1)
            cmds.progressBar(gMainProgressBar, edit=1, step=1)        
#sequence        
    else:
        for t in range(startFrame,endFrame+1,byFrame):
            numberExt = ''
            cmds.currentTime(t, e=1)
            currentFrame = t
            currentFrameSize = len(str(currentFrame))
            negative = 0
            
            if currentFrame < 0:
                currentFrameStr = str(currentFrame)
                currentFrameStr = currentFrameStr.replace('-', '')
                currentFrame = int(currentFrameStr)
                currentFrameSize = len(str(currentFrame))
                negative = 1
                
            if currentFrameSize < padding:
                pad = padding-currentFrameSize
                i = 1
                while i <= pad:
                    numberExt += '0'
                    i+=1
                    
            numberExt += str(currentFrame)
            if negative == 1:
                numberExt = '-' + numberExt
            
        #maya
            if bakeType == 1:
                for eachGeo in geometry:
                    geoCleanName = eachGeo.replace(':', '_')
                    shaderCleanName = shader[0]
                    shaderCleanName = shaderCleanName.replace(':', '_')
                    
                    imageName = (prefix + geoCleanName + '_' + shaderCleanName + '.' + numberExt + '.' + formatExt)
                    if doRename == 1:
                        imageName = (prefix + rename + '.' + numberExt + '.' + formatExt)
                    
                    imageDir = (outputDir + '/' + imageName)
                    file = cmds.convertSolidTx(shader, eachGeo, antiAlias=0, bm=1, fts=1, sp=0, sh=0, alpha=0, doubleSided=0, componentRange=0, resolutionX=xRes, resolutionY=xRes, fileFormat=fileFormat, fileImageName=imageDir)
                    cmds.delete(file)
        #mental ray
            else:
                for eachGeo in geometry:
                    geoCleanName = eachGeo.replace(':', '_')
                    shaderCleanName = shader[0]
                    shaderCleanName = shaderCleanName.replace(':', '_')
                    
                    mrDir = maya.mel.eval('miGetRootDir')
                    mrDir += 'lightMap/'
                    currentFolderFiles = []
                    currentFolderFiles = cmds.getFileList(folder=mrDir)
                    
                    cmds.select(eachGeo, shader[0], r=1)
                    maya.mel.eval(command)
                    cmds.undo()                

                    newFolderFiles = cmds.getFileList(folder=mrDir)
                    newFileSet = set(newFolderFiles) - set(currentFolderFiles)
                    newFile = list(newFileSet) 
                    if '.mayaSwatches' in newFile:
                        newFile.remove('.mayaSwatches') 
                        
                    if len(newFile) > 0:
                        newOutputDir = mrDir + newFile[0]
                        renameNewFile = newFile[0].split('.')
                        imageName = (prefix + geoCleanName + '_' + shaderCleanName + '.' + numberExt + '.' + renameNewFile[1])
                        if doRename == 1:
                            imageName = (prefix + rename + '.' + numberExt + '.' + renameNewFile[1])
                        
                        imageDir = (outputDir + '/' + imageName)
                        folderExists = cmds.file(outputDir, q=1, ex=1)
                        if folderExists==1:
                            cmds.sysFile(newOutputDir, rename=imageDir)
                        else:
                            print(newOutputDir + ' doesnt exist')
                    
        #progress bar update or cancel
            if cmds.progressBar(gMainProgressBar, q=1, isCancelled=1):
                isCancelled=1
                cmds.progressBar('bakeTextureSequence_progBar', e=1, progress=0)
                cmds.text('bakeTextureSequence_cancelTxt', e=1, label='')          
                break

            cmds.progressBar('bakeTextureSequence_progBar', e=1, step=1)
            cmds.progressBar(gMainProgressBar, edit=1, step=1)            

#timer
    endTime = time.time()
    totalTime =  (endTime - startTime)
    timeStr = ' seconds'
    if totalTime > 60:
        totalTime /= 60
        timeStr = ' minutes'

    if isCancelled == 0:    
        cmds.text('bakeTextureSequence_cancelTxt', e=1, label='Total Time: ' + str(totalTime) + timeStr)
    else: 
        cmds.text('bakeTextureSequence_cancelTxt', e=1, label='Cancelled -- Total Time: ' + str(totalTime) + timeStr)
    
#progress bar end
    cmds.progressBar('bakeTextureSequence_progBar', e=1, progress=0)
    cmds.progressBar(gMainProgressBar, edit=1, endProgress=1)
    
#close mr options win if open
    if cmds.window('OptionBoxWindow', exists=1)==1:
        cmds.deleteUI('OptionBoxWindow')    

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence_bake()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

#*************************************************************************************************************
#*start bakeTextureSequence()

def bakeTextureSequence():
    proc = 'bakeTextureSequence'
    printString = '\n\n////////////////////////////////////////////////////////////////////////////////////////////\n'
    printString += ('// ' + proc + ' details: \n//\n')
    #startTime = time.time()

#-------------------------------------------------------------------------------------------------------------
#window creation
    if cmds.window('bakeTextureSequence_win', exists=1)==1:
        cmds.deleteUI('bakeTextureSequence_win')

    cmds.window('bakeTextureSequence_win', title="Bake Texture Sequence  --  Maya or Mental Ray", resizeToFitChildren=1, maximizeButton=0, sizeable=1)
    cmds.formLayout('bakeTextureSequence_mainForm')     
    cmds.columnLayout('bakeTextureSequence_mainCol', adj=1, p='bakeTextureSequence_mainForm')
    cmds.progressBar('bakeTextureSequence_progBar', maxValue=100, h=10, p='bakeTextureSequence_mainForm')
    cmds.text('bakeTextureSequence_cancelTxt', font='tinyBoldLabelFont', label='', align='center', w=60, p='bakeTextureSequence_mainForm') 
    cmds.button('bakeTextureSequence_executeButton', l='Bake', c='bakeTextureSequence_bake()', h=10, p='bakeTextureSequence_mainForm') 

#load geo and texture frameLayout     
    cmds.frameLayout('bakeTextureSequence_loadGeoFrame', l='Load Geo & Texture', marginHeight=5, collapsable=1, collapse=0, borderStyle='etchedIn', p='bakeTextureSequence_mainCol')
    cmds.formLayout('bakeTextureSequence_loadGeoForm', p='bakeTextureSequence_loadGeoFrame')
    cmds.textScrollList('bakeTextureSequence_loadGeoTSL', numberOfRows=6, ann='double-click to remove or hit the delete key', dkc='remove = cmds.textScrollList(\'bakeTextureSequence_loadGeoTSL\', q=1, selectItem=1);cmds.textScrollList(\'bakeTextureSequence_loadGeoTSL\', e=1, ri=remove)', dcc='remove = cmds.textScrollList(\'bakeTextureSequence_loadGeoTSL\', q=1, selectItem=1);cmds.textScrollList(\'bakeTextureSequence_loadGeoTSL\', e=1, ri=remove)', p='bakeTextureSequence_loadGeoForm')
    cmds.textScrollList('bakeTextureSequence_loadTextureTSL', numberOfRows=6, ann='double-click to remove or hit the delete key', dkc='remove = cmds.textScrollList(\'bakeTextureSequence_loadTextureTSL\', q=1, selectItem=1);cmds.textScrollList(\'bakeTextureSequence_loadTextureTSL\', e=1, ri=remove)', dcc='remove = cmds.textScrollList(\'bakeTextureSequence_loadTextureTSL\', q=1, selectItem=1);cmds.textScrollList(\'bakeTextureSequence_loadTextureTSL\', e=1, ri=remove)', p='bakeTextureSequence_loadGeoForm')
    cmds.button('bakeTextureSequence_loadGeoButton', l='load geo', w=100, h=30, c='bakeTextureSequence_loadGeo()', p='bakeTextureSequence_loadGeoForm')
    cmds.button('bakeTextureSequence_loadTextureButton', l='load texture/shader', w=80, h=30, c='bakeTextureSequence_loadTexture()', p='bakeTextureSequence_loadGeoForm')
    
    cmds.formLayout('bakeTextureSequence_loadGeoForm',  e=1, 
    attachForm=[
    ('bakeTextureSequence_loadGeoButton', 'top', 5),
    ('bakeTextureSequence_loadGeoButton', 'left', 20),
    ('bakeTextureSequence_loadTextureButton', 'top', 5),
    ('bakeTextureSequence_loadTextureButton', 'right', 20),
    ('bakeTextureSequence_loadGeoTSL', 'bottom', 5),
    ('bakeTextureSequence_loadGeoTSL', 'left', 20),
    ('bakeTextureSequence_loadTextureTSL', 'bottom', 5),
    ('bakeTextureSequence_loadTextureTSL', 'right', 20)
    ],
    
    attachPosition=[
    ('bakeTextureSequence_loadGeoButton', 'right', 0, 48),
    ('bakeTextureSequence_loadTextureButton', 'left', 0, 52),
    ('bakeTextureSequence_loadGeoTSL', 'right', 0, 48),
    ('bakeTextureSequence_loadTextureTSL', 'left', 0, 52)   
    ],
    attachControl=[                  
    ('bakeTextureSequence_loadGeoTSL', 'top', 5, 'bakeTextureSequence_loadGeoButton'),
    ('bakeTextureSequence_loadTextureTSL', 'top', 5, 'bakeTextureSequence_loadTextureButton')
    ])

#frameRange frameLayout 
    cmds.frameLayout('bakeTextureSequence_frameRangeFrame', l='Frame Range Options', marginHeight=5, collapsable=1, collapse=0, borderStyle='etchedIn', p='bakeTextureSequence_mainCol')
    cmds.formLayout('bakeTextureSequence_frameRangeForm', p='bakeTextureSequence_frameRangeFrame')
    cmds.button('bakeTextureSequence_timeButton', l='time', w=35, h=35, c='cmds.intField(\'bakeTextureSequence_startIF\', e=1, value=cmds.playbackOptions(q=1, min=1));cmds.intField(\'bakeTextureSequence_endIF\', e=1, value=cmds.playbackOptions(q=1, max=1))', p='bakeTextureSequence_frameRangeForm')
    cmds.text('bakeTextureSequence_startFrameTxt', l='Start Frame:', w=65, p='bakeTextureSequence_frameRangeForm')
    cmds.text('bakeTextureSequence_endFrameTxt', l='End Frame:', w=65, p='bakeTextureSequence_frameRangeForm')
    cmds.intField('bakeTextureSequence_startIF', value=cmds.playbackOptions(q=1, min=1), editable=1, w=60, p='bakeTextureSequence_frameRangeForm')
    cmds.intField('bakeTextureSequence_endIF', value=cmds.playbackOptions(q=1, max=1), editable=1, w=60, p='bakeTextureSequence_frameRangeForm')
    cmds.checkBox('bakeTextureSequence_currentFrameCB', l='Current Frame Only', value=0, align='left', p='bakeTextureSequence_frameRangeForm')
    cmds.text('bakeTextureSequence_byFrameTxt', l='By Frame:', w=65, p='bakeTextureSequence_frameRangeForm')
    cmds.intField('bakeTextureSequence_byFrameIF', value=1, editable=1, w=60, p='bakeTextureSequence_frameRangeForm')

    cmds.formLayout('bakeTextureSequence_frameRangeForm',  e=1,
    attachForm=[
    ('bakeTextureSequence_timeButton', 'top', 8),
    ('bakeTextureSequence_timeButton', 'left', 80),
    ('bakeTextureSequence_startFrameTxt', 'top', 5),
    ('bakeTextureSequence_startIF', 'top', 2),
    ('bakeTextureSequence_currentFrameCB', 'top', 6)
    ],
    attachControl=[
    ('bakeTextureSequence_startFrameTxt', 'left', 30, 'bakeTextureSequence_timeButton'),
    ('bakeTextureSequence_endFrameTxt', 'top', 10, 'bakeTextureSequence_startFrameTxt'),
    ('bakeTextureSequence_endFrameTxt', 'left', 30, 'bakeTextureSequence_timeButton'),
    ('bakeTextureSequence_startIF', 'left', 5, 'bakeTextureSequence_startFrameTxt'),
    ('bakeTextureSequence_endIF', 'top', 4, 'bakeTextureSequence_startIF'),
    ('bakeTextureSequence_endIF', 'left', 5, 'bakeTextureSequence_endFrameTxt'),
    ('bakeTextureSequence_currentFrameCB', 'left', 65, 'bakeTextureSequence_startIF'),
    ('bakeTextureSequence_byFrameTxt', 'top', 8, 'bakeTextureSequence_currentFrameCB'),
    ('bakeTextureSequence_byFrameTxt', 'left', 60, 'bakeTextureSequence_startIF'),
    ('bakeTextureSequence_byFrameIF', 'top', 5, 'bakeTextureSequence_currentFrameCB'),
    ('bakeTextureSequence_byFrameIF', 'left', 2, 'bakeTextureSequence_byFrameTxt')    
    ])
    
#bake options frameLayout 
    cmds.frameLayout('bakeTextureSequence_bakeOptionsFrame', l='Bake Options', marginHeight=5, collapsable=1, collapse=0, borderStyle='etchedIn', p='bakeTextureSequence_mainCol')
    cmds.formLayout('bakeTextureSequence_bakeOptionsForm', p='bakeTextureSequence_bakeOptionsFrame')
    cmds.radioButtonGrp('bakeTextureSequence_bakeTypeRBG', columnWidth=[2, 80], adjustableColumn=1, select=1, label='Bake Type:               ', cc='bakeTextureSequence_mayaOrMR()', labelArray2=['Maya', 'Mental Ray'], numberOfRadioButtons=2, p='bakeTextureSequence_bakeOptionsForm')    
    cmds.checkBox('bakeTextureSequence_maintainCB', l='Maintain x/y ratio', value=1, onc='cmds.intSliderGrp(\'bakeTextureSequence_yResFSG\',e=1, enable=0);bakeTextureSequence_maintain()', ofc='cmds.intSliderGrp(\'bakeTextureSequence_yResFSG\',e=1, enable=1)', align='left', p='bakeTextureSequence_bakeOptionsForm')
    cmds.intSliderGrp('bakeTextureSequence_xResFSG', label='X resolution: ', field=True, minValue=1, maxValue=4096, value=512, step=1, cc='bakeTextureSequence_maintain()', dc='bakeTextureSequence_maintain()', p='bakeTextureSequence_bakeOptionsForm')    
    cmds.intSliderGrp('bakeTextureSequence_yResFSG', label='Y resolution: ', field=True, minValue=1, maxValue=4096, value=512, step=1, enable=0, p='bakeTextureSequence_bakeOptionsForm')
    cmds.optionMenuGrp('bakeTextureSequence_fileFormatOMG', label='File format: ', columnWidth=(2, 80), p='bakeTextureSequence_bakeOptionsForm')
    cmds.menuItem('bakeTextureSequence_fileFormatJpgMI', label='JEPG (jpg)')
    cmds.menuItem('bakeTextureSequence_fileFormatIffMI', label='Maya IFF (iff)')
    cmds.menuItem('bakeTextureSequence_fileFormatPsdMI', label='PSD (psd)')
    cmds.menuItem('bakeTextureSequence_fileFormatSgiMI', label='SGI (sgi)')
    cmds.menuItem('bakeTextureSequence_fileFormatTgaMI', label='Targa (tga)')
    cmds.menuItem('bakeTextureSequence_fileFormatTifMI', label='Tiff (tif)')
    cmds.intSliderGrp('bakeTextureSequence_paddingFSG', label='Padding: ', field=True, minValue=0, maxValue=10, value=4, step=1, p='bakeTextureSequence_bakeOptionsForm')
    cmds.textFieldGrp('bakeTextureSequence_prefixTFG', label='Prefix: ', text='', p='bakeTextureSequence_bakeOptionsForm' )
    cmds.checkBox('bakeTextureSequence_renameCB', l='Rename   --   (default name will be: "objectName_textureName.#.ext")', value=0, onc='cmds.textFieldGrp(\'bakeTextureSequence_renameTFG\',e=1, enable=1)', ofc='cmds.textFieldGrp(\'bakeTextureSequence_renameTFG\',e=1, enable=0)', align='left', p='bakeTextureSequence_bakeOptionsForm')
    cmds.textFieldGrp('bakeTextureSequence_renameTFG', label='New Name: ', text='', enable=0, p='bakeTextureSequence_bakeOptionsForm' )
    cmds.textFieldButtonGrp('bakeTextureSequence_browserFBG', columnWidth=[2, 200], adjustableColumn=2, label='Output Directory: ', buttonLabel='Browser', buttonCommand='bakeTextureSequence_browser()', p='bakeTextureSequence_bakeOptionsForm')
    
    cmds.formLayout('bakeTextureSequence_bakeOptionsForm',  e=1, 
    attachForm=[
    ('bakeTextureSequence_bakeTypeRBG', 'top', 8),
    ('bakeTextureSequence_bakeTypeRBG', 'left', 0),    
    ('bakeTextureSequence_maintainCB', 'left', 95),
    ('bakeTextureSequence_xResFSG', 'left', 0),
    ('bakeTextureSequence_xResFSG', 'right', 10),
    ('bakeTextureSequence_yResFSG', 'left', 0),
    ('bakeTextureSequence_yResFSG', 'right', 10),
    ('bakeTextureSequence_fileFormatOMG', 'left', 0),
    ('bakeTextureSequence_fileFormatOMG', 'right', 10),
    ('bakeTextureSequence_browserFBG', 'left', 0),
    ('bakeTextureSequence_browserFBG', 'right', 5),
    ('bakeTextureSequence_paddingFSG', 'left', 0),
    ('bakeTextureSequence_paddingFSG', 'right', 10),
    ('bakeTextureSequence_prefixTFG', 'left', 0),
    ('bakeTextureSequence_renameCB', 'left', 95),
    ('bakeTextureSequence_renameTFG', 'left', 0)
    ],
    attachControl=[
    ('bakeTextureSequence_maintainCB', 'top', 15, 'bakeTextureSequence_bakeTypeRBG'),
    ('bakeTextureSequence_xResFSG', 'top', 3, 'bakeTextureSequence_maintainCB'),
    ('bakeTextureSequence_yResFSG', 'top', 1, 'bakeTextureSequence_xResFSG'),
    ('bakeTextureSequence_fileFormatOMG', 'top', 5, 'bakeTextureSequence_yResFSG'),
    ('bakeTextureSequence_paddingFSG', 'top', 5, 'bakeTextureSequence_fileFormatOMG'),
    ('bakeTextureSequence_renameCB', 'top', 5, 'bakeTextureSequence_paddingFSG'),     
    ('bakeTextureSequence_renameTFG', 'top', 5, 'bakeTextureSequence_renameCB'), 
    ('bakeTextureSequence_prefixTFG', 'top', 5, 'bakeTextureSequence_renameTFG'),     
    ('bakeTextureSequence_browserFBG', 'top', 5, 'bakeTextureSequence_prefixTFG') 
    ])   
    
    
    
#edit mainForm
    cmds.formLayout('bakeTextureSequence_mainForm', e=1, 
    attachForm=[
    ('bakeTextureSequence_mainCol', 'top', 0),
    ('bakeTextureSequence_mainCol', 'left', 0),
    ('bakeTextureSequence_mainCol', 'right', 0),
    ('bakeTextureSequence_mainCol', 'bottom', 80),
    ('bakeTextureSequence_cancelTxt', 'left', 5),
    ('bakeTextureSequence_cancelTxt', 'right', 5),
    ('bakeTextureSequence_cancelTxt', 'bottom', 60),    
    ('bakeTextureSequence_progBar', 'left', 5),
    ('bakeTextureSequence_progBar', 'right', 5),
    ('bakeTextureSequence_progBar', 'bottom', 40),
    ('bakeTextureSequence_executeButton', 'left', 5),
    ('bakeTextureSequence_executeButton', 'right', 5),
    ('bakeTextureSequence_executeButton', 'bottom', 2)
    ],
    attachControl=[
    ('bakeTextureSequence_cancelTxt', 'top', 5, 'bakeTextureSequence_mainCol'),
    ('bakeTextureSequence_progBar', 'top', 5, 'bakeTextureSequence_cancelTxt'),
    ('bakeTextureSequence_executeButton', 'top', 5, 'bakeTextureSequence_progBar')
    ])  
    
#show and resize window        
    cmds.showWindow('bakeTextureSequence_win')  
    cmds.window('bakeTextureSequence_win', e=1, wh=[600,630]) 

#run some functions  
    bakeTextureSequence_outputDir()

#-------------------------------------------------------------------------------------------------------------
#print
    #endTime = time.time()
    #totalTime =  endTime - startTime
    #printString += '// total time: ' + str(totalTime) + ' seconds\n'
    printString += '////////////////////////////////////////////////////////////////////////////////////////////\n\n'
    #print printString
    #print ('COMPLETE -- check script editor for details...\n')

#*************************************************************************************************************
#*end bakeTextureSequence()

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
