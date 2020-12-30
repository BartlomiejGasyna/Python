#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:10:52 2020

@author: bartlomiejgasyna
"""

from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import csv #excel
from datetime import date
import matplotlib.pyplot as plt


ceny ={}
print('ceny paliw:\n')

#Leclerc

page_url = "https://slupsk.leclerc.pl"

# opens the connection and downloads html page from url
uClient = uReq(page_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

print('-Leclerc:\n')
print('ON: ')
cenaON = float(page_soup.select("li")[59].text.strip().replace(',','.'))
print(cenaON,'zł', sep = "")
print('PB:')
cenaPB = float(page_soup.select("li")[60].text.strip().replace(',','.'))
print(cenaPB,'zł',sep='')

ceny["Leclerc"]=(cenaON,cenaPB)

#MZK
page_url = "http://www.mzk.slupsk.pl/pl/page/nasza-oferta/stacja-paliw.html"

uClient = uReq(page_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print('\n-MZK:\n')
print('ON: ')
cenaON = round(float(page_soup.select("h2")[0].text.strip().replace(',','.')[0:-3]) - 0.03, 2)
print(cenaON, 'zł', sep='')
print('PB:')
cenaPB = round(float(page_soup.select("h2")[1].text.strip().replace(',','.')[0:-3]) - 0.03, 2)
print(cenaPB, 'zł', sep='')

ceny['MZK'] = (cenaON,cenaPB)



#MILA ytttty6y6666yyyyyyg
page_url = "https://emila.com.pl/stacja/14/slupsk-ul-szczecinska-6-kobylnica"
uClient = uReq(page_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
print('\n-MILA:')
print('\nON: ')
cenaON=''


for i in range(4):
    cenaON += page_soup.select('span')[25+i].text.strip()
cenaON = float(cenaON.replace(',','.'))
print(cenaON, 'zł', sep='')

print('PB: ')
cenaPB=''
for i in range(4):
    cenaPB += page_soup.select('span')[31+i].text.strip()
cenaPB = float(cenaPB.replace(',','.'))
print(cenaPB, 'zł', sep = '')

ceny['MILA'] = (cenaON, cenaPB)

LeON = []
LePB = []
MZKON = []
MZKPB = []
MilaON = []
MilaPB = []
Dates = []

with open('fuel_prices.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        LeON.append(row[0])
        LePB.append(row[1])
        MZKON.append(row[2])
        MZKPB.append(row[3])
        MilaON.append(row[4])
        MilaPB.append(row[5])
        Dates.append(row[6])
        
    LeON = list(map(float,LeON[2:]))
    LePB = list(map(float,LePB[2:]))
    MZKON = list(map(float,MZKON[2:]))
    MZKPB = list(map(float,MZKPB[2:]))
    MilaON = list(map(float,MilaON[2:]))
    MilaPB = list(map(float,MilaPB[2:]))
    Dates = Dates[2:]


 
    
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))

ax[0,0].plot(Dates, LeON, label='Leclerc ON')
ax[0,0].plot(Dates, LePB, label='Leclerc PB')
ax[0,0].legend()
#plt.xticks(range(1, len(Dates)), Dates, rotation='vertical')
ax[0,0].tick_params(axis='x', rotation=45)


ax[1,0].plot(Dates, MZKON, label='MZK ON')
ax[1,0].plot(Dates, MZKPB, label='MZK PB')
ax[1,0].legend()
ax[1,0].tick_params(axis='x', rotation=45)

ax[0,1].plot(Dates, MilaON, label='Mila ON')
ax[0,1].plot(Dates, MilaPB, label='Mila PB')
ax[0,1].legend()
ax[0,1].tick_params(axis='x', rotation=45)

plt.show()



if (Dates[-1] != date.today()):
    with open('fuel_prices.csv','a', newline='') as f:
        cf = csv.writer(f,delimiter=';')
        cf.writerow(ceny['Leclerc'] + ceny['MZK'] + ceny['MILA'] + (date.today().strftime('%d.%m.%y'),) )
