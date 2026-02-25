### Actividad de discusión guiada 5 (por grupos)

Tomar el **mismo caso de uso** elegido en la Actividad de la clase 1 (y refinado en las Actividades de las clases 2, 3 y 4) y proponer una **versión conceptual basada en visión computacional moderna y modelos multimodales** para ese problema, definiendo qué parte del caso requiere percepción visual, cómo compararían CNN vs. ViT, cómo usarían representaciones conjuntas texto-imagen (CLIP), y cómo evolucionarían hacia un sistema VLM/MLLM con texto, imagen, audio y video.

#### Uso de Copilot/ChatGPT (apoyo permitido)

Se permite usar Copilot o ChatGPT para:

* organizar ideas,
* aclarar conceptos,
* revisar coherencia técnica,
* resumir para diapositivas.

**No se permite** copiar texto sin entenderlo. El grupo debe poder explicar cada decisión.

#### Instrucciones para cada grupo

Usando su caso de uso de las actividades previas, respondan de forma breve:

#### 1. ¿Qué parte del caso requiere visión o multimodalidad?

Definan **qué parte** de su problema se beneficia de visión computacional o de un enfoque multimodal (no todo el pipeline tiene que ser multimodal).

* ¿Su caso usa imágenes, video, audio o texto + evidencia visual?
* ¿Qué tarea visual quieren resolver? (clasificación, detección, segmentación, recuperación, VQA, resumen multimodal)
* ¿Qué parte seguiría siendo no visual? (reglas, BD, validaciones, humano)

> Si su caso no requiere visión en una primera versión, indiquen si la multimodalidad **no** es la primera opción y en qué etapa futura podría aparecer.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Nuestro caso de uso es [caso] y el problema es [problema].
En las actividades anteriores propusimos [solución base/Transformer/LLM-agente].
Ayúdanos a identificar si visión computacional o multimodalidad tiene sentido aquí:
1) qué parte del pipeline lo usaría,
2) qué tipo de entrada manejaría (imagen/video/audio/texto),
3) qué salida produciría,
4) si realmente aporta valor frente a una versión solo textual o tabular.
Responde en viñetas, breve y técnico.
```

#### 2. Baseline visual: CNN (primera versión práctica)

Propongan una **primera aproximación con CNN** para la parte visual del caso.

Incluyan:

* ¿Qué entrada usarían? (imagen, lote de imágenes, frames de video)
* ¿Qué salida produce? (clase, bounding boxes, máscara, embedding)
* ¿Por qué CNN sirve como baseline en su caso?
* ¿Qué limitación esperan? (contexto global, escalabilidad, integración con texto, etc.)

> No se espera arquitectura detallada capa por capa; sí una decisión técnica razonable para una primera versión.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Para nuestro caso [caso], propón una primera solución visual usando CNN.
Incluye:
1) tipo de entrada (imagen/frame),
2) salida esperada,
3) por qué CNN sirve como baseline,
4) qué limitación tendría.
No inventes resultados; razona de forma práctica.
```

#### 3. De convoluciones a Vision Transformers (ViT): motivación y esquema general

Expliquen por qué considerarían un **Vision Transformer (ViT)** en su problema.

Incluyan:

* ¿Qué limitación de CNN podría motivar usar ViT?
* ¿Cómo se transforma la imagen en **patches**?
* ¿Cómo se convierten esos patches en "tokens"?
* ¿Qué rol juegan embeddings, codificación posicional y encoder Transformer?
* ¿Qué salida obtendrían en su caso?

> No se espera fórmula completa; sí una explicación clara del flujo: imagen -> patches -> embeddings -> Transformer -> salida.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Explica cómo aplicar un Vision Transformer (ViT) a nuestro caso [caso].
Incluye:
1) por qué usar ViT en vez de solo CNN,
2) cómo se divide la imagen en patches,
3) cómo se procesan como tokens,
4) qué salida obtendríamos.
Usa lenguaje técnico claro y sin fórmulas largas.
```

#### 4. CNN vs. ViT en su caso (comparación técnica y decisión práctica)

Comparen **CNN** y **ViT** para su caso.

Analicen:

* disponibilidad de datos (pocos vs muchos),
* costo de entrenamiento/inferencia,
* necesidad de contexto global,
* uso de modelos preentrenados,
* latencia esperada,
* facilidad de integración con texto (si aplica).

Definan:

* cuál usarían como **primera versión**,
* cuál dejarían como **segunda versión**,
* qué criterio usarían para decidir el cambio.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Compara CNN vs Vision Transformer (ViT) para nuestro caso [caso].
Analiza:
1) datos disponibles,
2) costo de entrenamiento/inferencia,
3) contexto global,
4) uso de modelos preentrenados,
5) latencia.
Recomienda una primera versión y una versión posterior.
```

#### 5. Representaciones conjuntas texto-imagen: CLIP y recuperación

Propongan cómo usarían **CLIP** (o una idea equivalente de embeddings conjuntos texto-imagen) en su caso.

Incluyan:

* ¿Qué texto tendrían? (consulta, descripción, reporte, etiqueta, pregunta)

* ¿Qué imágenes tendrían? (foto, frame, evidencia visual, documento escaneado)

* ¿Qué tarea de recuperación harían?

  * texto -> imagen
  * imagen -> texto
  * imagen -> imagen (similitud)

* ¿Qué ventaja práctica aporta CLIP en una primera versión?

* ¿Qué riesgo técnico ven? (sesgo, dominio distinto, ambigüedad semántica)

> Si su caso no requiere recuperación, indiquen cómo usarían embeddings conjuntos para clasificación guiada por texto o búsqueda de casos similares.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Ayúdanos a diseñar una versión con CLIP para nuestro caso [caso].
Necesitamos:
1) qué texto e imágenes tendríamos,
2) qué tarea de recuperación haríamos (texto->imagen, imagen->texto, imagen->imagen),
3) qué ventaja práctica aporta CLIP,
4) qué riesgo técnico debemos vigilar.
Responde en viñetas claras.
```

#### 6. Modelos visión-lenguaje y VQA (Visual Question Answering)

Definan una versión conceptual de **VLM/VQA** para su caso.

Incluyan:

* ¿Qué tipo de preguntas haría el usuario sobre una imagen o conjunto de imágenes?
* ¿Qué entrada recibe el modelo? (imagen(es) + pregunta)
* ¿Qué salida esperan? (respuesta corta, respuesta estructurada, respuesta + evidencia)
* ¿Cómo reducirían errores o respuestas inventadas?

  * permitir "no se observa"/"no es claro",
  * pedir evidencia,
  * restringir formato,
  * revisión humana en casos críticos.

> Si VQA no aplica directamente, propongan una variante VLM (captioning, clasificación guiada por texto, extracción visual con instrucción).

**Prompt sugerido (Copilot/ChatGPT):**

```text
Diseña una versión VLM/VQA para nuestro caso [caso].
Incluye:
1) ejemplos de preguntas que haría el usuario sobre imágenes,
2) formato de entrada (imagen + texto),
3) formato de salida recomendado,
4) cómo reducir respuestas inventadas o ambiguas.
No inventes datos; define el diseño.
```

#### 7. LLM multimodales (MLLM): texto, imagen, audio y video

Evolucionen su propuesta hacia un **MLLM** y definan qué modalidades usarían realmente en su caso.

Incluyan:

* ¿Qué modalidades entran? (texto, imagen, audio, video)

* ¿Cuál sería el flujo de entrada? (por ejemplo: video -> frames + audio -> transcripción + prompt)

* ¿Qué salida produce el MLLM? (resumen multimodal, respuesta, clasificación con justificación, reporte)

* ¿Qué problema práctico esperan?

  * costo/latencia,
  * contexto largo,
  * sincronización audio-video,
  * ruido visual/sonoro.

* ¿Qué simplificación harían en una primera versión?

  * solo texto + imagen,
  * muestreo de frames,
  * audio transcrito,
  * chunking temporal.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Convierte nuestra propuesta en una versión multimodal (MLLM) para [caso].
Define:
1) qué modalidades usaríamos realmente (texto/imagen/audio/video),
2) flujo de entrada,
3) salida esperada,
4) principal limitación práctica,
5) simplificación para una primera versión.
Usa viñetas técnicas y concretas.
```

#### 8. Puente con la Actividad 4: agente multimodal (herramientas, memoria y supervisión)

A partir de su propuesta multimodal, definan cómo se integraría con el enfoque de **LLM/agente** de la actividad anterior. (Mantengan el mismo lenguaje de herramientas, memoria, planificación y supervisión humana usado en la Actividad 4).  

Incluyan:

* ¿Qué herramientas externas usaría un agente multimodal?

  * extractor de frames,
  * OCR,
  * ASR,
  * buscador/vector DB,
  * base de datos/API,
  * motor de reglas.

* Para cada herramienta:

  * ¿qué consulta hace el agente?
  * ¿qué devuelve la herramienta?
  * ¿cómo usa eso el modelo para responder?

* ¿Dónde pondrían "human in the loop"?

* ¿Qué parte no debería automatizarse?

> No hace falta implementar APIs; se espera diseño operativo claro.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Convierte nuestra solución visual/multimodal para [caso] en un agente con herramientas.
Define 3-5 herramientas (OCR, ASR, frames, vector DB, API, etc.) y para cada una indica:
1) qué consulta haría el agente,
2) qué devuelve la herramienta,
3) cómo usaría el modelo ese resultado en la respuesta final.
Incluye dónde entra supervisión humana.
Usa viñetas concretas.
```

#### 9. Riesgos, sesgos y mini plan de evaluación (visión + multimodal)

Definan una validación mínima para su propuesta de visión/multimodal.

Incluyan:

* **1 riesgo de sesgo visual** (iluminación, calidad de cámara, cobertura de clases, dominio)
* **1 riesgo multimodal** (mala alineación texto-imagen, audio ruidoso, video incompleto)
* **1 riesgo de privacidad/uso indebido** (rostros, voz, documentos, datos sensibles)
* **1 riesgo operativo** (latencia, costo, almacenamiento, fallos de herramientas)

Para cada riesgo, definan un control mínimo:

* reglas/restricciones,
* validación automática,
* trazabilidad (fuente/evidencia),
* revisión humana,
* mensajes de incertidumbre,
* límites de uso.

Además, incluyan:

* **1 métrica técnica visual** (accuracy, F1, mAP, IoU, etc.)
* **1 métrica de recuperación** (Recall@K, Precision@K, top-k)
* **1 métrica de comportamiento** (cumplimiento de formato, utilidad, tasa de "no sé" correcto)
* **1 métrica operativa** (latencia, costo, llamadas a herramientas)
* **1 criterio mínimo de versión aceptable**

> No inventen resultados; solo diseñen cómo evaluarían la versión inicial.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Ayúdanos a definir riesgos y evaluación para una solución de visión/multimodal en [caso].
Incluye:
1) un riesgo de sesgo visual,
2) un riesgo multimodal,
3) un riesgo de privacidad/uso indebido,
4) un riesgo operativo,
5) controles mínimos,
6) métricas (visual, recuperación, comportamiento y operativa),
7) un criterio mínimo de éxito.
No inventes resultados; solo propone validación razonable.
```

#### 10. Entregable

Cada grupo entrega **3 o 4 diapositivas o 1 hoja** con este formato:

**Plantilla rápida**

1. **Caso de uso y problema (mismo de Actividad 1).**
2. **¿Qué parte del caso requiere visión/multimodalidad?**
3. **Baseline visual con CNN (entrada/salida + limitación).**
4. **ViT: motivación + flujo general (patches/tokens/encoder).**
5. **Comparación CNN vs. ViT + decisión práctica.**
6. **CLIP: representaciones conjuntas + recuperación.**
7. **VLM/VQA: preguntas, entradas, salidas y control de errores.**
8. **MLLM: modalidades (texto/imagen/audio/video) + simplificación inicial.**
9. **Agente multimodal: herramientas + supervisión humana.**
10. **Riesgos + métricas + criterio mínimo.**
