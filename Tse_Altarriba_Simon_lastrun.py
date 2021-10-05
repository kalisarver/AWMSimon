#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Mar  3 14:03:59 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Tse_Altarriba_Simon'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Liory/Dropbox/Lectures/IoE/Dissertations/Computerised tsks/PsychoPy/Simon Task/Tse_Altarriba_Simon_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Initial_instruction"
Initial_instructionClock = core.Clock()
initialinstr = visual.TextStim(win=win, name='initialinstr',
    text='The experiment is about to begin.\nPress the space bar for the instructions.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space1 = keyboard.Keyboard()

# Initialize components for Routine "Expt_Instructions"
Expt_InstructionsClock = core.Clock()
exptinstr = visual.TextStim(win=win, name='exptinstr',
    text='On each trial, you will see an arrow.\nYour job is to decide which direction the arrow is pointing to.\nIf the arrow is pointing to the RIGHT, press M\nIf the arrow is pointing to the LEFT, press Z\nIgnore the location, just focus on the direction.\nWe will start with a few practice trials.\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='pink', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space2 = keyboard.Keyboard()

# Initialize components for Routine "PracticeFix"
PracticeFixClock = core.Clock()
imageFix = visual.ImageStim(
    win=win,
    name='imageFix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "PracticeTrials"
PracticeTrialsClock = core.Clock()
imagePractice = visual.ImageStim(
    win=win,
    name='imagePractice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg=''
Feedback_2 = visual.TextStim(win=win, name='Feedback_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='pink', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Begin_Experiment"
Begin_ExperimentClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Practice over. Are you ready to start the experiment?\nRemember to pay attention only to the direction that the arrow is pointing to!\nYou will not get feedback from now on.\nPress the space bar when you are ready.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space3 = keyboard.Keyboard()

# Initialize components for Routine "ExperimentFix"
ExperimentFixClock = core.Clock()
imageFixation = visual.ImageStim(
    win=win,
    name='imageFixation', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ExpTrials"
ExpTrialsClock = core.Clock()
imageTrials = visual.ImageStim(
    win=win,
    name='imageTrials', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Take a little break and press the space bar when you are ready to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space4 = keyboard.Keyboard()

# Initialize components for Routine "ExperimentFix"
ExperimentFixClock = core.Clock()
imageFixation = visual.ImageStim(
    win=win,
    name='imageFixation', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "ExpTrials"
ExpTrialsClock = core.Clock()
imageTrials = visual.ImageStim(
    win=win,
    name='imageTrials', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
TheEnd = visual.TextStim(win=win, name='TheEnd',
    text='All done. Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initial_instruction"-------
# update component parameters for each repeat
Space1.keys = []
Space1.rt = []
# keep track of which components have finished
Initial_instructionComponents = [initialinstr, Space1]
for thisComponent in Initial_instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Initial_instructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Initial_instruction"-------
while continueRoutine:
    # get current time
    t = Initial_instructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Initial_instructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initialinstr* updates
    if initialinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initialinstr.frameNStart = frameN  # exact frame index
        initialinstr.tStart = t  # local t and not account for scr refresh
        initialinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initialinstr, 'tStartRefresh')  # time at next scr refresh
        initialinstr.setAutoDraw(True)
    
    # *Space1* updates
    waitOnFlip = False
    if Space1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space1.frameNStart = frameN  # exact frame index
        Space1.tStart = t  # local t and not account for scr refresh
        Space1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space1, 'tStartRefresh')  # time at next scr refresh
        Space1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Space1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Space1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Space1.status == STARTED and not waitOnFlip:
        theseKeys = Space1.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Space1.keys = theseKeys.name  # just the last key pressed
            Space1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initial_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initial_instruction"-------
for thisComponent in Initial_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('initialinstr.started', initialinstr.tStartRefresh)
thisExp.addData('initialinstr.stopped', initialinstr.tStopRefresh)
# check responses
if Space1.keys in ['', [], None]:  # No response was made
    Space1.keys = None
thisExp.addData('Space1.keys',Space1.keys)
if Space1.keys != None:  # we had a response
    thisExp.addData('Space1.rt', Space1.rt)
thisExp.addData('Space1.started', Space1.tStartRefresh)
thisExp.addData('Space1.stopped', Space1.tStopRefresh)
thisExp.nextEntry()
# the Routine "Initial_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Expt_Instructions"-------
# update component parameters for each repeat
Space2.keys = []
Space2.rt = []
# keep track of which components have finished
Expt_InstructionsComponents = [exptinstr, Space2]
for thisComponent in Expt_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Expt_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Expt_Instructions"-------
while continueRoutine:
    # get current time
    t = Expt_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Expt_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exptinstr* updates
    if exptinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exptinstr.frameNStart = frameN  # exact frame index
        exptinstr.tStart = t  # local t and not account for scr refresh
        exptinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exptinstr, 'tStartRefresh')  # time at next scr refresh
        exptinstr.setAutoDraw(True)
    
    # *Space2* updates
    waitOnFlip = False
    if Space2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space2.frameNStart = frameN  # exact frame index
        Space2.tStart = t  # local t and not account for scr refresh
        Space2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space2, 'tStartRefresh')  # time at next scr refresh
        Space2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Space2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Space2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Space2.status == STARTED and not waitOnFlip:
        theseKeys = Space2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Space2.keys = theseKeys.name  # just the last key pressed
            Space2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Expt_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Expt_Instructions"-------
for thisComponent in Expt_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Space2.keys in ['', [], None]:  # No response was made
    Space2.keys = None
thisExp.addData('Space2.keys',Space2.keys)
if Space2.keys != None:  # we had a response
    thisExp.addData('Space2.rt', Space2.rt)
thisExp.addData('Space2.started', Space2.tStartRefresh)
thisExp.addData('Space2.stopped', Space2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Expt_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SimonPractice.xlsx'),
    seed=None, name='Practice_loop')
thisExp.addLoop(Practice_loop)  # add the loop to the experiment
thisPractice_loop = Practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in Practice_loop:
    currentLoop = Practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeFix"-------
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    imageFix.setImage('Fixation.jpeg')
    # keep track of which components have finished
    PracticeFixComponents = [imageFix]
    for thisComponent in PracticeFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracticeFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageFix* updates
        if imageFix.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            imageFix.frameNStart = frameN  # exact frame index
            imageFix.tStart = t  # local t and not account for scr refresh
            imageFix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageFix, 'tStartRefresh')  # time at next scr refresh
            imageFix.setAutoDraw(True)
        if imageFix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageFix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                imageFix.tStop = t  # not accounting for scr refresh
                imageFix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageFix, 'tStopRefresh')  # time at next scr refresh
                imageFix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeFix"-------
    for thisComponent in PracticeFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('imageFix.started', imageFix.tStartRefresh)
    Practice_loop.addData('imageFix.stopped', imageFix.tStopRefresh)
    
    # ------Prepare to start Routine "PracticeTrials"-------
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    imagePractice.setImage(ImageFile)
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    PracticeTrialsComponents = [imagePractice, key_resp]
    for thisComponent in PracticeTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "PracticeTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imagePractice* updates
        if imagePractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imagePractice.frameNStart = frameN  # exact frame index
            imagePractice.tStart = t  # local t and not account for scr refresh
            imagePractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imagePractice, 'tStartRefresh')  # time at next scr refresh
            imagePractice.setAutoDraw(True)
        if imagePractice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imagePractice.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                imagePractice.tStop = t  # not accounting for scr refresh
                imagePractice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imagePractice, 'tStopRefresh')  # time at next scr refresh
                imagePractice.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['m', 'z'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp.keys == []:  # then this was the first keypress
                    key_resp.keys = theseKeys.name  # just the first key pressed
                    key_resp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (key_resp.keys == str(CorrAns)) or (key_resp.keys == CorrAns):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeTrials"-------
    for thisComponent in PracticeTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('imagePractice.started', imagePractice.tStartRefresh)
    Practice_loop.addData('imagePractice.stopped', imagePractice.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_loop (TrialHandler)
    Practice_loop.addData('key_resp.keys',key_resp.keys)
    Practice_loop.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        Practice_loop.addData('key_resp.rt', key_resp.rt)
    Practice_loop.addData('key_resp.started', key_resp.tStartRefresh)
    Practice_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    
    # ------Prepare to start Routine "Feedback"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if not key_resp.keys :
        msg="Failed to respond"
    elif key_resp.corr:#stored on last run routine
        msg="Correct!"
    else:
        msg="Oops! That was wrong"
    Feedback_2.setText(msg)
    # keep track of which components have finished
    FeedbackComponents = [Feedback_2]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback_2* updates
        if Feedback_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Feedback_2.frameNStart = frameN  # exact frame index
            Feedback_2.tStart = t  # local t and not account for scr refresh
            Feedback_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback_2, 'tStartRefresh')  # time at next scr refresh
            Feedback_2.setAutoDraw(True)
        if Feedback_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Feedback_2.tStop = t  # not accounting for scr refresh
                Feedback_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback_2, 'tStopRefresh')  # time at next scr refresh
                Feedback_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('Feedback_2.started', Feedback_2.tStartRefresh)
    Practice_loop.addData('Feedback_2.stopped', Feedback_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice_loop'

# get names of stimulus parameters
if Practice_loop.trialList in ([], [None], None):
    params = []
else:
    params = Practice_loop.trialList[0].keys()
# save data for this loop
Practice_loop.saveAsExcel(filename + '.xlsx', sheetName='Practice_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Practice_loop.saveAsText(filename + 'Practice_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Begin_Experiment"-------
# update component parameters for each repeat
Space3.keys = []
Space3.rt = []
# keep track of which components have finished
Begin_ExperimentComponents = [text, Space3]
for thisComponent in Begin_ExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Begin_ExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Begin_Experiment"-------
while continueRoutine:
    # get current time
    t = Begin_ExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Begin_ExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *Space3* updates
    waitOnFlip = False
    if Space3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space3.frameNStart = frameN  # exact frame index
        Space3.tStart = t  # local t and not account for scr refresh
        Space3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space3, 'tStartRefresh')  # time at next scr refresh
        Space3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Space3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Space3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Space3.status == STARTED and not waitOnFlip:
        theseKeys = Space3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Space3.keys = theseKeys.name  # just the last key pressed
            Space3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Begin_ExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begin_Experiment"-------
for thisComponent in Begin_ExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Space3.keys in ['', [], None]:  # No response was made
    Space3.keys = None
thisExp.addData('Space3.keys',Space3.keys)
if Space3.keys != None:  # we had a response
    thisExp.addData('Space3.rt', Space3.rt)
thisExp.addData('Space3.started', Space3.tStartRefresh)
thisExp.addData('Space3.stopped', Space3.tStopRefresh)
thisExp.nextEntry()
# the Routine "Begin_Experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SimonStimuli.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ExperimentFix"-------
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    imageFixation.setImage('Fixation.jpeg')
    # keep track of which components have finished
    ExperimentFixComponents = [imageFixation]
    for thisComponent in ExperimentFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExperimentFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ExperimentFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ExperimentFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExperimentFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageFixation* updates
        if imageFixation.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            imageFixation.frameNStart = frameN  # exact frame index
            imageFixation.tStart = t  # local t and not account for scr refresh
            imageFixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageFixation, 'tStartRefresh')  # time at next scr refresh
            imageFixation.setAutoDraw(True)
        if imageFixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageFixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                imageFixation.tStop = t  # not accounting for scr refresh
                imageFixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageFixation, 'tStopRefresh')  # time at next scr refresh
                imageFixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExperimentFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ExperimentFix"-------
    for thisComponent in ExperimentFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('imageFixation.started', imageFixation.tStartRefresh)
    trials.addData('imageFixation.stopped', imageFixation.tStopRefresh)
    
    # ------Prepare to start Routine "ExpTrials"-------
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    imageTrials.setImage(ImageFile)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    ExpTrialsComponents = [imageTrials, key_resp_2]
    for thisComponent in ExpTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExpTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ExpTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ExpTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExpTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTrials* updates
        if imageTrials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrials.frameNStart = frameN  # exact frame index
            imageTrials.tStart = t  # local t and not account for scr refresh
            imageTrials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrials, 'tStartRefresh')  # time at next scr refresh
            imageTrials.setAutoDraw(True)
        if imageTrials.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrials.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                imageTrials.tStop = t  # not accounting for scr refresh
                imageTrials.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrials, 'tStopRefresh')  # time at next scr refresh
                imageTrials.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['m', 'z'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys.name  # just the first key pressed
                    key_resp_2.rt = theseKeys.rt
                    # was this 'correct'?
                    if (key_resp_2.keys == str(CorrAns)) or (key_resp_2.keys == CorrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExpTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ExpTrials"-------
    for thisComponent in ExpTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('imageTrials.started', imageTrials.tStartRefresh)
    trials.addData('imageTrials.stopped', imageTrials.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Break"-------
# update component parameters for each repeat
Space4.keys = []
Space4.rt = []
# keep track of which components have finished
BreakComponents = [text_2, Space4]
for thisComponent in BreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Break"-------
while continueRoutine:
    # get current time
    t = BreakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *Space4* updates
    waitOnFlip = False
    if Space4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space4.frameNStart = frameN  # exact frame index
        Space4.tStart = t  # local t and not account for scr refresh
        Space4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space4, 'tStartRefresh')  # time at next scr refresh
        Space4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Space4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Space4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Space4.status == STARTED and not waitOnFlip:
        theseKeys = Space4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Space4.keys = theseKeys.name  # just the last key pressed
            Space4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Break"-------
for thisComponent in BreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if Space4.keys in ['', [], None]:  # No response was made
    Space4.keys = None
thisExp.addData('Space4.keys',Space4.keys)
if Space4.keys != None:  # we had a response
    thisExp.addData('Space4.rt', Space4.rt)
thisExp.addData('Space4.started', Space4.tStartRefresh)
thisExp.addData('Space4.stopped', Space4.tStopRefresh)
thisExp.nextEntry()
# the Routine "Break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SimonStimuli.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ExperimentFix"-------
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    imageFixation.setImage('Fixation.jpeg')
    # keep track of which components have finished
    ExperimentFixComponents = [imageFixation]
    for thisComponent in ExperimentFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExperimentFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ExperimentFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ExperimentFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExperimentFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageFixation* updates
        if imageFixation.status == NOT_STARTED and tThisFlip >= 0.75-frameTolerance:
            # keep track of start time/frame for later
            imageFixation.frameNStart = frameN  # exact frame index
            imageFixation.tStart = t  # local t and not account for scr refresh
            imageFixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageFixation, 'tStartRefresh')  # time at next scr refresh
            imageFixation.setAutoDraw(True)
        if imageFixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageFixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                imageFixation.tStop = t  # not accounting for scr refresh
                imageFixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageFixation, 'tStopRefresh')  # time at next scr refresh
                imageFixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExperimentFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ExperimentFix"-------
    for thisComponent in ExperimentFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('imageFixation.started', imageFixation.tStartRefresh)
    trials_2.addData('imageFixation.stopped', imageFixation.tStopRefresh)
    
    # ------Prepare to start Routine "ExpTrials"-------
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    imageTrials.setImage(ImageFile)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    ExpTrialsComponents = [imageTrials, key_resp_2]
    for thisComponent in ExpTrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExpTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ExpTrials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ExpTrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExpTrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imageTrials* updates
        if imageTrials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageTrials.frameNStart = frameN  # exact frame index
            imageTrials.tStart = t  # local t and not account for scr refresh
            imageTrials.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageTrials, 'tStartRefresh')  # time at next scr refresh
            imageTrials.setAutoDraw(True)
        if imageTrials.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageTrials.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                imageTrials.tStop = t  # not accounting for scr refresh
                imageTrials.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imageTrials, 'tStopRefresh')  # time at next scr refresh
                imageTrials.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['m', 'z'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys.name  # just the first key pressed
                    key_resp_2.rt = theseKeys.rt
                    # was this 'correct'?
                    if (key_resp_2.keys == str(CorrAns)) or (key_resp_2.keys == CorrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExpTrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ExpTrials"-------
    for thisComponent in ExpTrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('imageTrials.started', imageTrials.tStartRefresh)
    trials_2.addData('imageTrials.stopped', imageTrials.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    trials_2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    trials_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials_2.saveAsText(filename + 'trials_2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Thanks"-------
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [TheEnd]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Thanks"-------
while continueRoutine:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TheEnd* updates
    if TheEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TheEnd.frameNStart = frameN  # exact frame index
        TheEnd.tStart = t  # local t and not account for scr refresh
        TheEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TheEnd, 'tStartRefresh')  # time at next scr refresh
        TheEnd.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TheEnd.started', TheEnd.tStartRefresh)
thisExp.addData('TheEnd.stopped', TheEnd.tStopRefresh)
# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
