import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = """  

 _____             _            _             
|  __ \           | |          | |            
| |__) |__ _ _ __ | | _____ ___| | _____ _ __ 
|  _  // _` | '_ \| |/ / __/ _ \ |/ / _ \ '__|
| | \ \ (_| | | | |   < (_|  __/   <  __/ |   
|_|  \_\__,_|_| |_|_|\_\___\___|_|\_\___|_|   
by Nor Ahmad

"""
print (asci)
uDOMEN = input('Masukkan Domain : ')
url = get("https://www.alexa.com/siteinfo/" + uDOMEN)

soup = BeautifulSoup(url.text, 'html.parser')
aglobal = soup.find('strong',{'class':'metrics-data align-vmiddle'})
rglobal = aglobal.text.rstrip().lstrip()
acountry = soup.find('span',{'data-cat':'countryRank'})
rcountry = acountry.text.rstrip().lstrip()
print ('Domain :',uDOMEN)
print ('Link : https://www.alexa.com/siteinfo/'+uDOMEN)
print ('Global Rank :'+rglobal)
print (rcountry)
