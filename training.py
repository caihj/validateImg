#coding:utf-8





connectionRate = 1
learningRate = 0.008
desiredError = 0.001
maxIterations = 10000
iterationsBetweenReports = 100
inNum= 256
hideNum = 64
outNum=10
class NeuNet(neural_net):
	def __init__(self):
		neural_net.__init__(self)
		neural_net.create_standard_array(self,(inNum, hideNum, outNum))


	def train_on_file(self,fileName):
		neural_net.train_on_file(self,fileName,maxIterations,iterationsBetweenReports,desiredError)