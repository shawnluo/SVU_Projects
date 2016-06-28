
import urllib,urllib2
import re

#return the source code of the website
class GetImg(object):
    def getHtml(slef, url):
        html = urllib2.urlopen(url)
        srcCode = html.read()
        return srcCode

    def getImg(self, srcCode):
        pattern = re.compile(r'src="(.*?\.jpg)".*?pic_ext="jpeg"')
        imgSrc = pattern.findall(srcCode)
        num = 0
        for i in imgSrc:
            urllib.urlretrieve(i,'%s.jpg' % num)
            num += 1
            #print "Downloading..."
            #print i
        #print 'Done!'