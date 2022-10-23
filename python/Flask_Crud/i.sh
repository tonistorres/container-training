MENU_ACCES="
----------------------------------------------------
Crud Python utilizando Flask
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

UPDATE_PIP(){
  python3 -m pip install --upgrade pip
}


CRAIANDOAMBIENTEVIRTUAL(){
echo "$MENU_ISNTALL_ENVIRONMENT"
TIME
# deactivate
python3 -m venv .venv && source .venv/bin/activate
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

INSTALL_FLASK(){
  pip3 install flask
}

GITIGNORE(){
touch .gitignore
cat << EOF >> .gitignore
.venv/

EOF
}

INSTALADORES(){
UPDATE_PIP
CRAIANDOAMBIENTEVIRTUAL
ACESSANDOSITEINTERNET
GITIGNORE
MOSTRARPACOTESINSTALADOS
INTALL_CONNECTOR_MYSQ
INSTALL_FLASK
pip3 install pymysql
}


MAIN(){
INSTALADORES
}

MAIN
