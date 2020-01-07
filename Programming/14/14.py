from bs4 import BeautifulSoup
import requests
import re
import hashlib

payload = {
    'username': 'myusername',
    'password': 'mypassword'
}

challenge_url = "https://ringzer0ctf.com/challenges/14"

with requests.Session() as s:
    p = s.post('https://ringzer0ctf.com/login', data=payload)

    html_text = s.get(challenge_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    
    html_text=soup.find("div", {"class":"message"})
    #print(html_text)
    html_text=str(html_text)
    html_text=html_text[59:len(html_text)-44] #message
    print(len(html_text))
    new_text = ""
    for tmp in re.findall('........', html_text):
        new_text += chr(int(tmp, 2))
    new_text = new_text.encode("utf-8") 
    st = str(hashlib.sha512(new_text).hexdigest())
    post_url = challenge_url + "/" + str(st)
    r = s.post(post_url)
    print(post_url)
    
   
    f = open("response", "w")
    f.write(str(r.text))
    f.close()