from fastapi import FastAPI
from DataModel import DataModel
from PredictionModel import Model
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def default():
    return "Bienvenido al API de SpotScan!\nEnvía una petición POST a /predict con la URL de la imagen a analizar en el cuerpo."

@app.post("/predict")
async def make_predictions(data_model: DataModel):
    model = Model()
    raw_img = requests.get(data_model.image)
    file = open("data/image.jpg", "wb")
    file.write(raw_img.content)
    file.close()

    result = model.make_predictions("image.jpg")
    return {
        "probability": str(result[0][0])
    }
