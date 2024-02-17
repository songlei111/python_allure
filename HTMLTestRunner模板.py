
import unittest
import  HTMLTestRunner


class Test(unittest.TestCase):
    def test_01(self):
        print("测试用例1")

    def test_02(self):
        print("测试用例2")

if __name__ == '__main__':
    fp= open('D:/appium1/result.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告，测试结果如下：',
                                           description=u'用例执行情况')
    testunit = unittest.TestSuite()
    testunit.addTests(unittest.TestLoader.loadTestsFromTestCase(Test))
    runner.run(testunit)

    fp.close()


