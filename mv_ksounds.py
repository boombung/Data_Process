#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import subprocess
# flag = 0
filepath = "/data1/lanhaoyuan/datasets/ucf101/ucf101_videoframes/"
dst_path = "/data1/lanhaoyuan/datasets/ucf101/ucf101_rgbflowspec/rgb/"
for classname in  os.listdir(filepath):
    classpath = os.path.join(filepath, classname)
    for vname in os.listdir(classpath):
        vpath = os.path.join(classpath, vname)
        vpath = vpath + '/'
        dst_vpath = os.path.join(dst_path, vname)
        if not os.path.exists(dst_vpath):
            os.makedirs(dst_vpath)
        frame_num = 0
        for framename in os.listdir(vpath):
            frame_num += 1
            framepath = os.path.join(vpath, framename)
            flag = framename[-2 :]
            for picname in os.listdir(framepath):
                picpath = os.path.join(framepath, picname)
                # n_num = "%06d"%(int(flag) + 1)
                dstpicpath = dst_vpath + '/' + picname  # '/frame' + n_num + '.jpg'   
        # if not os.path.exists(classpath):
        #     flag += 1
        #     continue
                cmd = 'cp {} {}'.format(picpath, dstpicpath)
                fw = open('log_cp_ucf101_rgb.txt', 'a')
                fw.write(cmd)
                fw.write('\n')
                fw.close()
                subprocess.call(cmd, shell = True)
                # break
        fw = open('log_ucf101_vframenum.txt', 'a')
        fw.write('{} {}\n'.format(vname, frame_num))
        fw.close()


