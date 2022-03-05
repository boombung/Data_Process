#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#移动全部nostream rgb
import os
import subprocess
nostream = ['/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/exercising arm/PtGNGYRj-dU_3_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/canoeing or kayaking/sGsyoycj2io_11_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/crying/Xg9hTAPBwi8_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/crying/kADmHBYICP0_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/golf driving/XwR141DQ0bI_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/golf driving/4cT-he9iVeI_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cleaning shoes/y7cYaYX4gdw_47_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/waxing chest/kinMMqkswUk_120_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/pushing wheelchair/6niTWNbMlPQ_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing discus/jgqtWGKvfrg_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing discus/qARO-sCN1NY_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing discus/sjk8kWkpUP8_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/catching or throwing frisbee/M5B0gaLdf9s_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/catching or throwing frisbee/tXQo-v3YG1g_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/catching or throwing frisbee/OwCpIFH664c_16_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/catching or throwing frisbee/06btONmXJvM_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing ice hockey/FqjWgc6fVJs_262_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing ice hockey/uL-LQMiiJ30_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/celebrating/WxQgGMGNQsI_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/kicking soccer ball/82ZyRSpQto8_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/kicking soccer ball/2jYBZzaKNjQ_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/kicking soccer ball/G4wg4yzR9R0_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/sign language interpreting/8sr2ggiN0EY_241_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/bench pressing/eVShyf30r1E_10_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/blowing out candles/3DDTRsPjzGU_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/kitesurfing/35Nir0FjBDc_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/passing American football (not in game)/nod9BS4pPCA_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/passing American football (not in game)/W2Z0ajHKQfA_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/spraying/DFJD0i5fESQ_29_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/carrying baby/8jQ8nHaGVuw_97_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/applying cream/0MCDeDNMYCQ_33_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/applying cream/Xjcu53HVpmY_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/snatch weight lifting/_FbtZJI1BxA_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/snowkiting/Yp86jbuVMDg_27_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hitting baseball/vqMWN5bNSVc_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/dunking basketball/gxgIdR6zHkM_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/dunking basketball/buUQJIlsjfI_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hockey stop/ywyLzdcxpe8_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hockey stop/DCByBzwckYs_3_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hockey stop/i_NUejA5XzY_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hockey stop/Y2dqfI5Y0UU_26_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/slapping/moqm9Y0lYU0_1_10.mp4' ,'/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/slapping/F4iyooQfQ0c_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/swimming backstroke/11ak7MOIROI_50_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shooting basketball/pVosOyq4Fkk_50_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shooting basketball/ViOe7R1vS4E_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shooting basketball/Wy8mC2JN5g0_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shooting basketball/5uxNAd-NItk_4_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/riding mule/6oK6oHYy1l0_26_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/springboard diving/PRkblEYb3j8_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/tossing coin/D8bbpO8t03o_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/tossing coin/5y6bmd2nVW4_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/ripping paper/fIhzZYSQNHQ_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/lunge/OROvBjIFd78_17_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/lunge/KPX_KDCrl7k_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/lunge/vELJweizh9A_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/lunge/dfuhc510GA8_16_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/lunge/b6ZTftUjSfo_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/eating carrots/aqwBNrughC4_26_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/paragliding/4PBnhCHK0_M_3_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/moving furniture/bOL0aAwxDdQ_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/feeding goats/CTTpoMCHQ9A_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing squash or racquetball/SI1vZrfOeFU_64_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/high jump/b3PjtQpg_Kk_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/high jump/DUMv6JlC7E8_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/jogging/iLOOdW3SS7Q_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/parkour/rF-fiSJXu9E_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/water sliding/CB0n3xIAZFA_5_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/water sliding/hfgZ0lXrnHQ_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cooking sausages/DMyjP7LxzAQ_57_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/bouncing on trampoline/NW2cmBYr-lU_4_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/using computer/goK1Ct-HEPU_3_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/using computer/VtXET-IJ_fo_25_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/drop kicking/RWeyaLThBZw_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/training dog/mmgivQevR-Y_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/sled dog racing/iIYLCydMhU4_16_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/grooming dog/qS_Oh45nTfs_3_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/grooming dog/_G9D9Ms_TJo_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing poker/2xWiEVNUvhE_64_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/eating chips/LQLqvHyCPOM_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/holding snake/uvIh2s0lInM_3_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/holding snake/MRW4AouZ3cM_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/EwBxpirRlxY_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/EywTSGp14bg_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/vrsmeS_uN34_4_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/5AkgSP4UxIM_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/DugL11IliYA_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/ulIXx0bFtkc_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/7sWuxwpPNUU_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/7XZ3mZ3wZ20_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cracking neck/WhFeZ-dAZsI_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/beatboxing/x8FEbEMK4rw_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/beatboxing/yxSzPVesKxA_206_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/pole vault/5FTXZ6671SE_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/pole vault/TPHo3JzGhms_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing basketball/hKigO1XSAJo_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/kicking field goal/wD3G9Rj_jBo_12_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/pumping fist/LL6spoQdwno_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hurdling/H-5mj_Ye4pg_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing cricket/rf7TDUNmO9U_4_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/long jump/dcMN4JFjzFQ_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/long jump/0ug8QzhesOw_3_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/long jump/QGCQ7ZOjbeg_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/stretching leg/Ev08RdZrOLk_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/stretching leg/Kiw_jt12c3k_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/auctioning/Lw14NH9kAqE_759_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/petting cat/NAcuFPbn458_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/gargling/-Ng5opbmX0o_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/mf2QPxb95R0_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/ZYK58As-rDQ_4_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/tsv_-bEzUtY_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/19xXExyzZRo_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/q3zxzOlYJpQ_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/TqEFIy5HgZI_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/5Rhw9TL0z3g_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/UbByX0Vylbs_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/ob2yMCXjCmo_2_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/M6m-g8UqAL4_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/bONrrCJtZ8Q_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/finger snapping/CjxzEM53ZAE_4_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cartwheeling/cArJKtGaDFU_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/golf putting/fOfCvlhAg_0_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/swinging legs/emnBCTEPZeU_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/doing laundry/n0lW3I2DbqE_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing paintball/aWc1SjfSEIw_59_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/playing cello/X2ER3v4zVFU_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/climbing a rope/sGBEm64VxP0_11_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/driving car/RZvkqvvjLOg_183_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/jumping into pool/sJukApNxtBg_1_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/jumping into pool/OmStc__WJtE_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/peeling potatoes/ZJ8yj3OhJeI_4_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/hammer throw/_1YHBwzCuWk_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shot put/G_s9ZjA-Of4_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/rock climbing/UOSadtfc1sA_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/carving pumpkin/u6Vg_x8O62o_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/making bed/hJBXjYEiyKM_2_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/cleaning windows/K7QLhUFtZ1Q_5_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/eating hotdog/CxjipYE57Yo_199_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/tobogganing/aflwG5gKd3g_11_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/tobogganing/OADBCsCxkIE_10_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shooting goal (soccer)/e6JCMYRN72E_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/fixing hair/EPuqSs90NZ0_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/peeling apples/eG_BgAnQAYI_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/water skiing/-0Kz1lwvjdU_6_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/catching or throwing baseball/ZE7Ea4W6tKY_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing ball/svkX1fWGLKc_1_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shaking hands/xHDuPc9G0EE_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/shaking hands/SZNOraGpKyM_10_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/flipping pancake/vPbHGo3cq-c_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/flipping pancake/qTd5IAq_6NQ_0_10.mp4',
            '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing axe/3XQqsYmUmvM_16_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing axe/3A8xozP6k4M_0_10.mp4', '/data1/lanhaoyuan/datasets/kinetics/kinetics_video/test/throwing axe/Mmj9k2ktBCo_11_10.mp4']
basepath = "/data1/lanhaoyuan/datasets/kinetics/kinetics_rgb/"
allrgb = basepath + "test_normalsize/"
flag = 0
nostreamrgb = basepath + "test-normal-nostream/"
for filepath in nostream:
    dst_class_path = nostreamrgb + filepath.split('/')[-2]
#     if not os.path.exists(dst_class_path):
#         os.makedirs(dst_class_path)
    name, ext = os.path.splitext(filepath.split('/')[-1])
    #dst_path = dst_class_path + '/' + name + '.jpg'
    dir_allrgb = allrgb + filepath.split('/')[-2] + '/' + name
    if not os.path.exists(dir_allrgb):
        flag += 1 
        continue
    cmd = 'mv \"{}\" \"{}\"'.format(dir_allrgb, dst_class_path)
    fw = open('log0.txt', 'a')
    fw.write(cmd)
    fw.write('\n{}\n'.format(flag))
    fw.close()    
    subprocess.call(cmd, shell=True)
print(flag)

