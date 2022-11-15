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

INSTALL_NUMPY(){
 pip install numpy
}


INSTALL_PANDAS(){
# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# Instalação de pandas
# Se você já tem o Python e o PIP instalados em um sistema,
# a instalação do Pandas é muito fácil.
# C:\Users\Your Name>pip install pandas
# Se este comando falhar, use uma distribuição python que
# já tenha o Pandas instalado, como Anaconda, Spyder etc.

  echo '--------------'
  echo "Install Pandas"
  echo '--------------'
  sleep 1
  echo '2s'
  sleep 1
  echo '1s'
  sleep 1
  pip install pandas
}
INSTALL_MATPLOTLIB(){
  echo '--------------'
  echo "Install Matplotlib"
  echo '--------------'
  sleep 1
  echo '2s'
  sleep 1
  echo '1s'
  sleep 1
  python -m pip install -U pip
  python -m pip install -U matplotlib
}
INSTALL_SCIKIT_LEARN(){

  echo '---------------------'
  echo "Install Scikit-Learn"
  echo '---------------------'
  sleep 1
  echo '2s'
  sleep 1
  echo '1s'
  sleep 1
  pip install -U scikit-learn
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


INSTALL_COLORAMA(){
  pip install colorama
}


INSTALADORES(){
CRAIANDOAMBIENTEVIRTUAL
ACESSANDOSITEINTERNET
GITIGNORE
INSTALL_COLORAMA
INSTALL_NUMPY
INSTALL_PANDAS
INSTALL_MATPLOTLIB
INSTALL_SCIKIT_LEARN
MOSTRARPACOTESINSTALADOS
}


MAIN(){
INSTALADORES
}

MAIN
