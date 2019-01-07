### Export Texture Sequences
### Scipt based on Bake Texture script by Kiel Gnebba released 2010
### I do not own the script

### ---- HOW TO USE ---- ###
### Select mesh and run script ###

import maya.cmds as mc

shader = 'CHM003_L_eye_mat' ## change shader name
geo = mc.ls( sl = True )

name = 'l_eye' ## change name for the texutre files
shaderName = 'diffuse' ## change type of texture 
outputDir = 'C:/Users/kphan/Desktop/textureEyes' ## change output dir && change \ to /

resX = 512
rexY = 512
fileFormat = 'jpg'
padding = 4

##function starts here

for t in range(1,81,1):
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
    for eachGeo in geo:                
        imageName = (name + '_' + shaderName + '.' + numberExt + '.' + fileFormat)
        imageDir = (outputDir + '/' + imageName)
        file = mc.convertSolidTx(shader, eachGeo, antiAlias=1, bm=1, fts=1, sp=0, sh=0, alpha=0, doubleSided=0, componentRange=0, resolutionX=resX, resolutionY=rexY, fileFormat=fileFormat, fileImageName=imageDir)
        cmds.delete(file)