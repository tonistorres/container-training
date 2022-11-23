
#!/bin/bash
# https://giovannireisnunes.wordpress.com/2017/06/30/declaracao-de-variaveis-no-bash/
read -p 'Digite o número de app a serem criados -->> ' NUMEROS_APPS
START=1
END=$NUMEROS_APPS
echo "Countdown"

for (( c=$START; c<=$END; c++ ))
do
	echo -n "$c "
	sleep 1
done

echo
echo "Boom!"
