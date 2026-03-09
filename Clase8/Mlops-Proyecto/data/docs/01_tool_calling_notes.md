# Tool-calling en workflows

Un pipeline típico:
1) Parsear intención del usuario
2) Recuperar contexto (RAG)
3) Decidir herramientas (tool routing)
4) Ejecutar tools (con validaciones)
5) Sintetizar respuesta (LLM o plantilla)
6) Registrar métricas (latencia, errores, costo, tokens) y logs

Buenas prácticas:
- Validar inputs antes del tool-call
- Limitar timeouts y tamaño de respuesta
- Capturar errores y devolver mensajes útiles
