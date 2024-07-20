import xml.etree.ElementTree as ET
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session
import urllib3
urllib3.disable_warnings()

session = Session()
session.verify = False
session.auth = HTTPBasicAuth("edsa_canales", "Passw0rd")
client = Client('https://10.7.232.113:9443/ws_cx_soliseleccion/ManagerConsultaSoliSeleccionService/WEB-INF/wsdl/ManagerConsultaSoliSeleccionService.wsdl', transport=Transport(session=session))
result = client.service.seleccionarFormaPago()

PESO = 'P'
DOLAR = 'D'

productosPesos = set()
productosDolar = set()

for item in result:
   if item['moneda'] == PESO:
        if item['producto'] != '0':
            productosPesos.add(item['producto'])
   elif item['moneda'] == DOLAR:
        if item['producto'] != '0':
            productosDolar.add(item['producto'])

productosP_str = ', '.join(sorted(productosPesos))
productosD_str = ', '.join(sorted(productosDolar))

print(f"Lista de productos Pesos: {productosP_str}")
print(f"Lista de productos Dolar: {productosD_str}")