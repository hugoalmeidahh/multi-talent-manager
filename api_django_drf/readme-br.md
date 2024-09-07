# Talent Management API

Este projeto é uma API para gerenciamento de candidatos, desenvolvida com Django, Django Rest Framework e JWT para autenticação. A API permite operações de CRUD (Create, Read, Update, Delete) sobre perfis de candidatos e oferece autenticação baseada em tokens JWT.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o seguinte instalado em sua máquina:

- **Python 3.10+**
- **PostgreSQL**
- **Docker** (caso opte por rodar o projeto com Docker)

## Instalação sem Docker

### Passo 1: Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### Passo 2: Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
``` 

### Passo 3: Instalar as dependências
bash
pip install -r requirements.txt

### Passo 4: Configurar o banco de dados
Você precisará criar um banco de dados PostgreSQL e configurar as credenciais no arquivo settings.py. Aqui está um exemplo de configuração no arquivo settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Passo 5: Aplicar as migrações
```bash
python manage.py migrate
```

### Passo 6: Rodar o servidor de desenvolvimento
```bash
python manage.py runserver
Agora você pode acessar a API em http://localhost:8000.
```

### Passo 7: Acessar o Swagger (Documentação da API)
Após rodar o servidor, você pode acessar a documentação gerada automaticamente em http://localhost:8000/swagger/ para testar os endpoints.

## Rodar o projeto com Docker
Se você preferir rodar o projeto usando Docker, siga os ### passos abaixo:

### Passo 1: Instalar o Docker
Certifique-se de ter o Docker instalado. Caso não tenha, siga as instruções de instalação.

### Passo 2: Criar o arquivo .env
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

```bash
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario_do_banco
POSTGRES_PASSWORD=senha_do_banco
DJANGO_SECRET_KEY=sua_chave_secreta_django
```

### Passo 3: Construir a imagem Docker
Na raiz do projeto, execute o seguinte comando para construir a imagem Docker:

```bash
docker-compose build
```

### Passo 4: Rodar os containers
```bash
docker-compose up
Isso irá iniciar o Django e um container do PostgreSQL. A API estará acessível em http://localhost:8000 e o Swagger em http://localhost:8000/swagger/.
```
### Passo 5: Rodar as migrações dentro do container
Se for a primeira vez rodando o projeto, execute as migrações:

```bash
docker-compose exec web python manage.py migrate
Executar testes
Para rodar os testes, utilize o comando abaixo:
```
```bash
python manage.py test
Se estiver usando Docker, pode rodar dentro do container:
```
```bash
docker-compose exec web python manage.py test
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
```
## Licença
Este projeto está sob a licença MIT.

### Explicação

- **Instalação sem Docker**: Mostra como instalar o projeto manualmente, incluindo a criação do ambiente virtual, instalação das dependências e configuração do banco de dados.
- **Rodar com Docker**: Explica como usar Docker para rodar o projeto, utilizando o `docker-compose` para criar e rodar os containers, incluindo a configuração do banco de dados.
- **Testes**: Incluí um exemplo de como rodar os testes tanto localmente quanto no Docker.

Se precisar de algum ajuste ou adicionar mais detalhes, é só avisar!