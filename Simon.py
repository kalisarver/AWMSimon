#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Sep 30 17:20:07 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Simon'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='/Users/kalisarver/Desktop/Simon Task/Simon.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Initial_instruction"
Initial_instructionClock = core.Clock()
initialinstr = visual.TextStim(win=win, name='initialinstr',
    text='The experiment is about to begin.\nPress the space bar for the instructions.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='pink', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space1 = keyboard.Keyboard()

# Initialize components for Routine "Expt_Instructions"
Expt_InstructionsClock = core.Clock()
exptinstr = visual.TextStim(win=win, name='exptinstr',
    text='On each trial, you will see an arrow.\nYour job is to decide which direction the arrow is pointing to.\nIf the arrow is pointing to the RIGHT, press M\nIf the arrow is pointing to the LEFT, press Z\nIgnore the location, just focus on the direction.\nWe will start with a few practice trials.\nPress the space bar to continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='pink', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space2 = keyboard.Keyboard()

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
imageFix = visual.ImageStim(
    win=win,
    name='imageFix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Trials"
TrialsClock = core.Clock()
imagePractice = visual.ImageStim(
    win=win,
    name='imagePractice', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
response = keyboard.Keyboard()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
TheEnd = visual.TextStim(win=win, name='TheEnd',
    text='All done. Thank you!\nYou may now proceed to the next part of the study.',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='pink', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Initial_instruction"-------
continueRoutine = True
# update component parameters for each repeat
Space1.keys = []
Space1.rt = []
_Space1_allKeys = []
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
        _Space1_allKeys.extend(theseKeys)
        if len(_Space1_allKeys):
            Space1.keys = _Space1_allKeys[-1].name  # just the last key pressed
            Space1.rt = _Space1_allKeys[-1].rt
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
continueRoutine = True
# update component parameters for each repeat
Space2.keys = []
Space2.rt = []
_Space2_allKeys = []
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
        _Space2_allKeys.extend(theseKeys)
        if len(_Space2_allKeys):
            Space2.keys = _Space2_allKeys[-1].name  # just the last key pressed
            Space2.rt = _Space2_allKeys[-1].rt
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
Practice_loop = data.TrialHandler(nReps=5, method='random', 
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
    
    # ------Prepare to start Routine "Fixation"-------
    continueRoutine = True
    routineTimer.add(1.250000)
    # update component parameters for each repeat
    imageFix.setImage('Fixation.jpeg')
    # keep track of which components have finished
    FixationComponents = [imageFix]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixationClock)
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
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Fixation"-------
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('imageFix.started', imageFix.tStartRefresh)
    Practice_loop.addData('imageFix.stopped', imageFix.tStopRefresh)
    
    # ------Prepare to start Routine "Trials"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    imagePractice.setImage(ImageFile)
    response.keys = []
    response.rt = []
    _response_allKeys = []
    # keep track of which components have finished
    TrialsComponents = [imagePractice, response]
    for thisComponent in TrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trials"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialsClock)
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
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['m', 'z'], waitRelease=False)
            _response_allKeys.extend(theseKeys)
            if len(_response_allKeys):
                response.keys = _response_allKeys[0].name  # just the first key pressed
                response.rt = _response_allKeys[0].rt
                # was this correct?
                if (response.keys == str(CorrAns)) or (response.keys == CorrAns):
                    response.corr = 1
                else:
                    response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trials"-------
    for thisComponent in TrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('imagePractice.started', imagePractice.tStartRefresh)
    Practice_loop.addData('imagePractice.stopped', imagePractice.tStopRefresh)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           response.corr = 1;  # correct non-response
        else:
           response.corr = 0;  # failed to respond (incorrectly)
    # store data for Practice_loop (TrialHandler)
    Practice_loop.addData('response.keys',response.keys)
    Practice_loop.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        Practice_loop.addData('response.rt', response.rt)
    Practice_loop.addData('response.started', response.tStartRefresh)
    Practice_loop.addData('response.stopped', response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5 repeats of 'Practice_loop'

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

# ------Prepare to start Routine "Thanks"-------
continueRoutine = True
routineTimer.add(4.000000)
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

# -------Run Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
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
    if TheEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > TheEnd.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            TheEnd.tStop = t  # not accounting for scr refresh
            TheEnd.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TheEnd, 'tStopRefresh')  # time at next scr refresh
            TheEnd.setAutoDraw(False)
    
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

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
