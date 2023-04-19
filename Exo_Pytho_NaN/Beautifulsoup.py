import requests 
from bs4 import BeautifulSoup
import random
import json


# #test
# '''
# html_doc = requests.get('https://google.com').text
# print(html_doc)
# soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify())
# soup.title.name '''

# # EXO DE KOBOREÉ
# '''
# req = requests.get('https://dev-tuto.nan.ci').text
# print(req)
# s = BeautifulSoup(req,'html.parser')'''

# #Comment parcourir un fichier et  le modifier et l'afficher

#r = open("contact.txt","r")
#contacts = r.readlines()
#for contact in contacts :
  #   item = contact.split(':')

#print(f'''nom : {item[0]}
#prenom : {item[1]}
#Numero : {item[2]}''',end='\n **********')

#New exo

file = open('exo_moise.json','w')
data = {'nom':'altesse','envie':'argent','sport':'football'}
con_data = json.dumps(data)
file.write(con_data)
file.close()
f = open('exo_moise.json','r')
t = "altesse"
if t in data :
    print ("vous dejà inscrire")
else :
    print("vous êtes nouveua")



