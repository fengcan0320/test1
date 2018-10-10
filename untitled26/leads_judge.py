#coding=utf-8
from leads_element import l_leadsRightText,l_leadsNullText
from public import windowsText
def leadsRight(self):
    b=l_leadsRightText(self)
    if b==u"""×
线索添加成功！""":
        print u"新建正确的线索测试通过"
        return True
    else:
        print u"新建正确的线索测试失败"
        return False

def leadsNull(self):
    b=l_leadsNullText(self)
    if b==u"联系人姓名不能为空":
        print u"新建空线索测试通过"
        return True
    else:
        print u"新建空线索测试失败"
        return False

def leadsWindowsText(self):
    b=windowsText(self)
    if b==u"联系人姓名不能为空":
        print u"新建空联系人弹出框提示语正确"
        return True
    else:
        print u"新建空联系人弹出框提示语错误"
        return False