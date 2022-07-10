# Adicionalmente, responde de manera conceptual las siguientes preguntas.

# Al final del ciclo de desarrollo y con los resultados sobre la mesa

-   ¿Qué tipo de accionables se podrían tomar usando los resultados del modelo?
    Con el resultado del modelo se podría implementar la API en un motor de simulación de préstados para tener el estimado del valor de la propiedad en real time dado los parámetros solicitados. En principio se podría empezar en modo shadow (es decir, que prediga el precio pero que no se tome en cuenta) para evaluar frente a heurísticas utilizadas hasta el momento. Luego ir probando el modelo para tomar decisiones pero de manera progresiva, es decir, empezando con un porcentaje de las simulaciones para ir evaluando y perfeccionando el modelo.

-    ¿Qué puntos débiles/críticos puedes detectar en los resultados obtenidos?
    De los resultados obtenidos se pueden detectar mayores diferencias en montos más altos dada la menor representación de estos inmuebles en el dataset. Se podría corregir fácilmente obteniendo más datos en las siguientes iteraciones del modelo y con más conocimiento del negocio y nuevas varibales a utilizar.

-   ¿Cuáles serían los próximos pasos para mejorar los resultados?
    Obtener más datos y nuevas variables que nos eriquezcan el conocimiento por zona por ejemplo. Probar otros modelos más sofísticados como redes neuronales.

# En tu rol de comunicador/traductor:

-   ¿De qué forma y qué recursos usarías para argumentar al lado de negocio lo bueno que es tu modelo y el impacto que podría tener este si se usa en producción?¿Qué beneficios tiene para los clientes finales y para la empresa?
    Primero conocería más las métricas utilizadas a día de hoy del lado de negocio como así también la manera de realizar la simulación. Lo que nos brindan los modelos de ML es detectar patrones ocultos que nos permitan optimizar la menera de estimar un dato, como así también automatizar y crecer en la cantidad de casos a los que podemos llegar. Por ejemplo tener una sección en la web para simular préstamos en el acto a cualquier escala sería imposible sin algún tipo de automatización.
    Esto traería como beneficio que los clientes en el momento y de manera sencilla podrían tener posibles préstamos pre aprobados o al menos el monto que se le podría otorgar y permitiría a su vez a la empresa llegar a más clientes como así también mejorar el engagement.

-   ¿Qué métricas de negocio tendrías en consideración?
  Deberíamos acordar los KPI propios del negocio. Entendiendo qué es lo que se prioriza desde el área. Por ejemplo se podría buscar minimizar los precios estimados por debajo del valor real en detrimento de los sobreestimados por ser más importantes para el negocio aunque las métricas para ese modelo no sean las mejores en el overall.

-   ¿Cómo crees que debería ser la implementación del modelo en producción y que consideración transmitirias a los equipos/personas que te ayuden a llevar este a producción (ML Engineer y al DataOps)?
    Para esta primera iteración se debería validar los tiempos de respuesta esperados en cada parte del ciclo y la calidad de los datos. Los tiempos de autoscalling por picos de throughputs. También el agregado de herramientas de monitoreo para detección de cambios en la distribución de las features como así también para los retrains.
