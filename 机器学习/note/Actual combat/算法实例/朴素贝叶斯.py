# coding=utf-8
from numpy import *

def loadDataSet():
    postingList = [[1,'S'],
                   [1,'M'],
                   [1, 'M'],
                   [1, 'S'],
                   [1, 'S'],
                   [2, 'S'],
                   [2, 'M'],
                   [2, 'M'],
                   [2, 'L'],
                   [2, 'L'],
                   [3, 'L'],
                   [3, 'M'],
                   [3, 'M'],
                   [3, 'L'],
                   [3, 'L']]
    classVec = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
    return postingList,classVec

def calProb(featVec,dataSet):
    x1Labels = [temp[0] for temp in dataSet]
    x2Labels = [temp[1] for temp in dataSet]
    x1Counts ={};x2Counts = {}
    for label in x1Labels:
        if label not in x1Counts.keys():
            x1Counts[label] = 0
        x1Counts[label] += 1
    for label in x2Labels:
        if label not in x2Counts.keys():
            x2Counts[label] = 0
        x2Counts[label] += 1
    px1 = x1Counts[featVec[0]]/float(len(dataSet))
    px2 = x2Counts[featVec[1]] / float(len(dataSet))
    return px1*px2

def naiveBayes(featVec):
    trainingSet, labels = loadDataSet()
    cateCounts = {}
    for category in labels:
        if category not in cateCounts.keys():
            cateCounts[category] = 0
        cateCounts[category] += 1
    pPositive = cateCounts[1] / float(len(labels))
    pNegative = 1 - pPositive
    positiveMat = []; negativeMat = []
    for i in range(len(trainingSet)):
        if labels[i] == 1:
            positiveMat.append(trainingSet[i])
        else:
            negativeMat.append(trainingSet[i])
    posProb = calProb(featVec, positiveMat) * pPositive
    print(posProb)
    negProb = calProb(featVec, negativeMat) * pNegative
    print(negProb)
    if posProb >= negProb:
        print('the category is 1')
    else:
        print('the category is -1')

naiveBayes([2, 'S'])