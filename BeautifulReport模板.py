
import unittest
import BeautifulReport


class Test(unittest.TestCase):
    def test_01(self):
        print("测试用例1")

    def test_02(self):
        print("测试用例2")

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTests(unittest.TestLoader.loadTestsFromTestCase(Test))
    result = BeautifulReport.BeautifulReport(testunit)
    result.report(filename='report',description='测试报告',log_path = None)




