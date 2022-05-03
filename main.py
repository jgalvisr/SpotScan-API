from fastapi import FastAPI
import pandas as pd
from DataModel import DataModel
from PredictionModel import Model

app = FastAPI()

@app.get("/")
def default():
    return "Bienvenido al API de SpotScan!\nEnvía una petición POSTa /predict con la URL de la imagen a analizar en el cuerpo."

@app.post("/predict")
def make_predictions(data_model: DataModel):
    # df = pd.DataFrame(data_model.dict(), columns=data_model.dict().keys(), index=[0])
    model = Model()
    result = model.make_predictions(data_model)
    return "El paciente tiene un " + str(result) + "% de probabilidad de tener un melanoma"

