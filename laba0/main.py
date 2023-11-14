import urllib.request
import xml.dom.minidom as minidom
import pandas as pd
import datetime 
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
countday=20
date_size=(datetime.date.today()-datetime.timedelta(days=countday)).strftime('%d/%m/%Y')
today = datetime.date.today().strftime('%d/%m/%Y')
RQ=["R01235"]
url1 = "https://cbr.ru/scripts/XML_dynamic.asp?date_req1="+date_size+"&date_req2="+today+"&VAL_NM_RQ="+RQ[0]
url= "https://cbr.ru/scripts/XML_dynamic.asp?date_req1=01/10/2023&date_req2=10/10/2023&VAL_NM_RQ=R01235"
print(url1)
def get_data(xml_url):
    try:
        web_file = urllib.request.urlopen(xml_url)
        return web_file.read()
    except:
        pass

def get_currencies_dictionary(xml_content):

    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Record")
    currency_dict = {}
    record_date=1

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'VunitRate':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                        record_date+=1
        currency_dict[(datetime.date.today()-datetime.timedelta(days=(countday-record_date))).strftime('%d/%m')] = value
    return currency_dict







disk={}
print(disk)
disk=get_currencies_dictionary(get_data(url1))
myList = disk.items()
x, y = zip(*myList)

plt.plot(x, y)
plt.xlabel('дата')
plt.ylabel('курс доллара')
plt.grid()
plt.show()