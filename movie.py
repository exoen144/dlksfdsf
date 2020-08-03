import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import seaborn as sns

def get_movie():
    movies = []
    url_1= "https://movies.yahoo.com.tw/chart.html"
    resp_1 = requests.get(url_1)
    ms = BeautifulSoup(resp_1.text,"html.parser")

    ms.find_all("div","rank_txt")
    movies.append(ms.find('h2').text)

    for rank_txt in ms.find_all("div","rank_txt"):
        movies.append(rank_txt.text.strip())

    return movies

posts_title = []
url_2= "https://www.ptt.cc/bbs/movie/index.html"

for i in range(200): 
    resp = requests.get(url_2)
    bs = BeautifulSoup(resp.text,"html.parser")
    bs.find_all("div","title")
    
    for title in bs.find_all("div","title"):
        #print(title.text.strip())
        posts_title.append(title.text.strip())

    u = bs.select("div.btn-group.btn-group-paging a") 
    url_2 = "https://www.ptt.cc"+ u[1]["href"]

hot_movie=get_movie()
discuss_num=[]
movies_name=[]
for j in range (len(hot_movie)):
    count_1=0
    count_2=0
    count_3=0
    count_4=0
    print('台北票房第'+str(j+1)+'名:')
    print(hot_movie[j])
    name=str(j+1)+'.'+hot_movie[j]
    for title in posts_title:
        if hot_movie[j][0:2] in title:
            #print(title)
            count_1+=1
            
            if "[好雷]" in title or "[普好雷]" in title or "[極好雷]" in title:
                count_2+=1

            if "[普雷]" in title or "[雷]" in title:
                count_3+=1

            if "[負雷]" in title or "[極負雷]" in title or "[普負雷]" in title:
                count_4+=1

            else:
                continue
    movies_name.append(name)
    discuss_num.append(count_1)
    print('討論數:',count_1),print('好雷數量:',count_2),print('普雷數量:',count_3),print('負雷數量:',count_4),print('\n')
    
print('按排名畫出以下電影討論度圖表:')
for k in range(len(hot_movie)):
    print(movies_name[k],end=' ')

movies_num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
plt.figure(figsize=(15,5))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Movie',fontsize=20)
plt.ylabel('Number',fontsize=20)
plt.bar(movies_num,discuss_num)
plt.title("Movie Popularity",fontsize=25)
plt.show()






#bad person












