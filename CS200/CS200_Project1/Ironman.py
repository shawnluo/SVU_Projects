from io import StringIO
import sys
import unittest

import HTMLTestRunner

import DlPic
# from InsPic import InsPic
from DlPic import GetImg

from pyh import *
import os

myUrl = 'http://tieba.baidu.com/p/3698756921?see_lz=1&pn=1'

DownLoadPic = GetImg()
# getImg(getHtml(myUrl))
DownLoadPic.getImg(DownLoadPic.getHtml(myUrl))
# InsPic()


page = PyH('My wonderful PyH page')
page.addCSS('myStylesheet1.css', 'myStylesheet2.css')
page.addJS('myJavascript1.js', 'myJavascript2.js')

page << h1('Ironman', cl='center')
page << div(cl='myCSSclass1 myCSSclass2', id='myDiv1') << p('I love Ironman!', id='myP1')
page << img(src='6.jpg')
page << img(src='11.jpg')

'''
path = os.getcwd()

fileList = os.listdir(path)

i = 1
for file in fileList:
    ext = os.path.splitext(file)[1]
    if ext.strip() == '.jpg':
        i = i + 1

for i in range(1, i):
    fileName = str(i) + r'.jpg'
    image = r'<img src="' + fileName + r'">'
	page << img(src = 'fileName')

'''

mydiv2 = page << div(id='myDiv2')
mydiv2 << h2('Who is Iron man?') + p(
    'Iron Man (Tony Stark) is a fictional superhero appearing in American comic books published by Marvel Comics, as well as its associated media. The character was created by writer and editor Stan Lee, developed by scripter Larry Lieber, and designed by artists Don Heck and Jack Kirby. He made his first appearance in Tales of Suspense #39 (cover dated March 1963).')

page << div(id='myDiv3')
page.myDiv3.attributes['cl'] = 'myCSSclass3'
page.myDiv3 << p('Another paragraph')

page << h2('Most compact way to build a 4 by 4 table')
page << table() << tr(td('1') + td('2')) + tr(td('3') + td('4'))
page << h2('Another way to build a 4 by 4 table')
mytab = page << table()
tr1 = mytab << tr()
tr1 << td('1') + td('2')
tr2 = mytab << tr()
tr2 << td('3') + td('4')

page.printOut()
