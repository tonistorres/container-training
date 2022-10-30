MENU_ACCES="
----------------------------------------------------
Acessando um site na iternet para isso utilizaremos
uma dependência
---------------------------------------------------
"

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

CRAIANDOAMBIENTEVIRTUAL(){
echo "$MENU_ISNTALL_ENVIRONMENT"
TIME
# deactivate
python3 -m venv .venv && source .venv/bin/activate
}

INSTALL_COLORAMA(){
  pip install colorama
}


INSTALANDOBLACKFLAKE(){
echo "Install Black"
pip3 install black
TIME
echo "Install Flake8"
pip3 install flake8
TIME
}

MOSTRARPACOTESINSTALADOS(){
  pip3 freeze
}

# https://bobbyhadz.com/blog/python-no-module-named-mysql
INTALL_CONNECTOR_MYSQ(){
pip3 install mysql-connector-python
}

ACESSANDOSITEINTERNET(){
echo "$MENU_ACCES"
INSTALANDOBLACKFLAKE
source .venv/bin/activate
which python3
}


GITIGNORE(){
touch .gitignore
cat << EOF >> .gitignore
.venv/
__pycache__

EOF
}

INSTALADORES(){
python3 -m pip install --upgrade pip
CRAIANDOAMBIENTEVIRTUAL
ACESSANDOSITEINTERNET
GITIGNORE
INSTALL_COLORAMA
MOSTRARPACOTESINSTALADOS
}


MAIN(){
INSTALADORES
}

MAIN
