### Enlaces para la clase 3

#### 1. Tutoriales base (visión general + código)

* **The Annotated Transformer (Harvard NLP)** (explicación línea por línea + implementación).([Harvard NLP][1])
* **The Illustrated Transformer (Jay Alammar)** (visual e intuitivo, muy bueno para primera lectura). ([Jay Alammar][2])
* **Hugging Face LLM Course-How do Transformers work?** (explica atención, arquitectura y componentes). ([Hugging Face][3])
* **Hugging Face LLM Course-Transformer Architectures** (encoder-only /decoder-only/encoder-decoder). ([Hugging Face][4])

#### 2. Self-attention: consultas, claves y valores; complejidad cuadrática

* **Attention Is All You Need** (paper original; define Q/K/V y scaled dot-product attention). ([arXiv][5])
* **The Annotated Transformer** (muy útil para aterrizar Q/K/V en código PyTorch). ([Harvard NLP][1])
* **FlashAttention** (paper clave para discutir por qué la atención estándar tiene costo cuadrático y cómo se optimiza en práctica).([arXiv][6])

#### 3. Multi-head attention, normalización y conexiones residuales

* **Attention Is All You Need** (multi-head attention + residual connections + layer normalization en la arquitectura original).([arXiv][5])
* **The Annotated Transformer** (explicación integrada de subcapas, residual y normalización).([Harvard NLP][1])
* **Layer Normalization** (paper base para contextualizar la normalización usada en Transformers).([arXiv][7])

#### 4. Arquitectura encoder/decoder y variantes (solo decoder para LLM)

* **Attention Is All You Need** (arquitectura encoder-decoder clásica).([arXiv][5])
* **Hugging Face - Transformer Architectures** (comparación clara entre encoder-only, decoder-only y encoder-decoder).([Hugging Face][4])
* **Hugging Face - Causal language modeling** (base práctica para explicar decoder-only en LLMs).([Hugging Face Docs][8])

#### 5. Positional encodings y variantes (RoPE, ALiBi, etc.)

* **Attention Is All You Need** (positional encoding sinusoidal clásico). ([arXiv][5])
* **RoFormer: Enhanced Transformer with Rotary Position Embedding (RoPE)** (paper original de RoPE). ([arXiv][9])
* **Train Short, Test Long: ALiBi** (paper original de ALiBi, útil para longitud/extrapolación).([arXiv][10])
* **Hugging Face Blog - Designing Positional Encoding** (tutorial moderno, muy didáctico, conecta hasta RoPE).([Hugging Face Blog][11])

#### 6. Breve revisión de "Attention Is All You Need" y discusión en clase

* **Paper original (lectura obligatoria)**.([arXiv][5])
* **Versión HTML en arXiv** (útil para lectura en navegador).([arXiv HTML][12])
* **The Annotated Transformer** (lectura guiada paralela al paper).([Harvard NLP][1])

#### Ruta mínima sugerida (clase 3) para la maestría

1. **Illustrated Transformer** -> intuición visual.([2])
2. **Annotated Transformer** -> bloques + código.([1])
3. **Attention Is All You Need** -> paper original.([5])
4. **HF Transformer Architectures + Causal LM** -> encoder/decoder/decoder-only.([4], [8])
5. **RoPE + ALiBi** -> posiciones modernas.([9], [10], [11])

[1]: https://nlp.seas.harvard.edu/2018/04/03/attention.html "The Annotated Transformer (Harvard NLP)"
[2]: https://jalammar.github.io/illustrated-transformer/ "The Illustrated Transformer (Jay Alammar)"
[3]: https://huggingface.co/learn/llm-course/en/chapter1/4 "How do Transformers work? (Hugging Face LLM Course)"
[4]: https://huggingface.co/learn/llm-course/en/chapter1/6 "Transformer Architectures (Hugging Face LLM Course)"
[5]: https://arxiv.org/abs/1706.03762 "Attention Is All You Need"
[6]: https://arxiv.org/abs/2205.14135 "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
[7]: https://arxiv.org/abs/1607.06450 "Layer Normalization"
[8]: https://huggingface.co/docs/transformers/en/tasks/language_modeling "Causal language modeling (Hugging Face Docs)"
[9]: https://arxiv.org/abs/2104.09864 "RoFormer: Enhanced Transformer with Rotary Position Embedding"
[10]: https://arxiv.org/abs/2108.12409 "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
[11]: https://huggingface.co/blog/designing-positional-encoding "You could have designed state of the art positional encoding"
[12]: https://arxiv.org/html/1706.03762v7 "Attention Is All You Need (HTML)"
[13]: https://huggingface.co/learn/llm-course/en/chapter1/1 "Hugging Face LLM Course - Introduction"
[14]: https://huggingface.co/docs/transformers/en/training "Fine-tuning (Hugging Face Transformers)"
[15]: https://arxiv.org/abs/2203.02155 "Training language models to follow instructions with human feedback (InstructGPT)"
[16]: https://arxiv.org/abs/2305.18290 "Direct Preference Optimization (DPO)"
[17]: https://www.anthropic.com/research/building-effective-agents "Building Effective AI Agents (Anthropic)"
[18]: https://docs.langchain.com/oss/python/langgraph/workflows-agents "Workflows and agents (LangGraph Docs)"
[19]: https://developers.openai.com/api/docs/guides/agents/ "Agents (OpenAI API Docs)"
[20]: https://developers.openai.com/api/docs/guides/agents-sdk/ "Agents SDK (OpenAI API Docs)"
