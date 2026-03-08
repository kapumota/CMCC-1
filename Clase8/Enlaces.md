### Enlaces para la clase 8

#### 1. MLOps: fundamentos y operación de modelos

* **Rules of Machine Learning (Google)**: lectura clave para entender cómo pensar proyectos de ML como sistemas reales y no solo como notebooks. ([Google for Developers][1])
* **Hidden Technical Debt in Machine Learning Systems (Google Research)**: fundamental para entender por qué los sistemas de ML acumulan deuda técnica en datos, features, validación y serving. ([Google Research][2])
* **Full Stack Deep Learning-ML Projects**: muy útil para enseñar el paso de experimento a producción y la lógica de proyecto de ML completo. ([FSDL][3])
* **MLflow Documentation**: cubre tracking, registry y serving. Excelente para mostrar el ciclo entrenamiento -> registro -> despliegue. ([MLflow][4])
* **Kubeflow Pipelines**: muy bueno para enseñar pipelines reproducibles y orquestación en Kubernetes. ([Kubeflow][5])

#### 2. LLMOps: operación de aplicaciones con modelos fundacionales

* **A Developer's Guide to LLMOps (Arize)**: introduce bien los tres ejes más operativos: gestión de prompts, agentes y observabilidad. ([Arize][6])
* **Introduction: Fundamentals of LLMOps (Arize University)**: lectura de entrada para estudiantes antes de pasar a herramientas más específicas. ([Arize][7])
* **DeepLearning.AI-LLMOps course**: recorre pipeline de datos, ajuste, despliegue y operación de LLMs. ([DeepLearning.AI][8])
* **Full Stack Deep Learning-LLMOps**: muy útil para evaluación, despliegue y monitoreo de aplicaciones basadas en LLM. ([FSDL][9])
* **LLM Observability for AI Agents and Applications (Arize)**: excelente para enseñar trazas, costos, latencia, tool calls y evaluación de workflows. ([Arize][10])
* **LLM Tracing and Observability with Phoenix (Arize)**: más práctico si se quiere observar un sistema por spans y trazas. ([Arize][11])
* **LangSmith evaluation docs**: útil para enseñar evaluadores deterministas y evaluación continua de aplicaciones LLM. ([LangSmith Docs][12])

#### 3. PromptOps y prompts

* **OpenAI Prompting guide**: buena base para estructuración de instrucciones, contexto y prompting productivo. ([OpenAI Developers][13])
* **Anthropic-Prompt engineering overview**: conecta prompting con evaluación, guardrails, latencia y consistencia. ([Anthropic Docs][14])
* **Anthropic-Console prompting tools**: ayuda a mostrar flujo práctico de iteración y refinamiento de prompts. ([Anthropic Docs][15])
* **Prompt Engineering Guide**: mezcla teoría, técnicas y ejemplos; muy cómoda para estudiantes. ([Prompt Engineering Guide][16])
* **DeepLearning.AI - Prompt Compression and Query Optimization**: útil para conectar prompts con costo y latencia. ([DeepLearning.AI][17])

#### 4. Del modelo al sistema: entrenamiento, despliegue, monitorización y reentrenamiento

* **Full Stack Deep Learning-Lecture 5: ML Projects**: muy buena para framing, métricas, baselines y factibilidad. ([FSDL][3])
* **Lecture 6: MLOps Infrastructure & Tooling**: introduce el paisaje de tooling en datos, entrenamiento, evaluación y despliegue. ([FSDL][18])
* **Lecture 10: Testing & Explainability**: especialmente buena para enseñar evaluación antes de promover un modelo nuevo. ([FSDL][19])
* **Lecture 11: Deployment & Monitoring**: excelente para explicar tipos de despliegue y observabilidad en producción. ([FSDL][20])
* **Lecture 6: Continual Learning**: útil para conectar monitoreo con actualización y reentrenamiento continuo. ([FSDL][21])
* **MLflow Tracking Quickstart**: recurso práctico para registrar experimentos desde el inicio. ([MLflow][22])
* **MLflow Model Registry tutorial**: útil para versionar, promover y auditar modelos. ([MLflow][23])
* **MLflow deployment guides**: guía para servir modelos localmente o en infraestructura más grande. ([MLflow][24])

#### 5. Costos, latencia, privacidad y seguridad en sistemas basados en IA

##### 5.1 Costos y latencia

* **OpenAI-Cost optimization**: explica estrategias concretas para bajar costo, incluida reducción de tokens y uso de procesamiento batch. ([OpenAI Developers][25])
* **OpenAI-Latency optimization**: muy útil para disminuir tiempo de respuesta en aplicaciones LLM reales. ([OpenAI Developers][26])
* **OpenAI-Prompt caching**: muestra cómo reutilizar prefijos para reducir latencia y costo. ([OpenAI Developers][27])
* **OpenAI-Batch API**: útil para cargas asincrónicas con menor costo. ([OpenAI Developers][28])
* **Anthropic-Reducing latency**: guía práctica sobre selección de modelo, longitud de prompt, streaming y medición. ([Anthropic Docs][29])
* **Anthropic-Prompt caching/batch processing/usage & cost API**: útiles para enseñar optimización operativa y control de gasto. ([Anthropic Docs][30])

##### 5.2 Privacidad y residencia de datos

* **OpenAI-Data controls in the platform**: explica tipos de datos almacenados, retención y controles de residencia. ([OpenAI Developers][31])
* **OpenAI-Prompt caching and Zero Data Retention note**: importante para discutir trade-offs entre caching y privacidad. ([OpenAI Developers][27])
* **Anthropic API overview**: incluye información útil sobre operación general y residencia de inferencia. ([Anthropic Docs][32])
* **Azure Confidential AI**: muy útil para hablar de protección de datos y modelos "in use" mediante confidential computing. ([Microsoft Learn][33])

##### 5.3 Seguridad y riesgo

* **OWASP Top 10 for LLM Applications 2025**: bibliografía obligatoria para seguridad aplicada a LLMs. ([OWASP][34])
* **NIST AI RMF-Generative AI Profile**: excelente marco para gobernanza, riesgo y controles organizacionales. ([NIST][35])
* **NIST adversarial ML taxonomy**: muy bueno para vincular seguridad con ataques al ciclo de vida del ML. ([NIST][36])
* **Microsoft-Build a strong security posture for AI**: lectura aplicada de postura de seguridad empresarial. ([Microsoft Learn][37])

#### 6. Modelos grandes en la nube vs modelos pequeños en el borde (edge)

##### 6.1 Edge/Inferencia local

* **Google AI Edge**: punto de entrada oficial para on-device AI en móvil y web. ([Google AI for Developers][38])
* **Gemma on mobile devices**: muestra despliegue real de modelos en edge. ([Google AI for Developers][39])
* **Gemma get started**: útil para iniciar con modelos pequeños y despliegue ligero. ([Google AI for Developers][40])
* **llama.cpp README**: recurso práctico de primer nivel para enseñar inferencia local, cuantización y serving liviano. ([GitHub][41])
* **GBNF grammar guide en llama.cpp**: interesante para conectar edge con salidas estructuradas y guardrails locales. ([GitHub][42])

##### 6.2 Trade-off nube vs edge

* **Azure-Choose the Right AI Model for Your Workload**: sirve para explicar el compromiso entre capacidad, costo, rendimiento y despliegue. ([Microsoft Learn][43])
* **Azure model catalog featured models**: menciona explícitamente modelos pequeños para inferencia on-device y edge. ([Microsoft Learn][44])
* **Windows AI samples**: muestra ejemplos concretos de uso de modelos locales con aceleración. ([Microsoft Learn][45])

#### 7. Agentes autónomos

##### 7.1 Guías oficiales

* **OpenAI-Building agents**: buena introducción a modelos, herramientas, memoria y orquestación. ([OpenAI Developers][46])
* **OpenAI-Agents SDK**: sirve para mostrar el stack de construcción y optimización de agentes. ([OpenAI Developers][47])
* **OpenAI Cookbook - Agents**: recurso práctico para ejemplos. ([OpenAI Developers][48])
* **Anthropic-Tool use**: muy buena para explicar el patrón base de agente con herramientas. ([Anthropic Docs][49])

##### 7.2 Cursos y patrones de orquestación

* **Full Stack Deep Learning - Harrison Chase: Agents**: muy útil para evaluación de trayectorias y no solo del output final. ([FSDL][50])
* **Azure AI Agent orchestration patterns**: explica patrones como sequential, concurrent, handoff y group chat. ([Microsoft Learn][51])
* **Azure autonomous agent workflows**: buen ejemplo moderno de workflows autónomos con governance y rollback. ([Microsoft Learn][52])
* **Microsoft Agent Framework overview**: recurso reciente para multi-agent workflows en .NET y Python. ([Microsoft Learn][53])

#### 8. DevSecOps y seguridad en IA basada en agentes

* **OpenAI-Safety in building agents**: muy importante para prompt injection, tool misuse y riesgos en multi-agent workflows. ([OpenAI Developers][54])
* **OpenAI Cookbook - Building Governed AI Agents**: excelente material para gobernanza, trazabilidad y despliegue seguro de agentes en organizaciones. ([OpenAI Developers][55])
* **OpenAI - Skills guide**: importante para aprobaciones de acciones sensibles y requisitos de retención/residencia. ([OpenAI Developers][56])
* **Anthropic - Mitigate jailbreaks and prompt injections**: buena lectura para guardrails en sistemas agentic. ([Anthropic Docs][57])
* **Microsoft - DevSecOps on AKS**: útil para conectar seguridad de software con despliegue de plataformas IA. ([Microsoft Learn][58])
* **Microsoft Defender for Cloud - Overview**: bueno para una mirada operativa de seguridad continua. ([Microsoft Learn][59])
* **Microsoft - Governance and security for AI agents across the organization**: muy útil para hablar de gobierno institucional y adopción controlada de agentes. ([Microsoft Learn][60])

[1]: https://developers.google.com/machine-learning/guides/rules-of-ml "Rules of Machine Learning | Google for Developers"
[2]: https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/ "Hidden Technical Debt in Machine Learning Systems"
[3]: https://fullstackdeeplearning.com/spring2021/lecture-5/ "Lecture 5: ML Projects"
[4]: https://mlflow.org/docs/latest/ "MLflow Documentation"
[5]: https://www.kubeflow.org/docs/components/pipelines/ "Kubeflow Pipelines"

[6]: https://arize.com/blog-course/llmops-operationalizing-llms-at-scale/ "A Developer's Guide To LLMOps"
[7]: https://arize.com/blog-course/introduction-fundamentals/ "Introduction: Fundamentals of LLMOps"
[8]: https://learn.deeplearning.ai/courses/llmops/information "LLMOps"
[9]: https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/llmops/ "The Full Stack - LLMOps"
[10]: https://arize.com/blog/llm-observability-for-ai-agents-and-applications/ "LLM Observability for AI Agents and Applications"
[11]: https://arize.com/blog/llm-tracing-and-observability-with-arize-phoenix/ "LLM Tracing and Observability"
[12]: https://docs.smith.langchain.com/evaluation/evaluator-implementations "LangSmith evaluation docs"

[13]: https://developers.openai.com/api/docs/guides/prompting/ "Prompting | OpenAI API"
[14]: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview "Prompt engineering overview - Claude API Docs"
[15]: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator "Console prompting tools - Claude API Docs"
[16]: https://www.promptingguide.ai/ "Prompt Engineering Guide"
[17]: https://learn.deeplearning.ai/courses/prompt-compression-and-query-optimization/lesson/bgsip/conclusion "Prompt Compression and Query Optimization"

[18]: https://fullstackdeeplearning.com/spring2021/lecture-6/ "Lecture 6: MLOps Infrastructure & Tooling"
[19]: https://fullstackdeeplearning.com/spring2021/lecture-10/ "Lecture 10: Testing & Explainability"
[20]: https://fullstackdeeplearning.com/spring2021/lecture-11/ "Lecture 11: Deployment & Monitoring"
[21]: https://fullstackdeeplearning.com/course/2022/lecture-6-continual-learning/ "The Full Stack - Lecture 6: Continual Learning"
[22]: https://mlflow.org/docs/latest/ml/tracking/quickstart/ "MLflow Tracking Quickstart"
[23]: https://mlflow.org/docs/latest/ml/model-registry/tutorial/ "MLflow Model Registry tutorial"
[24]: https://mlflow.org/docs/latest/ml/deployment/ "MLflow Serving"

[25]: https://developers.openai.com/api/docs/guides/cost-optimization/ "Cost optimization | OpenAI API"
[26]: https://developers.openai.com/api/docs/guides/latency-optimization/ "Latency optimization | OpenAI API"
[27]: https://developers.openai.com/api/docs/guides/prompt-caching/ "Prompt caching | OpenAI API"
[28]: https://developers.openai.com/api/docs/guides/batch/ "Batch API"
[29]: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency "Reducing latency - Claude API Docs"
[30]: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching "Prompt caching - Claude API Docs"
[31]: https://developers.openai.com/api/docs/guides/your-data/ "Data controls in the OpenAI platform"
[32]: https://docs.anthropic.com/claude/reference/getting-started-with-the-api "API Overview - Claude API Docs"
[33]: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-ai "Confidential AI - Azure Confidential Computing"
[34]: https://owasp.org/www-project-top-10-for-large-language-model-applications/ "OWASP Top 10 for Large Language Model Applications"
[35]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf "Artificial Intelligence Risk Management Framework: Generative AI Profile"
[36]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations"
[37]: https://learn.microsoft.com/en-us/security/security-for-ai/posture "Build a strong security posture for AI"

[38]: https://ai.google.dev/edge "Google AI Edge"
[39]: https://ai.google.dev/gemma/docs/integrations/mobile "Deploy Gemma on mobile devices"
[40]: https://ai.google.dev/gemma/docs/get_started "Get started with Gemma models"
[41]: https://github.com/ggml-org/llama.cpp/blob/master/README.md "llama.cpp README"
[42]: https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md "llama.cpp grammars README"
[43]: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/choose-ai-model "Choose the Right AI Model for Your Workload"
[44]: https://learn.microsoft.com/en-us/azure/machine-learning/concept-models-featured?view=azureml-api-2 "Featured models of Foundry model catalog"
[45]: https://learn.microsoft.com/en-us/windows/ai/samples/ "AI on Windows code samples and tutorials"

[46]: https://developers.openai.com/tracks/building-agents/ "Building agents"
[47]: https://developers.openai.com/api/docs/guides/agents-sdk/ "Agents SDK | OpenAI API"
[48]: https://developers.openai.com/cookbook/topic/agents/ "Agents | OpenAI Cookbook"
[49]: https://docs.anthropic.com/en/docs/build-with-claude/tool-use "Tool use with Claude"
[50]: https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/chase-agents/ "Harrison Chase: Agents"
[51]: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns "AI Agent Orchestration Patterns"
[52]: https://learn.microsoft.com/en-us/azure/logic-apps/create-autonomous-agent-workflows "Create Autonomous AI Agentic Workflows"
[53]: https://learn.microsoft.com/en-us/agent-framework/overview/ "Microsoft Agent Framework Overview"

[54]: https://developers.openai.com/api/docs/guides/agent-builder-safety/ "Safety in building agents | OpenAI API"
[55]: https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook/ "Building Governed AI Agents"
[56]: https://developers.openai.com/api/docs/guides/tools-skills/ "Skills | OpenAI API"
[57]: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks "Mitigate jailbreaks and prompt injections"
[58]: https://learn.microsoft.com/en-us/azure/architecture/guide/devsecops/devsecops-on-aks "DevSecOps on Azure Kubernetes Service (AKS)"
[59]: https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction "Microsoft Defender for Cloud Overview"
[60]: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization "Governance and security for AI agents across the organization"
