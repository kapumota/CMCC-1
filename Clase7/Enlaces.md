### Enlaces para la clase 7


#### 1. Marco MDP: estados, acciones, recompensas, políticas y valores

* **Sutton & Barto (libro base de RL)**: formalismo MDP, funiones de valor, ecuaciones de Bellman, métodos tabulares. ([incompleteideas.net][1])
* **Curso de David Silver (UCL/DeepMind)**: lecturas/diapositivas: MDP, DP, control, policy gradients. ([David Silver][2])
* **OpenAI Spinning Up - Key Concepts**: glosario + formalismo RL/MDP (muy didáctico). ([Spinning Up][3])

#### 2. Métodos básicos: Q-learning y Policy Gradient (visión general)

* **Q-learning (Watkins & Dayan, 1992)**: paper clásico (idea central y convergencia). ([Springer][4])
* **REINFORCE/Policy Gradient (Williams, 1992)**: gradiente de política clásico. ([UMass PDF][5])
* **Spinning Up - Intro to Policy Optimization**: explicación moderna de policy gradients. ([Spinning Up][6])
* **TRPO (2015) y PPO (2017)**: estabilidad práctica en optimización de políticas (trust region/clipped objective). ([TRPO arXiv][7])


#### 3. RL en juegos, robótica y sistemas de recomendación

##### 3.1 Juegos/entornos estándar

* **Gymnasium - Basic usage**: loop agente/entorno y uso básico (ideal para laboratorio). ([Gymnasium][8])
* **Gym (docs legacy)**: referencia clásica (incluye LunarLander/CartPole, etc.). ([Gym Library][9])
* **DQN (Nature, 2015)**: RL profundo en Atari (paper emblemático). ([Nature][10])

##### 3.2 Robótica / control continuo (simulación)

* **MuJoCo (docs oficiales)**: simulador estándar para locomoción/control continuo. ([MuJoCo Docs][11])
* **DeepMind Control Suite (dm_control)**: suite de tareas continuas sobre MuJoCo. ([GitHub][12])
* **Gymnasium tutorial REINFORCE en MuJoCo (InvertedPendulum)**: ejemplo de "robótica" simplificada. ([Gymnasium Tutorial][13])

##### 3.3 Recomendación (RL como decisión secuencial)

* **Survey RL-based Recommender Systems (2021)**: MDP para recomendación; diseño de estado/acción/recompensa. ([arXiv][14])
* **Deep RL in Recommender Systems (2023)**: tendencias, taxonomías y retos. ([ScienceDirect][15])
* **ACM survey (2022)**: panorama centrado en RS con RL. ([ACM DL][16])

#### 4) Conexión RL-LLM: RLHF como RL sobre recompensas humanas

* **InstructGPT (OpenAI, 2022)**: pipeline SFT -> reward model -> RLHF. ([OpenAI PDF][17])
* **Deep RL from Human Preferences (2017)**: recompensa aprendida desde preferencias humanas. ([arXiv][18])
* **Learning to summarize with human feedback (OpenAI, 2020)**: caso de estudio RLHF en NLP. ([OpenAI][19])
* **Hugging Face - Illustrating RLHF**: explicación accesible + ecosistema open-source. ([HF Blog][20])
* **TRL (Hugging Face) - PPO Trainer**: documentación práctica para RLHF con PPO (incluye KL penalty). ([HF TRL Docs][21])
* **Guía de post-training RL para LLMs (HF, 2026)**: discusión moderna de KL, variantes y algoritmos. ([HF Blog][22])

##### Alternativas modernas a RLHF clásico

* **DPO (2023)**: optimiza preferencias sin loop de RL; conexión directa con objetivo RLHF+KL. ([arXiv][23])
* **ORPO (2024)**: preferencia "monolítica" sin modelo de referencia. ([arXiv][24])

#### 5. Diseño de recompensas y desafíos de estabilidad/seguridad

* **DeepMind - Specification gaming**: cómo optimizar la recompensa puede romper la intención. ([DeepMind][25])
* **Lilian Weng - Reward Hacking (2024)**: ejemplos y mitigaciones (muy claro). ([Lil'Log][26])
* **ICLR Blogposts - RLHF with PPO (2024)**: detalles prácticos (incluye KL penalty). ([ICLR Blogposts][27])
* **KL-regularized RL (Alignment Forum)**: intuición teórica para entender estabilidad con KL. ([Alignment Forum][28])
* **Detecting & mitigating reward hacking (arXiv, 2025)**: enfoque tipo "safety engineering". ([arXiv][29])


[1]: http://incompleteideas.net/book/the-book-2nd.html "Reinforcement Learning: An Introduction"
[2]: https://davidstarsilver.wordpress.com/teaching/ "Teaching - David Silver"
[3]: https://spinningup.openai.com/en/latest/spinningup/rl_intro.html "Part 1: Key Concepts in RL - Spinning Up"

[4]: https://link.springer.com/article/10.1007/BF00992698 "Q-learning | Machine Learning | Springer"
[5]: https://www-anw.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf "Simple Statistical Gradient-Following Algorithms for Connectionist RL"
[6]: https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html "Part 3: Intro to Policy Optimization - Spinning Up"
[7]: https://arxiv.org/abs/1502.05477 "Trust Region Policy Optimization"

[8]: https://gymnasium.farama.org/introduction/basic_usage/ "Gymnasium - Basic Usage"
[9]: https://www.gymlibrary.dev/ "Gym Documentation"
[10]: https://www.nature.com/articles/nature14236 "Human-level control through deep reinforcement learning"

[11]: https://mujoco.readthedocs.io/ "MuJoCo Documentation"
[12]: https://github.com/google-deepmind/dm_control "google-deepmind/dm_control"
[13]: https://gymnasium.farama.org/v0.29.0/tutorials/training_agents/reinforce_invpend_gym_v26/ "REINFORCE for MuJoCo - Gymnasium"

[14]: https://arxiv.org/abs/2101.06286 "Reinforcement learning based recommender systems: A survey"
[15]: https://www.sciencedirect.com/science/article/pii/S0950705123000850 "Deep reinforcement learning in recommender systems"
[16]: https://dl.acm.org/doi/10.1145/3543846 "Reinforcement Learning based Recommender Systems"

[17]: https://cdn.openai.com/papers/Training_language_models_to_follow_instructions_with_human_feedback.pdf "Training language models to follow instructions with human feedback"
[18]: https://arxiv.org/abs/1706.03741 "Deep reinforcement learning from human preferences"
[19]: https://openai.com/index/learning-to-summarize-with-human-feedback/ "Learning to summarize with human feedback"
[20]: https://huggingface.co/blog/rlhf "Illustrating RLHF - Hugging Face"
[21]: https://huggingface.co/docs/trl/en/ppo_trainer "TRL PPO Trainer - Hugging Face"
[22]: https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms "Guide to LLM post-training algorithms - Hugging Face"

[23]: https://arxiv.org/abs/2305.18290 "Direct Preference Optimization"
[24]: https://arxiv.org/abs/2403.07691 "Monolithic Preference Optimization without Reference Model"

[25]: https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ "Specification gaming - DeepMind"
[26]: https://lilianweng.github.io/posts/2024-11-28-reward-hacking/ "Reward Hacking in RL - Lil'Log"
[27]: https://iclr-blogposts.github.io/2024/blog/the-n-implementation-details-of-rlhf-with-ppo/ "RLHF with PPO - ICLR Blogposts"
[28]: https://www.alignmentforum.org/posts/eoHbneGvqDu25Hasc/rl-with-kl-penalties-is-better-seen-as-bayesian-inference "RL with KL penalties - Alignment Forum"
[29]: https://arxiv.org/html/2507.05619v1 "Detecting and Mitigating Reward Hacking in RL"
