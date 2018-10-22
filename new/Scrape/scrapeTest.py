from bs4 import BeautifulSoup as BS
import requests

base = 'http://opendata.camara.cl/camaradiputados/WServices/WSDiputado.asmx/retornarDiputados?'
r = requests.get(base)
data = r.text
soup = BS(data, 'xml')

f = open("diputados.txt", "w")

diputados = soup.find_all("Diputado")
for diputado in diputados:
    Id =  diputado.Id.text.encode('utf-8')
    nombre = diputado.Nombre.text.encode('utf-8')
    AP = diputado.ApellidoPaterno.text.encode('utf-8')
    AM = diputado.ApellidoMaterno.text.encode('utf-8')
    sexo = diputado.Sexo.text.encode('utf-8')
    f.write(Id + " " + nombre + " " + AP + " " + AM + " " + sexo + "\n")

f.close()