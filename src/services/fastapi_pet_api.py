from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
import time

app = FastAPI()

# Modelo de Dados do Pet
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

# Estrutura para armazenar métricas do sistema
metricas = {
    "total_cadastros": 0,
    "sucessos": 0,
    "falhas": 0,
    "tempo_total": 0.0,
    "tempo_medio": 0.0
}

@app.post("/cadastrar_pet/")
def cadastrar_pet(pet: PetCadastro):
    start_time = time.time()
    
    metricas["total_cadastros"] += 1
    
    try:
        # Simulação de tempo de processamento
        processing_time = time.time() - start_time
        metricas["tempo_total"] += processing_time
        metricas["tempo_medio"] = metricas["tempo_total"] / metricas["total_cadastros"]
        
        # Verificando tempo limite de armazenamento
        if processing_time > 5:
            metricas["falhas"] += 1
            raise HTTPException(status_code=500, detail=f"Tempo de processamento {processing_time}s ultrapassou o limite de 5s")
        
        cadastros_pets.append(pet)
        metricas["sucessos"] += 1
        return {"message": "Cadastro realizado com sucesso!", "processing_time": processing_time}
    
    except HTTPException as e:
        raise e

@app.get("/listar_pets/", response_model=List[PetCadastro])
def listar_pets():
    return cadastros_pets

@app.get("/metricas-plano-de-saude/")
def metricas_plano_de_saude():
    return metricas

# Roda o servidor FastAPI
# Comando para rodar: uvicorn nome_do_arquivo:app --reload
