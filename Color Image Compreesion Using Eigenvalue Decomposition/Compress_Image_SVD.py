import numpy as np
from PIL import Image

def imgCompress(channel,percent):
    # channel表示需要进行压缩处理的单个颜色通道矩阵
    # percent表示利用SVD进行矩阵重建过程保留奇异值的百分比
    U, sigma, V_T = np.linalg.svd(channel)
    #对通道矩阵进行奇异值分解
    m = U.shape[0]
    n = V_T.shape[0]
    reChannel = np.zeros((m,n))
    # 初始化mxn大小的全零矩阵reChannel
    for k in range(len(sigma)):
        reChannel = reChannel + sigma[k]* np.dot(U[:,k].reshape(m,1),V_T[k,:].reshape(1,n))
        #依照percent参数值，取前k个奇异值
        #依照近似公式重建经过压缩处理的通道矩阵reChannel
        if float(k)/len(sigma) > percent:
            reChannel[reChannel < 0] = 0
            reChannel[reChannel > 255] = 255
            #需要把处理后的数据约束在0-255范围内
            break

    return np.rint(reChannel).astype("uint8")


# 对数值进行取证，类型为8位无符号整型

oriImage = Image.open(r'lenna.jpg', 'r')
imgArray = np.array(oriImage)

R = imgArray[:, :, 0]
G = imgArray[:, :, 1]
B = imgArray[:, :, 2]
# A = imgArray[:, :, 3]

for p in [0.001,0.005,0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    #p表示取所有奇异值的前多少比例
    reR = imgCompress(R, p)
    reG = imgCompress(G, p)
    reB = imgCompress(B, p)
    # reA = imgCompress(A, p)
    reI = np.stack((reR, reG, reB), 2)

    Image.fromarray(reI).save("{}".format(p)+"PercentCompressLenna.png")