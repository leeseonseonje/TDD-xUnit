from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.log = ''
        TestCase.__init__(self, name)

    def setUp(self):
        if self.name == 'setUp Exception':
            raise Exception
        self.log = 'setUp '
        
    def testMethod(self):
        self.log = self.log + 'testMethod '

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + 'tearDown '




