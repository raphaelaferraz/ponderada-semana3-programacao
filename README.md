# 📌 API de Cadastro de Pets - Petlove

Este repositório contém a implementação de uma API mockada utilizando **FastAPI** para o **Cadastro de Pets no Plano de Saúde da Petlove**. A API inclui funcionalidades para cadastrar pets, listar os cadastros e exibir métricas sobre os cadastros realizados, contemplando requisitos funcionais e não funcionais.

---

##  Endpoints Disponíveis

### **1️⃣ Cadastrar um pet**
`POST /cadastrar_pet/`

**Request Body:**
```json
{
  "nome_pet": "Rex",
  "raca": "Golden Retriever",
  "sexo": "Macho",
  "cor_pelagem": "Dourado",
  "nome_responsavel": "João Silva",
  "endereco": "Rua A, 123",
  "email": "joao@email.com",
  "telefone": "11999999999",
  "tipo_plano": "Avançado"
}
```

**Response:**
```json
{
  "message": "Cadastro realizado com sucesso!",
  "processing_time": 0.0023
}
```

### **2️⃣ Listar todos os pets cadastrados**
`GET /listar_pets/`

**Response:**
```json
[
  {
    "nome_pet": "Rex",
    "raca": "Golden Retriever",
    "sexo": "Macho",
    "cor_pelagem": "Dourado",
    "nome_responsavel": "João Silva",
    "endereco": "Rua A, 123",
    "email": "joao@email.com",
    "telefone": "11999999999",
    "tipo_plano": "Avançado"
  }
]
```

### **3️⃣ Obter métricas do sistema**
`GET /metricas-plano-de-saude/`

**Response:**
```json
{
  "total_cadastros": 10,
  "sucessos": 9,
  "falhas": 1,
  "tempo_total": 4.5,
  "tempo_medio": 0.45
}
```

---

## 📌 Tecnologias Utilizadas
- **FastAPI** 🚀 - Framework para APIs rápidas e eficientes
- **Pydantic** ✅ - Validação de dados
- **Uvicorn** ⚡ - Servidor ASGI

---

## 📄 Notas Importantes
- A API é totalmente **mockada**, não armazenando dados permanentemente.
- Os tempos de processamento são simulados para representar um ambiente realista.
- O objetivo é validar requisitos funcionais e não funcionais da arquitetura.
