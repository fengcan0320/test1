# coding=utf-8
from API import getDetailById,postCreateDev
from public import readExcel
from unittest import TestCase
import pymysql,requests

class DetailById(TestCase): #连接数据库写法
    def test001(self):
        c=pymysql.connect(host="192.168.1.200",port=3306,user="root",password="123456",db="db_public")#连接数据库
        new=c.cursor()#创建一个游标，相当于新建查询器
        new.execute("SELECT name FROM t_dev_list WHERE id=13")#返回的是行数
        SqlResult=new.fetchone()
        (name,)=SqlResult
        requestResult=getDetailById(readExcel("getDetailById",1,2))
        #excelResult='{"msg": "Success", "code": 0, "data": {"id": 13, "name": "%s"}}'%name
        excelResult=readExcel("getDetailById",1,3)%name
        self.assertEqual(requestResult,excelResult)

    def test002(self):
        c=pymysql.connect(host="192.168.1.200",port=3306,user="root",password="123456",db="db_public")#连接数据库
        new=c.cursor()#创建一个游标，相当于新建查询器
        self.assertEqual(new.execute("SELECT * FROM t_dev_list WHERE id=1"),0)
        self.assertEqual(getDetailById(readExcel("getDetailById",2,2)),readExcel("getDetailById",2,3))
'''
class DetailById(TestCase):  #简单写法
    def test001(self):
        self.assertEqual(getDetailById(readExcel("getDetailById",1,2)),readExcel("getDetailById",1,3))
        print "pass"

    def test002(self):
        self.assertEqual(getDetailById(readExcel("getDetailById",2,2)),readExcel("getDetailById",2,3))
        print "pass"

    def test003(self):
        self.assertEqual(getDetailById(readExcel("getDetailById",3,2)),readExcel("getDetailById",3,3))
        print "pass"

    def test004(self):
        self.assertEqual(getDetailById(readExcel("getDetailById",4,2)),readExcel("getDetailById",4,3))
        print "pass"
'''

class CreateDev(TestCase): #简单写法
    def test001(self):
        self.assertEqual(postCreateDev(readExcel("createDev",1,2)),readExcel("createDev",1,3))

    def test002(self):
        self.assertEqual(postCreateDev(readExcel("createDev",2,2)),readExcel("createDev",2,3))

#作业：在下面写，参考上面的DetailById类写法，用连接数据库写法，检查新建之后，请求的SN码是不是与数据库的SN码一致