#-*- coding: utf8 -*-
import xlrd
from pyExcelerator import *
from bs4 import BeautifulSoup
import urllib
import lxml
from xlutils.copy import copy
from xlwt import Style


fname = "D:\text.xls"
bk = xlrd.open_workbook(r'D:\test.xls')
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1"% fname


def Youdao(word):
    url='http://dict.youdao.com/search?q=%s'%word
    content=urllib.urlopen(url)
    soup = BeautifulSoup(content,"html.parser")
    tag = soup.find_all("span",class_="pronounce")
    tag = tag[0].find("span",class_="phonetic")
    phonetic = '/'+ tag.string[1:-1] + '/'
    return phonetic
'''
def writeExcel(row, col, str, style=Style.default_style):  
    rb = xlrd.open_workbook(file, formatting_info=True)  
    wb = copy(rb)  
    ws = wb.get_sheet(0)  
    ws.write(row, col, str, style)  
    wb.save('D:\bingo.xls') 
'''

words = []
phonetics = []
nrows = sh.nrows
for i in range(nrows):
    value = sh.cell_value(i,1)
    words.append(value)

m = 0

for item in words:
    if (item != u'') and ((' ' in value) == False):
        try:
            phonetics.append(Youdao(item))
        except:
            phonetics.append(u'')
    else:
        phonetics.append(u'')
    print phonetics[m]
    m = m + 1
    
'''
for ps in phonetics:
    print ps
    #writeExcel(ps,4,phonetics[ps],style)
'''

    
