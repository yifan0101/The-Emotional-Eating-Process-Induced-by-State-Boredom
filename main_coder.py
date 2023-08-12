#!/usr/bin/env pythons
# -*- coding: utf-8 -*-
import csv
import random
import itertools
import numpy as np
import time
from psychopy import gui , visual , event , clock , core
import os
import cv2  #加载 OpenCV
import matplotlib.pyplot as plt  #加载 Matplotlib . pyplot 存进 plt
from psychopy.hardware import keyboard
import pandas as pd
kb = keyboard . Keyboard ()

#收集被试的基本信息
sub_info = {'被试编号':'','Group':['b','p','s'],'age':'','gender':''}
inputDlg=gui.DlgFromDict(dictionary=sub_info,title='基本信息',
                         order=['被试编号','Group','age','gender'])
subId=sub_info['被试编号']
groupId=sub_info['Group']
gender=sub_info['gender']
age=sub_info['age']

if inputDlg.OK: #点击OK
    print(sub_info)
else: #点击Cancel
    core.quit
#生成实验数据文件
import time
date = time.strftime ("_20%y_%m_%d_%H%M",time.localtime()) #获取当前时间
file ='data/'+' main'+'_'+sub_info['被试编号']+sub_info['Group']+''+date #文档名（含路径）

with open("%s.csv"%(file),'a') as D: #写入表头
    D.write('SubId'+','+'Group'+','+'state'+','+'imagefile'+','+'EmotionType'+','+'Emotion_Resp'+','+'intention'+','+'gender'+','+'age'+'\n')
#打开的窗口，白色背景，全屏，单位为像素，中心坐标是（0,0)
win_weith=2560
win_high=1440
win=visual.Window(size=[win_weith,win_high],color=[1,1,1],colorSpace='rgb',fullscr=False,allowGUI=False,allowStencil=False,useFBO=True)
event.Mouse(visible=False)#隐藏鼠标指针

###生成实验材料
#指导语言和注视点
#fixation = visual.TextStim(win,text=u'+',font =' SimHei ', color ='#FFFFFF')
intro0=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intro0.PNG')
intro1=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intro1.JPG')
end_intro=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intro2.PNG')
intro3=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intro3.PNG')
#intro_movie呈现指导语，空格跳出
intro0.draw()
win.flip()
event.waitKeys(keyList=["space"])
#emotion_prime_movie
if groupId=='b':
    emotion_prime_movie=visual.MovieStim3(win=win,noAudio=False,filename='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/CAT10min.MOV',size=[win_weith,win_high])
    #OnsetTime_video=timer.getTime()
    while emotion_prime_movie.status!=visual.FINISHED:
        emotion_prime_movie.draw()
        win.flip()
        if event.getKeys(keyList=['y']):
            emotion_prime_movie.pause()
            break
    emotion_prime_movie.stop()
    win.flip()
elif groupId=='p':
    emotion_prime_movie=visual.MovieStim3(win=win,noAudio=False,filename='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/peace_10.MOV',size=[win_weith,win_high])
    #OnsetTime_video=timer.getTime()
    while emotion_prime_movie.status!=visual.FINISHED:
        emotion_prime_movie.draw()
        win.flip()
        if event.getKeys(keyList=['y']):
            emotion_prime_movie.pause()
            break
    emotion_prime_movie.stop()
    win.flip()
elif groupId=='s':
    emotion_prime_movie=visual.MovieStim3(win=win,noAudio=False,filename='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/sad1.mp4',size=[win_weith,win_high])
    #OnsetTime_video=timer.getTime()
    while emotion_prime_movie.status!=visual.FINISHED:
        emotion_prime_movie.draw()
        win.flip()
        if event.getKeys(keyList=['y']):
            emotion_prime_movie.pause()
            break
    emotion_prime_movie.stop()
    win.flip()

#intro_问卷，空格跳出
intro1.draw()
win.flip()
event.waitKeys(keyList=["space"])

#问卷部分
#读取Excel数据
#dataPath='E:/202209-202301/20221119BORE+EE/PlanA/emotion_ques_relative.xlsx'
#EmotionSitm=pd.read_csv(dataPath)
j=0
EmotionStim={'bore':1,'grieve':3,'free':2,'depress':3,'bore1':1,'bore2':1,'bore3':1,'sad':3,'relax':2,'environment':0,'happy':0,'trick3':0}
Emotion=list(EmotionStim.keys())
random.shuffle(Emotion)

for m in Emotion:
    imagefile='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/'+m+'.PNG'
    pic=visual.ImageStim(win,image=(imagefile))
    pic.draw()
    win.flip()
    Emotion_Resp=event.waitKeys(keyList=['0','1','2','3','4','5'])
    with open("%s.csv"%(file),'a') as D: #写入表头
        D.write(str(subId)+','+groupId+','+str(j)+','+str(m)+','+str(EmotionStim[m])+','+str(Emotion_Resp[0])+','+''+','+gender+','+age+'\n')
intent=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intention.png')
intent.draw()
win.flip()
intention=event.waitKeys(keyList=['0','1','2','3','4','5'])
with open("%s.csv"%(file),'a') as D: #写入表头
        D.write(str(subId)+','+groupId+','+str(j)+','+''+','+''+','+''+','+str(intention[0])+','+gender+','+age+'\n')

#第二阶段指导语
end_intro.draw()
win.flip()
event.waitKeys(keyList=["space"])

filen='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/'
movie_bore=['CTA1_5min.MOV','CTA2_5min.MOV','CTA3_5min.MOV']
movie_sad=['sad2.mp4','sad3.mp4','sad4.mp4']
movie_peace=['peace1_5min.MOV','peace2_5min.MOV','peace3_5min.MOV']
for j in range(1,4):
    if groupId=='b':
        movie=visual.MovieStim3(win=win,noAudio=False,filename=filen+movie_bore[j-1],size=[win_weith,win_high])
    elif groupId=="s":
        movie=visual.MovieStim3(win=win,noAudio=False,filename=filen+movie_sad[j-1],size=[win_weith,win_high])
    elif groupId=="p":
        movie=visual.MovieStim3(win=win,noAudio=False,filename=filen+movie_peace[j-1],size=[win_weith,win_high])
    #OnsetTime_video=timer.getTime()
    while movie.status!=visual.FINISHED:
        movie.draw()
        win.flip()
        if event.getKeys(keyList=['y']):
            movie.pause()
            break
    movie.stop()
    win.flip()
    #问卷指导语
    intro1.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    #问卷题目随机呈现
    random.shuffle(Emotion)
    for m in Emotion:
        imagefile='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/'+m+'.PNG'
        pic=visual.ImageStim(win,image=(imagefile))
        pic.draw()
        win.flip()
        Emotion_Resp=event.waitKeys(keyList=['0','1','2','3','4','5'])
        with open("%s.csv"%(file),'a') as D: #写入表头
            D.write(str(subId)+','+groupId+','+str(j)+','+str(m)+','+str(EmotionStim[m])+','+str(Emotion_Resp[0])+','+''+','+gender+','+age+'\n')
    intent=visual.ImageStim(win,image='E:/202209-202301/20221119BORE+EE/PlanA/stimulus/intention.png')
    intent.draw()
    win.flip()
    intention=event.waitKeys(keyList=['0','1','2','3','4','5'])
    with open("%s.csv"%(file),'a') as D: #写入表头
        D.write(str(subId)+','+groupId+','+str(j)+','+''+','+''+','+''+','+str(intention[0])+','+gender+','+age+'\n')

#呈现结束语
intro3.draw()
win.flip()
event.waitKeys(keyList=["space"])

