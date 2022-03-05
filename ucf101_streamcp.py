import os
import sys
import subprocess
from moviepy.editor import *
nosounds = []
# 文件夹全拷贝，未剔除无音频视频对应文件夹

def get_video_info(video_file_path):
    video = VideoFileClip(video_file_path)
    if video.audio is None:        
        return False
    else:
        return True

def class_process(dir_path, dst_dir_path, class_name):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return

    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)

    for file_name in os.listdir(class_path):
        if '.avi' not in file_name:
            # print(class_path, '/', file_name)
            continue
        name, ext = os.path.splitext(file_name)

        video_file_path = os.path.join(class_path, file_name)
        flag = get_video_info(video_file_path)
        if flag == 0:
            nosounds.append(video_file_path)
        else:
            cmd = 'cp {} {}'.format(video_file_path, dst_class_path)
        #    print(cmd)
            fw = open('log_streamcp.txt', 'a')
            fw.write(cmd)
            fw.close()
            subprocess.call(cmd, shell=True)
            # print('\n')

if __name__=="__main__":

    # dir_path = sys.argv[1]
    # dst_dir_path = sys.argv[2]
    dir_path = "/data1/lanhaoyuan/datasets/ucf101/ucf101_video"
    dst_dir_path = "/data1/lanhaoyuan/datasets/ucf101-sounds/ucf101_sounds_video/"

    for class_name in os.listdir(dir_path):
        class_process(dir_path, dst_dir_path, class_name)

    fw = open('log_nosounds_ucf101.txt', 'w')
    # fw.writelines(len(nosounds))
    fw.write("\nnosounds:")
    fw.writelines(nosounds)    
    fw.close()
    # print(nosounds)
    # print(len(nosounds))




# def get_video_info(source_video_path):
#     probe = ffmpeg.probe(source_video_path)
#     audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
#     if audio_stream is None:
#         nostream.append[source_video_path]