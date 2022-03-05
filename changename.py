#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import subprocess
flag = 0
basepath = "/data1/lanhaoyuan/datasets/ucf101/ucf101_rgbflowspec/spec_1/"
for classname in os.listdir(basepath):
    filepath = basepath + classname
    for videoname in os.listdir(filepath):
        vid = videoname[:-4]
        vids = vid.split('-')
        n_num = "%06d"%int(vids[1])
        basename = filepath + '/' + videoname
        dirname = filepath + '/frame' + n_num + '.jpg'
        if not os.path.exists(basename):
            flag += 1
            continue
        cmd = 'mv {} {}'.format(basename, dirname)
        fw = open('log_changename_ucf101_1.txt', 'a')
        fw.write(cmd)
        fw.write('\n{}\n'.format(flag))
        fw.close()
        subprocess.call(cmd, shell = True)
print(flag)        
        
# basepath = "/data1/lanhaoyuan/datasets/ucf101/ucf101_rgbflowspec/spec/"
# classname = 'v_ApplyEyeMakeup_g01_c01'
# filepath = basepath + classname
# videoname = 'v_ApplyEyeMakeup_g01_c01-10.jpg'
# vid = videoname[:-4]
# vids = vid.split('-')
# vids = "%06d"%int(vids[1])
# basename = filepath + '/' + videoname
# dirname = filepath + '/frame' + vids + '.jpg'
# print(basename,'\n',dirname)

