
# mysn


## Levantar el proyecto con docker-compose

- Crear un .env a partir del .env.template y completar las constantes que falten.
- Ejecutar docker-compose build
- Ejecutar docker-compose up
- En local puedes acceder a http://0.0.0.0:8000/


## Informacion sobre los endpoints
En local puedes acceder a la documentacion de swagger con http://0.0.0.0:8000/docs

## Ejemplo con queryparams
http://0.0.0.0:8000/user/?order_by=-name&page=1&size=10


## Ejecutar los tests
Puedes ejecutar los tests ejecutando:
docker-compose run --rm fastapi pytest .

## Otras librerias usadas
[fastapi-filter](https://fastapi-filter.netlify.app/) para los filtros de busqueda.
[fastapi-pagination](https://uriyyo-fastapi-pagination.netlify.app/) para la paginacion en listados.
[alembic](https://alembic.sqlalchemy.org/en/latest/) para manejo de migraciones.
