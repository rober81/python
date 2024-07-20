import base64

with open('C:\\Temp\\F70000A9546.pdf', 'rb') as f:
    pdf_content = f.read()

pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')

with open('C:\\Temp\\archivo_base64.txt', 'w') as f2:
    f2.write(pdf_base64)

print("Listo")