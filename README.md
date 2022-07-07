# peya-challenge

## Descripción
 Este proyecto se llevó adelante con el fin de resolver el desafío de PeYa. El enunciado del problema se encuentra en el root de este proyecto.
Su resolución cuenta en 2 pasos:
-   Desarrollo del modelo de ML
-   Deploy del modelo seleccionado usando flask

## Desarrollo del modelo
 Para esto se creó la carpeta models. En la misma se tienen:
 - Stg: Carpeta que contiene toda la exploración, desarrollo y selección del modelo. La idea es poder tener trazabilidad de los experimentos.
 - Prod: Modelo productivo y los artefactos necesarios para su ejecución

## API flask
   Se creó server.py para la implementación de la API que carga el modelo productivo y el pipeline productivo a partir de los datos del Yaml.

## Extras
- request example: Contiene un request de ejemplo para consultar la API.
- manual example: Jupyter con ejecución manual de la predicción, simulando la API.

## Modo de ejecución de la API
- Desde el root del proyecto ejecutar server.py
Una vez levantada la API se puede usar 'request_example.py' para probar la API.

## TO DO
Para iterar sobre este proyecto se tienen en consideración muchas tareas.
Para entrenamiento:
- Hyperparameter tuning.
- Métricas para monitoreo.
- Wrapper de cada paso del entrenamiento.
- Refactor de las funciones de preprocess para reutilizar las de utils.
Para deploy:
- Pytest
- Nuevos métodos http
- Error handling
- Posibilidad de tener share productivo de modelos
- Posibilidad de modelos en BKG
- Dockerizar

## Conclusiones
Si bien este proyecto es sólo una muestra al cual le falta muchísimo, me parece un buen puntapié para comenzar a hacer ML engineering.

