<p align="center">
<img src="icon.png" width="400"/>
</p>

# ScotlandYard - Servidor

Servidor do app scotland yard, um jogo de tabuleiro jogado com o auxílio do app. 

## Como rodar

Para rodar o servidor localmente é necessário ter os **pip3** e **virtualenv** instalado, logo após é só rodar os comandos:
```shell
$ source env/bin/activate
$ pip3 install requirements.txt
$ python3 manage.py migrate
```

Pronto, sua máquina está pronta para rodar o servidor com o comando:
```shell
$ python3 manage.py runserver
```