import os
import cv2


# 读取路径下的所有图片
def read_imgs_from(dir_path):
    if os.path.isdir(dir_path):
        imgs = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            imgs.append(cv2.imread(file_path, cv2.IMREAD_COLOR))
    else:
        raise Exception(dir_path + ' is not a document.')
    return imgs


# 图片灰度化处理
def imgs_graying(imgs):
    gray_imgs = []
    for img in imgs:
        gray_imgs.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    return gray_imgs


# 图片直方图均衡化
def imgs_hist_equalize(imgs):
    equ_imgs = []
    for img in imgs:
        if img.ndim == 2:
            equ_imgs.append(cv2.equalizeHist(img))
        else:
            raise Exception('Exist not gray image.')
    return equ_imgs


# 图片去噪 (MeanBlur,MediumBlur,GaussianBlur)
def imgs_denoise(imgs, method_name, ksize):
    deno_imgs = []
    if method_name == 'MeanBlur':  # 均值滤波
        for img in imgs:
            deno_imgs.append(cv2.blur(img, ksize))
    elif method_name == 'MediumBlur':  # 中值滤波
        for img in imgs:
            deno_imgs.append(cv2.medianBlur(img, ksize))
    elif method_name == 'GaussianBlur':  # 高斯滤波
        for img in imgs:
            deno_imgs.append(cv2.GaussianBlur(img, ksize, 0))
    else:
        raise Exception('Denoise do not have method name:' + method_name + '.')
    return deno_imgs


# 图片边缘检测 (Canny算法已进行Gaussian平滑去噪)
def imgs_edge_detect(imgs, low_threshold, high_threshold):
    edge_imgs = []
    for img in imgs:
        edge_imgs.append(cv2.Canny(img, low_threshold, high_threshold))
    return edge_imgs


# 二值化
def img_binarization(gray_imgs):
    binary_imgs = []
    bsize = 11
    c = 5
    for gray_img in gray_imgs:
        binary_img = cv2.adaptiveThreshold(
            src=gray_img,
            maxValue=255,
            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType=cv2.THRESH_BINARY_INV,
            blockSize=bsize,
            C=c
        )
        binary_imgs.append(binary_img)
        # 阈值函数：retval, dst = cv2.threshold(src, thresh, maxval, type)，返回值为retval, dst其中：
        # 输入：src是灰度图像,thresh是起始阈值,maxval是最大值,type是定义如何处理数据与阈值的关系。
        # 输出：dst：输出图像
    return binary_imgs
