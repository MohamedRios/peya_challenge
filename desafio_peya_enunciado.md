# Machine Learning aplicado
En esta notebook se presenta un problema práctico de negocio que se desea resolver usando técnicas de ML.
 
La idea es que puedas demostrar tus capacidades en el desarrollo del ciclo completo de un problema de ML, desde el entendimiento, modelo y comunicación del problema. En lo particular se espera es que puedas:
 
* entender el caso planteado desde la óptica del negocio y el problema de ML a resolver
* definir las métricas con las que se va a evaluar el performance del modelo
* leer, limpiar y transformar el dato si es necesario
* realizar una exploratoria inicial
* seleccionar y entrenar el/los modelo(s) que resuelvan el problema
* evaluar el performance de el/los modelo(s)
* seleccionar el mejor modelo y guardarlo en un archivo que pueda ser usado en producción
* Desarrollar un código que sea mantenible, reproducible y apto para ser automatizado.
 
Adicionalmente, responde de manera conceptual las siguientes preguntas.
 
1. Al final del ciclo de desarrollo y con los resultados sobre la mesa
 * ¿Qué tipo de accionables se podrían tomar usando los resultados del modelo?
 * ¿Qué puntos débiles/críticos puedes detectar en los resultados obtenidos?
 * ¿Cuáles serían los próximos pasos para mejorar los resultados?
 
2. En tu rol de comunicador/traductor:
 - ¿De qué forma y qué recursos usarías para argumentar al lado de negocio lo bueno que es tu modelo y el impacto que podría tener este si se usa en producción?¿Qué beneficios tiene para los clientes finales y para la empresa?
 - ¿Qué métricas de negocio tendrías en consideración?
 - ¿Cómo crees que debería ser la implementación del modelo en producción y que consideración transmitirias a los equipos/personas que te ayuden a llevar este a producción (ML Engineer y al DataOps)?
 
Notas:
* El uso de herramientas y frameworks es de libre elección.
* La evaluación **no estará centrada en el performance del modelo** si no en el desarrollo de todas las partes del problema, las definiciones tomadas para desarrollar el problema y la explicación de los resultados.
 

-----


## Caso 1

La consultora coreML tiene que presentar una propuesta a un banco para predecir el valor de tasación de una propiedad para crear un nuevo servicion que complemente el actual servicio de simulación de préstamos. 

Para ello disponibilizaron un dataset de casas y apartamentos a la venta en Montevideo [(Dataset)](data/num_dataset_houses.csv) con un conjunto de caracteristicas de las propiedades. La idea es que a la hora de la simulación las personas puedan ingresar las características de la propiedad y que un modelo de ML pueda predecir el valor de esta propiedad el cual sera un insumo a la hora de la simulación.

Haz los supuestos que creas necesarios a la hora de construir features como el modelo.


### Descripción de atributos de las propiedades en el dataset
| Field | Type | Description |
|---|---|---|
| ano_de_construccion  | int | Año de  construcción de la propiedad |
| banos                | int | número de baños |
| disposicion          | str | disposición de la propiedad |
| dormitorios          | int | numero de dormitorio |
| estado               | str | calidad de la propiedad |
| garajes              | int | número de garajes |
| gastos_comunes       | float | gastos comunes de la propiedad |
| m2_de_la_terraza     | float | área de la terraza |
| m2_del_terreno       | float | área de la propiedad |
| m2_edificados        | float | area construida |
| price                | float | precio de la propiedad |
| tipo_propiedad       | str | tipo de propiedad (casa o apartamento) |
| vivienda_social      | bool | si es una cooperativa o no |
| zona                 | str | Nombre del barrio donde se encuentra la propiedad |
