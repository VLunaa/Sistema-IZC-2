# PROYECTO IZC

## Herramientas
- Django
- Contenedor Docker
- HTML
- CSS
- JS
- Bootstrap
- Google Maps API


## Correr el sistema en pruebas
docker-compose up --build

docker-compose exec app bash

python3 manage.py check

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver 0:8000

## Instalar requerimientos 
python3 manage.py -r requirements.txt

## Correr las pruebas de gestion y el coverage

python3 manage.py test gestion/tests

coverage run --branch --source='.' --omit=*test*,*migrations*,*__init*,*settings*,*apps*,*wsgi*,*admin.py,*asgi.py,manage.py,*urls.py,*usuarios* manage.py test gestion/tests

coverage run --branch --source='.' --omit=*test*,*migrations*,*__init*,*settings*,*apps*,*wsgi*,*admin.py,*asgi.py,manage.py,*urls.py manage.py test gestion/tests usuarios/tests

coverage html -d coverage_html

## Correr pruebas de behave en especifico
 
behave -i nombre.feature

## Estandares de codificacion

autopep8 -ir .

flake8 --max-complexity=7 --max-line-length=205 --exclude settings*,admin* .

## Limpiar base de datos y docker

docker container prune

docker image prune -f

docker volume prune -f

docker network prune

docker system prune

docker system prune --volumes

## Jmeter comando

jmeter -l salida -e -o dashboard -n -t NOMBREPROYECTO.jmp -f

jmeter -l salida -e -o dashboard -n -t NOMBREPROYECTO.jmx -f
