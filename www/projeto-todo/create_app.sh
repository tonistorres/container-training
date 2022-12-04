# Bootstrap grid
# https://www.youtube.com/watch?v=VAgZE2yQNHY

# https://www.youtube.com/watch?v=NAstsS4rVrY&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=3
# https://www.youtube.com/watch?v=6EpHpUoBQDc&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=4
# https://www.youtube.com/watch?v=gBnLE2rFpqk&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=5
# https://www.youtube.com/watch?v=zKHxYWIjj3U&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=6
# https://www.youtube.com/watch?v=biuNVj1PuGs&list=PLnDvRpP8BnewqnMzRnBT5LeTpld5bMvsj&index=7
echo --------------------------------------------------------
echo -e "\033[31m Deseja Criar um App Djago? \033[m"
read -p "s (SIM ) e n (NÃO) -->> " CONFIRM
echo --------------------------------------------------------
if [ "$CONFIRM" = s ];then

read -p 'Digite o número de app a serem criados -->> ' NUMEROS_APPS

START=1
END=$NUMEROS_APPS

for (( c=$START; c<=$END; c++ ))
do
    read -p 'Digite o nome do App Django -->> ' NAME_APP_DJANGO
    python manage.py startapp $NAME_APP_DJANGO
    sleep 1
    echo '************************'
    echo 'Entrando na pasta do App'
    echo '************************'
    cd $NAME_APP_DJANGO
    sleep 1
    echo '************************'
    echo 'Criando o arquivo urls.py'
    echo '************************'
    touch urls.py
    sleep 1
    echo '****************************'
    echo 'Adicionando conteudo urls.py'
    echo '****************************'

cat << EOF >> urls.py
from django.urls import path
from .views import here_name_view
urlpatterns = [path("", here_name_view, name="here_name_view")]
EOF

    sleep 1
    echo '**************************'
    echo 'Excluindo arquivo views.py'
    echo '**************************'
    rm -rf views.py
    sleep 1
    echo '**************************'
    echo 'Criando arquivo views.py'
    echo '**************************'
    touch views.py
    sleep 1
    echo '******************************'
    echo 'Adicionando conteudo views.py'
    echo '******************************'
cat << EOF >> views.py
from django.shortcuts import render
from django.http import HttpResponse
def tasksList(request):
    return render(request, "nome_pasta_dentro_template/example.html")
EOF

    sleep 1
    echo '**************************'
    echo 'Excluindo arquivo admin.py'
    echo '**************************'
    rm -rf admin.py
    sleep 1
    echo '**************************'
    echo 'Criando arquivo admin.py'
    echo '**************************'
    touch admin.py
    sleep 1
    echo '******************************'
    echo 'Adicionando conteudo admin.py'
    echo '******************************'
cat << EOF >> admin.py
from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)
EOF

 sleep 1
    echo '**************************'
    echo 'Excluindo arquivo models.py'
    echo '**************************'
    rm -rf models.py
    sleep 1
    echo '**************************'
    echo 'Criando arquivo models.py'
    echo '**************************'
    touch models.py
    sleep 1
    echo '******************************'
    echo 'Adicionando conteudo models.py'
    echo '******************************'
cat << EOF >> models.py
from django.db import models
class Xsingular(models.Model):
    exemplo = models.CharField("exemplo", max_length=50)
def __str__(self):
    return f"Exemplo: {self.exemplo}\n"
EOF




    mkdir templates
    cd templates
    mkdir $NAME_APP_DJANGO
    cd $NAME_APP_DJANGO
    touch index.html

cat << EOF >> index.html
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Documento Exemplo</title>
</head>
<body>
  <h1>EXAMPLE PARA ALTERAÇÃO</h1>
</body>
</html>
EOF
    cd ..
    cd ..
done

echo
echo "Fim execução comando cria App!"
else
echo 'exit in 3s'
sleep 1
echo 'exit in 2s'
sleep 1
echo 'exit in 1s'
sleep 1
echo 'The End Execution'
fi
