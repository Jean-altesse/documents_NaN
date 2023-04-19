import requests 
from bs4 import BeautifulSoup

#a = requests.get("https://google.com")
#print(a.text)

# Methode get
'''
b = requests.get('https://jsonplaceholder.typicode.com/users')

user = b.json()
# methode push 
for i in user :
    #print(i['id'],":",i['name']) 
    if i['id'] == 1 :
        user1 = i 
print(user1) 

r = requests.put('https://jsonplaceholder.typicode.com/users/id')'''

# Methode post
'''
p = requests.post('https://jsonplaceholder.typicode.com/posts',data= {'title ':'foo','body': 'bar', 'userId':'1'})
modif = p.json()
print(modif)

#Methode put

pu = requests.put('https://jsonplaceholder.typicode.com/posts/1',data= {'title':'momo','title ':'foo','body': 'bar', 'userId':'1'})
modif = pu.json()
print(modif)'''



html_doc = requests.get('https://google.com').text
print(html_doc)
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
soup.title.name

