Feature: Cadastro do Pet no Plano de Saúde da Petlove

  Scenario: Cadastro bem-sucedido de um pet no plano de saúde
    Given que o sistema está operante
    When o usuário submete um cadastro de pet com os seguintes dados:
      | Nome do Pet | Raça | Sexo | Cor da Pelagem | Nome do Responsável | Endereço | E-mail | Telefone | Tipo do Plano |
      | Rex        | Golden Retriever | Macho | Dourado | João Silva | Rua A, 123 | joao@email.com | 11999999999 | Avançado |
    Then o sistema deve armazenar o cadastro com sucesso
    And deve exibir uma mensagem de confirmação "Cadastro realizado com sucesso!"

  Scenario: Cadastro falha devido a dados obrigatórios ausentes
    Given que o sistema está operante
    When o usuário submete um cadastro sem preencher o campo "Nome do Pet"
    Then o sistema deve exibir uma mensagem de erro "Nome do Pet é obrigatório"

  Scenario: Cadastro processado dentro do tempo limite
    Given que o sistema está operante
    When 500 cadastros de pets são submetidos simultaneamente
    Then 95% dos cadastros devem ser processados em menos de 5 segundos
