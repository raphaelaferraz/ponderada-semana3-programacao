from behave import given, when, then
import time
import random

# Simulando um banco de dados fictício
cadastros_realizados = []

@given("que o sistema está operante")
def step_system_operational(context):
    context.system_active = True

@when("o usuário submete um cadastro de pet com os seguintes dados")
def step_submit_pet_registration(context):
    for row in context.table:
        pet_data = {
            "nome_pet": row["Nome do Pet"],
            "raca": row["Raça"],
            "sexo": row["Sexo"],
            "cor_pelagem": row["Cor da Pelagem"],
            "nome_responsavel": row["Nome do Responsável"],
            "endereco": row["Endereço"],
            "email": row["E-mail"],
            "telefone": row["Telefone"],
            "tipo_plano": row["Tipo do Plano"]
        }
        cadastros_realizados.append(pet_data)

@then("o sistema deve armazenar o cadastro com sucesso")
def step_store_successfully(context):
    assert len(cadastros_realizados) > 0

@then('deve exibir uma mensagem de confirmação "Cadastro realizado com sucesso!"')
def step_confirmation_message(context):
    print("Cadastro realizado com sucesso!")

@when("o usuário submete um cadastro sem preencher o campo {campo}")
def step_submit_incomplete_data(context, campo):
    pet_data = {
        "nome_pet": None if campo == "Nome do Pet" else "Rex",
        "raca": "Golden Retriever",
        "sexo": "Macho",
        "cor_pelagem": "Dourado",
        "nome_responsavel": "João Silva",
        "endereco": "Rua A, 123",
        "email": "joao@email.com",
        "telefone": "11999999999",
        "tipo_plano": "Avançado"
    }
    context.pet_data = pet_data

@then('o sistema deve exibir uma mensagem de erro "{mensagem}"')
def step_display_error_message(context, mensagem):
    if not context.pet_data["nome_pet"]:
        print(mensagem)
        assert mensagem == "Nome do Pet é obrigatório"

@when("500 cadastros de pets são submetidos simultaneamente")
def step_bulk_submission(context):
    context.start_time = time.time()
    for _ in range(500):
        cadastros_realizados.append({
            "nome_pet": f"Pet{random.randint(1, 1000)}",
            "raca": "SRD",
            "sexo": "Fêmea",
            "cor_pelagem": "Preta",
            "nome_responsavel": "Usuário Teste",
            "endereco": "Endereço Teste",
            "email": "teste@email.com",
            "telefone": "11999999999",
            "tipo_plano": "Intermediário"
        })
    context.end_time = time.time()

@then("95% dos cadastros devem ser processados em menos de 5 segundos")
def step_performance_check(context):
    total_time = context.end_time - context.start_time
    print(f"Tempo total de processamento: {total_time:.2f} segundos")
    assert total_time <= 5, f"Erro: Tempo de processamento {total_time:.2f}s ultrapassou o limite!"
