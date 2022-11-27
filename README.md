# Teste-Tecnico

## testebackend

1. Instalando...

Em seu terminal digite o seguinte comando abaixo para clonar o repositório :

    ** git clone git@github.com:izamaraa/teste-tecnico.git **

Após o clone, e com projeto já sendo executado em sua máquina utilize os
seguintes comandos:

    pip install -r requirements.txt

    python manage.py makemigrations

    python manage.py migrate

ou:

pip install -r requirements.txt

    ./manage.py makemigrations

    ./manage.py migrate

Em seguida rodar o servidor :

    python manage.py runserver

ou :

    ./manage.py runserver

2. Enviando Arquivo ...

Com o servidor rodando é possivel acessar algumas rotas, seriam elas :

envio de arquivo entrega-back-end.txt
http://127.0.0.1:8000/api/files/

listagem e post de valores, ja com a leitura de um arquivo entrega-back-end.txt
http://127.0.0.1:8000/api/ values/

3. CNAB:
   Para população do banco de dados ja existe um arquivo txt quese encontra dentro da pasta upload)

Para enviar um arquivo no formato use a seguinte configuração:

- Tipo
- Data
- Valor
- CPF
- Cartão
- Hora
- Dono
- Loja

3 20190301 00000142000 9620676017 4753\*\*\*\*3153 153453 NOME TESTE LOJA TESTE
