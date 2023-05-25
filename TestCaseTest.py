import unittest

from TestResult import TestResult
from TestSuite import TestSuite
from WasRun import WasRun


class TestCaseTest(unittest.TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run(self.result)
        assert 'setUp testMethod tearDown ' == test.log

    def testResult(self):
        test = WasRun('testMethod')
        test.run(self.result)
        assert '1 run, 0 failed' == self.result.summary()

    def testFailedResult(self):
        test = WasRun('testBrokenMethod')
        test.run(self.result)
        assert '1 run, 1 failed' == self.result.summary()

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert '1 run, 1 failed' == self.result.summary()

    def testSetupFailed(self):
        test = WasRun('setUp Exception')
        test.run(self.result)
        assert 'set up failed' == self.result.summary()

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        suite.run(self.result)
        assert '2 run, 1 failed' == self.result.summary()


if __name__ == '__main__':
    unittest.main()
