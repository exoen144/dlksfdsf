import requests
from bs4 import BeautifulSoup

numb= []
special=[]
url_1= "https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx"
resp_1 = requests.get(url_1)
ms = BeautifulSoup(resp_1.text,"html.parser")

t1=ms.find_all("td","td_w font_black14b_center")
for child in t1:
    numb.append(child.text.strip())

t3=ms.find_all("span",id="Lotto649Control_history_dlQuery_L649_DDate_0")
for child in t3:
    print(child.text)
print('開出順序：')
for i in range(12):
    print(numb[i],end=' ')
    if i==5:
        print('\n')
        print('大小順序')

print('\n')
print('特別號：')        
t2=ms.find_all("td","td_w font_red14b_center")
for child in t2:
    special.append(child.text.strip())
print(special[0])
