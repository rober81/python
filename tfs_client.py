from tfs import TFSAPI

# URL del servidor TFS y proyecto
server_url = "http://smf12ac0001:8080/tfs/"
project_name = "BNA"
#project_name = "DefaultCollection/BNA/BNA.CX/BNA.CX"
user="d78185"
password="rober05p"

# Ruta local al archivo que deseas commitear
file_path = "$/BNA.CX/Java/CX/EDSA/orpa/comex/comex-webEAR/META-INF/application.xml"

# Mensaje de commit
commit_message = "Prueba"

# Inicializar la API de TFS
client = TFSAPI(server_url, project=project_name, user=user, password=password, connect_timeout=30, read_timeout=None)

#changeset = client.get_changeset(92140)
all_projects = client.get_projects()

print(all_projects)



# Obtener información sobre el control de versiones del archivo
#file_version_info = client.get_item(path=file_path)

# Obtener el último cambio del archivo
#latest_change = file_version_info["version"]

# Leer el contenido del archivo
#with open(file_path, "r") as file:
#    file_content = file.read()

# Realizar el checkin (commit) del archivo
#tfs.checkin(path=file_path, content=file_content, comment=commit_message, latest_change=latest_change)