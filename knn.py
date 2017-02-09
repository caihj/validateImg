from numpy import *
import operator
from os import listdir
import matplotlib
import matplotlib.pyplot as plt
import pdb


def classify0(inX, dataSet, labels, k=3):
    # pdb.set_trace()
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # ascend sorted,
    # return the index of unsorted, that is to choose the least 3 item
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,
                                                0) + 1  # a dict with label as key and occurrence number as value
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    '''descend sorted according to value, '''
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    # pdb.set_trace()
    L = fr.readlines()
    numberOfLines = len(L)  # get the number of lines in the file
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    index = 0
    for line in L:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        # classLabelVector.append((listFromLine[-1]))
        index += 1
    fr.close()
    return returnMat, classLabelVector


def plotscattter():
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')  # load data setfrom file
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    ax3 = fig.add_subplot(111)
    ax1.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    # ax2.scatter(datingDataMat[:,0],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    # ax2.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
    return normDataSet, ranges, minVals


def datingClassTest(hoRatio=0.20):
    # hold out 10%
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')  # load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print
        "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print
    "the total error rate is: %.2f%%" % (100 * errorCount / float(numTestVecs))
    print
    'testcount is %s, errorCount is %s' % (numTestVecs, errorCount)


def classifyPerson():
    '''
    input a person , decide like or not, then update the DB
    '''
    resultlist = ['not at all', 'little doses', 'large doses']
    percentTats = float(raw_input('input the person\' percentage of time playing video games:'))
    ffMiles = float(raw_input('flier miles in a year:'))
    iceCream = float(raw_input('amount of iceCream consumed per year:'))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    normPerson = (array([ffMiles, percentTats, iceCream]) - minVals) / ranges
    result = classify0(normPerson, normMat, datingLabels, 3)
    print
    'you will probably like this guy in:', resultlist[result - 1]

    # update the datingTestSet
    print
    'update dating DB'
    tmp = '\t'.join([repr(ffMiles), repr(percentTats), repr(iceCream), repr(result)]) + '\n'

    with open('datingTestSet2.txt', 'a') as fr:
        fr.write(tmp)


def img2file(filename):
    # vector = zeros(1,1024)
    with open(filename) as fr:
        L = fr.readlines()
    vector = [int(L[i][j]) for i in range(32) for j in range(32)]
    return array(vector, dtype=float)


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')  # load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')  # iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print
        "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print
    "\nthe total number of errors is: %d" % errorCount
    print
    "\nthe total error rate is: %f" % (errorCount / float(mTest))


if __name__ == '__main__':
    datingClassTest()
    # handwritingClassTest()