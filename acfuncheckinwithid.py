# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import time

num = 3

while num > 0:

    #初始化一个CookieJar来处理Cookie的信息#
    cookie = cookielib.CookieJar()

    #创建一个新的opener来使用我们的CookieJar#
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    postdata = urllib.urlencode({
        'username':'',
        'password':''
    })
    #headers = {
         #'referer':'http://www.acfun.tv/login/'
    #}
    req = urllib2.Request(
        url = 'http://www.acfun.tv/login.aspx',
        data = postdata,
        #headers = headers
    )
    result = opener.open(req)
    print result.read()

    #print cookie

    #个人主页
    myspace = opener.open('http://www.acfun.tv/member/#area=splash')

    #print result.read()

    #签到地址
    checkin = opener.open('http://www.acfun.tv/member/checkin.aspx')

    print checkin.read()

    time.sleep(5)

    num = num - 1





