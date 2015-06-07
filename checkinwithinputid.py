# -*- coding:gbk -*-
import urllib
import urllib2
import cookielib
import os
import sys

#定义获取cookie函数
def get_cookie():
    cookiefile = 'coofile'
    cookie = cookielib.MozillaCookieJar(cookiefile)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    userna = raw_input("请输入acfun账号：")
    passwd = raw_input("请输入acfun密码：")
    postdata = urllib.urlencode({
        'username':userna,
        'password':passwd
    })

    req = urllib2.Request(
        url = 'http://www.acfun.tv/login.aspx',
        data = postdata,

    )

    result = opener.open(req)
   # print result.read()
   # maxcheck = ("您已达到最大尝试次数,请稍候再登录.")
    #print (maxcheck.decode('utf-8'))
    #print (result.read()["result"])
    #if maxcheck in result.read()["result"]
       # sys.exit()

#保存cookie到本地
    cookie.save(ignore_discard=True,ignore_expires=True)
    return cookie

#测试本地cookie是否正常函数
def test_cook():
    try:
        cookie = cookielib.MozillaCookieJar()
        cookie.load('coofile',ignore_discard=True,ignore_expires=True)

    except Exception:

        cookie = get_cookie();

    return cookie

#签到主程序
def checkacfun():
    cookie =  test_cook()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    checkin = opener.open('http://www.acfun.tv/member/checkin.aspx')
    rd = checkin.read()
    print rd

#如果签到页返回401未登录状态返回重新获取cookie
    if str(401) in rd:
        os.remove('coofile')
        print("账号或密码错误请重新输入！")
        cookie = get_cookie()
        checkacfun()
    return


cookiefile = 'coofile'
cookie = cookielib.MozillaCookieJar(cookiefile)
cookie = test_cook()
checkacfun()





