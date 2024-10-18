# django-estudos

##### Link da Aula: https://www.youtube.com/watch?v=Q2tEqNfgIXM

## 🔨 ROADMAP

# CONFIGURAÇÃO

##### 1. Criar a VENV

##### 2. Ativar a VENV e selecionar o interpretador

##### 3. Instalar Django + Restframework + Corsheaders

## Pastas

### 🔨Pasta do Projeto [📁api_root]
#### ➡️ [settings.py] = Configurações gerais

#### ➡️ [urls.py] = Linkar a aplicação

### 🔨Pasta do APP [📁api_rest]
#### ➡️ [models.py] = Criar os modelos para o DB
#### ➡️ [admin.py] = Configurar edição de modelos (opcional)
#### ➡️ [serializers.py] = Gerar JSON's dos modelos (Models)
#### ➡️ [views.py] = FUnções da API
#### ➡️ [urls.py] = Linkar as funções

----

#### 1. Crie a VENV: 
```
py -m venv venv
```
#### 2. Ative a VENV:
```
./venv/scripts/activate
```
#### 3. Ative o INTERPRETADOR no VSCODE: Vá na barra de busca da IDE, digite "Python: Select Interpreter" e então *selecione* a VENV.

#### 4. Instale as dependências/libs:
```
pip install django djangorestframework django-cors-headers
```

#### 5. Verifique:
```
pip freeze
```
#### 6. Se estiver certo, crie um arquivo de requerimentos:
 ```
pip freeze > requirements.txt
 ```

 #### 7. Ativar o arquivo de requerimentos:
  ```
 pip install -r requirements.txt
  ```

## Okay, agora vamos criar nosso projeto Django:
###### "api_root" é o nome da nossa pasta. E lembre de usar um " ." (espaço ponto) no final, para ele não criar pasta sob pasta.
  ```
  django-admin startproject api_root .
  ```

#### Criar agora de fato o "aplicativo", sempre com o manage.py (Arquivo raiz de tudo que for executar no Django)
###### Daremos o nome de "api_rest"
```
py manage.py startapp api_rest
```

-----

# Agora, mais algumas configurações:
### 🔨 settings.py [📁api_root]
#### ➡️ Em INSTALLED_APPS adicione
```
"rest_framework"
"corsheaders"
"api_rest" (temos que colocar também nossa aplicação criada)
```
#### ➡️ Em MIDDLEWARE adicione
```
'corsheaders.middleware.CorsMiddleware'
```


Perfeito! Agora bora codar os modeos! :smile: 

-----

# Modelos

#### Após modelar a classe, crie o migrations:
```
py manage.py makemigrations
py manage.py migrate
```

# Configurando o ADMIN

#### Após configurar a importação das models, crie um super-usuário:
```
py manage.py createsuperuser
```
Ex.: Edu / edu@edu.com / edu / edu

# Rode o servidor :smile:
```
py manage.py runserver
```

# Criando o SERIALIZERS
Os **serializers** no Django REST Framework (DRF) são responsáveis por converter objetos complexos (como modelos e querysets) em formatos como JSON ou XML, para que possam ser enviados via API. Eles também realizam o processo inverso, convertendo dados de entrada (como JSON) em instâncias de objetos Django, garantindo que sejam validados antes de serem salvos no banco de dados.

Principais funções dos serializers:
- **Serialização**: Converte objetos Django em formatos como JSON.
- **Desserialização**: Valida e converte dados recebidos pela API em objetos Django.
- **Validação**: Verifica se os dados estão corretos antes de serem salvos no banco.

Os serializers podem ser criados com base nos modelos do Django (usando `ModelSerializer`), ou de forma personalizada (usando `Serializer`), permitindo validações específicas por campo ou globais.

## 🔨 Crie dentro da [📁api_rest] um arquivo chamado 'serializers.py'


# VIEWS

### Finalmente, na views.py começamos a desenvolver nosso bom e velho CRUD :heart:


# Criar um arquivo de urls.py na pasta do APP [📁api_rest]

### Importante pensar que URLs e VIEWs trabalham juntas. Nós "setamos" as url para a função relacionada, sempre atreladas a determinada model, que será transformada em json pelo serializers.

## Processo Completo
##### Cliente faz uma requisição para o endpoint /users/.
##### O Django direciona a requisição para a função de view associada, que no caso é get_users.
##### A view recupera os dados do modelo User no banco de dados e os passa para o serializador.
##### O serializador transforma os dados do modelo em JSON.
##### A view retorna uma resposta HTTP com o JSON contendo os dados dos usuários.

#### Diagrama Resumido
URL: /users/ ➡️
View: get_users ➡️
Model: User ➡️
Serializer: UserSerializer ➡️
Resposta: JSON com dados dos usuários

### Conclusão
Sim, URLs e views trabalham juntas, e cada view geralmente está associada a um modelo (ou vários) que será transformado em JSON pelo serializador. Esse fluxo é a base para a criação de APIs RESTful no Django usando o Django Rest Framework (DRF).


## Teste de API do GET view:
```
http://127.0.0.1:8000/api/data/?user=Edu
```