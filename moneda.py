import locale
import requests
from bs4 import BeautifulSoup

url = 'https://www.bna.com.ar/Personas'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
tabla = soup.find('table', {'class': 'table cotizacion'})

if tabla:
    filas = tabla.find('tbody').find_all('tr')
    celdas = filas[0].find_all('td')
    valor_usd = celdas[2].text.strip()
    print(f"Valor encontrado: {valor_usd}")
else:
    print("No se encontró la tabla especificada.")

locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
ars_usd = float(valor_usd.replace(',', '.'))
imp_pais = 1.6

#mx_usd = 6.90
mx_usd = 18.06
sudafrica_usd = 18.28

moneda_a_usar = input("Seleccione moneda a usar (mex, sudafrica): ")
if moneda_a_usar == 'mex':
    pesos_mx = float(input("Ingrese el monto en pesos mx: "))
    dolares =  pesos_mx / mx_usd
elif moneda_a_usar == 'sudafrica':
    rand_suda = float(input("Ingrese el monto en rand sudafrica: "))
    dolares =  rand_suda / sudafrica_usd
else:
    print("Moneda no encontrada")

#dolares =  mx_usd * pesos_mx / 100
pesos_arg = dolares * ars_usd * imp_pais

print(f"Tienes {locale.currency(dolares, grouping=True)} dolares")


print(f"Tienes {locale.currency(pesos_arg, grouping=True)} pesos argentinos")
