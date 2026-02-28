### Enlaces para la clase 6

#### 1. Tutoriales base (visión general + código)

* **What are Diffusion Models? (Lilian Weng)** (visión general muy clara: intuición, formulación y variantes). ([Lilian Weng][1])
* **The Annotated Diffusion Model (Hugging Face Blog)** (DDPM explicado con código, ideal para seguir paso a paso). ([Hugging Face Blog][2])
* **A Beginner's Guide to Diffusion Models** (introducción amigable y panorámica "de cero a variantes"). ([Hashnode][3])
* **Hugging Face Diffusers-Conceptual: Evaluation** (cómo evaluar pipelines/modelos de difusión en práctica). ([Hugging Face Docs][4])
* **HEIM /HELM (Stanford CRFM)** (marco de evaluación para modelos multimodales/generativos; útil para discusión de benchmarks). ([Stanford CRFM][5])

#### 2. Repaso breve: autoencoders, VAE y GANs (fortalezas y limitaciones)

* **What is Transposed Convolutional Layer?** (clave para entender decoders/upsampling en AE/VAE/GAN). ([Towards Data Science][6])

#### 3. Idea central de la difusión: añadir ruido y aprender a denoiser

* **Denoising Diffusion Probabilistic Models (DDPM)** (paper fundacional; define forward/reverse y objetivo de entrenamiento). ([arXiv][7])
* **Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise** (variante útil para debatir "difusión sin ruido gaussiano"). ([arXiv][8])

#### 4. Esquema de entrenamiento y muestreo (DDPM / DDIM, noción general)

* **Denoising Diffusion Probabilistic Models (DDPM)** (entrenamiento base + muestreo probabilístico). ([arXiv][7])
* **Denoising Diffusion Implicit Models (DDIM)** (muestreo implícito: menos pasos, más rápido). ([arXiv][9])
* **Elucidating the Design Space of Diffusion-Based Generative Models (EDM)** (diseño de samplers/schedules; lectura moderna clave). ([arXiv][10])
* **Common Diffusion Noise Schedules and Sample Steps are Flawed** (discusión crítica de schedules y pasos de muestreo). ([arXiv][11])
* **Simple diffusion: End-to-end diffusion for high resolution images** (referencia para discutir diseño "simple" y escalamiento). ([arXiv][12])

#### 5. Difusión para imágenes y más allá: texto, audio, datos científicos

* **CLIP: correlación entre texto e imágenes (OpenAI)** (alineamiento texto–imagen; base para condicionamiento/evaluación). ([OpenAI][13])
* **open_clip (MLFoundations)** (implementación abierta de CLIP; útil para experimentos). ([GitHub][14])
* **CLAP (LAION)** (alineamiento audio-texto; puente natural para difusión en audio). ([GitHub][15])
* **HEIM / HELM (Stanford CRFM)** (marco para evaluar modelos multimodales/generativos en distintos escenarios). ([Stanford CRFM][5])

#### 6. Difusión + Transformers (DiT) y generación condicionada por texto

* **Scalable Diffusion Models with Transformers (DiT)** (paper base de Diffusion Transformers). ([arXiv][16])
* **Scalable Adaptive Computation for Iterative Generation** (RINs + generación iterativa con difusión; eficiencia y escalamiento). ([arXiv][17])
* **CLIP (OpenAI)** (condición por texto y evaluación semántica). ([OpenAI][13])
* **open_clip** (alternativa abierta para embeddings CLIP en pipelines). ([GitHub][14])

#### 7. Evaluación práctica (para reportes y comparaciones en clase)

* **Hugging Face Diffusers – Evaluation** (métricas/consideraciones para evaluar modelos de difusión). ([Hugging Face Docs][4])
* **HEIM / HELM (Stanford CRFM)** (comparación sistemática de modelos multimodales/generativos). ([Stanford CRFM][5])
* **EDM (Elucidating...)** (trade-offs calidad/velocidad; decisiones de diseño). ([arXiv][10])

#### Ruta mínima sugerida (para una primera pasada)

1. **What are Diffusion Models? (Lilian Weng)** -> intuición global. ([1])
2. **Annotated Diffusion Model** -> entrenamiento/muestreo con código. ([2])
3. **DDPM + DDIM** -> fundamentos + aceleración del muestreo. ([7], [9])
4. **EDM + Schedules/Steps Flawed** -> discusión moderna de schedules/samplers. ([10], [11])
5. **DiT** -> Transformers en difusión. ([16])
6. **CLIP + open_clip + CLAP** -> condicionamiento multimodal (texto–imagen/audio–texto). ([13], [14], [15])
7. **Diffusers Evaluation + HEIM/HELM** -> evaluación y comparación de sistemas. ([4], [5])

[1]: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ "What are Diffusion Models? (Lilian Weng)"
[2]: https://huggingface.co/blog/annotated-diffusion "The Annotated Diffusion Model (Hugging Face Blog)"
[3]: https://roysubhradip.hashnode.dev/a-beginners-guide-to-diffusion-models-understanding-the-basics-and-beyond "A Beginner's Guide to Diffusion Models"
[4]: https://huggingface.co/docs/diffusers/en/conceptual/evaluation "Hugging Face Diffusers - Conceptual Evaluation"
[5]: https://crfm.stanford.edu/helm/heim/latest/ "HEIM (HELM) - Stanford CRFM"
[6]: https://towardsdatascience.com/what-is-transposed-convolutional-layer-40e5e6e31c11/ "What is Transposed Convolutional Layer?"
[7]: https://arxiv.org/abs/2006.11239 "Denoising Diffusion Probabilistic Models"
[8]: https://arxiv.org/abs/2208.09392 "Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise"
[9]: https://arxiv.org/abs/2010.02502 "Denoising Diffusion Implicit Models"
[10]: https://arxiv.org/abs/2206.00364 "Elucidating the Design Space of Diffusion-Based Generative Models"
[11]: https://arxiv.org/abs/2305.08891 "Common Diffusion Noise Schedules and Sample Steps are Flawed"
[12]: https://arxiv.org/abs/2301.11093 "Simple diffusion: End-to-end diffusion for high resolution images"
[13]: https://openai.com/es-419/index/clip/ "CLIP: correlación entre texto e imágenes (OpenAI)"
[14]: https://github.com/mlfoundations/open_clip "open_clip"
[15]: https://github.com/LAION-AI/CLAP "CLAP"
[16]: https://arxiv.org/abs/2212.09748 "Scalable Diffusion Models with Transformers"
[17]: https://arxiv.org/abs/2212.11972 "Scalable Adaptive Computation for Iterative Generation"
