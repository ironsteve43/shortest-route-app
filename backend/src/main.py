from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # no futuro, restrinja ao domínio do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PointsRequest(BaseModel):
    points: List[List[float]]

@app.post("/calculate-route")
def calculate_route(data: PointsRequest):
    # Por enquanto, só devolvemos os mesmos pontos e uma distância fake
    route = data.points  # no futuro você substitui pela lógica de roteamento
    total_distance = 0  # cálculo da distância ainda não implementado
    return {"route": route, "distance": total_distance}

@app.get("/")
def root():
    return {"message": "Backend rodando!"}