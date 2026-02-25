### Enlaces para la clase 6

#### 1. De convoluciones a Vision Transformers (ViT): motivación y esquema general

* **Vision Transformer (ViT) - documentación de Transformers** (explicación del modelo, patches, checkpoints y uso práctico). ([Hugging Face][1])
* **Repositorio oficial de Google Research: `vision_transformer`** (implementación de referencia y Colab). ([GitHub][2])
* **D2L - Transformers for Vision** (explicación didáctica de ViT y comparación conceptual con CNNs). ([Dive into Deep Learning][3])
* **Paper original de ViT** *An Image is Worth 16x16 Words* (base teórica y resultados fundacionales). ([arXiv][4])

#### 2. Representaciones conjuntas texto-imagen: CLIP y tareas de recuperación

* **CLIP: Connecting text and images** (blog oficial; intuición y casos de uso zero-shot). ([OpenAI][5])
* **Paper de CLIP** *Learning Transferable Visual Models From Natural Language Supervision* (fundamento contrastivo texto-imagen). ([arXiv][6])
* **CLIP - documentación de Transformers** (uso del modelo y componentes en Hugging Face). ([Hugging Face][7])
* **Ejemplo de Image Search con embeddings conjuntos** (búsqueda/recuperación texto-imagen con embeddings). ([Sentence Transformers][8])
* **Repositorio `openai/CLIP`** (código y ejemplos base). ([GitHub][9])

#### 3. Modelos visión-lenguaje y VQA (Visual Question Answering)

* **Visual Question Answering (paper original)** (definición del problema y formulación clásica). ([arXiv][10])
* **Sitio oficial de VQA / VQAv2** (benchmark, datasets y evaluación). ([VisualQA][11])
* **Task guide de VQA en Transformers** (pipeline práctico, fine-tuning y ejemplos). ([Hugging Face][12])
* **BLIP-2 - documentación** (modelo VL fuerte para tareas tipo VQA, captioning e instruction-following visual). ([Hugging Face][13])

#### 4. LLM multimodales (MLLM): texto, imagen, audio y vídeo

* **Multimodal Chat Templates (visión + audio)** (guía práctica para prompts multimodales en Transformers). ([Hugging Face][14])
* **Visual Instruction Tuning (LLaVA)** (paper clave para LLMs con imagen + texto). ([arXiv][15])
* **LLaVA - documentación** (uso práctico del modelo en Transformers). ([Hugging Face][16])
* **BLIP-2 (paper)** (puente eficiente entre encoder visual y LLM congelado vía Q-Former). ([arXiv][17])
* **ImageBind** (espacio de embeddings conjunto para múltiples modalidades: imagen, texto, audio, etc.). ([arXiv][18])
* **Qwen2-Audio Technical Report** (audio-language model; entrada de audio + texto). ([arXiv][19])
* **Video-LLaVA** (MLLM para comprensión conjunta de imágenes y vídeo). ([arXiv][20])

#### 5. Aplicaciones en salud, industria, educación y sistemas interactivos

##### Salud
* **Medical Visual Question Answering: A Survey** (panorama de datasets, métodos y retos en Med-VQA). ([arXiv][21])
* **Generative Models in Medical Visual Question Answering** (revisión reciente de enfoques generativos en Med-VQA). ([MDPI][22])
* **TREC-MedVQA benchmark** (benchmark y dataset para VQA en dominio médico). ([arXiv][23])

##### Industria
* **Guide to Vision Language Models and Prompt Engineering** (guía práctica de VLMs y prompting; útil para inspección y operaciones). ([NVIDIA][24])
* **InspecSafe-V1** (benchmark multimodal para evaluación de seguridad en inspección industrial). ([arXiv][25])
* **TEMAI** (foundation model multimodal para análisis industrial/time-series + visión). ([arXiv][26])

##### Educación
* **UNESCO - Guidance for Generative AI in Education and Research** (marco de adopción responsable en educación). ([UNESCO][27])
* **Multimodal Learning Analytics Methods: A Review and Future Challenges** (revisión sobre analítica multimodal aplicada a educación).([arXiv][28])
* **LLMs as Educational Analysts** (uso de LLMs para análisis educativo a partir de datos multimodales) ([arXiv][29])
* **M2LADS demo** (demo de learning analytics multimodal para apoyo a decisiones educativas). ([ACM DL][30])

##### Sistemas interactivos
* **Visual ChatGPT** (paper clásico de orquestación de herramientas visuales + LLM conversacional). ([arXiv][31])
* **LLaVA project page** (demostración/proyecto de asistente visión-lenguaje interactivo). ([LLaVA][32])
* **Multimodal Chat Templates (visión/audio)** (para prototipos interactivos con entradas multimodales). ([Hugging Face][14])

#### 6. Blogs y tutoriales de apoyo (lectura guiada)

* **Deep (Learning) Focus - Cameron R. Wolfe** (blog técnico con explicaciones claras y profundas de IA, visión y multimodalidad). ([Substack][33])
* **Vision Transformers - Cameron R. Wolfe** (tutorial/blog sobre ViT, motivación y aplicaciones). ([Substack][34])
* **Using CLIP to Classify Images without any Labels** (explicación práctica de CLIP y zero-shot classification). ([Substack][35])
* **Vision Large Language Models (vLLMs)** (muy útil para conectar visión-lenguaje con MLLM modernos). ([Substack][36])

[1]: https://huggingface.co/docs/transformers/en/model_doc/vit
[2]: https://github.com/google-research/vision_transformer
[3]: https://d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html
[4]: https://arxiv.org/abs/2010.11929

[5]: https://openai.com/index/clip/
[6]: https://arxiv.org/abs/2103.00020
[7]: https://huggingface.co/docs/transformers/en/model_doc/clip
[8]: https://sbert.net/examples/sentence_transformer/applications/image-search/README.html
[9]: https://github.com/openai/CLIP

[10]: https://arxiv.org/abs/1505.00468
[11]: https://visualqa.org/
[12]: https://huggingface.co/docs/transformers/en/tasks/visual_question_answering
[13]: https://huggingface.co/docs/transformers/en/model_doc/blip-2

[14]: https://huggingface.co/docs/transformers/v4.49.0/en/chat_template_multimodal
[15]: https://arxiv.org/abs/2304.08485
[16]: https://huggingface.co/docs/transformers/en/model_doc/llava
[17]: https://arxiv.org/abs/2301.12597
[18]: https://arxiv.org/abs/2305.05665
[19]: https://arxiv.org/abs/2407.10759
[20]: https://arxiv.org/abs/2311.10122

[21]: https://arxiv.org/abs/2111.10056
[22]: https://www.mdpi.com/2076-3417/14/23/11486
[23]: https://arxiv.org/abs/2408.04762

[24]: https://developer.nvidia.com/blog/vision-language-model-prompt-engineering-guide-for-image-and-video-understanding/
[25]: https://arxiv.org/abs/2601.21173
[26]: https://arxiv.org/abs/2509.14805

[27]: https://unesdoc.unesco.org/ark:/48223/pf0000386693
[28]: https://arxiv.org/abs/2408.14491
[29]: https://arxiv.org/abs/2502.10430
[30]: https://dl.acm.org/doi/10.1145/3448139.3448223

[31]: https://arxiv.org/abs/2303.04671
[32]: https://llava-vl.github.io/

[33]: https://cameronrwolfe.substack.com/
[34]: https://cameronrwolfe.substack.com/p/vision-transformers
[35]: https://cameronrwolfe.substack.com/p/using-clip-to-classify-images-without-any-labels-b255bb7205de
[36]: https://cameronrwolfe.substack.com/p/vision-llms
