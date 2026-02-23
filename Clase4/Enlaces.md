### Enlaces para la clase 4

#### 1. LLM (base práctica)

* **Hugging Face LLM Course - Introduction** (entrada recomendada para LLMs). ([Hugging Face][1])
* **Hugging Face - Fine-tuning** (ruta práctica para conectar Transformer -> LLM aplicado). ([Hugging Face Docs][2])
* **Hugging Face - Causal language modeling** (enlace directo al paradigma decoder-only). ([Hugging Face Docs][3])

#### 2. Alineamiento (alignment)

* **InstructGPT (RLHF)** (paper fundamental para introducir alineamiento). ([arXiv][4])
* **DPO (Direct Preference Optimization)** (alternativa moderna a RLHF, muy útil para discusión). ([arXiv][5])


#### 3. Agentes (arquitectura y orquestación)

* **Anthropic - Building Effective AI Agents** (patrones de diseño y recomendaciones prácticas). ([Anthropic][6])
* **LangGraph - Workflows and agents** (diferencia explícita entre workflow determinístico y agente). ([LangChain Docs][7])
* **OpenAI - Agents (guía oficial)** (visión general de agentes y toolkit). ([OpenAI Docs][8])
* **OpenAI - Agents SDK** (documentación para construir agentes con tools y handoffs). ([OpenAI Docs][9])

#### 4. Ruta mínima sugerida (Clase 4)

1. **HF LLM Course - Introduction** -> panorama LLM. ([Hugging Face][1])
2. **HF Causal LM** -> decoder-only en práctica. ([Hugging Face Docs][3])
3. **InstructGPT** -> alineamiento con feedback humano. ([arXiv][4])
4. **DPO** -> alternativa moderna de preferencias. ([arXiv][5])
5. **Anthropic: Building Effective AI Agents** -> diseño de agentes. ([Anthropic][6])
6. **LangGraph + OpenAI Agents/SDK** -> orquestación y herramientas. ([LangChain Docs][7], [OpenAI Docs][8], [OpenAI Docs][9])


[1]: https://huggingface.co/learn/llm-course/en/chapter1/1 "Hugging Face LLM Course - Introduction"
[2]: https://huggingface.co/docs/transformers/en/training "Fine-tuning (Hugging Face Transformers)"
[3]: https://huggingface.co/docs/transformers/en/tasks/language_modeling "Causal language modeling (Hugging Face Docs)"
[4]: https://arxiv.org/abs/2203.02155 "Training language models to follow instructions with human feedback (InstructGPT)"
[5]: https://arxiv.org/abs/2305.18290 "Direct Preference Optimization (DPO)"
[6]: https://www.anthropic.com/engineering/building-effective-agents "Building Effective AI Agents (Anthropic)"
[7]: https://docs.langchain.com/oss/python/langgraph/workflows-agents "Workflows and agents (LangGraph Docs)"
[8]: https://developers.openai.com/api/docs/guides/agents/ "Agents (OpenAI API Docs)"
[9]: https://developers.openai.com/api/docs/guides/agents-sdk/ "Agents SDK (OpenAI API Docs)"
