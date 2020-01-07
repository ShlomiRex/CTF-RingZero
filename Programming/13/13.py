from bs4 import BeautifulSoup
import requests
import re
import hashlib

payload = {
    'username': 'myusername',
    'password': 'mypassword'
}

with requests.Session() as s:
    p = s.post('https://ringzer0ctf.com/login', data=payload)

    html_text = s.get("https://ringzer0ctf.com/challenges/13").text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    html_text=soup.find("div", {"class":"message"})
    #print(html_text)
    html_text=str(html_text)
    html_text=html_text[59:len(html_text)-44]
    html_text = html_text.encode("utf-8")
    #print(html_text)
    st = str(hashlib.sha512(html_text).hexdigest())
    post_url = "https://ringzer0ctf.com/challenges/13/" + str(st)
    print(post_url)
    r = s.post(post_url)
    
   
    f = open("test", "w")
    f.write(str(r.text))
    f.close()