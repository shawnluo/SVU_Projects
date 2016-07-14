import urllib
from urllib.request import urlopen
import re


# return the source code of the website
class GetImg(object):
    def getHtml(slef, url):
        html = urlopen(url)
        #srcCode = html.read()
        srcCode = html.read().decode('utf-8')
        return srcCode

    #html = response.read().decode('utf-8')

    def getImg(self, srcCode):
        pattern = re.compile(r'src="(.*?\.jpg)".*?pic_ext="jpeg"')
        imgSrc = pattern.findall(srcCode)
        num = 0
        for i in imgSrc:
            #urllib.urlretrieve(i, '%s.jpg' % num)
            urllib.request.urlretrieve(i, '%s.jpg' % num)
            #import urllib.request
            #data = urllib.request.urlretrieve("http://...")
            num += 1
            # print "Downloading..."
            # print i
            # print 'Done!'
