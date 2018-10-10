#coding=utf-8
from  login_element import l_loginRightText,l_loginErrorText

def loginRiht(self):
        b=l_loginRightText(self)
        if b==u"""×
登录成功""":
            print u"登录测试通过"
            return True
        else:
            print u"登录测试失败"
            return False

def loginError(self):
        c=l_loginErrorText(self)
        if c==u"""×
用户名或密码错误！2222222222222222222222222222222222""":
            print u"错误密码登录测试通过"
            return True
        else:
            print u"错误密码登录测试失败"
            return False

def loginNull(self):
        d=l_loginErrorText(self)
        if d==u"""×
请正确输入用户名和密码！""":
            print u"空密码登录测试通过"
            return True
        else:
            print u"空密码登录测试失败"
            return False

def loginOften(self):
        d=l_loginErrorText(self)
        if d==u"""×
您登录的错误次数过于频繁，请10分钟后再试。或点击忘记密码重置""":
                print u"频繁输错密码测试通过"
                return True
        else:
                print u"频繁输错密码测试失败"
                return False
