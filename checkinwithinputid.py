# -*- coding:gbk -*-
import urllib
import urllib2
import cookielib
import os
import sys

#�����ȡcookie����
def get_cookie():
    cookiefile = 'coofile'
    cookie = cookielib.MozillaCookieJar(cookiefile)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    userna = raw_input("������acfun�˺ţ�")
    passwd = raw_input("������acfun���룺")
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
   # maxcheck = ("���Ѵﵽ����Դ���,���Ժ��ٵ�¼.")
    #print (maxcheck.decode('utf-8'))
    #print (result.read()["result"])
    #if maxcheck in result.read()["result"]
       # sys.exit()

#����cookie������
    cookie.save(ignore_discard=True,ignore_expires=True)
    return cookie

#���Ա���cookie�Ƿ���������
def test_cook():
    try:
        cookie = cookielib.MozillaCookieJar()
        cookie.load('coofile',ignore_discard=True,ignore_expires=True)

    except Exception:

        cookie = get_cookie();

    return cookie

#ǩ��������
def checkacfun():
    cookie =  test_cook()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    checkin = opener.open('http://www.acfun.tv/member/checkin.aspx')
    rd = checkin.read()
    print rd

#���ǩ��ҳ����401δ��¼״̬�������»�ȡcookie
    if str(401) in rd:
        os.remove('coofile')
        print("�˺Ż�����������������룡")
        cookie = get_cookie()
        checkacfun()
    return


cookiefile = 'coofile'
cookie = cookielib.MozillaCookieJar(cookiefile)
cookie = test_cook()
checkacfun()





