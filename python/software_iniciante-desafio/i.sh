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

MENU_ISNTALL_PARSEL="
----------------------------------------------------
Instalando Parsel
---------------------------------------------------
"

MENU_ISNTALL_REQUESTS="
----------------------------------------------------
Instalando Parsel
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




INSTALANDOBLACKFLAKE(){
echo "Install Black"
pip install black
TIME
echo "Install Flake8"
pip install flake8
TIME
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
}


MAIN(){
INSTALADORES
}

MAIN
