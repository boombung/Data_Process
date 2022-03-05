import numpy as np
import librosa
import pickle
import os
import pdb
import cv2

# def scale_minmax(X, min=0.0, max=1.0):
#     X_std = (X - X.min()) / (X.max() - X.min())
#     X_scaled = X_std * (max - min) + min
#     return X_scaled

def spectrogram_image(S):
    eps=1e-6
    xmin = np.min(S)
    xmax = np.max(S)

    scale_p = (S-xmin) / ((xmax-xmin)+eps) * 255
    scale_p = np.flip(scale_p,axis=0)
    scale_p = scale_p.astype(np.uint8)
    # mels = S 
    # # min-max scale to fit inside 8-bit range
    # img = scale_minmax(mels, 0, 255).astype(np.uint8)
    # img = np.flip(img, axis=0) # put low frequencies at the bottom in image
    # img = 255-img # invert. make black==more energy
    return scale_p

# 1s提取16张mel图：
def audio_extract(wav_file, save_path, sr=24000):
    wav, cur_sr = librosa.load(wav_file, sr=sr)
    eps=1e-6
    if cur_sr != sr:
        pdb.set_trace()
    secs = int(len(wav)/sr)  # 音频时长=音频信号值/采样率
    # print(secs)
    count = 0
    for i in range(secs):
        for j in range(16):
            count += 1
            start = int(sr * (i + j/16.0))
            end = int(sr * (i + (j + 1)/16.0))
            cur_wav = wav[start:end]
            #spec = librosa.core.stft(cur_wav, n_fft=0.01*sr, hop_length=0.005*sr, 
            #    window='hann', center=True, pad_mode='constant')
            # spec = librosa.core.stft(cur_wav, n_fft=160, hop_length=80, 
            #     window='hann', center=True, pad_mode='constant')
            # spec = np.log(np.real(spec * np.conj(spec)) + eps)
            # mel = librosa.feature.melspectrogram(S = np.abs(spec), sr=sr, n_mels=128, fmax=sr/2) hop_length = 128,
            mel = librosa.feature.melspectrogram(y = cur_wav, sr = sr, n_mels = 256, fmax = sr/2, win_length = 10, hop_length=10)
            log_mel = librosa.core.power_to_db(mel, ref=np.max)
            log_img = spectrogram_image(log_mel)
            # log_mel_T = log_img.T.astype('float32')
            # assert log_mel_T.shape == (201,32)

            im_color = cv2.applyColorMap(log_img, 13) # COLORMAP_MAGMA 

            save_name = os.path.join(save_path, 'frame{:06d}.jpg'.format(count))  # i
            
            cv2.imencode('.jpg', im_color)[1].tofile(save_name)
            # with open(save_name, 'wb') as fid:
            #     pickle.dump(log_mel_T, fid)

# 一段音频提取一张mel图：
def audio_extract_whole(wav_file, save_path, sr=24000):
    wav, cur_sr = librosa.load(wav_file, sr=sr)
    eps=1e-6
    if cur_sr != sr:
        pdb.set_trace()
    mel = librosa.feature.melspectrogram(y = wav, sr = sr, n_mels = 256, fmax = sr/2, win_length = 1024, hop_length=512)
    log_mel = librosa.core.power_to_db(mel, ref=np.max)
    log_img = spectrogram_image(log_mel)

    im_color = cv2.applyColorMap(log_img, 13) # COLORMAP_MAGMA 

    video_name = save_path.split('/')[-1]
    save_name = os.path.join(save_path, '{}.jpg'.format(video_name)) 
            
    cv2.imencode('.jpg', im_color)[1].tofile(save_name)



def class_process(audio_dir, save_dir, class_name):
    class_path = os.path.join(audio_dir, class_name)
    if not os.path.isdir(class_path):
        return

    dst_class_path = os.path.join(save_dir, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)

    for each_audio in os.listdir(class_path):
        if not each_audio.endswith('.wav'):
            continue
        audio_path = os.path.join(class_path, each_audio)
        save_path = os.path.join(dst_class_path, each_audio[:-4])
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        audio_extract_whole(audio_path, save_path)
 
if __name__=="__main__":
    
    audio_dir = '/data1/lanhaoyuan/datasets/ucf101/ucf101_audio/' # sys.argv[1]
    save_dir = '/data1/lanhaoyuan/datasets/ucf101/ucf101_rgbflowspec/wholemel/470x256/' # sys.argv[2]
 
    for class_name in os.listdir(audio_dir):
        class_process(audio_dir, save_dir, class_name)
