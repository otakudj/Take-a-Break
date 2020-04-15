#!/usr/bin/python
# -*- coding: UTF-8 -*-

# GUI Import
import os
import numpy as np
import _tkinter
from tkinter import *
import random
import time
import cv2
import re
from config import *

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# GUI
class Take_a_Break():
    def video_player(self, cap, exer):
        # 弹出窗口，视频首先暂停
        img = cv2.imread(os.path.join(BASE_PATH, PATH_PIC, COVER))
        cv2.putText(img, 'Exercise', (100, 270), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 10)
        cv2.putText(img, 'Press space to start', (250, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 128, 128), 2)
        cv2.imshow('Take a Break', img)
        cv2.waitKey(0)

        for target in exer:
            print(target)
            # 捕获视频
            cap = cv2.VideoCapture(os.path.join(BASE_PATH, PATH, target))

            # 读取文字说明图片
            pic = cv2.imread(os.path.join(BASE_PATH,PATH_PIC, target.replace(FORMAT, FORMAT_PIC)))
            pic = pic[:, -450:, :]
            pic_height = pic.shape[0]

            while cap.isOpened():
                # t = time.time()
                ret, frame = cap.read()

                # 是否捕获到图片
                if frame is None:
                    break
                else:
                    frame = cv2.resize(frame, (pic_height, pic_height))
                    # 图片和视频帧拼接在一起
                    frame = np.concatenate((frame, pic), axis=1)

                # 调整窗口大小
                HEIGHT, WIDTH = frame.shape[0: 2]
                cv2.namedWindow('Take a Break', 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
                cv2.resizeWindow('Take a Break', WIDTH, HEIGHT)  # 设置长和宽
                cv2.imshow('Take a Break', frame)

                # 每帧延迟
                if cv2.waitKey(DELAY) == ord(START):
                    cv2.waitKey(0)

                # 按键开始/暂停播放

                # print(time.time() - t)

    def exercise_generater(self, vids, seq):
        if len(seq) < NUM:
            # 根据图片的数量，生成一个随机排列
            seq.extend(np.random.permutation(len(vids)))
        # 25个训练，4个为一组
        return [vids[seq.pop(0)] for _ in range(NUM)]

    def vid(self):
        # 读取vid_ch文件夹中的所有视频名称
        vids = [vid for vid in os.listdir(os.path.join(BASE_PATH, PATH)) if re.match(r'^ex[0-9]{2}\.' + str(FORMAT) + '$', vid)]
        seq = []

        # 无限循环
        while 1:
            exer = self.exercise_generater(vids, seq)
            cap = cv2.VideoCapture()

            self.video_player(cap, exer)

            cap.release()
            cv2.destroyAllWindows()

            # 结束一轮3个动作之后，40~50分钟之后进行下一组动作
            time.sleep(random.randint(40, 50) * 60)


if __name__ == '__main__':
    Take_a_Break().vid()
