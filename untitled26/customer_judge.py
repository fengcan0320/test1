#coding=utf-8
from customer_element import c_customerRightText,c_custmoerErrorText
from public import windowsText

def customerRight(self):
    b=c_customerRightText(self)
    if b==u"""×
添加客户成功""":
        print u"新建正确的客户名测试通过"
        return True
    else:
        print u"新建正确的客户名测试失败"
        return False

def customerWindowsText(self,customerName):
    b=windowsText(self)
    if customerName !="":
        if b==u"该客户名称不可用，请更换客户名称":
            print u"重复客户名弹出框提示语正确"
            return True
        else:
            print u"重复客户名弹出框提示语错误"
            return False
    elif customerName =="":
        if b==u"请填写客户名":
            print u"空客户名弹出框提示语正确"
            return True
        else:
            print u"空客户名弹出框提示语错误"
            return False


def customerRename(self):
        c=c_custmoerErrorText(self)
        if c==u"该客户名称不可用，请更换客户名称":
            print u"新建重复客户名测试通过"
            return True
        else:
            print u"新建重复客户名测试失败"
            return False

def customerNull(self):
        c=c_custmoerErrorText(self)
        if c==u"客户名称不能为空！":
            print u"新建空客户名测试通过"
            return True
        else:
            print u"新建空客户名测试失败"
            return False