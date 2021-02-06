import numpy as np
sourceData  = np.mat([[4,2,2,5],
                      [1,1,0,1],
                      [4,0,4,4],
                      [3,0,2,4],])

def cosSim(vector_1,vector_2):
    dotProd = float(np.dot(vector_1.T,vector_2))
    normProd = np.linalg.norm(vector_1) * np.linalg.norm(vector_2)
    return 0.5 + 0.5 * (dotProd / normProd)

print(cosSim(sourceData[:,0],sourceData[:,1]))
#叉烧肠粉与新疆手抓饭相似度
print(cosSim(sourceData[:,0],sourceData[:,2]))
#叉烧肠粉与四川火锅相似度
print(cosSim(sourceData[:,0],sourceData[:,3]))
#叉烧肠粉与粤式叉烧饭相似度
print(cosSim(sourceData[:,1],sourceData[:,2]))
#新疆手抓饭与四川火锅相似度
print(cosSim(sourceData[:,1],sourceData[:,3]))
#新疆手抓饭与粤式叉烧饭相似度
print(cosSim(sourceData[:,2],sourceData[:,3]))
#四川火锅与粤式叉烧饭