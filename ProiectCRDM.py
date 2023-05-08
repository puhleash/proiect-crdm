
import requests #permite să facem solicitări HTTP în Python

#analiza fișierului text HTML
from bs4 import BeautifulSoup #facilitează colectarea de informații din paginile web 

#analiză și manipulare a datelor
import pandas as pd

URL='https://www.medicover.ro/medici/iasi,l,' #sursa

data1=[]  #creează o listă (list) goală numită data1
data2=[]

#functie de colectarea datelor de pe toate paginile de pe site
for page in range (1,5): #nr de pagine posibile
    pagina=requests.get(URL + str(page) + ',s')  #solicitarea tuturor paginilor
    soup=BeautifulSoup(pagina.content, 'html.parser') #conținutul informației (inclusiv tagurile, textele, etc...)
    results=soup.find('div', class_='doctors-list') #găsirea tuturor secțiunilor div cu clasa doctor (informație Nume Prenume)
    lista_doctori=results.find_all('div', class_="result-text") #crearea unei liste care conține toate elementele div cu clasa result-text

    for result in lista_doctori:
        nume_doctor=result.find("h2", class_="result-title") #conține primul element h2 cu clasa result-title din fișierul HTML 
        nume_doctor_stripped=" ".join(nume_doctor.text.split()) #crearea unui șir de caractere fără spațiile suplimentare dintre cuvinte
        specializare=result.find("span", class_="values") #căutare primului element care conține 'span' cu clasa 'values'
        specializare_stripped=specializare.text.strip() # accesează textul și elimina spațiile suplimentare
        data1.append(nume_doctor_stripped)  #crearea unei liste care conține numele medicilor găsiți pe pagină
        data2.append(specializare_stripped) #crearea unei liste care conține specializarea medicilor găsiți pe pagină 
        print(nume_doctor_stripped) #afisarea listei
        print(specializare_stripped)
        print()
       
df=pd.DataFrame() #crearea unui obiect DataFrame gol
df['Nume doctori']=data1 #adăugarea listei de doctori în DataFrame create anterior
df['Specializare']=data2
df.to_excel("Tabel_doctori_Medicover.xlsx", index=True) #salvarea obiectului DataFrame 'df' sub formă de fișier Excel