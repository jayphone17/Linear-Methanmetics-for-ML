import numpy as np
import xlrd

def excel_to_Matrix(path):
#读excel数据转为矩阵函数
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    #获取excel中第一个sheet表
    nrows = table.nrows
    #行数
    ncols = table.ncols
    #列数
    datamatrix = np.zeros((nrows, ncols))
    for x in range(ncols):
        cols = table.col_values(x)
        cols1 = np.matrix(cols)
        #把list转换为矩阵进行矩阵操作
        datamatrix[:, x] = cols1
        #把数据进行存储
    return datamatrix

sourceData = excel_to_Matrix("评分表.xlsx")

def cosSim(vector_1,vector_2):
    dotProd = float(np.dot(vector_1.T , vector_2))
    normProd = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
    return 0.5 + 0.5 * (dotProd / normProd)

def estimateScore(sourceData,sourceDataRC,userIndex,itemIndex):
    n = np.shape(sourceData)[1]
    #获取菜品总数
    scoreMutipleCosSimSum = 0
    #加权相似度之和
    cosSimSum = 0
    #itemIndex菜品与其他菜品两两相似度之和
    for i in range(n):
        userScore = sourceData[userIndex,i]
        if userScore ==0 or i == itemIndex:
            continue
        weight = cosSim(sourceDataRC[:, i],sourceDataRC[:, itemIndex])
        #利用SVD后的矩阵
        #itemIndex与第i个菜品的相似度
        cosSimSum = float(cosSimSum + weight)
        scoreMutipleCosSimSum = scoreMutipleCosSimSum + userScore * weight
    if cosSimSum == 0 :
        return 0
    return scoreMutipleCosSimSum / cosSimSum

U, sigma, VT = np.linalg.svd(sourceData)
sigmaSum = 0
k_num = 0

for k in range(len(sigma)):
    sigmaSum = sigmaSum + sigma[k] * sigma[k]
    if float(sigmaSum) / float(np.sum(sigma ** 2)) > 0.9:
        k_num = k+1
        break
sigma_k = np.mat(np.eye(3) * sigma[:3])
sourceDataRC = sigma_k * U.T[:3,:] * sourceData

n = np.shape(sourceData)[1]
userIndex = 23
for i in range(n):
    userScore = sourceData[23,i]
    if userScore != 0 :
        continue
    print("index:{},score:{}".format(i,estimateScore(sourceData,sourceDataRC,userIndex,i)))