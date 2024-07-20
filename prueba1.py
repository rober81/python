from datetime import datetime

print ("hola mundo")


secuencia = ""
for i in range(1, 5):
    secuencia += str(i) * 35
print(secuencia)


# Obtén la fecha actual
fecha_actual = datetime.now()

# Formatea la fecha en el formato deseado
fecha_formateada = fecha_actual.strftime("hoy %Y%m%d")

# Imprime la fecha formateada
print(fecha_formateada)