MENU_ACCES="
----------------------------------------------------
Acessando um site na iternet para isso utilizaremos
uma dependĂȘncia
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

INSTALL_NUMPY(){
  pip3 install numpy
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

EOF
}

INSTALADORES(){
CRAIANDOAMBIENTEVIRTUAL
ACESSANDOSITEINTERNET
GITIGNORE
INSTALL_NUMPY
MOSTRARPACOTESINSTALADOS
}


MAIN(){
INSTALADORES
}

MAIN
