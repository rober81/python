from fastapi import FastAPI
import uvicorn

app = FastAPI()

# @app.get("/devtools/operacionesdecambio/alertas/{CUITEntidad}/{CUITEmpresa}", status_code=400)
# async def get_error_400(CUITEntidad, CUITEmpresa):
#     mensaje = "El servicio se encuentra fuera de horario operativo."
#     return {"Mensaje": mensaje}

@app.get("/devtools/operacionesdecambio/alertas/{CUITEntidad}/{CUITEmpresa}")
async def get_ok(CUITEntidad, CUITEmpresa):
    mensaje = f"Ingreso CUITEntidad: {CUITEntidad} y CUITEmpresa: {CUITEmpresa}"
    return {"Mensaje": mensaje}


if __name__ == "__main__":
    uvicorn.run("operacionesDeCambio:app", port=80, reload=True)