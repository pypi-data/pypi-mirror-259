# cython:language_level=3
import numpy as np
import cv2 as cv
import os

class Img_base:

    #   0 参数设置
    def __init__(self):
        #   定位点圈定区域，可修改
        roi_pos = [
            [0, 250], [0, 2500]  # [startY, endY] [StartX, endX]
        ]
        #   定位点的兴趣区间
        self.roiPos = roi_pos
        #   定义灰度阈值
        self.gray_value = 0
        #   环境灰度值
        self.gray_round = 0

    #   1 图像旋转
    def rotate_img(self, img, angle):
        '''
        参数1  img           --输入图像
        参数2  angle         --旋转角度
        返回1  rotated_img   --输出旋转后的图像
        '''
        #   获取图像高度和宽度
        h, w = img.shape[:2]
        #   获取图像的中心点
        rotate_center = (w / 2, h / 2)
        #   获取旋转矩阵
        #   参数1为旋转中心点；
        #   参数2为旋转角度，正值-逆时针旋转；负值-顺时针旋转；
        #   参数3为各向同性的比例因子，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
        M = cv.getRotationMatrix2D(rotate_center, angle, 1.0)
        #   计算图像新边界
        new_w = int(h * np.abs(M[0, 1]) + w * np.abs(M[0, 0]))
        new_h = int(h * np.abs(M[0, 0]) + w * np.abs(M[0, 1]))
        #   调整旋转矩阵以考虑平移
        M[0, 2] += (new_w - w) / 2
        M[1, 2] += (new_h - h) / 2
        #   根据矩阵，旋转图像
        rotated_img = cv.warpAffine(img, M, (new_w, new_h))
        return rotated_img

    #   2 获取范围内灰度值总和
    def sum_gray(self, img, x, y, radius):
        '''
        参数1     img         --图像转化为灰度数值
        参数2     x           --横轴坐标
        参数3     y           --纵轴坐标
        参数4     radius      --圈定区域半径
        返回1     gray_sum    --圈定区域灰度均值
        '''
        gray_number = 0  # 获取灰度像素个数
        gray_sum = 0  # 获取灰度像素数值总和
        x_InitialPoint = x - radius  # 横向初始值
        y_InitialPoint = y - radius  # 纵向初始值
        #   查看圈定灰度区域是否超过阈值
        if (x + radius) >= img.shape[0] or (y + radius) >= img.shape[1]:
            return 0
        else:
            # 遍历区域内符合要求的像素点
            for i in range(radius * 2 + 1):
                for j in range(radius * 2 + 1):
                    gray_number += 1
                    gray_sum += img[x_InitialPoint + i, y_InitialPoint + j]
        return gray_sum  # 灰度值总和

    #   3 获取范围内灰度值总和的均值
    def sum_gray_ave(self, img, x, y, radius):
        '''
                img     --图像转化为灰度数值
                x       --横轴坐标
                y       --纵轴坐标
                radius  --圈定区域半径
                return  --圈定区域灰度均值
                '''
        gray_number = 0  # 获取灰度像素个数
        gray_sum = 0  # 获取灰度像素数值总和
        gray_ave = 0
        x_InitialPoint = x - radius  # 横向初始值
        y_InitialPoint = y - radius  # 纵向初始值
        #   查看圈定灰度区域是否超过阈值
        if (x + radius) >= img.shape[0] or (y + radius) >= img.shape[1]:
            return 0
        else:
            # 遍历区域内符合要求的像素点
            for i in range(radius * 2 + 1):
                for j in range(radius * 2 + 1):
                    gray_number += 1
                    gray_sum += img[x_InitialPoint + i, y_InitialPoint + j]
        gray_ave = int(gray_sum / gray_number * 100) / 100
        return gray_ave  # 灰度值总和

    #   4 删除缓存图片
    def clear_cache(self, path):
        os.remove(path)

    #   5 获取环境灰度值
    def get_gray_round(self, img):
        '''
        参数1 img --图像
        返回1 num --二值化阈值
        '''
        gray_number = 0  # 获取灰度像素个数
        gray_sum = 0  # 获取灰度像素数值总和
        gray_ave = 0  # 灰度像素均值
        x_InitialPoint = 800  # 横向初始值
        x_length = 600  # 横向长度
        y_InitialPoint = 300  # 纵向初始值
        y_length = 100  # 纵向长度
        #   图像转换为灰度值数组
        img_array = np.transpose(np.array(img))
        #   总和区域内的灰度值
        for i in range(x_length):
            for j in range(y_length):
                gray_number += 2
                gray_sum += img_array[x_InitialPoint + i, y_InitialPoint + j]
                gray_sum += img_array[x_InitialPoint + i, y_InitialPoint + 4700 + j]
        #   计算区域内灰度值均值
        gray_ave = gray_sum / gray_number
        self.gray_round = int(gray_ave * 100) / 100
        #   换算成二值化阈值
        num = int(gray_ave / 10) * 10 + 100

        return num

    #   6 输出试剂点X轴坐标
    def point_X(self, min, mid, max):
        '''
        参数1 min     --定位点X轴最小值
        参数2 mid     --定位点X轴中间值
        参数3 max     --定位点X轴最大值
        返回1 point   --试剂点X轴5个值
        '''
        point = [0] * 5
        point[0] = min
        point[1] = min + (mid - min) / 2
        point[2] = mid
        point[3] = max - (max - mid) / 2
        point[4] = max
        return point

    #   7 获取二维矩阵中最小值
    def find_min_value(self, arr):
        '''
        参数1 arr         --输入发光值矩阵
        返回1 min_value   --输出发光值最小值
        '''
        #   删除矩阵第一行数据
        arr = np.delete(arr, 0, axis=0)
        #   假设矩阵第一个是最小值
        min_value = arr[0][0]
        #   循环比较出最小值，输出最小值
        for row in arr:
            for num in row:
                if num < min_value:
                    min_value = num
        print("背景值-扣除：", int(min_value))
        return min_value

    #   8 过敏原性质判定
    def nature_positive_negative(self, g_arr, n_arr):
        '''
        参数1 g_arr   --发光值矩阵
        参数2 n_arr   --发光值性质矩阵
        返回1 n_arr   --返回赋值的性质矩阵
        '''
        #   判断发光值的性质
        for i in range(9):
            for j in range(5):
                if i > 0:
                    if g_arr[i][j] < 60000:
                        n_arr[i][j] = "阴性"
                    elif g_arr[i][j] < 660000:
                        n_arr[i][j] = "弱阳性"
                    elif g_arr[i][j] < 1100000:
                        n_arr[i][j] = "中阳性"
                    elif g_arr[i][j] > 1100000:
                        n_arr[i][j] = "强阳性"
                    else:
                        n_arr[i][j] = "error"
        return n_arr

class Img_show:

    #   0 参数设置
    def __init__(self):
        pass

    #   1 获取图像，并进行灰度化
    def img_read(self, path_read):
        '''
        参数1 path_read       --图像路径
        返回1 img_original    --原始图像
        '''
        #   读取原始图像，并灰度化
        img_original = cv.cvtColor(cv.imread(path_read), cv.COLOR_RGB2GRAY)
        #   获取图像的宽度和高度
        (w, h) = img_original.shape[:2]
        #   判断图像宽度和高度是否等于5472pix
        if w == 5472 and h ==5472:
            #   获取图像的中心点位
            center = (w // 2, h // 2)
            #   获取图像的旋转矩阵
            M = cv.getRotationMatrix2D(center, -90, 1.0)
            #   旋转图像
            img_original = cv.warpAffine(img_original, M, (w, h))
            #   圈定图像获取区域
            img_original = img_original[0:w, (h - 2300):h]
        else:
            pass

        return img_original

    #   2 图像二值化
    def img_dst(self, img, dat_num):
        '''
        参数1 img         --原始图像
        参数2 dat_num     --二值化阈值
        返回1 img_thres   --二值化图像
        '''
        #   二值化图像
        ret, img_thres = cv.threshold(img, dat_num, 255, cv.THRESH_BINARY)

        return img_thres

    #   3 图像腐蚀
    def img_erosion(self, img, num_erosion):
        '''
        参数1 img             --图像
        参数2 num_erosion     --腐蚀核（3,7,9,11）
        返回1 img_erosion     --腐蚀后图像
        '''
        #   设置图像腐蚀核系数
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (num_erosion, num_erosion))
        #   图像腐蚀
        img_erosion = cv.erode(img, kernel)

        return img_erosion

    #   4 图像膨胀
    def img_dilation(self, img, num_dilation):
        '''
        参数1 img             --图像
        参数2 num_erosion     --膨胀核（3,7,9,11）
        返回1 img_erosion     --膨胀后图像
        '''
        #   设置图像膨胀核系数
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (num_dilation, num_dilation))
        #   图像膨胀
        img_dilation = cv.dilate(img, kernel)

        return img_dilation
