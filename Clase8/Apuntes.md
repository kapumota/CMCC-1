### Apuntes sobre el proyecto

#### 1. API de inferencia (FastAPI)

El proyecto expone el pipeline como un **servicio HTTP** usando FastAPI. Esto convierte el workflow en un "producto" consumible por cualquier cliente (curl, navegador, otra app, un frontend, etc.). La API ofrece endpoints de verificación (`/health`), observabilidad (`/metrics`) y el endpoint principal (`/workflow`) que recibe una solicitud en JSON y responde con un JSON estructurado con el resultado del pipeline. Además, incluye un endpoint administrativo (`/admin/reindex`) para disparar una actualización controlada del conocimiento RAG. En términos de MLOps/LLMOps, este componente representa el "serving layer": dónde se integra el modelo o el pipeline con el resto del sistema.

#### 2. Workflow/pipeline (secuencial: parseo -> RAG -> tool-calling -> respuesta)

El corazón del sistema es un **pipeline secuencial** que transforma una petición en una respuesta útil. Primero ocurre el **parseo**, donde se extraen señales mínimas de la intención del usuario (por ejemplo, códigos de aeropuerto como LAX/JFK y una ciudad de hotel). Luego entra el bloque de **RAG**, que recupera fragmentos relevantes desde un conjunto de documentos locales para aportar contexto. Con esa intención + contexto, el workflow decide si necesita ejecutar acciones externas mediante **tool-calling**, por ejemplo una herramienta de "flight_lookup" y otra de "hotel_lookup". Finalmente, el sistema **sintetiza** la salida: puede hacerlo con un LLM real (si está configurado) o con un fallback local. Este diseño es ideal porque muestra que una app LLM es, en la práctica, una cadena de decisiones y componentes operacionales, no un "modelo suelto".

#### 3. RAG local (TF-IDF) con reindex como "reentrenamiento" práctico

El RAG se implementa localmente con **TF-IDF** (recuperación por similitud textual) sobre documentos en `data/docs/`. El flujo típico es: documentos -> división en "chunks" -> vectorización TF-IDF -> índice persistido en `data/indexes/`. Cuando el sistema responde a una consulta, calcula similitud y devuelve los **top-k fragmentos** más relevantes. Lo interesante es el mecanismo de **reindex**: actualizar documentos y regenerar el índice equivale, en la práctica, a un "ciclo de actualización" comparable al reentrenamiento, pero más accesible en una clase. Con reindex, el sistema puede incorporar conocimiento nuevo o corregido sin tocar el código del pipeline ni "reentrenar" un modelo grande.

#### 4. Observabilidad: logs JSON y métricas Prometheus (`/metrics`)

En un sistema operable, no basta con que funcione: hay que **verlo funcionar**. Por eso el proyecto incluye dos pilares de observabilidad. Primero, **logs en JSON**, útiles para depurar y auditar: por ejemplo, registrar latencia del workflow, rutas llamadas, errores o identificadores de request. Segundo, **métricas Prometheus** expuestas en `/metrics`, que convierten el comportamiento del sistema en números: contadores de requests, latencias (histogramas), cantidad de tool calls y estado de consultas RAG. Esto permite discutir temas clave: qué medir, cómo detectar degradación, cómo comparar rendimiento antes/después de cambios, y cómo conectar estas señales con decisiones de operación (alertas, rollback, reindex, etc.).

#### 5. Docker y Docker Compose: empaquetado reproducible + Prometheus opcional

Docker encapsula el proyecto (código + dependencias + runtime) en una **imagen reproducible**, evitando problemas de "en mi máquina funciona". Con `docker build` se genera una imagen y con `docker run` se expone el servicio en el puerto 8000. Para ir un paso más allá, Docker Compose levanta un mini-stack: **API + Prometheus**, conectados en la misma red. Esto permite demostrar el circuito completo de observabilidad: la API expone métricas, Prometheus las recolecta, y el equipo puede inspeccionarlas en su UI. Para la sesión, esto marca la transición clara de "demo local" a "despliegue operable", aunque sea en entorno de laboratorio.

#### 6. Tests (pytest) y CI (GitHub Actions): calidad mínima y regresión

El proyecto incorpora tests con pytest para verificar que la API está viva y que el endpoint principal devuelve una estructura de respuesta coherente. Aunque sean tests simples, cumplen un rol didáctico fundamental: construir el hábito de **no romper el sistema** al modificar el pipeline. A nivel de ingeniería, se conectan con la idea de "regression set" en LLM apps: no basta con que el sistema responda; debe mantener comportamientos mínimos esperados. Con GitHub Actions, ese control se automatiza: cada push o pull request corre lint y tests. Este componente es el puente directo hacia prácticas reales de MLOps/LLMOps: cambios pequeños, validación automática, y reducción de errores antes de desplegar.


#### 7. LLM opcional y fallback local: funcionamiento offline y separación de preocupaciones

El sistema puede operar de dos maneras. Si se configura un endpoint **OpenAI-compatible** (por ejemplo vLLM o LM Studio), el pipeline llama a ese LLM para sintetizar una respuesta más natural y robusta. Si no hay LLM disponible, el proyecto usa un **fallback local** que produce un resumen determinístico/plantilla. Esto es excelente para clase porque separa lo esencial: el objetivo es entender el pipeline, la operación, las métricas y el ciclo de actualización; el LLM se enchufa como un componente intercambiable. Además, permite que todo funcione offline en laboratorio, evitando bloqueos por credenciales, cuotas o conectividad.

#### 8. Notebook y agentes: laboratorio para entender "pensamiento->acción->observación"

El notebook `notebooks/Workflows_Pipelines_Agentes_Local.ipynb` se usa como entorno de **exploración y explicación**. Ahí el pipeline puede verse paso a paso: cómo se interpreta la solicitud, qué contexto recupera RAG, por qué se elige una herramienta, qué devuelve la herramienta y cómo se integra en la respuesta final. En términos de agentes, el notebook ayuda a enseñar el ciclo típico **pensamiento (decisión) -> acción (tool-call) -> observación (resultado) -> nueva decisión**, aunque en esta versión sea una aproximación "ligera" (heurísticas + herramientas + síntesis). En clase, el notebook sirve para depurar y hacer demostraciones controladas; la API sirve para mostrar la versión "productizada" del mismo flujo con observabilidad y operación.

