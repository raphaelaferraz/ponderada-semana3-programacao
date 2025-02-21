from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
import time

app = FastAPI()

class PetCadastro(BaseModel):
    nome_pet: str
    raca: str
    sexo: str
    cor_pelagem: str
    nome_responsavel: str
    endereco: str
    email: EmailStr
    telefone: str
    tipo_plano: str

# Simulação de banco de dados
cadastros_pets = []

@app.post("/cadastrar_pet/")
def cadastrar_pet(pet: PetCadastro):
    start_time = time.time()
    
    # Simulação de tempo de processamento
    processing_time = round(time.time() - start_time, 3)
    
    # Verificando tempo limite de armazenamento
    if processing_time > 5:
        raise HTTPException(status_code=500, detail=f"Tempo de processamento {processing_time}s ultrapassou o limite de 5s")
    
    cadastros_pets.append(pet)
    return {"message": "Cadastro realizado com sucesso!", "processing_time": processing_time}

@app.get("/listar_pets/", response_model=List[PetCadastro])
def listar_pets():
    return cadastros_pets
