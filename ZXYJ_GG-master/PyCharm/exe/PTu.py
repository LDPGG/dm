# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 0027 下午 1:46
# @Author  : 刘登攀阿！！
# @FileName: PTu.py
# @Software: PyCharm

import cv2
import os
import sys
import re
'''
美化图片
'''

def tt():
    # 加载一张图片
    print('------------提示：文件夹路径与文件夹命名只能带字母--------------------')
    print('-------------放入图片------------------')
    print('提示：需要带后缀哟！！！')
    a = input('请输入您的图片地址(如：D:\PyCharm\\tt.jpg):')
    # sele_images = os.path.isfile(a)
    if os.access(a, os.F_OK):
        images = cv2.imread(a)
        # 图片美白 值越大，美白效果越大
        value = 15
        images_date = cv2.bilateralFilter(images, value, value * 2, value / 2)
        # 生成图片
        print('------------------保存图片--------------------------')
        b = input('请输入您要保存的图片地址(如：F:\)：')
        if os.access(b, os.F_OK):
            print('提示：暂时只支持字母命名哦！！！')
            panduan = re.compile('[\u4e00-\u9fa5]')
            c = input('请给您的图片取一个名字（如：tupian,gg）：')
            sele_c = panduan.search(c)
            # 检查是否是汉字
            if sele_c is None:
                cv2.imwrite(b + '\\' + c + '.jpg', images_date)
                print('P图成功，请在' + b + '中查看您的图片，谢谢使用！')
            else:
                pp = input('因为软件暂不支持中文命名，所以现在已死机,输入1关闭软件，输入任意数重启软件：')
                if pp == '1':
                    print('谢谢您的使用，再见')
                    # 关闭程序
                    sys.exit()
                else:
                    # 回调方法
                    tt()
            # 创建一个窗口
            cv2.namedWindow('images')
            # # 展示窗口
            cv2.imshow('images', images_date)
            # # 窗口等待
            cv2.waitKey(0)
            # # 销毁窗口
            cv2.destroyAllWindows()
        else:
            pp = input('因为没有找到您要保存的文件夹，所以现在已死机,输入1关闭软件，输入任意数重启软件：')
            if pp == '1':
                print('谢谢您的使用，再见')
                # 关闭程序
                sys.exit()
            else:
                # 回调方法
                tt()
    else:
        pp = input('因为没有找到您的文件，所以现在已死机,输入1关闭软件，输入任意数重启软件：')
        if pp == '1':
            print('谢谢您的使用，再见')
            # 关闭程序
            sys.exit()
        else:
            # 回调方法
            tt()


# 运行代码
if __name__ == '__main__':
    tt()