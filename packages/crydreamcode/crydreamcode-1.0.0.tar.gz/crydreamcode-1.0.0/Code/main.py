import sys
import os

sys.path.append(os.path.dirname(__file__))

from AnalysisiMerterCore.imgCore import Img_core

class Print_log:
    # 程序初始化
    def __init__(self):
        #   初始化
        self.imgCore = Img_core()

    #   图像处理日志
    def Img_process_log(self):
        return True
