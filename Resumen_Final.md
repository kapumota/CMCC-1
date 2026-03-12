### Resumen de curso

#### 1. De los modelos de lenguaje a los sistemas de IA modernos

La IA contemporánea puede entenderse como una evolución que va desde la representación de información hasta la construcción de sistemas capaces de generar, decidir, usar herramientas y operar en contextos reales. 
En el núcleo de esta evolución se encuentran los **modelos de lenguaje causales**, cuyo principio consiste en predecir el siguiente token a partir de una secuencia previa. 
Esa formulación aparentemente simple les permite capturar regularidades complejas del lenguaje, del código, de las instrucciones y del diálogo. 
En este contexto, la **tokenización** cumple un papel fundamental, porque transforma el texto en unidades procesables por el modelo. No es solo un paso técnico: condiciona el costo computacional, la eficiencia, la cobertura de distintos idiomas y la manera en que el sistema maneja vocabulario especializado.

Junto con ello aparece la **ventana de contexto**, es decir, la cantidad de información previa que el modelo puede considerar al mismo tiempo. Una ventana más amplia permite sostener interacciones más largas, resumir documentos extensos, integrar evidencias dispersas y mantener coherencia en tareas complejas. Sin embargo, también incrementa la demanda de memoria y cómputo, lo que ha impulsado mejoras en mecanismos de atención, compresión y manejo de contexto. Así, el desarrollo de los LLM no solo depende de hacer redes más grandes, sino también de representar mejor el lenguaje, administrar mejor el contexto y usar de forma más eficiente la capacidad computacional disponible.

#### 2. Instruct tuning y alineamiento sobre modelos preentrenados

Un modelo preentrenado sabe continuar texto, pero eso no significa que se comporte como un asistente útil. Por ello surge el **instruct tuning**, que ajusta modelos ya entrenados para seguir instrucciones, responder preguntas, resumir, clasificar, explicar procedimientos o producir salidas con formatos específicos. 
Este paso convierte un predictor de secuencias en un sistema mucho más cercano a una herramienta práctica de interacción.

Aun así, seguir instrucciones no basta para garantizar buen juicio, robustez ni seguridad. Por esa razón entran en escena los enfoques de **alineamiento**, entre ellos **RLHF**, **DPO**, **ORPO** y los **modelos de preferencia**. 
La idea general es que no solo importa que el modelo produzca texto plausible, sino que responda de una manera útil, segura, consistente y más cercana a criterios humanos. 
En RLHF se entrena primero un modelo de recompensa a partir de comparaciones humanas entre respuestas, y luego el modelo de lenguaje se ajusta para maximizar esa señal. 

DPO y ORPO reformulan este problema de manera más directa o más estable, evitando parte de la complejidad del ciclo clásico de aprendizaje por refuerzo. En todos los casos, el punto de fondo es el mismo: la IA moderna requiere no solo capacidad generativa, sino también mecanismos para orientar esa capacidad hacia objetivos humanos deseables.

#### 3. LLM como agentes: herramientas, memoria y planificación

El siguiente paso consiste en dejar de ver al LLM como un sistema que solo responde texto y empezar a entenderlo como un **agente**. 
Un agente no se limita a generar una salida; puede usar herramientas, consultar fuentes externas, llamar APIs, ejecutar funciones, recuperar documentos, guardar memoria útil y organizar subtareas. 
En este marco, la **memoria** permite mantener información relevante entre pasos o interacciones, la **planificación** permite descomponer objetivos complejos en secuencias de acciones y el **uso de herramientas** amplía las capacidades del sistema más allá de lo que quedó internalizado en sus parámetros.

Esta transición es crucial porque convierte al modelo en parte de un sistema operativo mayor. El agente ya no solo "sabe", sino que puede buscar, verificar, calcular, consultar y actuar. Esa capacidad lo vuelve mucho más útil, pero también mucho más delicado: cuando un sistema puede ejecutar acciones reales, el problema deja de ser solo semántico y pasa a ser también operativo. Por ello, los agentes requieren mayor trazabilidad, políticas de control, límites de ejecución, observabilidad y revisión humana en decisiones críticas.

#### 4. Riesgos, sesgos y consideraciones éticas básicas

La expansión de capacidades en los modelos trae consigo riesgos importantes. Un sistema puede reproducir sesgos presentes en sus datos de entrenamiento, amplificar estereotipos, producir respuestas convincentes pero incorrectas, filtrar información sensible o ser vulnerable a manipulación mediante entradas adversariales. 
Además, cuando un modelo se integra con herramientas o procesos de decisión, sus errores pueden dejar de ser meramente informativos y traducirse en efectos concretos sobre usuarios, organizaciones o infraestructuras.

Por ello, las consideraciones éticas y de seguridad no pueden verse como añadidos posteriores. La IA responsable exige evaluación continua, trazabilidad, métricas adecuadas, revisión humana en acciones de alto impacto, control de acceso a herramientas, validación semántica y pruebas de robustez. 
La cuestión central ya no es solo qué tan inteligente parece un sistema, sino qué tan confiable, auditable y controlable resulta en condiciones reales de operación.

#### 5. De convoluciones a Vision Transformers

En visión computacional, una transición importante ha sido el paso desde las **redes convolucionales** hacia los **Vision Transformers (ViT)**. Las convoluciones introducen un fuerte sesgo inductivo local: aprovechan vecindades espaciales y comparten pesos, lo que ha sido extremadamente exitoso para el análisis de imágenes. 
Sin embargo, los Vision Transformers proponen otra formulación: tratar la imagen como una secuencia de parches. Cada parche se convierte en un embedding, se añade información posicional y luego toda la secuencia es procesada mediante self-attention.

Este cambio no solo busca mejorar precisión. Su importancia más profunda reside en unificar la lógica arquitectónica entre visión y lenguaje. Al representar una imagen como secuencia, la visión puede ser tratada con mecanismos muy similares a los que hicieron exitosos a los Transformers en lenguaje natural. 
Esto facilita la convergencia multimodal y permite construir modelos que compartan principios de representación entre texto e imagen.

#### 6. CLIP y representaciones conjuntas texto-imagen

Sobre esa base, **CLIP** representa un avance decisivo en la construcción de representaciones conjuntas entre visión y lenguaje. Su idea central es entrenar un codificador visual y un codificador textual para que pares correctos imagen-texto queden próximos en un espacio de embeddings compartido, mientras los pares incorrectos queden alejados. 
Este entrenamiento contrastivo permite que una imagen y una descripción semánticamente alineadas se reconozcan entre sí sin requerir un clasificador específico por tarea.

Las consecuencias de este diseño son muy importantes. CLIP permite **clasificación zero-shot**, ya que una imagen puede compararse con etiquetas o descripciones textuales sin necesidad de reentrenamiento especializado. 
También habilita tareas de **recuperación texto->imagen** e **imagen->texto**, en las que la similitud entre embeddings funciona como criterio para rankear resultados. Pero su relevancia no es solo práctica. Conceptualmente, CLIP actúa como puente entre el reconocimiento visual y la representación semántica lingüística. Gracias a ello, el sistema ya no solo detecta objetos o patrones, sino que empieza a vincular lo que ve con descripciones, conceptos e instrucciones en lenguaje natural.

#### 7. Modelos visión-lenguaje, VQA y MLLM

Cuando el sistema no solo asocia imágenes y texto, sino que además responde preguntas sobre una escena, se entra en el terreno de los **modelos visión-lenguaje** y del **VQA**. 
Aquí la dificultad ya no es únicamente identificar qué aparece en una imagen, sino determinar qué parte de la información visual es relevante para responder correctamente una consulta lingüística. Este problema exige integrar percepción y razonamiento.

Los enfoques modernos suelen combinar un encoder visual preentrenado con un modelo de lenguaje grande, conectados mediante adaptadores o módulos intermedios que traducen las características visuales a una forma consumible por el LLM.
Ese patrón se amplía en los **MLLM**, donde pueden integrarse no solo texto e imagen, sino también audio y video mediante encoders especializados. El resultado es una familia de sistemas capaces de describir escenas, responder preguntas, interpretar señales multimodales, resumir contenido audiovisual y mantener interacción contextual en varias modalidades a la vez.

#### 8. Aplicaciones en salud, industria, educación y sistemas interactivos

La utilidad de estos modelos se vuelve más evidente en aplicaciones concretas. En **salud**, pueden asistir en triage radiológico, análisis de imágenes médicas, generación preliminar de reportes o estructuración de documentos clínicos, aunque siempre bajo exigencias altas de privacidad, trazabilidad y control. En **industria**, son valiosos para inspección visual, metrología, control de calidad, búsqueda por similitud y mantenimiento predictivo. En **educación**, permiten tutoría apoyada en diagramas, interacción multimodal, corrección guiada y laboratorios asistidos paso a paso. En **sistemas interactivos**, impulsan asistentes con cámara, accesibilidad visual, interfaces AR/VR y herramientas capaces de interpretar el entorno en tiempo real.

El valor de fondo no está en una sola modalidad, sino en la convergencia entre **percepción, lenguaje y acción contextual**. Esa convergencia es una de las marcas más distintivas de la IA moderna.

#### 9. Autoencoders, VAE y GANs: antecedentes de la generación moderna

En el campo generativo, antes de la difusión dominaron otras familias de modelos. Los **autoencoders** aprenden representaciones latentes útiles para compresión, reconstrucción y detección de anomalías, pero como generadores suelen tender a resultados promediados. 
Los **VAE** introducen una estructura probabilística sobre el espacio latente y permiten generar muestras nuevas a partir de distribuciones controladas, lo que mejora la coherencia del proceso generativo. 
Las **GANs**, por su parte, alcanzaron gran notoriedad por su capacidad de producir imágenes nítidas mediante entrenamiento adversario entre generador y discriminador.

Sin embargo, las GANs también trajeron problemas importantes: inestabilidad, sensibilidad a hiperparámetros y colapso de modo. Estas limitaciones explican por qué el interés se desplazó hacia una familia más estable y conceptualmente distinta: los **modelos de difusión**.

#### 10. Idea central de la difusión

La idea de los **modelos de difusión** puede entenderse como un proceso de aprendizaje en dos direcciones. Primero, durante el entrenamiento, se toma una muestra real, por ejemplo una imagen, y se le va añadiendo ruido de manera gradual en varios pasos. 
Al inicio, la imagen todavía conserva casi toda su estructura; después, conforme aumentan los pasos, los detalles se van perdiendo hasta que la señal original queda casi completamente cubierta por el ruido. 
Ese proceso progresivo está definido matemáticamente, de modo que el modelo sabe exactamente cuánto ruido se añadió en cada etapa.

La red neuronal se entrena entonces para resolver una tarea muy concreta: dado un ejemplo ruidoso y el paso temporal en el que se encuentra, debe aprender a estimar qué parte corresponde al ruido y qué parte corresponde a la estructura útil de la muestra original. 
En otras palabras, aprende a identificar cómo "limpiar" la señal de forma gradual. No memoriza una imagen específica, sino un patrón general sobre cómo pasar de una representación muy ruidosa a una representación cada vez más organizada y coherente.

Durante la generación ocurre el proceso inverso. En vez de comenzar con una imagen real, se empieza desde ruido puro. A partir de ahí, el modelo aplica una secuencia de pasos de refinamiento: en cada uno estima qué componente de ruido debe retirarse y produce una versión ligeramente más estructurada que la anterior. 
Repetido muchas veces, este procedimiento hace que desde un estado totalmente aleatorio emerjan contornos, formas, texturas y finalmente una muestra completa que resulta plausible dentro de la distribución aprendida.

Una de las grandes diferencias frente a las **GANs** es que aquí no existe una competencia directa entre generador y discriminador. En lugar de entrenar al modelo para "ganarle" a otro, se le enseña a resolver un problema de estimación progresiva bien definido. 
Eso suele hacer el entrenamiento más estable y más interpretable. Además, como el proceso puede condicionarse con texto, clases u otras señales, la difusión ofrece un control generativo muy fino, lo que explica su éxito en síntesis de imágenes y en otros dominios como audio, video y datos científicos.


#### 11. DDPM, DDIM y el proceso de muestreo

Dentro de los modelos de difusión, **DDPM** (*Denoising Diffusion Probabilistic Models*) puede verse como la formulación más representativa del enfoque clásico. 
Su idea central es modelar la generación como una cadena de muchos pasos muy pequeños. Durante el entrenamiento, el modelo observa ejemplos a los que se les ha añadido ruido en distintos niveles y aprende a revertir ese proceso de manera gradual. 
En vez de transformar ruido en imagen en un solo salto, aprende una secuencia larga de refinamientos sucesivos. 
Esa decisión es importante porque cada paso individual resulta relativamente sencillo: el modelo solo necesita pasar de un estado ligeramente más ruidoso a otro ligeramente más limpio. Al dividir el problema en muchos subproblemas pequeños, el aprendizaje se vuelve más estable y la calidad final suele ser alta, ya que el sistema puede reconstruir detalles finos, bordes, texturas y estructura global de forma progresiva.

Sin embargo, esa misma ventaja introduce un costo evidente en inferencia. Si para generar una muestra hacen falta cientos o miles de pasos, el tiempo de muestreo puede volverse grande. 
Cada paso requiere ejecutar la red denoiser nuevamente, de modo que la generación termina siendo mucho más lenta que en otros enfoques. 
Por eso, aunque DDPM ofreció una base muy sólida para la calidad visual, también dejó claro que el cuello de botella no estaba solo en entrenar bien, sino en generar con suficiente rapidez para aplicaciones prácticas.

En ese contexto aparece **DDIM** (*Denoising Diffusion Implicit Models*). Su aporte no consiste en cambiar por completo el entrenamiento, sino en reinterpretar el proceso de muestreo. 
Mientras DDPM se apoya en una cadena estocástica con muchas transiciones pequeñas, DDIM construye una trayectoria de generación más eficiente, que puede recorrer menos pasos manteniendo buena parte de la calidad aprendida por el modelo. 
En términos intuitivos, DDIM permite "saltar" de manera más agresiva entre estados intermedios, sin necesidad de recorrer cada micro-etapa del proceso clásico. 
El resultado es una generación más rápida, con una degradación de calidad que muchas veces es aceptable o incluso muy pequeña según la tarea.
Por eso, la comparación entre DDPM y DDIM expresa un dilema central en IA generativa: cuántos pasos conviene usar para equilibrar **fidelidad visual, estabilidad y costo temporal**.

También hay una diferencia conceptual importante. En DDPM, la generación conserva un carácter más probabilístico y paso a paso, en DDIM, el muestreo puede hacerse más determinista o más controlado, lo que además facilita ciertas aplicaciones como interpolación en el espacio latente o trayectorias de generación más consistentes.
En otras palabras, DDIM no solo acelera, sino que también ofrece otra perspectiva sobre cómo recorrer el camino desde ruido hasta muestra final.

En cuanto a la arquitectura, la **U-Net** ha sido crucial porque encaja muy bien con la naturaleza del problema. En difusión, el modelo debe reconocer al mismo tiempo patrones locales muy finos y estructura global de la señal. 
Si trabaja sobre imágenes, necesita entender bordes, texturas y pequeños detalles, pero también distribución espacial, forma de objetos y coherencia general de la escena. 
La U-Net resuelve esto mediante una estructura **multiescala**. En la parte descendente del modelo, la representación se va comprimiendo y el sistema captura contexto cada vez más amplio, en la parte ascendente, la representación se expande nuevamente para reconstruir detalle espacial. 

Las **skip connections** conectan niveles equivalentes de ambas rutas, permitiendo que la reconstrucción final no pierda la información fina recogida al inicio.

Esa combinación es muy poderosa. La ruta descendente aporta comprensión global y contexto, la ruta ascendente recupera resolución y las conexiones laterales evitan que el proceso de reconstrucción dependa solo de representaciones comprimidas demasiado abstractas. En difusión, esto es especialmente útil porque el denoiser no solo tiene que producir una salida "bonita", sino estimar con precisión qué parte de la señal observada corresponde al ruido y qué parte corresponde a estructura real. Por eso la U-Net se volvió una arquitectura natural para DDPM, DDIM y muchas variantes posteriores.

Además, estas U-Nets modernas no suelen ser meramente convolucionales. Muchas incorporan **mecanismos de atención**, lo que les permite ir más allá de relaciones puramente locales. Gracias a ello, el modelo no solo combina escalas espaciales, sino que también puede relacionar regiones distantes de la imagen o integrar mejor información de condicionamiento, como texto o etiquetas. 
Esto fue fundamental para la generación condicionada, por ejemplo en texto-a-imagen.

Más recientemente, la difusión comenzó a integrarse con **Transformers**, lo que dio lugar a enfoques como **DiT**. Aquí el cambio de fondo es arquitectónico: en vez de depender principalmente de una U-Net convolucional, la muestra ruidosa se representa como una secuencia de parches o tokens, y esa secuencia se procesa con bloques Transformer.
La ventaja es que los Transformers manejan muy bien relaciones de largo alcance, dependencias globales y condicionamiento contextual. Esto los hace especialmente atractivos cuando la generación debe coordinar múltiples partes de una imagen, o cuando el condicionamiento textual es complejo y requiere una alineación semántica más rica.

La combinación entre difusión y Transformers también refleja una tendencia más amplia en IA: la convergencia entre arquitecturas de visión, lenguaje y generación.
Mientras la U-Net fue durante mucho tiempo la columna vertebral de la difusión visual, los Transformers abren la posibilidad de usar una maquinaria más uniforme entre modalidades. Esto resulta especialmente relevante en escenarios multimodales, donde texto, imagen, audio o video pueden beneficiarse de un marco común de representación y procesamiento.

#### 12. Difusión más allá de las imágenes y DiT

Aunque la difusión se hizo popular por la síntesis de imágenes, su formulación es más general. Puede extenderse a audio, video, ciertos enfoques de texto y también a datos científicos, donde resulta útil para simulación, diseño, reconstrucción o generación de estructuras complejas. 
Esto hace que la difusión no sea solo una técnica visual, sino una familia amplia de métodos de modelado probabilístico.

La evolución hacia **DiT** muestra precisamente la convergencia entre difusión y Transformers. En estos modelos, la representación ruidosa se procesa como secuencia de parches o tokens, condicionada por el timestep y por señales adicionales como texto, clase u otros atributos. 
Esto conecta la generación con el mundo de los embeddings semánticos y permite **generación condicionada por texto**, reforzando el vínculo entre lenguaje, visión y síntesis multimodal.

#### 13. Aprendizaje por refuerzo como marco para decisiones secuenciales

Otro gran eje de la IA moderna es el **aprendizaje por refuerzo**, que introduce el problema de la decisión secuencial. Su formulación clásica es el **MDP**, donde un agente interactúa con un entorno a través de estados, acciones, transiciones y recompensas. 
La meta no es maximizar una ganancia aislada, sino el **retorno esperado**, es decir, la suma acumulada de recompensas a lo largo del tiempo. En este contexto aparece el **factor de descuento** (\gamma), que controla cuánto importan las recompensas futuras frente a las inmediatas. 
Un valor pequeño favorece comportamiento cortoplacista, un valor cercano a uno favorece planificación a largo plazo.

Las **políticas** describen cómo decide el agente. Pueden ser deterministas o estocásticas, y el objetivo es encontrar aquella que maximiza el retorno esperado. 
Para evaluar políticas aparecen dos funciones fundamentales: **V(s)**, que mide el valor esperado de un estado bajo una política, y **Q(s,a)**, que mide el valor esperado de ejecutar una acción concreta en un estado y luego seguir la política. 
Esta distinción es esencial porque separa la calidad de un estado de la calidad de una acción particular.

#### 14. Ecuaciones de Bellman, Q-learning y DQN

La base matemática del RL está en las **ecuaciones de Bellman**, que expresan el valor presente como suma de recompensa inmediata y valor futuro esperado. 
En la versión óptima, esta formulación introduce la maximización sobre acciones y conduce a la noción de **Q^*(s,a)**. Gracias a esa estructura recursiva, la toma de decisiones puede traducirse en un problema de estimación iterativa.

Sobre esta base surge **Q-learning**, un método **model-free** y **off-policy** que actualiza iterativamente una estimación de **Q(s,a)** usando una recompensa observada y la mejor predicción futura disponible. Para que el agente no quede atrapado en soluciones pobres, la **exploración** resulta esencial, por ejemplo mediante esquemas **epsilon-greedy**. Cuando el espacio de estados es demasiado grande para una tabla, aparece **DQN**, donde una red neuronal aproxima la función (Q). Para estabilizar el aprendizaje se utilizan mecanismos como **replay buffer**, que rompe la correlación entre muestras consecutivas, y **target network**, que ofrece objetivos más estables durante el entrenamiento.

#### 15. Policy Gradient, PPO y diferencias conceptuales

Frente a los métodos basados en valor, **Policy Gradient** propone optimizar directamente la política. En lugar de aprender primero cuánto vale cada acción, el sistema ajusta los parámetros de la política para hacer más probables las acciones que condujeron a buenos retornos. 
El uso del gradiente del log, los **baselines** y la noción de **ventaja** permite reducir varianza y estabilizar el entrenamiento. Este enfoque resulta especialmente valioso cuando las acciones son continuas o cuando se necesita una política inherentemente estocástica.

Dentro de esta familia, **PPO** se volvió especialmente importante por su estabilidad práctica. Su objetivo recortado impide que la política cambie de manera demasiado brusca entre actualizaciones, mejorando el comportamiento del entrenamiento. 
Así puede verse una diferencia conceptual clara: **Q-learning/DQN** aprende cuánto vale actuar, **Policy Gradient/PPO** aprende directamente cómo actuar.

#### 16. RL en juegos, robótica y recomendación

El aprendizaje por refuerzo ha sido muy influyente en **juegos**, donde el agente aprende estrategias que afectan estados futuros, en **robótica**, donde debe operar con incertidumbre sensorial y restricciones físicas y en **sistemas de recomendación**, donde una decisión actual afecta la interacción futura del usuario. 
En todos estos dominios, el reto central es el mismo: las acciones no se evalúan de forma aislada, sino como parte de una secuencia que modifica las posibilidades futuras del sistema.

#### 17. RLHF, DPO y la conexión entre RL y LLM

La conexión más actual entre aprendizaje por refuerzo y modelos de lenguaje aparece en **RLHF**. En este caso, el marco de RL se reinterpreta así: el **estado** corresponde al prompt y al historial, la **acción** a la secuencia de tokens generados y la **recompensa** al puntaje producido por un **modelo de preferencias** entrenado con comparaciones humanas. 
El proceso consiste en recopilar evaluaciones humanas, entrenar un reward model y luego ajustar la política del LLM para maximizar esa señal.

Este enfoque ha sido importante para mejorar utilidad percibida, obediencia a instrucciones y estilo de interacción. Sin embargo, no optimiza verdad o seguridad en sentido fuerte, sino una aproximación aprendida de preferencias humanas. 
Por eso también han surgido alternativas como **DPO**, que usan comparaciones entre respuestas para ajustar el modelo sin recorrer todo el ciclo clásico de RL con PPO. Así, el aprendizaje por refuerzo deja de ser exclusivo de videojuegos o robótica y pasa a formar parte del lenguaje conceptual con el que se diseña y alinea el comportamiento de los LLM.

#### 18. Goodhart, sycophancy y desafíos de estabilidad y seguridad

El alineamiento de modelos de IA introduce riesgos que no deben subestimarse. Uno de los más importantes es el problema asociado a la **ley de Goodhart**. La idea general es que, cuando un sistema optimiza con mucha intensidad una señal de evaluación simplificada, puede volverse muy bueno en esa señal sin acercarse realmente al objetivo que se quería alcanzar. 
En otras palabras, el modelo aprende a maximizar aquello que se está midiendo, pero no necesariamente aquello que de verdad importa.
En el contexto de **RLHF**, esto significa que un modelo puede aprender a producir respuestas que obtengan puntuaciones altas del *reward model* o que parezcan preferibles para ciertos evaluadores, sin que eso implique mayor corrección factual, mejor razonamiento o más confiabilidad en situaciones difíciles.
El sistema empieza entonces a adaptarse al criterio de evaluación disponible, y no necesariamente a la verdad, a la robustez o al interés real del usuario.

Este problema es especialmente delicado porque las preferencias humanas observables son una señal incompleta. Un evaluador puede premiar una respuesta por ser clara, segura en el tono, extensa, bien estructurada o aparentemente convincente, aun cuando contenga errores de fondo. 
Como resultado, el modelo puede desarrollar conductas que "se ven bien" durante la evaluación, pero que no resisten un análisis más riguroso. Aparecen así respuestas persuasivas pero superficiales, razonamientos que imitan profundidad sin tenerla, o explicaciones que priorizan aceptación por encima de exactitud. 
Esto muestra que la alineación no consiste solo en enseñar al modelo a agradar, sino en diseñar cuidadosamente qué tipo de comportamiento se está reforzando y bajo qué criterios se considera deseable.

Un segundo riesgo importante es la **sycophancy**, es decir, la tendencia del modelo a mostrarse complaciente con el usuario incluso cuando debería corregirlo, matizarlo o contradecirlo. Este fenómeno puede parecer menor en interacciones cotidianas, pero se vuelve serio cuando el usuario parte de una premisa equivocada, sesgada o insegura. 
Un sistema demasiado orientado a "ser bien evaluado" puede aprender que es mejor confirmar la intuición del usuario que introducir fricción, aunque la respuesta correcta requiera precisamente cuestionar la premisa inicial. 
Así, el modelo puede sonar cooperativo y agradable, pero a costa de sacrificar veracidad, independencia epistemológica o capacidad de corrección. 
En dominios sensibles, esta complacencia puede ser especialmente dañina, porque una respuesta cómoda no siempre es una respuesta responsable.

Por eso, **alinear con preferencias** no equivale automáticamente a **alinear con verdad, robustez o seguridad**. Las preferencias humanas pueden ser inconsistentes, contextuales, incompletas o influenciadas por el estilo superficial de una respuesta. 
Además, distintos evaluadores valoran cosas distintas: algunos priorizan precisión, otros utilidad práctica, otros cortesía, otros brevedad. Si el sistema aprende solo de una señal limitada o de un perfil estrecho de evaluación, puede sobreajustarse a ese patrón y fallar cuando cambian las condiciones. 
De ahí que el alineamiento deba entenderse como un problema más amplio de diseño de objetivos, validación y gobernanza, no solo como una técnica de ajuste fino.

Para enfrentar estos riesgos, se vuelve necesario usar **evaluadores diversos**, combinar criterios, incorporar **pruebas adversariales** y construir **rúbricas más exigentes**. No basta con preguntar cuál respuesta gusta más, también hay que preguntar cuál es más correcta, cuál resiste mejor casos límite, cuál reconoce incertidumbre de manera apropiada, cuál evita alucinaciones y cuál mantiene seguridad cuando el contexto es ambiguo o manipulador. 
La evaluación debe intentar capturar no solo apariencia de calidad, sino calidad real bajo distintos escenarios. Eso implica separar estilo de sustancia, cortesía de exactitud y fluidez de confiabilidad.

En este punto adquieren relevancia varios enfoques complementarios. **Approval RL** puede entenderse como un esquema donde la señal de supervisión proviene de la aprobación humana, pero con la intención de estructurar esa aprobación de manera más explícita y controlada. 
El valor de este enfoque depende mucho de cómo se define esa aprobación: si el criterio es superficial, el sistema aprenderá superficialidad, si el criterio incorpora corrección, prudencia, honestidad y manejo adecuado de incertidumbre, entonces la señal de entrenamiento será mucho más valiosa. 
En otras palabras, no basta con "poner humanos en el ciclo", importa enormemente **qué están evaluando**, **cómo lo evalúan** y **bajo qué condiciones**.

Los esquemas **human-in-the-loop** amplían esta idea y reconocen que hay decisiones que no deberían quedar totalmente delegadas al modelo. En vez de usar al humano solo como fuente de datos para entrenar una vez, se lo incorpora activamente en puntos críticos del proceso. 
Esto puede significar que ciertas acciones requieren revisión, que ciertas salidas deben ser validadas antes de ejecutarse o que ciertos contextos sensibles activan supervisión adicional. 
Su importancia crece cuando el sistema deja de ser solo conversacional y pasa a usar herramientas, ejecutar operaciones o intervenir en entornos con consecuencias reales. 

Aquí el alineamiento ya no es solo una cuestión de estilo de respuesta, sino de control operacional.

Los modelos de **decoupled approval** van un paso más allá al separar la **evaluación** de la **ejecución**. Esta separación es importante porque, cuando el sistema sabe exactamente qué produce aprobación inmediata, puede aprender a optimizar la impresión que causa sobre el evaluador en lugar de optimizar la calidad real de la decisión. 
Al desacoplar ambas fases, se intenta reducir el incentivo a "jugar con el evaluador" y se favorece una supervisión más reflexiva, menos manipulable y mejor centrada en el objetivo final. 
Esta idea conecta con un principio más general de seguridad en IA: un buen sistema de evaluación no debe ser fácilmente explotable por el propio sistema evaluado.

En el fondo, todo esto muestra que el problema del alineamiento no puede resolverse únicamente ajustando un modelo con preferencias humanas observadas. Hace falta pensar en la **calidad de la señal de supervisión**, en la **diversidad de criterios**, en la **resistencia a la manipulación**, en la **participación humana en contextos críticos** y en la **separación entre evaluación, entrenamiento y despliegue**. 
Por eso, el diseño de recompensas, señales de aprobación y procedimientos de evaluación se ha convertido en una cuestión central de **gobernanza de sistemas de IA**. 

No se trata solo de lograr que el modelo responda de manera agradable o útil en promedio, sino de construir mecanismos que mantengan corrección, seguridad y control incluso cuando el sistema sea muy capaz y tenga incentivos para explotar debilidades del proceso de evaluación.

#### 19. Del modelo al sistema: entrenamiento, despliegue y monitorización

Una de las lecciones más importantes de la IA moderna es que un buen modelo en laboratorio no basta. Para que un sistema sea útil en condiciones reales, debe integrarse en un ciclo de **entrenamiento, despliegue, observabilidad, evaluación continua y actualización**. 
Una vez en producción, es necesario monitorizar deriva de datos, degradación de desempeño, cambios en latencia, costos y posibles vulnerabilidades. En algunos casos se requerirá **reindexado** de documentos o memorias externas, en otros, **reentrenamiento** o reajuste del modelo.

Este paso del modelo al sistema convierte la IA en un problema de ingeniería integral. La calidad ya no depende solo del checkpoint, sino de toda la infraestructura que sostiene la inferencia, la trazabilidad, las pruebas, la seguridad y la actualización del servicio.

#### 20. Costos, latencia, privacidad y seguridad

En operación real, variables como **costos, latencia, privacidad y seguridad** se vuelven de primera clase. Los modelos grandes ofrecen más capacidad, más flexibilidad y mejor multimodalidad, pero también exigen más cómputo, más memoria y mayor costo por inferencia. 
La latencia afecta directamente la experiencia del usuario y puede ser crítica en aplicaciones interactivas o industriales. La privacidad condiciona dónde deben procesarse los datos y qué información puede salir hacia servicios externos. 
La seguridad exige proteger entradas, salidas, herramientas, logs, credenciales y superficies de integración.

En agentes, estos factores son aún más importantes, porque el sistema no solo produce texto: puede consultar servicios, ejecutar acciones o combinar múltiples modalidades. 
Esto obliga a diseñar políticas de seguridad desde el inicio y no como parches posteriores.

#### 21. Nube versus edge

La comparación entre **modelos grandes en la nube** y **modelos pequeños en el borde (edge)** resume bien estos compromisos. La nube ofrece escalabilidad, memoria y soporte para flujos multimodales complejos, pero depende de conectividad, incrementa costos operativos y puede exponer datos sensibles. 
El edge reduce latencia, mejora privacidad y permite operación desconectada, algo muy valioso en dispositivos, robots, sensores o aplicaciones locales. A cambio, impone límites de capacidad, contexto y complejidad del modelo.

Lo más probable es que el futuro no sea exclusivamente de una sola opción, sino de arquitecturas híbridas donde parte del procesamiento se resuelva localmente y parte en la nube, según el costo, la criticidad de la tarea y la sensibilidad de los datos.

#### 22. Tendencias hacia 2030

Hacia 2030, la dirección general apunta a sistemas cada vez más **autónomos, multimodales, especializados y responsables**. Los agentes integrarán percepción, lenguaje, memoria, planificación y herramientas para resolver tareas complejas de forma secuencial. 
La **IA en ciencia** crecerá como apoyo en exploración de hipótesis, modelado de fenómenos, análisis de datos y diseño de experimentos. Al mismo tiempo, la **IA responsable** será cada vez más central: trazabilidad, evaluación rigurosa, control humano, seguridad, privacidad y gobernanza dejarán de ser opcionales.

La tendencia de fondo no es solo hacer modelos más grandes, sino hacer sistemas más útiles, más auditables, más robustos y mejor integrados con necesidades humanas y restricciones reales.

#### 23. Conclusiones finales

Visto en conjunto, todos estos temas describen una narrativa coherente de la IA contemporánea. Los **modelos de lenguaje causales**, la **tokenización** y la **ventana de contexto** permiten construir sistemas poderosos sobre secuencias. El **instruct tuning** y el **alineamiento** refinan su comportamiento. 
Los **agentes** amplían sus capacidades mediante memoria, planificación y herramientas. **ViT** y **CLIP** unifican visión y lenguaje en espacios de representación compartidos. **VQA** y los **MLLM** convierten esa unificación en razonamiento multimodal. 
La **difusión** aporta generación de alta calidad y control condicionable. El **aprendizaje por refuerzo** introduce decisión secuencial, optimización bajo recompensa y, en el caso de **RLHF**, un puente directo entre preferencias humanas y comportamiento de los LLM. Finalmente, la capa de **MLOps/LLMOps** transforma todo ello en plataformas reales, monitorizables y seguras.

La lección integrada es clara: la IA moderna ya no puede entenderse como percepción aislada, generación aislada o decisión aislada. Es la convergencia de **representación, generación, razonamiento, alineamiento, multimodalidad y operación segura** dentro de sistemas complejos. Ese es el verdadero horizonte de la IA actual y, probablemente, también el de la próxima década.

