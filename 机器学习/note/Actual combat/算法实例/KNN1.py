# coding=utf-8
from numpy import *
import operator

class KNNClassifier():
    def __init__(self,k=3):
        self._k = k

    def _calDistance(self,inputX,trainX):
        dataSetSize=trainX.shape[0]

        diffMat=tile(inputX,(dataSetSize,1))-trainX
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistIndicies = distances.argsort()
        return sortedDistIndicies

    def _classify(self, sample, trainX, trainY):
        if isinstance(sample, ndarray) and isinstance(trainX, ndarray) and isinstance(trainY, ndarray):
            pass
        else:
            try:
                sample = array(sample)
                trainX = array(trainX)
                trainY = array(trainY)
            except:
                raise TypeError("numpy.ndarray	required	for	trainX	and	..")
        sortedDistIndicies = self._calDistance(sample, trainX)
        classCount = {}
        for i in range(self._k):
            label = trainY[sortedDistIndicies[i]]
            classCount[label] = classCount.get(label, 0) + 1
        sorteditem = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sorteditem[0][0]

    def classify(self, inputX, trainX, trainY):
        if isinstance(inputX, ndarray) and isinstance(trainX, ndarray)and isinstance(trainY, ndarray):
            pass
        else:
            try:
                inputX = array(inputX)
                trainX = array(trainX)
                trainY = array(trainY)
            except:
                raise TypeError("numpy.ndarray	required	for	trainX	and	..")
        d = len(shape(inputX))
        results = []
        if d == 1:
            result = self._classify(inputX, trainX, trainY)
            results.append(result)
        else:
            for i in range(len(inputX)):
                result = self._classify(inputX[i], trainX, trainY)
                results.append(result)
        return results

if __name__=="__main__":
    trainX = [[1, 1.1],
              [1, 1],
              [0, 0],
              [0, 0.1]]
    trainY = ['A', 'A', 'B', 'B']
    clf = KNNClassifier(k=3)
    inputX = [[0, 0.1], [0, 0]]
    result = clf.classify(inputX, trainX, trainY)
    print(result)