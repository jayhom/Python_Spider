import requests
from bs4 import BeautifulSoup
url=requests.get("https://www.dcard.tw/f/sex")
soup = BeautifulSoup(url.text,"html.parser")
sel = soup.select("div.PostList_wrapper_2BLUM a.PostEntry_root_V6g0r")
a=[]
for s in sel:
    a.append(s["href"])
url = "https://www.dcard.tw"+ a[2]
j=0
q=0
for i in a[2:]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_jpg = soup.select("div.Post_content_NKEl9 div div div img.GalleryImage_image_3lGzO")
    for c in sel_jpg:
        q+=1
        print("第",q,"張:",c["src"])
        pic=requests.get(c["src"])
        img2 = pic.content
        pic_out = open("spider/sex/"+str(c["src"][23:]),'wb')
        pic_out.write(img2)
        pic_out.close()