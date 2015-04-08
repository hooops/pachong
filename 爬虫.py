# -*- coding: utf-8 -*-
__author__ = 'iswing'
import urllib2
import re

global arr
arr=[]
global arr2
arr2=[]

def zhizhu(url,value):
    cong=urllib2.urlopen(url)
    print type(cong)
    target=cong.read()
    zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
    imgre = re.compile(zhengze)
    imglist = re.findall(imgre,target)
    if value is not None:
        key = re.search(value,target)
        if key is not None:
            print url
    else:
        for s in imglist:
            arr=s[:-2]
            print s[:-2]
            zhizhu2(arr,value)


def zhizhu2(url,value):
 try:
    cong=urllib2.urlopen(url)

    target=cong.read()
    zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
    imgre = re.compile(zhengze)
    imglist = re.findall(imgre,target)
    if value is not None:
        key = re.search(value,target)
        if key is not None:
            print url
    else:
        for s in imglist:
            arr=s[:-2]
            print s[:-2]
            zhizhu3(arr,value)
 except:
     pass


def zhizhu3(url,value):
 try:
    cong=urllib2.urlopen(url)

    target=cong.read()
    zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
    imgre = re.compile(zhengze)
    imglist = re.findall(imgre,target)
    if value is not None:
        key = re.search(value,target)
        if key is not None:
            print url
    else:
        for s in imglist:
            arr=s[:-2]
            print s[:-2]
            zhizhu4(arr,value)
 except:
     pass


def zhizhu4(url,value):
 try:
    cong=urllib2.urlopen(url)

    target=cong.read()
    zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
    imgre = re.compile(zhengze)
    imglist = re.findall(imgre,target)
    if value is not None:
        key = re.search(value,target)
        if key is not None:
            print url
    else:
        for s in imglist:
            arr=s[:-2]
            print s[:-2]
 except:
     pass





if __name__=='__main__':

        url=raw_input('url,(²»¼Óhttp://)')
        value=raw_input('value')
        keys=raw_input('y/n')

        zhizhu('http://'+url,value)


