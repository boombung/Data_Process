import os
import cv2
import pdb
import math
import subprocess

def video2frame(video_path, frame_save_path, frame_interval=1):

    vid = cv2.VideoCapture(video_path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    #pdb.set_trace()
    success, image = vid.read()
    count = 0
    while success:
        count +=1
        if count % frame_interval == 0:
            #cv2.imencode('.png', image)[1].tofile(frame_save_path+'/fame_%d.png'%count)
            save_name = '{}/frame_{}_{}.jpg'.format(frame_save_path, int(count/fps),count)
            cv2.imencode('.jpg', image)[1].tofile(save_name)
        success, image = vid.read()
    print(count)


def video2frame_update(video_path, frame_save_path, frame_kept_per_second=16):

    vid = cv2.VideoCapture(video_path)
    fps = vid.get(cv2.CAP_PROP_FPS)                   # 获取帧率（一般为30帧每秒）
    video_frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取帧数
    
    nostreampath = "/data1/lanhaoyuan/datasets/ucf101/ucf101_no_video/"
    smaller_one_path = "/data1/lanhaoyuan/datasets/ucf101/ucf101_smaller_than_one/"
    # if video_path == '/data1/lanhaoyuan/datasets/kinetics-sounds/kinetics-sound_video/tt/bowling/v_bowling_015.avi':
    # print('fps:', fps, ' video_frames:', video_frames)
    video_len = int(video_frames/fps)                 # 获取视频时长
    # print('video_len:', video_len)
    if fps == 0 or video_len < 1:      
        if fps == 0:
            cmd = "mv \"{}\" \"{}\"".format(video_path, nostreampath)
            fw = open('log_streammv_novideo_ucf101.txt', 'a')
        else:
            cmd = "cp \"{}\" \"{}\"".format(video_path, smaller_one_path)
            fw = open('log_streammv_small1_ucf101.txt', 'a')
        fw.write(cmd)
        fw.write('\n')
        fw.close()
        subprocess.call(cmd, shell=True)
    else:
        count = 0
        n_num = 0
        frame_interval = int(fps/frame_kept_per_second)   # 采样间隔
        while(count < fps*video_len):                     # = video_frames ???
            ret, image = vid.read()
            if not ret:
                break
            # if count % fps == 0:
            #     frame_id = 0     # fps不为整数时无法取到
            if count % math.ceil(fps) == 0:
                frame_id = 0
            if frame_id < frame_interval*frame_kept_per_second and frame_id%frame_interval == 0:
                # cv2.imencode('.png', image)[1].tofile(frame_save_path+'/fame_%d.png'%count)
                save_dir = '{}/frame_{:03d}'.format(frame_save_path, int(count/fps))
                # print(save_dir)
                if not os.path.exists(save_dir):
                    os.mkdir(save_dir)
                n_num += 1
                save_name = '{}/frame_{:03d}/frame{:06d}.jpg'.format(frame_save_path, int(count/fps), n_num) # count
                # print(save_name)
                cv2.imencode('.jpg', image)[1].tofile(save_name)
            
            frame_id += 1
            count += 1


def class_process(video_dir, save_dir, class_name):
    class_path = os.path.join(video_dir, class_name)
    if not os.path.isdir(class_path):
        return

    dst_class_path = os.path.join(save_dir, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)

    vid_count = 0
    for each_video in os.listdir(class_path):
        if not each_video.endswith('.avi') and not each_video.endswith('.mp4'):
            continue
        # print(each_video)
        video_path = os.path.join(class_path, each_video)
        save_path = os.path.join(dst_class_path, each_video[:-4])
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        video2frame_update(video_path, save_path, frame_kept_per_second=16)
        #pdb.set_trace()
        vid_count += 1
    print('cut %d videos' % vid_count)



if __name__=="__main__":
    
    video_dir = '/data1/lanhaoyuan/datasets/ucf101/ucf101_video/' # sys.argv[1]
    save_dir = '/data1/lanhaoyuan/datasets/ucf101/ucf101_videoframes/' # sys.argv[2]

    for class_name in os.listdir(video_dir):
        class_process(video_dir, save_dir, class_name)

    # fw = open('log_cutvideos.txt', 'w')
    # fw.write("errornum:")
    # fw.writelines(errornum)
    # fw.write("\nnostream:")
    # fw.writelines(nostream)    
    # fw.close()

