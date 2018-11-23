#coding:utf-8
"""
NAME:01.手写数字识别.py
Author:刘立东
Contect:1147024853@qq.com
Date:2018-11-14
Desc:
"""
from numpy import *
import numpy as np
from os import listdir
import operator

#能够在输出时不隐藏
np.set_printoptions(threshold=np.NaN)


#训练
#KNN--初步步骤：
#1.整理数据
#读取数据到矩阵
#功能：传一个文件名，我就读取该文件，并且将该文件的内容存储在一个1*1024的矩阵当中
def img2vector(filename):
    #创建向量--用于存储文件的内容
    vect = zeros((1,1024))

    #读取文件
    fr = open(filename)
    for i in range(32):#每个文件有32行
        lineStr = fr.readline()#读取每行的内容
        # '00000000000001100000000000000000'

        #
        for j in range(32):#每行有32个字符
            vect[0,32*i+j]= lineStr[j]

    return vect

def trainingFunc():

    #样本数据的类标签列表
    hwLabels = []

    #把该目录下所有的文件都放在列表当中
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)#有多少个文件

    #初始化样本数据矩阵（M*1024）--用于存储所有文件的内容
    trainingMat = zeros((m,1024))

    #依次读取所有样本数据到数据矩阵trainingMat
    for i in range(m):
        fileNameStr = trainingFileList[i]#文件名，例如：0_101.txt

        #读取单个文件到矩阵当中--singleFileVect
        fullFileName = 'digits/trainingDigits/%s'%fileNameStr
        singleFileVect = img2vector(fullFileName)

        #将单个文件数据放到trainingMat
        trainingMat[i,:] = singleFileVect

        #存储对应的类标签
        numStr = fileNameStr.split('_')[0]#例如：把0_101.txt中‘0’（下划线前）取出来
        hwLabels.append(int(numStr))
    # print('trainingMat:',trainingMat.shape)
    # print('hwLabels count:',len(hwLabels))
    #类标签与矩阵当中的数据一一对应---表示机器已经学习到了判定的依据
    # print(hwLabels[0],trainingMat[0,:])

    #检验我们的机器学习的准确率
    testFunc(trainingMat,hwLabels)

#测试
def testFunc(trainingMat,hwlabels):
    #初始化错误率
    errorCount = 0.0

    #读取测试集数据
    testFileList = listdir('digits/testDigits')
    for i in range(len(testFileList)):
        fileNameStr = testFileList[i]

        #实际结论
        trueResult =int( fileNameStr.split('_')[0])

        #预测结论
        #（1）读文件
        fullFileName = 'digits/testDigits/%s'%fileNameStr
        singleFileVect = img2vector(fullFileName)

        #（2）预测---对数据文件进行分类
        result = classify(singleFileVect,trainingMat,hwlabels,3)

        print('实际值：',trueResult,' -----预测值:',result)


        #错误率统计
        if trueResult != result:
            errorCount+=1

    #分类器的准确率
    rate=1-errorCount/len(testFileList)
    print('准确率能达到：',rate)

#kNN实现分类器
# 功能：通过传入一个文件，预测这个文件是哪个一数字
def classify(inX,dataSet,hwLabels,k):
    #获取样本数据数据
    dataSetSize = dataSet.shape[0]#取出多少条数据

    # 2.计算距离
    #矩阵运算
    # inX---1*1024----->1934*1024
    newX= tile(inX,(dataSetSize,1))#1934*1024
    # （1）相减  （2）平方
    sq_X = (newX -  dataSet)**2
    # （3）求和
    sum_line_X_= sq_X.sum(axis=1)

    # （4）开方
    distances =sum_line_X_**0.5

    #3.排序
    #间接排序---因为不能够打乱原始数据的位置，因为原始数据与hwlabels是一一对应的
    sortedDis = distances.argsort()

    #4.选k个样本，做类标签的统计
    numDict = {}
    for i in range(k):
        #依次取出最近的样本数据
        #记录该样本所属类别---类标签
        num = hwLabels[sortedDis[i]]
        numDict[num] = numDict.get(num,0)+1

    #统计谁出现的次数最多
    sortedData = sorted(numDict.items(),key=operator.itemgetter(1),reverse=True)

    return sortedData[0][0]

if __name__ == '__main__':
    # result = img2vector('digits/testDigits/0_0.txt')
    # print(result)
    trainingFunc()