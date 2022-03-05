#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
os.system("python /data1/lanhaoyuan/code/kinetics-sounds/kinetics_streammv.py")
os.system("python /data1/lanhaoyuan/code/Simplified_DMC/data/cut_videos.py")
os.system("python /data1/lanhaoyuan/code/audio-extract/audio_wav_ucf101_hmdb51.py")
os.system("python /data1/lanhaoyuan/code/Simplified_DMC/data/cut_audios.py")
os.system("python /data1/lanhaoyuan/code/kinetics-sounds/mv_ksounds.py")
os.system("python /data1/lanhaoyuan/code/kinetics-sounds/mv_ksounds_mel.py")
# os.system("python /data1/lanhaoyuan/code/ttrun/minmax.py")

