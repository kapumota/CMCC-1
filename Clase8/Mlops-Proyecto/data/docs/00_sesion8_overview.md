# Sesión 8: Sistemas de IA (MLOps/LLMOps)

Una app de IA en producción no es solo el modelo. Requiere:

- Empaquetado y despliegue (Docker, servicios, escalado)
- Observabilidad (métricas, logs, trazas)
- Calidad y "drift" (cambios en datos/consultas)
- Actualización controlada (reentrenar o reindexar RAG; versionar prompts)
- Seguridad (auth, rate limiting, protección de endpoints, auditoría)

En LLM apps, "reentrenar" muchas veces se reemplaza por:
- refrescar documentos del RAG,
- mejorar prompts/plantillas,
- evaluar con un conjunto de regresión,
- y promover cambios con control.
