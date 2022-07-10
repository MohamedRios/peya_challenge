# peya-challenge

## Descripción
 Este proyecto se llevó adelante con el fin de resolver el desafío de PeYa. El enunciado del problema se encuentra en el root de este proyecto.
Su resolución cuenta en 2 pasos:
-   Desarrollo del modelo de ML
-   Deploy del modelo seleccionado usando flask

## Desarrollo del modelo
 Para esto se creó la carpeta models. En la misma se tienen:
 - Stg: Carpeta que contiene toda la exploración, desarrollo y selección del modelo (agrupado por experimento). La idea es poder tener trazabilidad de los experimentos para su reutilización o verificación. Para esto se creó un archivo yaml por experimento a fin de facilitar la automatización.
 - Prod: Modelo productivo y los artefactos necesarios para su ejecución. A día de hoy se soporta un sólo modelo productivo a la vez.
 Para la utilización del modelo se deberán realizar las siguientes tareas:
 - Completar el params.yaml del experimento a implementar (para el experimento_1 ya está completo). 
 - Ejecutar preprocess.ipynb que generará el pipeline (mismo que usará la API) y los datasets para entrenar.
 - Ejecutar train.ipynb que generará los modelos a validar.
 - Ejecutar validate.ipynb para seleccionar el mejor modelo y completar el params.yaml con los datos del modelo a productizar (para para el experimento_1 ya está completo). 
 - Ejecutar deploy.ipynb que llevará el modelo seleccionado y su pipeline a la carpeta prod para que la API pueda utilizarlo.

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
- Métricas para monitoreo.
- Feedback para reentrenamiento (ej. continous training)
Para deploy:
- Pytest
- Nuevos métodos http
- Error handling
- Posibilidad de tener share productivo de modelos
- Posibilidad de modelos en BKG
- Dockerizar
- Soportar valores distintos a los esperados

## Conclusiones
Si bien este proyecto es sólo una muestra al cual le falta muchísimo, me parece un buen puntapié para comenzar a hacer ML engineering.

