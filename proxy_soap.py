import xml.etree.ElementTree as ET
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session
import urllib3
urllib3.disable_warnings()

from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


def call_first_soap_service():
    usuario = "edsa_canales"
    password = "Passw0rd"
    url_wsdl = "https://10.7.232.113:9443/ws_cx_soliseleccion/ManagerConsultaSoliSeleccionService/WEB-INF/wsdl/ManagerConsultaSoliSeleccionService.wsdl"

    session = Session()
    session.verify = False
    session.auth = HTTPBasicAuth(usuario, password)
    client = Client(url_wsdl, transport=Transport(session=session))

    response = client.service.seleccionarFormaPago()
    return response

def modify_response(response):
    # Aquí puedes modificar la respuesta como necesites
    #response['someField'] = 'new value'  # Ejemplo de modificación
    PESO = 'P'
    DOLAR = 'D'
    for item in response:
        if item['moneda'] == PESO:
            item['web'] = "web peso"
        elif item['moneda'] == DOLAR:
            item['web'] = "web dolar"
    return response

# Definir el servicio SOAP con Spyne
class SoapService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def SomeOperation(ctx, some_param):
        response = call_first_soap_service()
        modified_response = modify_response(response)
        # Convertir el diccionario de la respuesta modificada a una cadena XML
        response_xml = Client.helpers.serialize_object(modified_response)
        return str(response_xml)

# Configurar la aplicación SOAP
app = Application(
    [SoapService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Configurar el servidor WSGI
wsgi_app = WsgiApplication(app)

router = {
    '/ws_cx_soliseleccion/ManagerConsultaSoliSeleccionService': SoapService,
}

if __name__ == '__main__':
    
    puerto = 9080

    response = call_first_soap_service()
    new_response = modify_response(response)

    server = make_server('0.0.0.0', puerto, wsgi_app)
    print(f"Listening on port {puerto}...")
    server.serve_forever()












peso = 'P'
dolar = 'D'
productosPesos = set()
productosDolar = set()
for item in result:
   if item['moneda'] == peso:
        if item['producto'] != '0':
            productosPesos.add(item['producto'])
   elif item['moneda'] == dolar:
        if item['producto'] != '0':
            productosDolar.add(item['producto'])
productosP_str = ', '.join(sorted(productosPesos))
productosD_str = ', '.join(sorted(productosDolar))
print(f"Lista de productos Pesos: {productosP_str}")
print(f"Lista de productos Dolar: {productosD_str}")