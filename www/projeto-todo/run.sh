TIME(){
  sleep 1
  echo '2s'
  sleep 1
  echo '1s'
}

RODANDO_PROJETO(){
# TIME
echo '**************************'
echo 'Rodando Projeto Django'
echo '**************************'
python manage.py runserver

}

MAIN(){
RODANDO_PROJETO
}

MAIN
