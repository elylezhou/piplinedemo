#coding=utf-8
import unittest
#这里需要导入测试文件
import baidu
import youdao
import HTMLTestRunner

testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)
#定义个报告存放路径，支持相对路径。
filename = 'result.html'
fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
stream=fp,
title=u'搜索网站测试报告',
    description=u'用例执行情况：')

#执行测试用例
runner.run(testunit)
