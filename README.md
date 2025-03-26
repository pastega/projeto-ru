# Sistema para o Gerenciamento de um Restaurante Universitário

Este projeto foi desenvolvido como parte da disciplina de **Análise e Projeto Orientado a Objetos** na **UTFPR - Campus Cornélio Procópio**. Ele tem como objetivo gerenciar as operações de um restaurante universitário, incluindo o controle de cardápios, estoque, e registro de refeições dos estudantes.

## Funcionalidades

- **Gerenciamento de Cardápios**: Cadastro e visualização de cardápios para almoço e jantar.
- **Controle de Estoque**: Adição e listagem de itens no estoque.
- **Registro de Refeições**: Registro de estudantes nas refeições vigentes.
- **Autenticação**: Sistema de login e logout para controle de acesso.

## Tecnologias Utilizadas

- **Backend**: Django 4.1.3
- **Frontend**: Bootstrap 5
- **Banco de Dados**: SQLite
- **Outras Bibliotecas**:
  - `django-crispy-forms` para estilização de formulários.
  - `crispy-bootstrap5` para integração com Bootstrap 5.

## Requisitos

- Python 3.8 ou superior
- Virtualenv (opcional, mas recomendado)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-ru.git
   cd projeto-ru
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

6. Acesse o sistema no navegador em: [http://localhost:8000](http://localhost:8000)

## Estrutura do Projeto

- **meals**: Aplicação principal que contém os modelos, views, templates e URLs.
- **ru**: Configurações do projeto Django.
- **templates**: Arquivos HTML compartilhados entre as aplicações.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto é de uso acadêmico e não possui uma licença específica.
