
#生成自动化测试报告#
# main函数放到测试脚本中时，无法生成测试结果和测试报告
# 测试 test_demo2.py 脚本
import pytest
import os


if __name__ == '__main__':
    pytest.main(['-s','test_demo2.py','--alluredir','./result'])   #生成测试结果 result
    os.system('allure generate ./result -o  ./report')  #自动生成报告