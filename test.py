#!/usr/bin/python
# -*- coding: UTF-8 -*-

# GUI Import
import os
import numpy as np
import _tkinter
from tkinter import *
import random
import time

# GUI
class Take_a_Break():
    def demo(self):
        def change_to_2():
        # 第二个按钮"next"的动作
            label.configure(image = exer2)
            button.configure(text = 'Next', command = change_to_3)

        def change_to_3():
        # 第三个按钮“Finished”的动作
            label.configure(image = exer3)    
            button.configure(text = 'Finished', command = close)

        def close():
        # 命令close的动作——关闭窗口
            top.destroy()
        
    # 读取pic_ch文件夹中的所有图片名称
        pics = [pic for pic in os.listdir('./pic_ch/')]

        # 无限循环
        while 1:
            # 根据图片的数量，生成一个随机排列
            seq = np.random.permutation(len(pics))

            # 24张图片，3个为一组
            for i in range(0, len(seq), 3):
        
                # 开启一个窗口
                top = Tk()

                # 标题
                top.title('Take a Break')

                # 本次Break的三张图片
                exer1 = PhotoImage(file = './pic_ch/' + pics[i])
                exer2 = PhotoImage(file = './pic_ch/' + pics[i + 1])
                exer3 = PhotoImage(file = './pic_ch/' + pics[i + 2])
                
                # 显示exercise1的图片
                label = Label(top, image = exer1)
                label.pack()
                
                # 按钮的动作
                button = Button(top, text = "Next", command = change_to_2)
                button.pack()
                button.focus_set()

                top.mainloop()

                # 结束一轮3个动作之后，40~50分钟之后进行下一组动作
                time.sleep(random.randint(40, 50) * 60)
 
if __name__=='__main__':
    Take_a_Break().demo()
