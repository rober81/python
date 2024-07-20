import requests
from bs4 import BeautifulSoup

# Obtener el contenido HTML de la página web
url = 'https://www.bna.com.ar/Personas'
response = requests.get(url)
html_content = response.text

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar la tabla específica, por ejemplo, por su clase "table cotizacion"
tabla = soup.find('table', {'class': 'table cotizacion'})

# Verificar que la tabla existe
if tabla:
    # Encontrar todas las filas dentro del cuerpo de la tabla (<tbody>)
    filas = tabla.find('tbody').find_all('tr')
    
    # Recorrer cada fila y obtener el valor del tercer <td>
    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) >= 3:  # Asegurarse de que hay al menos 3 celdas en la fila
            valor_deseado = celdas[2].text.strip()
            print(f"Valor encontrado: {valor_deseado}")
else:
    print("No se encontró la tabla especificada.")