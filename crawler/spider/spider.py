import re
import urllib

def getHtml(url):
    webPage = urllib(url)
    html = webPage.read()
    return html

def getImage(html):
    imageReg = re.compile(r'src="(.+?\.jpg)"pic_ext')
    images = re.findall(imageReg, html)
    return images

    
def main():
    with open('D:/python/spider/system.txt', 'w')
        f.write(getImage(getHtml('')))
main()




