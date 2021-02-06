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
print(sourceData)