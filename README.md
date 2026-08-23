### Introducción a la Inteligencia Artificial

Este es el repositorio de un curso corto de nivel introductorio para estudiantes que inician una maestría en Ciencia de la Computación, con una visión integrada de la IA moderna: aprendizaje automático, aprendizaje profundo, transformers, LLM, modelos generativos, visión computacional, aprendizaje por refuerzo y MLOps. 

El curso tiene una orientación conceptual con ejemplos y minidemostraciones en Python. 

#### Propósito del curso

El curso busca que el estudiante construya un **mapa mental claro del ecosistema actual de IA (2025)** y comprenda tendencias hacia 2030, como base para cursos avanzados de maestría. Se cubren desde paradigmas clásicos de aprendizaje hasta modelos fundacionales, LLM, multimodalidad, difusión, RL y despliegue en sistemas reales. 

### Temario del curso (por sesiones)

#### Sesión 1: Panorama 2025-2030 y fundamentos de aprendizaje automático

**Temas:**

* Tipos de aprendizaje: supervisado, no supervisado, autosupervisado y refuerzo.
* Pipeline típico de ML: datos -> modelo -> evaluación -> despliegue.
* Modelos fundacionales y reutilización en múltiples tareas.
* Tendencias 2025-2030: escalamiento de modelos y cómputo, IA como infraestructura.
* Discusión guiada de casos de uso (ciencia, industria y sociedad).

#### Sesión 2: Aprendizaje profundo, redes neuronales y optimización

**Temas:**

* Perceptrón y MLP.
* Funciones de activación y función de pérdida.
* Entrenamiento y retropropagación (gradientes).
* Regularización y generalización: L2, dropout, batch normalization, early stopping.
* Optimizadores modernos: SGD con momentum, Adam/AdamW, programación de tasa de aprendizaje.
* Limitaciones de RNN/LSTM y motivación para atención.

#### Sesión 3: Transformers y atención como bloque universal

**Temas:**

* Self-attention: queries, keys, values.
* Complejidad cuadrática.
* Multi-head attention.
* Normalización y conexiones residuales.
* Arquitecturas encoder/decoder y variantes (decoder-only para LLM).
* Positional encodings (incluyendo RoPE).
* Revisión del paper:  [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

#### Sesión 4: LLM, alineamiento y agentes

**Temas:**

* Modelos de lenguaje causales.
* Tokenización y ventana de contexto.
* Instruct tuning / ajuste fino.
* Alineamiento: RLHF, DPO/ORPO, modelos de preferencia.
* LLM como agentes: herramientas, memoria y planificación.
* Riesgos, sesgos y ética básica.

#### Sesión 5: Visión computacional moderna y modelos multimodales

**Temas:**

* De CNN a Vision Transformers (ViT).
* Representaciones conjuntas texto-imagen (CLIP).
* Modelos visión-lenguaje y VQA.
* LLM multimodales (texto, imagen, audio, video).
* Aplicaciones en salud, industria, educación y sistemas interactivos.

#### Sesión 6:Modelos generativos y difusión

**Temas:**

* Repaso de autoencoders, VAE y GAN.
* Idea central de la difusión: ruido + denoising.
* Entrenamiento y muestreo (DDPM/DDIM, noción general).
* Difusión para imágenes, texto, audio y datos científicos.
* Difusión + Transformers (DiT).
* Generación condicionada por texto.

#### Sesión 7: Aprendizaje por refuerzo y toma de decisiones

**Temas:**

* Marco MDP: estados, acciones, recompensas, políticas y valores.
* Métodos base: Q-learning y policy gradient (visión general).
* RL en juegos, robótica y recomendación.
* Conexión RL-LLM (RLHF como RL con recompensas humanas).
* Diseño de recompensas y desafíos de estabilidad/seguridad.

#### Sesión 8: MLOps, sistemas de IA y tendencias hacia 2030

**Temas:**

* Ciclo de vida: entrenamiento, despliegue, monitorización, reentrenamiento.
* Costos, latencia, privacidad y seguridad.
* Nube vs edge (modelos grandes vs modelos pequeños).
* Tendencias 2030: agentes autónomos, IA en ciencia, IA responsable.
* Presentación y discusión de propuestas o avances del trabajo final.

#### Metodología

El curso combina:

* Exposiciones breves del docente.
* Discusión guiada de lecturas y artículos recientes.
* Actividades prácticas ligeras (análisis de casos, mini ejercicios, demostraciones en notebook).
* Trabajo autónomo orientado al proyecto final. 

#### Evaluación

* **Participación y actividades en clase:** 40%
* **Trabajo final integrador:** 60% 

#### Trabajo final integrador

El trabajo final consiste en un **miniproyecto** o **survey crítico** que combine al menos dos bloques del curso (por ejemplo: visión + LLM, difusión + lenguaje, RL + LLM), e incluya:

* Informe técnico o cuaderno bien documentado.
* Repositorio con código y datos mínimos para reproducibilidad.
