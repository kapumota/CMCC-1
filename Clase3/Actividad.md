### Actividad de discusión guiada 3 (por grupos)

Tomar el **mismo caso de uso** elegido en la Actividad de la clase 1 (y refinado en la Actividad de la clase 2) y proponer una **versión conceptual basada en Transformer/LLM** para ese problema, identificando qué parte del caso realmente requiere atención, qué arquitectura conviene y qué decisiones dejarían preparadas para la siguiente clase (**LLM, alineamiento y agentes**).

#### Uso de Copilot/ChatGPT (apoyo permitido)

Se permite usar Copilot o ChatGPT para:

* organizar ideas,
* aclarar conceptos,
* revisar coherencia técnica,
* resumir para diapositivas.

**No se permite** copiar texto sin entenderlo. El grupo debe poder explicar cada decisión.

#### Referencia sugerida para esta actividad

Usen como apoyo:

* **[The Annotated Transformer (Harvard)](https://nlp.seas.harvard.edu/annotated-transformer/)** 
* y la lectura breve del artículo [**"Attention Is All You Need"**](https://github.com/kapumota/CMCC-1/blob/main/Clase3/Resumen_Attention_Is_All_You_Need.pdf), resumen trabajado en clase.

> En el material de apoyo ya se usa explícitamente The Annotated Transformer como referencia de implementación y explicación del flujo del modelo.  

#### Instrucciones para cada grupo

Usando su caso de uso de las actividades previas, respondan de forma breve:

#### 1. ¿Dónde entra el Transformer en su caso?

Definan **qué parte** de su problema se beneficia de atención/Transformer (no todo el pipeline tiene que ser Transformer).

* ¿La entrada es secuencial? (texto, audio, series, logs, historial, eventos)
* ¿Necesitan contexto lejano entre elementos?
* ¿La salida sería clasificación, extracción, generación o recomendación?

> Si su caso no es naturalmente secuencial, indiquen si el Transformer **no** es la primera opción y en qué etapa futura podría aparecer.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Nuestro caso de uso es [caso] y el problema es [problema].
En la Actividad 2 propusimos [solución base].
Ayúdanos a identificar si un Transformer tiene sentido aquí:
1) qué parte del pipeline lo usaría,
2) qué tipo de entrada manejaría,
3) qué salida produciría,
4) si realmente aporta valor frente a un MLP/CNN/RNN.
Responde en viñetas, breve y técnico.
```

#### 2. Self-attention en su problema (consultas, claves y valores)

Expliquen **conceptualmente** cómo mapearían **consultas (Q), claves (K) y valores (V)** a su caso.

* ¿Qué sería un "token" o unidad de análisis? (palabra, evento, sensor, registro, frame, etc.)
* ¿Qué información usaría el modelo para "preguntar" (Q)?
* ¿Qué información permitiría comparar contexto (K)?
* ¿Qué información se combinaría para producir la salida contextual (V)?

> No se espera fórmula completa; sí una interpretación clara del mecanismo en su dominio.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Explica self-attention para nuestro caso [caso] con lenguaje técnico claro.
Mapea:
- token
- consulta (Q)
- clave (K)
- valor (V)
y describe qué significa "atender" en este problema.
No uses fórmulas largas. Usa 1 ejemplo concreto.
```

> En la lectura base se explica que Q, K y V se obtienen con proyecciones lineales distintas sobre la misma representación, y que los puntajes se escalan por sqrt(d_k) antes del softmax. Úsenlo como guía conceptual. 

#### 3. Complejidad cuadrática y decisión práctica

Analicen la implicancia de la **complejidad cuadrática** de self-attention respecto a la longitud de la secuencia.

* ¿Qué tan largas serían sus secuencias?
* ¿Qué problema práctico podría aparecer? (memoria, costo, latencia)
* ¿Qué estrategia inicial usarían para una primera versión?

  * truncar ventana,
  * resumir por bloques,
  * usar chunks,
  * atención local (si aplica),
  * o mantener un contexto corto.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Para nuestro caso [caso], analiza el impacto de la complejidad de self-attention cuando crece la longitud de secuencia.
Indica:
1) qué tan largas serían las secuencias,
2) qué limitación práctica aparecería,
3) una estrategia simple para una primera versión.
No inventes números; razona por órdenes de magnitud.
```

> En el material revisado, la atención produce matrices de puntajes/pesos por cabecera con forma `[L, L]` (por lote y cabecera), lo que hace visible el crecimiento con la longitud de secuencia. 

#### 4. Multi-head attention, normalización y conexiones residuales

Expliquen por qué **múltiples cabeceras**, **conexiones residuales** y **LayerNorm** ayudan en su caso.

* ¿Qué "subperspectivas" o patrones distintos podrían capturar distintas cabeceras?
* ¿Por qué conviene sumar la entrada original (residual)?
* ¿Qué aporta LayerNorm a la estabilidad del entrenamiento?

**Prompt sugerido (Copilot/ChatGPT):**

```text
Para nuestro caso [caso], explica por qué multi-head attention podría capturar patrones distintos.
Además, explica brevemente:
- conexión residual,
- LayerNorm,
y cómo ayudan a estabilidad y aprendizaje.
Usa lenguaje conceptual y 1 ejemplo del dominio.
```

> El documento de apoyo describe la atención multi-cabecera (8 cabeceras en el modelo base) y cómo se concatena la salida, además de la idea de "Add & Norm" (residual + LayerNorm) alrededor de cada subcapa.   


#### 5. Arquitectura: encoder/decoder o solo decoder (puente a LLM)

Elijan la variante de arquitectura más adecuada para su caso:

* **Encoder-only** (representación/clasificación/etiquetado, etc.)
* **Encoder-decoder** (traducción, transformación de secuencia a secuencia)
* **Decoder-only** (generación/autocompletado/chat), que conecta mejor con LLM modernos

Expliquen:

* cuál elegirían para su caso,
* qué entrada y salida tendría,
* y por qué.

**Prompt sugerido (Copilot/ChatGPT):**

```text
Ayúdanos a elegir arquitectura Transformer para nuestro caso [caso]:
- encoder-only
- encoder-decoder
- decoder-only
Compara brevemente las tres y recomienda una.
Conecta la respuesta con el tipo de tarea (clasificación, extracción, generación, etc.).
```

> El material muestra la estructura del codificador (capas apiladas con autoatención + feed-forward) y también las diferencias del decodificador, incluyendo atención enmascarada y capa final para probabilidades de salida.  


#### 6. Positional encodings y variantes (RoPE, ALiBi, aprendidos)

Definan cómo incorporarían información de posición/orden.

* ¿Por qué no basta con embeddings "sin posición"?
* ¿Qué opción usarían en una primera versión?

  * **posicional aprendida**
  * **sinusoidal** (clásica)
  * **RoPE** (moderna, útil en muchos LLM)
  * **ALiBi** (moderna, sesgo posicional lineal)
* ¿Qué ventaja esperada tendría esa elección en su caso?

**Prompt sugerido (Copilot/ChatGPT):**

```text
Explica por qué nuestro caso [caso] necesita información de orden/posición en un Transformer.
Compara estas opciones para una primera versión:
- posicional aprendida
- sinusoidal
- RoPE
- ALiBi
Recomienda una y justifica la elección según el tipo de secuencia.
```

> En la lectura base se explica que el Transformer procesa tokens en paralelo y por eso necesita codificación posicional; también se menciona la opción aprendida vs calculada (sinusoidal). 

#### 7. Mini revisión de "Attention Is All You Need" (para discusión en clase)

Hagan una mini revisión guiada (breve, 5-7 viñetas) del artículo y de la idea central que se llevarían a su proyecto. Utiliza el resumen entregado.

Incluyan:

* 1 idea central del artículo
* 1 componente que les pareció clave (self-attention, multi-head, máscara, residual+norm, etc.)
* 1 cosa que cambiaría hoy al pensar en LLM modernos (por ejemplo, usar decoder-only, RoPE, contexto largo, etc.)
* 1 pregunta para discutir en clase

**Prompt sugerido (Copilot/ChatGPT):**

```text
Haz una mini revisión de "Attention Is All You Need" orientada a nuestro caso [caso].
Necesitamos:
1) idea central del artículo,
2) componente clave para entenderlo,
3) cómo se conecta con LLM modernos,
4) una pregunta para discusión en clase.
Máximo 7 viñetas, claro y sin relleno.
```

> En el resumen del documento se remarca que el Transformer mostró que la atención (sin recurrencia) podía lograr resultados de vanguardia y que de ahí derivaron modelos posteriores como BERT. 


#### 8. Puente directo a la clase 4 (LLM, alineamiento y agentes)

A partir de su propuesta Transformer, definan **insumos concretos** para la siguiente clase.

##### 8.1. Si su solución fuera un LLM (o usara uno)

Definan:

* **Rol del modelo:** ¿qué hace exactamente?
* **Instrucción principal (prompt base):** ¿qué tarea le pedirían?
* **Restricciones de comportamiento (alineamiento inicial):**

  * qué sí debe hacer,
  * qué no debe hacer,
  * cuándo debe pedir aclaración,
  * cuándo debe escalar a humano.

##### 8.2. Si su solución fuera un agente (o asistente con herramientas)

Definan:

* ¿Qué herramientas externas usaría? (buscador, base de datos, hoja de cálculo, API, etc.)
* ¿Qué entradas recibe el agente?
* ¿Qué salidas produce?
* ¿Dónde pondrían "human in the loop"?

**Prompt sugerido (Copilot/ChatGPT):**

```text
Convierte nuestra propuesta Transformer/LLM para [caso] en un borrador para la siguiente clase sobre LLM, alineamiento y agentes.
Necesitamos:
1) rol del modelo,
2) prompt base,
3) reglas de comportamiento (qué sí/no),
4) herramientas externas (si fuera agente),
5) puntos de supervisión humana.
Responde en viñetas claras y operativas.
```

#### 9. Mini plan de evaluación (para la siguiente clase)

Definan una validación mínima que sirva tanto para su versión Transformer como para la discusión de LLM/agentes en la siguiente sesión.

Incluyan:

* **1 métrica técnica principal** (por ejemplo, accuracy/F1/MAE/ROUGE según tarea)
* **1 métrica de comportamiento** (por ejemplo, tasa de respuestas útiles, tasa de alucinación, cumplimiento de formato)
* **1 riesgo técnico**
* **1 riesgo de alineamiento/uso**
* **1 criterio mínimo de versión aceptable**

**Prompt sugerido (Copilot/ChatGPT):**

```text
Ayúdanos a definir una mini-validación para nuestro caso [caso] en una versión con Transformer/LLM.
Incluye:
1) una métrica técnica,
2) una métrica de comportamiento,
3) un riesgo técnico,
4) un riesgo de alineamiento/uso,
5) un criterio mínimo de éxito.
No inventes resultados; solo propone validación razonable.
```

#### 10. Entregable

Cada grupo entrega **3 diapositivas o 1 hoja** con este formato:

**Plantilla rápida**

1. **Caso de uso y problema (mismo de Actividad 1)**,
2. **¿Dónde entra Transformer en el pipeline?**,
3. **Q/K/V en su dominio (interpretación)**,
4. **Complejidad cuadrática y decisión práctica**,
5. **Multi-head + residual + LayerNorm (por qué)**,
6. **Arquitectura elegida (encoder/encoder-decoder/decoder-only)**,
7. **Positional encoding elegido (incluyendo variante moderna si aplica: RoPE/ALiBi)**,
8. **Mini revisión del resumen "Attention Is All You Need" + pregunta de discusión**,
9. **Puente a clase 4: rol LLM/agente + alineamiento básico + herramientas**,
10. **Métrica + riesgo + criterio mínimo**.
