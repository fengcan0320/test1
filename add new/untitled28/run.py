#coding=utf-8
from unittest import TestSuite,makeSuite
from HTMLTestRunner import HTMLTestRunner
from testCase import DetailById

a=TestSuite()
a.addTest(makeSuite(DetailById))
b=file("./result.html","wb")
c=HTMLTestRunner(b,1,u"自动化测试报告",u"本次测试情况如下：")
c.run(a)
b.close()