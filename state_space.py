class StateSpace:
    def __init__(self, learningRate, discountFactor, statePoolSize):
        self.learningRate = learningRate
        self.discountFactor = discountFactor
        self.statePoolSize = statePoolSize
        self.qDict = {}

    def getQuality(self, pool, roundNum, rollNum, banksAction):
        keyVal = self.getKeyVal(pool, roundNum, rollNum, banksAction)

        if keyVal not in self.qDict.keys():
            self.qDict[keyVal] = 0
        return self.qDict[keyVal]

    def setNewQVal(self, pool, roundNum, rollNum, banksAction):
        lr = self.learningRate
        curVal = self.getQuality(pool, roundNum, rollNum, banksAction)
        reward = 0
        if banksAction is True:
            reward = pool

        nextVal = reward + self.discountFactor * self.estimatePool(pool)
        newVal = (1-lr) * curVal + lr * nextVal

        keyVal = self.getKeyVal(pool, roundNum, rollNum, banksAction)
        self.qDict[keyVal] = newVal

    def estimatePool(self, pool):
        newPool = 0
        newPool += 7 * 4/6
        newPool += pool * 1/6
        return newPool

    def getKeyVal(self, pool, roundNum, rollNum, banksAction):
        poolVal = pool // self.statePoolSize
        return f"{poolVal},{roundNum},{rollNum},{banksAction}"
