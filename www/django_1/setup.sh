MENU_ISNTALL_ENVIRONMENT="
----------------------------------------------------
Criando um Ambiente Virtual
---------------------------------------------------
https://www.youtube.com/watch?v=NAstsS4rVrY&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=3
"

TIME(){
echo "In 2s"
sleep 1
echo "In 1s"
sleep 1
}

VERIFICANDO_VERSAO_PYTHON(){
TIME
python3 --version
}

CRAIANDO_AMBIENTE_VIRTUAL(){
echo "$MENU_ISNTALL_ENVIRONMENT"
TIME
python3 -m venv .venv
}

ATIVANDO_AMBIENTE_VIRTUAL(){
TIME
source .venv/bin/activate
}

INSTALANDO_DJANGO(){
  TIME
  echo 'Instalando Django'
  pip install django
}


INSTALANDO_BLACK_FLAKE(){
TIME
echo "Install Black"
pip install black
TIME
echo "Install Flake8"
pip install flake8

}

MOSTRAR_PACOTES_INSTALADOS(){
  pip freeze
}

# https://bobbyhadz.com/blog/python-no-module-named-mysql
INTALL_CONNECTOR_MYSQ(){
pip3 install mysql-connector-python
}


GUARDANDO_DEPENDENCIAS(){
TIME
echo 'guardando dependencia'
pip freeze > requeriments.txt
}


GITIGNORE(){
touch .gitignore
cat << EOF >> .gitignore
.venv/

EOF
}






CRIANDO_PROJETO_DJANGO(){
echo "Criando um Projeto Django"
TIME
echo
echo --------------------------------------------------------
echo -e "\033[31m Deseja Criar um projeto Djago \033[m"
read -p "s (SIM ) e n (NÃO) -->> " CONFIRM
echo --------------------------------------------------------
if [ "$CONFIRM" = s ];then

# PASSO 2: Criar um ambiente virtual
CRAIANDO_AMBIENTE_VIRTUAL

# PASSO 4: Instalando Black e Flake
INSTALANDO_BLACK_FLAKE

# PASSO 5: Criando o arquivo git ignore
GITIGNORE


# PASSO 7: Guardando as dependências instaladas na minha aplicação em um arquivo txt
GUARDANDO_DEPENDENCIAS


# PASSO FINAL: Mostrar Pacotes que foram intalados
MOSTRAR_PACOTES_INSTALADOS

# read -p 'Digite o nome do Projeto -->> ' PROJETO
PROJETO="folder_project"
django-admin startproject $PROJETO .


#Ativar o Ambiente virtual
echo '-------------------------'
echo 'Ativando Ambiente Virtual'
echo '-------------------------'
TIME
echo '----Diretorio para Ativação----'
ls -a
echo '-------------------------------'
source .venv/bin/activate
pip install django

echo '---------------------------'
echo 'Criando primeiro App Django'
echo '---------------------------'
python manage.py startapp app
echo '***************************************'
echo 'Mostrar o Diretório e arquivos contido '
echo '***************************************'
ls -a
TIME
echo 'Entrando na pasta App'
cd app


echo 'Criando a pasta templates'
TIME

mkdir templates
echo 'Criando arquivo urls.py'
TIME
touch urls.py

echo 'Escrevendo no arquivo urls.py'
TIME
cat << EOF >> urls.py
from django.urls import path
from .views import index
urlpatterns = [path("", index, name="index")]
EOF

rm -rf views.py
touch views.py
cat << EOF >> views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!!")

EOF
cd ..

TIME

echo 'Entrando na pasta folder_project'
cd folder_project
echo 'Excluindo o arquivo settings.py'
rm -rf settings.py

touch settings.py
cat << EOF >> settings.py
"""
Django settings for folder_project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ugz3p-4^+8$_8d&3t^bxi#(&lo-dvcxnocuat=(wc-hfd1xj%p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "folder_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "folder_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EOF

echo 'Excluindo o arquivo urls.py'
TIME
rm -rf urls.py

touch urls.py

cat << EOF >> urls.py
"""folder_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("app/", include("app.urls")),
    path("admin/", admin.site.urls),
]

EOF
cd ..

google-chrome http://127.0.0.1:8000/app/

echo '----------------'
echo 'Subindo Servidor'
echo '----------------'
python manage.py runserver

else
echo 'exit in 3s'
sleep 1
echo 'exit in 2s'
sleep 1
echo 'exit in 1s'
sleep 1
echo 'The End Execution'
fi
}

# PASSOS PARA CRIAR UM APLICAÇÃO WEB
INSTALADORES(){

# PASSO 1: Verificar a versão do python instalada
CRIANDO_PROJETO_DJANGO
}

MAIN(){
INSTALADORES
}

MAIN
