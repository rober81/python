import PyPDF2 as pypdf


readerOriginal = pypdf.PdfReader("C:\\workspace\\formularios\\F070042 prod.pdf")
readerModified = pypdf.PdfReader("C:\\workspace\\formularios\\F070042 mal.pdf")

textFieldsOrignal = readerOriginal.get_form_text_fields()
textFieldsModified = readerModified.get_form_text_fields()

print("\nCampos Nuevos que no estan en el Viejo")
for key in textFieldsModified.keys():
    if not key in textFieldsOrignal:
        print(key)

print("\nCampos Viejos que no estan en el Nuevo")
for key in textFieldsOrignal.keys():
    if not key in textFieldsModified:
        print(key)