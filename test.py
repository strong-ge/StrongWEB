# -*- coding: utf-8 -*-
import re,urllib2,urllib
from bs4 import BeautifulSoup
url='http://www.pvc123.com/news/zhorus.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html=response.read().decode('utf-8', 'ignore')

pattern_all=re.compile(r'<div class="area_main_list">(.*?)<p class="summary">',re.S)
res_abstract=re.findall(pattern_all,html)
if res_abstract:
    #print res_abstract[0]
    pattern_artical=re.compile(r'<div id="endText">(.*?)<div class="ep-source cDGray">',re.S)
    res_artical=re.findall(pattern_artical,res_abstract[0])
    if res_artical:
        #print res_artical[0]
        artical= re.sub("<(?!img|p|/p).*?>","",res_artical[0])
        print artical
        soup = BeautifulSoup(artical,"lxml")
        urllist=soup.find_all("img")
        for list in urllist:
            soup_imgurl=BeautifulSoup(str(list),"lxml")
            imgurl=soup_imgurl.img["src"]
            print imgurl
              
        
        
        
        