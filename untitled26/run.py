#coding=utf-8
from unittest import TestSuite,makeSuite
from login_testCase import login
from customer_testCase import customer
from leads_testCase import leads
from HTMLTestRunner import HTMLTestRunner

a=TestSuite() #定义一个测试集，相当于一个容器
#a.addTest(makeSuite(login,"case"))#makeSuite（）指要执行的测试测试类，和以什么开头的方法, addTest往测试集里面添加测试项
#a.addTest(makeSuite(customer,"test"))
#a.addTest(makeSuite(leads,"test"))
for ClassName,TestDef in [[login,"case"],[customer,"test"],[leads,"test"]]:
    a.addTest(makeSuite(ClassName,TestDef))
b=file("./result.html","wb")#file文件读写类，./result.html指在当前目录生成叫result.html的文件，"wb"指写操作和每次都覆盖操作
c=HTMLTestRunner(b,1,u"自动化测试报告",u"本次测试情况如下：")
#HTMLTestRunner指导入的HTMLTestRunner插件类支持html文件读写
#b,指HTMLTestRunner往b对象输出内容，1版本号，u"自动化测试报告"指标题，u"本次测试情况如下：指描述
c.run(a)#指HTMLTestRunner执行的run方法，run（）里面的参数指要执行的测试集a
b.close()#关闭文件读写