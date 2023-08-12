#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on 十一月 19, 2022, at 15:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'test'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'age': '',
    'gender': 'male',
}
# --- Show participant info dialog --
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
    originPath='D:\\psychopy\\PlanA\\test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1500, 1000], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 0.9922, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "intro_movie" ---
intro0 = visual.ImageStim(
    win=win,
    name='intro0', 
    image='stimulus/intro0.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro0_resp = keyboard.Keyboard()

# --- Initialize components for Routine "movieprime" ---
emotion_priming_movie = visual.MovieStim3(
    win=win, name='emotion_priming_movie', units='',
    noAudio = False,
    filename='CAT10min.MOV',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=0.0,
    )
movieesc_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intro_ques" ---
intro1 = visual.ImageStim(
    win=win,
    name='intro1', 
    image='stimulus/intro1.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro1_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ques" ---
stim_ques = visual.ImageStim(
    win=win,
    name='stim_ques', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ques_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intention" ---
intention0 = visual.ImageStim(
    win=win,
    name='intention0', 
    image='stimulus/intention.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intention_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prime_end" ---
end_intro = visual.ImageStim(
    win=win,
    name='end_intro', 
    image='stimulus/intro2.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
end_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intro_movie" ---
intro0 = visual.ImageStim(
    win=win,
    name='intro0', 
    image='stimulus/intro0.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro0_resp = keyboard.Keyboard()

# --- Initialize components for Routine "movie_1" ---
movie_bore1 = visual.MovieStim3(
    win=win, name='movie_bore1', units='',
    noAudio = False,
    filename='stimulus/CTA1_5min.MOV',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=0.0,
    )
movie_bore1_esc = keyboard.Keyboard()

# --- Initialize components for Routine "intro_ques" ---
intro1 = visual.ImageStim(
    win=win,
    name='intro1', 
    image='stimulus/intro1.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro1_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ques" ---
stim_ques = visual.ImageStim(
    win=win,
    name='stim_ques', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ques_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intention" ---
intention0 = visual.ImageStim(
    win=win,
    name='intention0', 
    image='stimulus/intention.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intention_resp = keyboard.Keyboard()

# --- Initialize components for Routine "movie2" ---
movie_bore2 = visual.MovieStim3(
    win=win, name='movie_bore2', units='',
    noAudio = False,
    filename='stimulus/CTA2_5min.MOV',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=0.0,
    )
movie_bore2_esc = keyboard.Keyboard()

# --- Initialize components for Routine "intro_ques" ---
intro1 = visual.ImageStim(
    win=win,
    name='intro1', 
    image='stimulus/intro1.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro1_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ques" ---
stim_ques = visual.ImageStim(
    win=win,
    name='stim_ques', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ques_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intention" ---
intention0 = visual.ImageStim(
    win=win,
    name='intention0', 
    image='stimulus/intention.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intention_resp = keyboard.Keyboard()

# --- Initialize components for Routine "movie3" ---
movie_bore3 = visual.MovieStim3(
    win=win, name='movie_bore3', units='',
    noAudio = False,
    filename='stimulus/CTA3_5min.MOV',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False, anchor='center',
    depth=0.0,
    )
movie_bore3_esc = keyboard.Keyboard()

# --- Initialize components for Routine "intro_ques" ---
intro1 = visual.ImageStim(
    win=win,
    name='intro1', 
    image='stimulus/intro1.JPG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intro1_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ques" ---
stim_ques = visual.ImageStim(
    win=win,
    name='stim_ques', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
ques_resp = keyboard.Keyboard()

# --- Initialize components for Routine "intention" ---
intention0 = visual.ImageStim(
    win=win,
    name='intention0', 
    image='stimulus/intention.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
intention_resp = keyboard.Keyboard()

# --- Initialize components for Routine "final_end" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='stimulus/intro3.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
final_end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "intro_movie" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro0_resp.keys = []
intro0_resp.rt = []
_intro0_resp_allKeys = []
# keep track of which components have finished
intro_movieComponents = [intro0, intro0_resp]
for thisComponent in intro_movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_movie" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro0* updates
    if intro0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro0.frameNStart = frameN  # exact frame index
        intro0.tStart = t  # local t and not account for scr refresh
        intro0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro0, 'tStartRefresh')  # time at next scr refresh
        intro0.setAutoDraw(True)
    
    # *intro0_resp* updates
    if intro0_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro0_resp.frameNStart = frameN  # exact frame index
        intro0_resp.tStart = t  # local t and not account for scr refresh
        intro0_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro0_resp, 'tStartRefresh')  # time at next scr refresh
        intro0_resp.status = STARTED
        # keyboard checking is just starting
        intro0_resp.clock.reset()  # now t=0
        intro0_resp.clearEvents(eventType='keyboard')
    if intro0_resp.status == STARTED:
        theseKeys = intro0_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro0_resp_allKeys.extend(theseKeys)
        if len(_intro0_resp_allKeys):
            intro0_resp.keys = _intro0_resp_allKeys[-1].name  # just the last key pressed
            intro0_resp.rt = _intro0_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_movie" ---
for thisComponent in intro_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro0_resp.keys in ['', [], None]:  # No response was made
    intro0_resp.keys = None
thisExp.addData('intro0_resp.keys',intro0_resp.keys)
if intro0_resp.keys != None:  # we had a response
    thisExp.addData('intro0_resp.rt', intro0_resp.rt)
thisExp.nextEntry()
# the Routine "intro_movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "movieprime" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
movieesc_resp.keys = []
movieesc_resp.rt = []
_movieesc_resp_allKeys = []
# keep track of which components have finished
movieprimeComponents = [emotion_priming_movie, movieesc_resp]
for thisComponent in movieprimeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movieprime" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *emotion_priming_movie* updates
    if emotion_priming_movie.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        emotion_priming_movie.frameNStart = frameN  # exact frame index
        emotion_priming_movie.tStart = t  # local t and not account for scr refresh
        emotion_priming_movie.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(emotion_priming_movie, 'tStartRefresh')  # time at next scr refresh
        emotion_priming_movie.setAutoDraw(True)
    if emotion_priming_movie.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *movieesc_resp* updates
    if movieesc_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movieesc_resp.frameNStart = frameN  # exact frame index
        movieesc_resp.tStart = t  # local t and not account for scr refresh
        movieesc_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movieesc_resp, 'tStartRefresh')  # time at next scr refresh
        movieesc_resp.status = STARTED
        # keyboard checking is just starting
        movieesc_resp.clock.reset()  # now t=0
        movieesc_resp.clearEvents(eventType='keyboard')
    if movieesc_resp.status == STARTED:
        theseKeys = movieesc_resp.getKeys(keyList=['y'], waitRelease=False)
        _movieesc_resp_allKeys.extend(theseKeys)
        if len(_movieesc_resp_allKeys):
            movieesc_resp.keys = _movieesc_resp_allKeys[-1].name  # just the last key pressed
            movieesc_resp.rt = _movieesc_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movieprimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movieprime" ---
for thisComponent in movieprimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
emotion_priming_movie.stop()
# check responses
if movieesc_resp.keys in ['', [], None]:  # No response was made
    movieesc_resp.keys = None
thisExp.addData('movieesc_resp.keys',movieesc_resp.keys)
if movieesc_resp.keys != None:  # we had a response
    thisExp.addData('movieesc_resp.rt', movieesc_resp.rt)
thisExp.nextEntry()
# the Routine "movieprime" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_ques" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro1_resp.keys = []
intro1_resp.rt = []
_intro1_resp_allKeys = []
# keep track of which components have finished
intro_quesComponents = [intro1, intro1_resp]
for thisComponent in intro_quesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_ques" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *intro1_resp* updates
    if intro1_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_resp.frameNStart = frameN  # exact frame index
        intro1_resp.tStart = t  # local t and not account for scr refresh
        intro1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_resp, 'tStartRefresh')  # time at next scr refresh
        intro1_resp.status = STARTED
        # keyboard checking is just starting
        intro1_resp.clock.reset()  # now t=0
        intro1_resp.clearEvents(eventType='keyboard')
    if intro1_resp.status == STARTED:
        theseKeys = intro1_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro1_resp_allKeys.extend(theseKeys)
        if len(_intro1_resp_allKeys):
            intro1_resp.keys = _intro1_resp_allKeys[-1].name  # just the last key pressed
            intro1_resp.rt = _intro1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_quesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_ques" ---
for thisComponent in intro_quesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro1_resp.keys in ['', [], None]:  # No response was made
    intro1_resp.keys = None
thisExp.addData('intro1_resp.keys',intro1_resp.keys)
if intro1_resp.keys != None:  # we had a response
    thisExp.addData('intro1_resp.rt', intro1_resp.rt)
thisExp.nextEntry()
# the Routine "intro_ques" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_ques = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('emotion_ques_relative.xlsx'),
    seed=None, name='emotion_ques')
thisExp.addLoop(emotion_ques)  # add the loop to the experiment
thisEmotion_que = emotion_ques.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_que.rgb)
if thisEmotion_que != None:
    for paramName in thisEmotion_que:
        exec('{} = thisEmotion_que[paramName]'.format(paramName))

for thisEmotion_que in emotion_ques:
    currentLoop = emotion_ques
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_que.rgb)
    if thisEmotion_que != None:
        for paramName in thisEmotion_que:
            exec('{} = thisEmotion_que[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ques" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim_ques.setImage( imagefile)
    ques_resp.keys = []
    ques_resp.rt = []
    _ques_resp_allKeys = []
    # keep track of which components have finished
    quesComponents = [stim_ques, ques_resp]
    for thisComponent in quesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ques" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_ques* updates
        if stim_ques.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_ques.frameNStart = frameN  # exact frame index
            stim_ques.tStart = t  # local t and not account for scr refresh
            stim_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_ques, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_ques.started')
            stim_ques.setAutoDraw(True)
        
        # *ques_resp* updates
        waitOnFlip = False
        if ques_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ques_resp.frameNStart = frameN  # exact frame index
            ques_resp.tStart = t  # local t and not account for scr refresh
            ques_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ques_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ques_resp.started')
            ques_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ques_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ques_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ques_resp.status == STARTED and not waitOnFlip:
            theseKeys = ques_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
            _ques_resp_allKeys.extend(theseKeys)
            if len(_ques_resp_allKeys):
                ques_resp.keys = _ques_resp_allKeys[-1].name  # just the last key pressed
                ques_resp.rt = _ques_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ques" ---
    for thisComponent in quesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ques_resp.keys in ['', [], None]:  # No response was made
        ques_resp.keys = None
    emotion_ques.addData('ques_resp.keys',ques_resp.keys)
    if ques_resp.keys != None:  # we had a response
        emotion_ques.addData('ques_resp.rt', ques_resp.rt)
    # the Routine "ques" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emotion_ques'


# --- Prepare to start Routine "intention" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intention_resp.keys = []
intention_resp.rt = []
_intention_resp_allKeys = []
# keep track of which components have finished
intentionComponents = [intention0, intention_resp]
for thisComponent in intentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intention" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intention0* updates
    if intention0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention0.frameNStart = frameN  # exact frame index
        intention0.tStart = t  # local t and not account for scr refresh
        intention0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention0, 'tStartRefresh')  # time at next scr refresh
        intention0.setAutoDraw(True)
    
    # *intention_resp* updates
    if intention_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention_resp.frameNStart = frameN  # exact frame index
        intention_resp.tStart = t  # local t and not account for scr refresh
        intention_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention_resp, 'tStartRefresh')  # time at next scr refresh
        intention_resp.status = STARTED
        # keyboard checking is just starting
        intention_resp.clock.reset()  # now t=0
        intention_resp.clearEvents(eventType='keyboard')
    if intention_resp.status == STARTED:
        theseKeys = intention_resp.getKeys(keyList=['4','5','6','7','8','9','3','2','1'], waitRelease=False)
        _intention_resp_allKeys.extend(theseKeys)
        if len(_intention_resp_allKeys):
            intention_resp.keys = _intention_resp_allKeys[-1].name  # just the last key pressed
            intention_resp.rt = _intention_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intention" ---
for thisComponent in intentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intention_resp.keys in ['', [], None]:  # No response was made
    intention_resp.keys = None
thisExp.addData('intention_resp.keys',intention_resp.keys)
if intention_resp.keys != None:  # we had a response
    thisExp.addData('intention_resp.rt', intention_resp.rt)
thisExp.nextEntry()
# the Routine "intention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "prime_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
prime_endComponents = [end_intro, end_resp]
for thisComponent in prime_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prime_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_intro* updates
    if end_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_intro.frameNStart = frameN  # exact frame index
        end_intro.tStart = t  # local t and not account for scr refresh
        end_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_intro, 'tStartRefresh')  # time at next scr refresh
        end_intro.setAutoDraw(True)
    
    # *end_resp* updates
    if end_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        end_resp.clock.reset()  # now t=0
        end_resp.clearEvents(eventType='keyboard')
    if end_resp.status == STARTED:
        theseKeys = end_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prime_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prime_end" ---
for thisComponent in prime_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.nextEntry()
# the Routine "prime_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_movie" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro0_resp.keys = []
intro0_resp.rt = []
_intro0_resp_allKeys = []
# keep track of which components have finished
intro_movieComponents = [intro0, intro0_resp]
for thisComponent in intro_movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_movie" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro0* updates
    if intro0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro0.frameNStart = frameN  # exact frame index
        intro0.tStart = t  # local t and not account for scr refresh
        intro0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro0, 'tStartRefresh')  # time at next scr refresh
        intro0.setAutoDraw(True)
    
    # *intro0_resp* updates
    if intro0_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro0_resp.frameNStart = frameN  # exact frame index
        intro0_resp.tStart = t  # local t and not account for scr refresh
        intro0_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro0_resp, 'tStartRefresh')  # time at next scr refresh
        intro0_resp.status = STARTED
        # keyboard checking is just starting
        intro0_resp.clock.reset()  # now t=0
        intro0_resp.clearEvents(eventType='keyboard')
    if intro0_resp.status == STARTED:
        theseKeys = intro0_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro0_resp_allKeys.extend(theseKeys)
        if len(_intro0_resp_allKeys):
            intro0_resp.keys = _intro0_resp_allKeys[-1].name  # just the last key pressed
            intro0_resp.rt = _intro0_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_movie" ---
for thisComponent in intro_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro0_resp.keys in ['', [], None]:  # No response was made
    intro0_resp.keys = None
thisExp.addData('intro0_resp.keys',intro0_resp.keys)
if intro0_resp.keys != None:  # we had a response
    thisExp.addData('intro0_resp.rt', intro0_resp.rt)
thisExp.nextEntry()
# the Routine "intro_movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "movie_1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
movie_bore1_esc.keys = []
movie_bore1_esc.rt = []
_movie_bore1_esc_allKeys = []
# keep track of which components have finished
movie_1Components = [movie_bore1, movie_bore1_esc]
for thisComponent in movie_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movie_1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_bore1* updates
    if movie_bore1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore1.frameNStart = frameN  # exact frame index
        movie_bore1.tStart = t  # local t and not account for scr refresh
        movie_bore1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore1, 'tStartRefresh')  # time at next scr refresh
        movie_bore1.setAutoDraw(True)
    if movie_bore1.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *movie_bore1_esc* updates
    if movie_bore1_esc.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore1_esc.frameNStart = frameN  # exact frame index
        movie_bore1_esc.tStart = t  # local t and not account for scr refresh
        movie_bore1_esc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore1_esc, 'tStartRefresh')  # time at next scr refresh
        movie_bore1_esc.status = STARTED
        # keyboard checking is just starting
        movie_bore1_esc.clock.reset()  # now t=0
        movie_bore1_esc.clearEvents(eventType='keyboard')
    if movie_bore1_esc.status == STARTED:
        theseKeys = movie_bore1_esc.getKeys(keyList=['y'], waitRelease=False)
        _movie_bore1_esc_allKeys.extend(theseKeys)
        if len(_movie_bore1_esc_allKeys):
            movie_bore1_esc.keys = _movie_bore1_esc_allKeys[-1].name  # just the last key pressed
            movie_bore1_esc.rt = _movie_bore1_esc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movie_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movie_1" ---
for thisComponent in movie_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie_bore1.stop()
# check responses
if movie_bore1_esc.keys in ['', [], None]:  # No response was made
    movie_bore1_esc.keys = None
thisExp.addData('movie_bore1_esc.keys',movie_bore1_esc.keys)
if movie_bore1_esc.keys != None:  # we had a response
    thisExp.addData('movie_bore1_esc.rt', movie_bore1_esc.rt)
thisExp.nextEntry()
# the Routine "movie_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_ques" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro1_resp.keys = []
intro1_resp.rt = []
_intro1_resp_allKeys = []
# keep track of which components have finished
intro_quesComponents = [intro1, intro1_resp]
for thisComponent in intro_quesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_ques" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *intro1_resp* updates
    if intro1_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_resp.frameNStart = frameN  # exact frame index
        intro1_resp.tStart = t  # local t and not account for scr refresh
        intro1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_resp, 'tStartRefresh')  # time at next scr refresh
        intro1_resp.status = STARTED
        # keyboard checking is just starting
        intro1_resp.clock.reset()  # now t=0
        intro1_resp.clearEvents(eventType='keyboard')
    if intro1_resp.status == STARTED:
        theseKeys = intro1_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro1_resp_allKeys.extend(theseKeys)
        if len(_intro1_resp_allKeys):
            intro1_resp.keys = _intro1_resp_allKeys[-1].name  # just the last key pressed
            intro1_resp.rt = _intro1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_quesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_ques" ---
for thisComponent in intro_quesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro1_resp.keys in ['', [], None]:  # No response was made
    intro1_resp.keys = None
thisExp.addData('intro1_resp.keys',intro1_resp.keys)
if intro1_resp.keys != None:  # we had a response
    thisExp.addData('intro1_resp.rt', intro1_resp.rt)
thisExp.nextEntry()
# the Routine "intro_ques" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_ques1 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('emotion_ques_relative.xlsx'),
    seed=None, name='emotion_ques1')
thisExp.addLoop(emotion_ques1)  # add the loop to the experiment
thisEmotion_ques1 = emotion_ques1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques1.rgb)
if thisEmotion_ques1 != None:
    for paramName in thisEmotion_ques1:
        exec('{} = thisEmotion_ques1[paramName]'.format(paramName))

for thisEmotion_ques1 in emotion_ques1:
    currentLoop = emotion_ques1
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques1.rgb)
    if thisEmotion_ques1 != None:
        for paramName in thisEmotion_ques1:
            exec('{} = thisEmotion_ques1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ques" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim_ques.setImage( imagefile)
    ques_resp.keys = []
    ques_resp.rt = []
    _ques_resp_allKeys = []
    # keep track of which components have finished
    quesComponents = [stim_ques, ques_resp]
    for thisComponent in quesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ques" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_ques* updates
        if stim_ques.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_ques.frameNStart = frameN  # exact frame index
            stim_ques.tStart = t  # local t and not account for scr refresh
            stim_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_ques, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_ques.started')
            stim_ques.setAutoDraw(True)
        
        # *ques_resp* updates
        waitOnFlip = False
        if ques_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ques_resp.frameNStart = frameN  # exact frame index
            ques_resp.tStart = t  # local t and not account for scr refresh
            ques_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ques_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ques_resp.started')
            ques_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ques_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ques_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ques_resp.status == STARTED and not waitOnFlip:
            theseKeys = ques_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
            _ques_resp_allKeys.extend(theseKeys)
            if len(_ques_resp_allKeys):
                ques_resp.keys = _ques_resp_allKeys[-1].name  # just the last key pressed
                ques_resp.rt = _ques_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ques" ---
    for thisComponent in quesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ques_resp.keys in ['', [], None]:  # No response was made
        ques_resp.keys = None
    emotion_ques1.addData('ques_resp.keys',ques_resp.keys)
    if ques_resp.keys != None:  # we had a response
        emotion_ques1.addData('ques_resp.rt', ques_resp.rt)
    # the Routine "ques" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emotion_ques1'


# --- Prepare to start Routine "intention" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intention_resp.keys = []
intention_resp.rt = []
_intention_resp_allKeys = []
# keep track of which components have finished
intentionComponents = [intention0, intention_resp]
for thisComponent in intentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intention" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intention0* updates
    if intention0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention0.frameNStart = frameN  # exact frame index
        intention0.tStart = t  # local t and not account for scr refresh
        intention0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention0, 'tStartRefresh')  # time at next scr refresh
        intention0.setAutoDraw(True)
    
    # *intention_resp* updates
    if intention_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention_resp.frameNStart = frameN  # exact frame index
        intention_resp.tStart = t  # local t and not account for scr refresh
        intention_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention_resp, 'tStartRefresh')  # time at next scr refresh
        intention_resp.status = STARTED
        # keyboard checking is just starting
        intention_resp.clock.reset()  # now t=0
        intention_resp.clearEvents(eventType='keyboard')
    if intention_resp.status == STARTED:
        theseKeys = intention_resp.getKeys(keyList=['4','5','6','7','8','9','3','2','1'], waitRelease=False)
        _intention_resp_allKeys.extend(theseKeys)
        if len(_intention_resp_allKeys):
            intention_resp.keys = _intention_resp_allKeys[-1].name  # just the last key pressed
            intention_resp.rt = _intention_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intention" ---
for thisComponent in intentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intention_resp.keys in ['', [], None]:  # No response was made
    intention_resp.keys = None
thisExp.addData('intention_resp.keys',intention_resp.keys)
if intention_resp.keys != None:  # we had a response
    thisExp.addData('intention_resp.rt', intention_resp.rt)
thisExp.nextEntry()
# the Routine "intention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "movie2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
movie_bore2_esc.keys = []
movie_bore2_esc.rt = []
_movie_bore2_esc_allKeys = []
# keep track of which components have finished
movie2Components = [movie_bore2, movie_bore2_esc]
for thisComponent in movie2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movie2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_bore2* updates
    if movie_bore2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore2.frameNStart = frameN  # exact frame index
        movie_bore2.tStart = t  # local t and not account for scr refresh
        movie_bore2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore2, 'tStartRefresh')  # time at next scr refresh
        movie_bore2.setAutoDraw(True)
    if movie_bore2.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *movie_bore2_esc* updates
    waitOnFlip = False
    if movie_bore2_esc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore2_esc.frameNStart = frameN  # exact frame index
        movie_bore2_esc.tStart = t  # local t and not account for scr refresh
        movie_bore2_esc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore2_esc, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movie_bore2_esc.started')
        movie_bore2_esc.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(movie_bore2_esc.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(movie_bore2_esc.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if movie_bore2_esc.status == STARTED and not waitOnFlip:
        theseKeys = movie_bore2_esc.getKeys(keyList=['y'], waitRelease=False)
        _movie_bore2_esc_allKeys.extend(theseKeys)
        if len(_movie_bore2_esc_allKeys):
            movie_bore2_esc.keys = _movie_bore2_esc_allKeys[-1].name  # just the last key pressed
            movie_bore2_esc.rt = _movie_bore2_esc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movie2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movie2" ---
for thisComponent in movie2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie_bore2.stop()
# check responses
if movie_bore2_esc.keys in ['', [], None]:  # No response was made
    movie_bore2_esc.keys = None
thisExp.addData('movie_bore2_esc.keys',movie_bore2_esc.keys)
if movie_bore2_esc.keys != None:  # we had a response
    thisExp.addData('movie_bore2_esc.rt', movie_bore2_esc.rt)
thisExp.nextEntry()
# the Routine "movie2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_ques" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro1_resp.keys = []
intro1_resp.rt = []
_intro1_resp_allKeys = []
# keep track of which components have finished
intro_quesComponents = [intro1, intro1_resp]
for thisComponent in intro_quesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_ques" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *intro1_resp* updates
    if intro1_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_resp.frameNStart = frameN  # exact frame index
        intro1_resp.tStart = t  # local t and not account for scr refresh
        intro1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_resp, 'tStartRefresh')  # time at next scr refresh
        intro1_resp.status = STARTED
        # keyboard checking is just starting
        intro1_resp.clock.reset()  # now t=0
        intro1_resp.clearEvents(eventType='keyboard')
    if intro1_resp.status == STARTED:
        theseKeys = intro1_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro1_resp_allKeys.extend(theseKeys)
        if len(_intro1_resp_allKeys):
            intro1_resp.keys = _intro1_resp_allKeys[-1].name  # just the last key pressed
            intro1_resp.rt = _intro1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_quesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_ques" ---
for thisComponent in intro_quesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro1_resp.keys in ['', [], None]:  # No response was made
    intro1_resp.keys = None
thisExp.addData('intro1_resp.keys',intro1_resp.keys)
if intro1_resp.keys != None:  # we had a response
    thisExp.addData('intro1_resp.rt', intro1_resp.rt)
thisExp.nextEntry()
# the Routine "intro_ques" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_ques3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('emotion_ques_relative.xlsx'),
    seed=None, name='emotion_ques3')
thisExp.addLoop(emotion_ques3)  # add the loop to the experiment
thisEmotion_ques3 = emotion_ques3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques3.rgb)
if thisEmotion_ques3 != None:
    for paramName in thisEmotion_ques3:
        exec('{} = thisEmotion_ques3[paramName]'.format(paramName))

for thisEmotion_ques3 in emotion_ques3:
    currentLoop = emotion_ques3
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques3.rgb)
    if thisEmotion_ques3 != None:
        for paramName in thisEmotion_ques3:
            exec('{} = thisEmotion_ques3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ques" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim_ques.setImage( imagefile)
    ques_resp.keys = []
    ques_resp.rt = []
    _ques_resp_allKeys = []
    # keep track of which components have finished
    quesComponents = [stim_ques, ques_resp]
    for thisComponent in quesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ques" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_ques* updates
        if stim_ques.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_ques.frameNStart = frameN  # exact frame index
            stim_ques.tStart = t  # local t and not account for scr refresh
            stim_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_ques, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_ques.started')
            stim_ques.setAutoDraw(True)
        
        # *ques_resp* updates
        waitOnFlip = False
        if ques_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ques_resp.frameNStart = frameN  # exact frame index
            ques_resp.tStart = t  # local t and not account for scr refresh
            ques_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ques_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ques_resp.started')
            ques_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ques_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ques_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ques_resp.status == STARTED and not waitOnFlip:
            theseKeys = ques_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
            _ques_resp_allKeys.extend(theseKeys)
            if len(_ques_resp_allKeys):
                ques_resp.keys = _ques_resp_allKeys[-1].name  # just the last key pressed
                ques_resp.rt = _ques_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ques" ---
    for thisComponent in quesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ques_resp.keys in ['', [], None]:  # No response was made
        ques_resp.keys = None
    emotion_ques3.addData('ques_resp.keys',ques_resp.keys)
    if ques_resp.keys != None:  # we had a response
        emotion_ques3.addData('ques_resp.rt', ques_resp.rt)
    # the Routine "ques" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emotion_ques3'


# --- Prepare to start Routine "intention" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intention_resp.keys = []
intention_resp.rt = []
_intention_resp_allKeys = []
# keep track of which components have finished
intentionComponents = [intention0, intention_resp]
for thisComponent in intentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intention" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intention0* updates
    if intention0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention0.frameNStart = frameN  # exact frame index
        intention0.tStart = t  # local t and not account for scr refresh
        intention0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention0, 'tStartRefresh')  # time at next scr refresh
        intention0.setAutoDraw(True)
    
    # *intention_resp* updates
    if intention_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention_resp.frameNStart = frameN  # exact frame index
        intention_resp.tStart = t  # local t and not account for scr refresh
        intention_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention_resp, 'tStartRefresh')  # time at next scr refresh
        intention_resp.status = STARTED
        # keyboard checking is just starting
        intention_resp.clock.reset()  # now t=0
        intention_resp.clearEvents(eventType='keyboard')
    if intention_resp.status == STARTED:
        theseKeys = intention_resp.getKeys(keyList=['4','5','6','7','8','9','3','2','1'], waitRelease=False)
        _intention_resp_allKeys.extend(theseKeys)
        if len(_intention_resp_allKeys):
            intention_resp.keys = _intention_resp_allKeys[-1].name  # just the last key pressed
            intention_resp.rt = _intention_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intention" ---
for thisComponent in intentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intention_resp.keys in ['', [], None]:  # No response was made
    intention_resp.keys = None
thisExp.addData('intention_resp.keys',intention_resp.keys)
if intention_resp.keys != None:  # we had a response
    thisExp.addData('intention_resp.rt', intention_resp.rt)
thisExp.nextEntry()
# the Routine "intention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "movie3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
movie_bore3_esc.keys = []
movie_bore3_esc.rt = []
_movie_bore3_esc_allKeys = []
# keep track of which components have finished
movie3Components = [movie_bore3, movie_bore3_esc]
for thisComponent in movie3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "movie3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_bore3* updates
    if movie_bore3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore3.frameNStart = frameN  # exact frame index
        movie_bore3.tStart = t  # local t and not account for scr refresh
        movie_bore3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'movie_bore3.started')
        movie_bore3.setAutoDraw(True)
    if movie_bore3.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # *movie_bore3_esc* updates
    if movie_bore3_esc.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_bore3_esc.frameNStart = frameN  # exact frame index
        movie_bore3_esc.tStart = t  # local t and not account for scr refresh
        movie_bore3_esc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_bore3_esc, 'tStartRefresh')  # time at next scr refresh
        movie_bore3_esc.status = STARTED
        # keyboard checking is just starting
        movie_bore3_esc.clock.reset()  # now t=0
    if movie_bore3_esc.status == STARTED:
        theseKeys = movie_bore3_esc.getKeys(keyList=['y'], waitRelease=False)
        _movie_bore3_esc_allKeys.extend(theseKeys)
        if len(_movie_bore3_esc_allKeys):
            movie_bore3_esc.keys = _movie_bore3_esc_allKeys[-1].name  # just the last key pressed
            movie_bore3_esc.rt = _movie_bore3_esc_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in movie3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "movie3" ---
for thisComponent in movie3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie_bore3.stop()
# check responses
if movie_bore3_esc.keys in ['', [], None]:  # No response was made
    movie_bore3_esc.keys = None
thisExp.addData('movie_bore3_esc.keys',movie_bore3_esc.keys)
if movie_bore3_esc.keys != None:  # we had a response
    thisExp.addData('movie_bore3_esc.rt', movie_bore3_esc.rt)
thisExp.nextEntry()
# the Routine "movie3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro_ques" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intro1_resp.keys = []
intro1_resp.rt = []
_intro1_resp_allKeys = []
# keep track of which components have finished
intro_quesComponents = [intro1, intro1_resp]
for thisComponent in intro_quesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intro_ques" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro1* updates
    if intro1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro1.frameNStart = frameN  # exact frame index
        intro1.tStart = t  # local t and not account for scr refresh
        intro1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1, 'tStartRefresh')  # time at next scr refresh
        intro1.setAutoDraw(True)
    
    # *intro1_resp* updates
    if intro1_resp.status == NOT_STARTED and t >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        intro1_resp.frameNStart = frameN  # exact frame index
        intro1_resp.tStart = t  # local t and not account for scr refresh
        intro1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro1_resp, 'tStartRefresh')  # time at next scr refresh
        intro1_resp.status = STARTED
        # keyboard checking is just starting
        intro1_resp.clock.reset()  # now t=0
        intro1_resp.clearEvents(eventType='keyboard')
    if intro1_resp.status == STARTED:
        theseKeys = intro1_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro1_resp_allKeys.extend(theseKeys)
        if len(_intro1_resp_allKeys):
            intro1_resp.keys = _intro1_resp_allKeys[-1].name  # just the last key pressed
            intro1_resp.rt = _intro1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_quesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro_ques" ---
for thisComponent in intro_quesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intro1_resp.keys in ['', [], None]:  # No response was made
    intro1_resp.keys = None
thisExp.addData('intro1_resp.keys',intro1_resp.keys)
if intro1_resp.keys != None:  # we had a response
    thisExp.addData('intro1_resp.rt', intro1_resp.rt)
thisExp.nextEntry()
# the Routine "intro_ques" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
emotion_ques4 = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('emotion_ques_relative.xlsx'),
    seed=None, name='emotion_ques4')
thisExp.addLoop(emotion_ques4)  # add the loop to the experiment
thisEmotion_ques4 = emotion_ques4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques4.rgb)
if thisEmotion_ques4 != None:
    for paramName in thisEmotion_ques4:
        exec('{} = thisEmotion_ques4[paramName]'.format(paramName))

for thisEmotion_ques4 in emotion_ques4:
    currentLoop = emotion_ques4
    # abbreviate parameter names if possible (e.g. rgb = thisEmotion_ques4.rgb)
    if thisEmotion_ques4 != None:
        for paramName in thisEmotion_ques4:
            exec('{} = thisEmotion_ques4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ques" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stim_ques.setImage( imagefile)
    ques_resp.keys = []
    ques_resp.rt = []
    _ques_resp_allKeys = []
    # keep track of which components have finished
    quesComponents = [stim_ques, ques_resp]
    for thisComponent in quesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ques" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_ques* updates
        if stim_ques.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_ques.frameNStart = frameN  # exact frame index
            stim_ques.tStart = t  # local t and not account for scr refresh
            stim_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_ques, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stim_ques.started')
            stim_ques.setAutoDraw(True)
        
        # *ques_resp* updates
        waitOnFlip = False
        if ques_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ques_resp.frameNStart = frameN  # exact frame index
            ques_resp.tStart = t  # local t and not account for scr refresh
            ques_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ques_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ques_resp.started')
            ques_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ques_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ques_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ques_resp.status == STARTED and not waitOnFlip:
            theseKeys = ques_resp.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
            _ques_resp_allKeys.extend(theseKeys)
            if len(_ques_resp_allKeys):
                ques_resp.keys = _ques_resp_allKeys[-1].name  # just the last key pressed
                ques_resp.rt = _ques_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ques" ---
    for thisComponent in quesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if ques_resp.keys in ['', [], None]:  # No response was made
        ques_resp.keys = None
    emotion_ques4.addData('ques_resp.keys',ques_resp.keys)
    if ques_resp.keys != None:  # we had a response
        emotion_ques4.addData('ques_resp.rt', ques_resp.rt)
    # the Routine "ques" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'emotion_ques4'


# --- Prepare to start Routine "intention" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intention_resp.keys = []
intention_resp.rt = []
_intention_resp_allKeys = []
# keep track of which components have finished
intentionComponents = [intention0, intention_resp]
for thisComponent in intentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "intention" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intention0* updates
    if intention0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention0.frameNStart = frameN  # exact frame index
        intention0.tStart = t  # local t and not account for scr refresh
        intention0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention0, 'tStartRefresh')  # time at next scr refresh
        intention0.setAutoDraw(True)
    
    # *intention_resp* updates
    if intention_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intention_resp.frameNStart = frameN  # exact frame index
        intention_resp.tStart = t  # local t and not account for scr refresh
        intention_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intention_resp, 'tStartRefresh')  # time at next scr refresh
        intention_resp.status = STARTED
        # keyboard checking is just starting
        intention_resp.clock.reset()  # now t=0
        intention_resp.clearEvents(eventType='keyboard')
    if intention_resp.status == STARTED:
        theseKeys = intention_resp.getKeys(keyList=['4','5','6','7','8','9','3','2','1'], waitRelease=False)
        _intention_resp_allKeys.extend(theseKeys)
        if len(_intention_resp_allKeys):
            intention_resp.keys = _intention_resp_allKeys[-1].name  # just the last key pressed
            intention_resp.rt = _intention_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intention" ---
for thisComponent in intentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intention_resp.keys in ['', [], None]:  # No response was made
    intention_resp.keys = None
thisExp.addData('intention_resp.keys',intention_resp.keys)
if intention_resp.keys != None:  # we had a response
    thisExp.addData('intention_resp.rt', intention_resp.rt)
thisExp.nextEntry()
# the Routine "intention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "final_end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
final_end_resp.keys = []
final_end_resp.rt = []
_final_end_resp_allKeys = []
# keep track of which components have finished
final_endComponents = [image, final_end_resp]
for thisComponent in final_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "final_end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *final_end_resp* updates
    if final_end_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        final_end_resp.frameNStart = frameN  # exact frame index
        final_end_resp.tStart = t  # local t and not account for scr refresh
        final_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(final_end_resp, 'tStartRefresh')  # time at next scr refresh
        final_end_resp.status = STARTED
        # keyboard checking is just starting
        final_end_resp.clock.reset()  # now t=0
        final_end_resp.clearEvents(eventType='keyboard')
    if final_end_resp.status == STARTED:
        theseKeys = final_end_resp.getKeys(keyList=['space'], waitRelease=False)
        _final_end_resp_allKeys.extend(theseKeys)
        if len(_final_end_resp_allKeys):
            final_end_resp.keys = _final_end_resp_allKeys[-1].name  # just the last key pressed
            final_end_resp.rt = _final_end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "final_end" ---
for thisComponent in final_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if final_end_resp.keys in ['', [], None]:  # No response was made
    final_end_resp.keys = None
thisExp.addData('final_end_resp.keys',final_end_resp.keys)
if final_end_resp.keys != None:  # we had a response
    thisExp.addData('final_end_resp.rt', final_end_resp.rt)
thisExp.nextEntry()
# the Routine "final_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
