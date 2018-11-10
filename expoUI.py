import maya.cmds as mc
import maya.mel as mel

def HammerVisOn(*args):
    hammer = mc.select("hammer_geo")
    hams = mc.ls( sl=True )
    for ham in hams:
        
        mc.setAttr(ham + '.visibility', 1)
    
def HammerVisOff(*args):
    hammer = mc.select('hammer_geo')
    hams = mc.ls(sl=True)
    
    for ham in hams:
        
        mc.setAttr(ham + '.visibility', 0)
    
def LoadDance(*args):
    
    mc.playbackOptions(minTime = 1, maxTime = 200)
    ResetAnim(*args)
    danceSet = mc.select("AllAnimatableControls")
    mel.eval('source "D:/kyle/scripts/LoadAnim.mel"')
    mel.eval('LoadDance;')
    HammerVisOff(*args)

def LoadBuild(*args):
    
    mc.playbackOptions(minTime = 1, maxTime = 100)
    ResetAnim(*args)
    buildSet = mc.select("AllAnimatableControls")
    mel.eval('source "D:/kyle/scripts/LoadAnim.mel"')
    mel.eval('LoadBuild;')
    HammerVisOn(*args)
    
def LoadWalk(*args):
    
    mc.playbackOptions(minTime = 1, maxTime = 24)
    ResetAnim(*args)
    walkSet = mc.select("AllAnimatableControls")
    mel.eval('source "D:/kyle/scripts/LoadAnim.mel"')
    mel.eval('LoadWalk;')
    HammerVisOff(*args)

def ResetAnim(*args):
    
    HammerVisOff(*args)   
    set = mc.select("AllAnimatableControls")
    controls = mc.ls( sl = True)    
    for ctrl in controls:
        ## delete keyframes
        mc.cutKey(ctrl)
        ## custom attribute
        if (ctrl == 'l_leg_ctrl' or ctrl == 'r_leg_ctrl'):
            mc.setAttr(ctrl + '.toeCurl', 0)
            mc.setAttr(ctrl + '.roll', 0)
        if (ctrl == 'jawSync_ctrl'):
            mc.setAttr(ctrl + '.phoneticM', 0)
            mc.setAttr(ctrl + '.pucker', 0)
        if (ctrl == 'l_upperEyelid_ctrl' or ctrl == 'r_upperEyelid_ctrl'):
            mc.setAttr(ctrl + '.blink', 0)      
        if (ctrl == 'master_eyebrow_ctrl'):
            mc.setAttr(ctrl + '.squeeze', 0) 
        ## translate and rotate    
        if (mc.getAttr(ctrl + '.translateX', lock = True) == True and mc.getAttr(ctrl + '.translateY', lock = True) == True and mc.getAttr(ctrl + '.translateZ', lock = True) == True):
            mc.setAttr(ctrl + '.rotateX', 0)
            mc.setAttr(ctrl + '.rotateY', 0)
            mc.setAttr(ctrl + '.rotateZ', 0)
        elif (mc.getAttr(ctrl + '.rotateX', lock = True) == True and mc.getAttr(ctrl + '.rotateY', lock = True) == True and mc.getAttr(ctrl + '.rotateZ', lock = True) == True):
            mc.setAttr(ctrl + '.translateX', 0)
            mc.setAttr(ctrl + '.translateY', 0)
            mc.setAttr(ctrl + '.translateZ', 0)
        else:
            mc.setAttr(ctrl + '.translateX', 0)
            mc.setAttr(ctrl + '.translateY', 0)
            mc.setAttr(ctrl + '.translateZ', 0)
            mc.setAttr(ctrl + '.rotateX', 0)
            mc.setAttr(ctrl + '.rotateY', 0)
            mc.setAttr(ctrl + '.rotateZ', 0)    

## window UI starts here
windowID = 'exposureUI'
MAIN_PANE = mel.eval('$gViewportWorkspaceControl=$gViewportWorkspaceControl')
if mc.window( windowID, exists = True ):
    mc.deleteUI(windowID)

mc.window( windowID, title = 'Exposure UI' )

mc.columnLayout()

mc.text(label = 'Click Reset button before animating')
mc.button( label = 'Reset Animation', command = ResetAnim)
mc.text(label = 'Load animation preset ( Hit Play button afterwards )')

mc.rowColumnLayout( nr = 1, cs = (1,5))

mc.button( label = 'Dance animation', command = LoadDance)

mc.button( label = 'Build animation', command = LoadBuild)

mc.button( label = 'Walk animation', command = LoadWalk)

mc.dockControl( aa = 'all', area = 'top', content = 'exposureUI', label = 'Exposure UI', fw = False, fh = False)
mc.showWindow()    
    
    