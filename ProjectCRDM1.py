
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL='https://www.medicover.ro/medici/iasi,l,'

data1=[]
data2=[]

for page in range (1,5):
    pagina=requests.get(URL + str(page) + ',s')
    soup=BeautifulSoup(pagina.content, 'html.parser')
    results=soup.find('div', class_='doctors-list')
    lista_doctori=results.find_all('div', class_="result-text")

    for result in lista_doctori:
        nume_doctor=result.find("h2", class_="result-title")
        nume_doctor_stripped=" ".join(nume_doctor.text.split())
        specializare=result.find("span", class_="values")
        specializare_stripped=specializare.text.strip()
        data1.append(nume_doctor_stripped)
        data2.append(specializare_stripped)
        print(nume_doctor_stripped)
        print(specializare_stripped)
        print()
       
df=pd.DataFrame()
df['Nume doctori']=data1
df['Specializare']=data2
df.to_csv('Tabel_doctori_Medicover.csv')
