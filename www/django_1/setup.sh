MENU_ISNTALL_ENVIRONMENT="
----------------------------------------------------
Criando um Ambiente Virtual
---------------------------------------------------
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
cd app
mkdir templates
touch urls.py
cd ..
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
