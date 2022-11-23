
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
