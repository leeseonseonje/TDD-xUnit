class TestResult:

    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
        self.isSetUpFailed = False

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.failureCount = self.failureCount + 1

    def setUpFailed(self):
        self.isSetUpFailed = True

    def summary(self):
        if self.isSetUpFailed:
            return 'set up failed'
        return '%d run, %d failed' % (self.runCount, self.failureCount)
