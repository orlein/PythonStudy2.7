'''
Created on 2015. 7. 27.

@author: PCJ
'''
#-*-encoding:utf-8-*-
import requests as rs  # @UnresolvedImport
import bs4  # @UnresolvedImport

def getTopRank():
    naver_url = 'http://www.naver.com'
    response = rs.get(naver_url)
    html_content = response.text.encode(response.encoding);
    navigator = bs4.BeautifulSoup(html_content)
    realRankTag = navigator.find_all(id='realrank')
    resultList=realRankTag[0].find_all('a')
    keywords = [item['title'] for item in resultList]
    for index,keyword in enumerate(keywords):
        resultText = '[rank %d]%s'%(index,keyword.encode('utf-8'))
        print(resultText.decode('utf-8').encode('euc-kr'))
