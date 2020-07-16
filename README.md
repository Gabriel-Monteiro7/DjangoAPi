
# [](<[https://github.com/Gabriel-Monteiro7/DjangoAPi](https://github.com/Gabriel-Monteiro7/DjangoAPi)>)  Django Api
## [](<[https://github.com/Gabriel-Monteiro7/DjangoAPi](https://github.com/Gabriel-Monteiro7/DjangoAPi)#Descrição>)Descrição

Api desenvolvida para simular um sistema de lista de tarefas (ToDo), onde o usuário possa criar, excluir ou concluir uma tarefa. O usuário deverá fazer login na aplicação com um email e uma senha. 

## [](<[https://github.com/Gabriel-Monteiro7/DjangoAPi](https://github.com/Gabriel-Monteiro7/DjangoAPi)tecnologias>)Tecnologias utilizadas

Para o desenvolvimento do projeto foi utilizada as seguintes tecnologias:

- :snake: **Python 3** 
- :snake:  **Django** — Framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view
- :oil_drum: **Django Rest Framework** — Biblioteca para o Framework Django que disponibiliza funcionalidades para implementar APIs Rest de forma extremamente rápida.
- :anchor: **Djoser**  — Fornece um conjunto de visualizações do Django Rest Framework para lidar com ações básicas, como registro, login, logout, redefinição de senha e ativação da conta. Funciona com modelo de usuário personalizado
- :closed_lock_with_key: **Jwt**  — É um padrão da Internet para a criação de dados com assinatura opcional e/ou criptografia cuja sua payload contém o JSON que afirma algum número de declarações.
- :whale2: **Docker** — É um software que garante maior facilidade na criação e administração de ambientes isolados, garantindo a rápida disponibilização de programas para o usuário final.

## Instalação

Para facilitar os teste utilize o Insominia que possui todas as rotas utilizadas.

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Django%20Api&uri=https%3A%2F%2Fgithub.com%2FGabriel-Monteiro7%2FDjangoAPi%2Fblob%2Fmaster%2FInsomnia.json)
```
# Clone o repositório
	git clone git@github.com:Gabriel-Monteiro7/DjangoAPi.git

# Vá para o diretório principal
	cd DjangoAPi
```

```
# Verifique se possui o python e a virtualenv instalado

# Inicie o Docker compose para usar o Banco Postgres
	docker-compose up -d

# running on port 5433

# Credenciais configuradas no Docker

	database:  "management",
	user:  "management",
	password:  "root",
	port:  "5433"

#Credenciais configuradas do DataBase

	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'management',
			'USER': 'management',
			'PASSWORD': 'root',
			'HOST': 'localhost',
			'PORT': '5433', # 8000 is default
		}
	}

#Configuração do Djoser 

	# As urls de confirmações vão ser enviadas via email
	
	DJOSER = {
		'LOGIN_FIELD': 'email',
		'PASSWORD_RESET_CONFIRM_URL': Url do front para confirmação do reset Password,
		'USERNAME_RESET_CONFIRM_URL':  Url do front para confirmação do reset Username,
		'ACTIVATION_URL': Url do front para confirmação do cadastro do user,
		'SEND_ACTIVATION_EMAIL': True,
		'SERIALIZERS': {
			'user_create': 'accounts.serializers.UserCreateSerializer',
			'user': 'accounts.serializers.UserCreateSerializer',
		}
	}
	
# Agora vamos criar um ambiente virtual e ativa-lo

	python3 -m venv .

	. bin/activate

# Instalar as Dependência
	pip install -r requirements.tx

# Gerar e executar as migrations

	python manage.py makemigrations
	
	python manage.py migrate 

# Rodar o servidor 
	python manage.py runserver

# running on port 8000
```

## [](<[https://github.com/Gabriel-Monteiro7/DjangoAPi](https://github.com/Gabriel-Monteiro7/DjangoAPi)#autor>):man_technologist: Autor

- **Gabriel Monteiro** - [GitHub](https://github.com/Gabriel-Monteiro7) - Email: [gabrielmont713@gmail.com](mailto:gabrielmont713@gmail.com)
