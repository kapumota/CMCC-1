## Mini-proyecto de ejemplo

Este mini-proyecto está diseñado para **la Sesión 8**: pasar de "tengo un workflow con LLM/herramientas" a "tengo un **sistema operable**" con endpoints, RAG, métricas y una ruta de actualización controlada.

### ¿Qué incluye?

- **API de inferencia** (FastAPI)
- **Workflow/pipeline** (secuencial: parseo -> RAG -> tool-calling -> respuesta)
- **RAG local** (TF-IDF) con *reindex* (equivalente práctico al "reentrenamiento" en apps LLM)
- **Observabilidad**: logs JSON + métricas Prometheus (`/metrics`)
- **Docker** + (opcional) Prometheus vía `docker-compose`
- **Tests** (pytest) + CI (GitHub Actions)
- **LLM opcional**: si no configuras un endpoint OpenAI-compatible, el sistema usa un **fallback local** para funcionar offline.
- **Notebook**: `notebooks/Workflows_Pipelines_Agentes_Local.ipynb` para laboratorio/explicación paso a paso del pipeline.

> Nota: el objetivo de la sesión es **ingeniería de sistema** (pipeline + operación + observabilidad), no maximizar "calidad lingüística" del modelo.

### Linux/macOS/WSL
```bash
python3 -m venv mlops
source mlops/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

bash scripts/ingest_docs.sh
bash scripts/run_local.sh
```

En otra terminal:
```bash
curl http://127.0.0.1:8000/health
curl -X POST "http://127.0.0.1:8000/workflow" -H "Content-Type: application/json" \
  -d '{"request":"Quiero viajar de LAX a JFK y hospedarme en New York. Dame 2 opciones."}'
```

#### Windows (VS Code Terminal + Git Bash)
> **Recomendado**: usar **PowerShell** o **WSL**.  
> Si estás usando **Git Bash**, el venv puede crear estructura Windows (`Scripts/`) y causar confusión con `source .../bin/activate`. Abajo tienes receta específica para Git Bash.

#### 1. Requisitos

##### Software
- **Python 3.10+** (recomendado **3.11**)
- **pip**
- (Opcional) **Docker Desktop** si ejecutarás con contenedores
- (Opcional) **WSL** si estás en Windows y quieres usar `bash` sin fricción

#### Verificar versión
#####  Linux/macOS/WSL
```bash
python3 --version
pip --version
```

##### Windows (PowerShell)
```powershell
python --version
pip --version
```

#### 2. Preparación: crear entorno `mlops`

##### 2.1 Linux/macOS/WSL
```bash
cd CMCC-1
python3 -m venv mlops
source mlops/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

Para desarrollo/tests:
```bash
pip install -r requirements-dev.txt
```

##### 2.2 Windows (VS Code Terminal + Git Bash)

##### (A) Crear venv
En Git Bash, dentro del proyecto:
```bash
cd CMCC-1
python -m venv mlops
```

##### (B) Activar venv (Git Bash)
En **Git Bash** normalmente se activa así (nota: usa `Scripts`, no `bin`):
```bash
source mlops/Scripts/activate
```

Si te funciona `mlops/bin/activate`, estás en WSL/Linux; si no existe, usa `Scripts/activate`.

##### (C) Instalar dependencias
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Para desarrollo/tests:
```bash
pip install -r requirements-dev.txt
```

> Tip: verifica que estás dentro del venv con:
```bash
which python
python --version
```

##### 2.3 Windows (PowerShell) (alternativa estable)
```powershell
cd CMCC-1

python -m venv mlops
.\mlops\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt
```

> Si PowerShell bloquea la activación:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```


#### 3. Ejecutar local (recomendado para clase)

##### (A) Construir índice RAG (docs -> index)

**¿Qué hace?** Toma `data/docs/`, genera chunks y construye el índice TF-IDF en `data/indexes/`.

##### Linux/macOS/WSL
```bash
bash scripts/ingest_docs.sh
```

##### Windows (PowerShell o Git Bash sin depender de `.sh`)
```bash
# Git Bash
export PYTHONPATH=./src
python -m rag.ingest
```

```powershell
# PowerShell
$env:PYTHONPATH=".\src"
python -m rag.ingest
```

**Salida esperada**: `Index OK: ... (chunks=XX)`.


##### (B) Levantar API

##### Linux/macOS/WSL
```bash
bash scripts/run_local.sh
```

##### Windows (PowerShell o Git Bash)
```bash
# Git Bash
export PYTHONPATH=./src
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

```powershell
# PowerShell
$env:PYTHONPATH=".\src"
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

**Salida esperada** (consola):
- `Uvicorn running on http://127.0.0.1:8000`

##### (C) Verificar endpoints (GET)

Con la API corriendo:

##### Opción 1: Navegador
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/metrics`
- `http://127.0.0.1:8000/docs` (Swagger UI)

##### Opción 2: curl (Git Bash / Linux / WSL / macOS)
```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/metrics
```

#### Opción 3: PowerShell
```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod http://127.0.0.1:8000/metrics
```

**¿Qué debería devolver `/health`?** Un JSON como:
```json
{"status":"ok","env":"dev","rag_ready":true,"llm_enabled":false}
```

**¿Qué devuelve `/metrics`?** Texto con métricas tipo:
- `sesion8_requests_total ...`
- `sesion8_workflow_latency_ms_bucket ...`


##### (D) Probar workflow (POST)

> Importante: `curl` NO depende del venv. El venv solo es necesario para correr la API y scripts Python.

##### curl (Git Bash / Linux / WSL / macOS)
```bash
curl -X POST "http://127.0.0.1:8000/workflow" \
  -H "Content-Type: application/json" \
  -d '{"request":"Quiero viajar de LAX a JFK y hospedarme en New York. Dame 2 opciones."}'
```

##### Swagger UI (más fácil)
Abre `http://127.0.0.1:8000/docs` -> **POST /workflow** -> Try it out -> Execute.

##### PowerShell
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/workflow" `
  -ContentType "application/json" `
  -Body '{"request":"Quiero viajar de LAX a JFK y hospedarme en New York. Dame 2 opciones."}' |
  ConvertTo-Json -Depth 20
```

**Salida esperada**: JSON con `parsed`, `rag`, `flights`, `hotels`, `summary`.

#### 4. Usar un LLM real (OpenAI-compatible)

Por defecto el proyecto usa un **fallback local**. Para que el `summary` lo genere un LLM, configura un backend **OpenAI-compatible** (vLLM/LM Studio/etc.).

##### (A) Crear `.env` desde plantilla
##### Linux/macOS/WSL/Git Bash
```bash
cp .env.example .env
```

##### Windows PowerShell
```powershell
Copy-Item .env.example .env
```

##### (B) Editar variables clave
En `.env`:
- `LLM_BASE_URL` (ej: `http://localhost:8001/v1`)
- `LLM_API_KEY` (puede ser dummy si no valida)
- `LLM_MODEL`

Ejemplo:
```ini
LLM_BASE_URL=http://localhost:8001/v1
LLM_API_KEY=dummy
LLM_MODEL=local-model
```

##### (C) Verificar que se activó
1) Reinicia la API
2) Revisa `/health`: `llm_enabled` debería ser `true`.


#### 5. Notebook (cuaderno)-cómo usarlo en la sesión

El cuaderno `notebooks/Workflows_Pipelines_Agentes_Local.ipynb` se usa como **laboratorio** para ver el pipeline paso a paso, y la API como **modo producción** (operación, métricas, endpoints).

##### 5.1 Ejecutar el cuaderno con el entorno `mlops`
Instala Jupyter dentro del venv (una sola vez):
```bash
pip install jupyter ipykernel
python -m ipykernel install --user --name mlops --display-name "Python (mlops)"
```

Luego:
```bash
jupyter notebook
```

Abre el notebook y selecciona kernel **Python (mlops)**.

##### 5.2 Si el notebook no encuentra módulos (`rag`, `app`, etc.)
Añade al inicio del notebook:
```python
import os, sys
sys.path.append(os.path.abspath("../src"))
```

##### 5.3 Flujo recomendado (Notebook -> API)
1) Ejecutar celdas del notebook para explicar: parseo -> RAG -> tools -> síntesis.
2) Construir índice RAG (`python -m rag.ingest`) y mostrar cómo cambia la recuperación.
3) Levantar API y repetir la misma query vía `POST /workflow`.
4) Abrir `/metrics` y mostrar:
   - contador de requests
   - histograma de latencia del workflow


#### 6.  "Actualización controlada": reindex seguro (demostración)

Este proyecto usa un endpoint demo para simular refresh del RAG:

- `POST /admin/reindex` requiere header `x-admin-token`
- Configura `ADMIN_TOKEN` en `.env` (default `devtoken`)

Ejemplo:
```bash
curl -X POST "http://127.0.0.1:8000/admin/reindex" \
  -H "x-admin-token: devtoken"
```

> En producción real: autenticar/autorizar, rate-limiting, auditoría.

#### 7. Tests (opcional)

Con `requirements-dev.txt` instalado:
```bash
pytest -q
ruff check .
```
#### 8. Docker (rápido)-sin venv `mlops`

Docker encapsula Python + dependencias dentro del contenedor.

#####  Build
```bash
docker build -t llm-workflows -f docker/Dockerfile .
```

##### Run
```bash
docker run --rm -p 8000:8000 llm-workflows
```

Luego abre:
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/metrics`
- `http://127.0.0.1:8000/docs`

> Si `rag_ready=false`, ejecuta:
```bash
curl -X POST "http://127.0.0.1:8000/admin/reindex" -H "x-admin-token: devtoken"
```

#### 9. Docker Compose (API + Prometheus)

Levanta:
- **API**: `http://127.0.0.1:8000`
- **Prometheus**: `http://127.0.0.1:9090`

##### Up
```bash
docker compose -f docker/docker-compose.yml up --build
```

##### Verificar Prometheus
En `http://127.0.0.1:9090`:
- **Status -> Targets**: `sesion8_api` debería estar **UP**
- Queries sugeridas:
  - `sesion8_requests_total`
  - `sesion8_workflow_latency_ms_count`

##### Down
```bash
docker compose -f docker/docker-compose.yml down
```

#### 10. Estructura (alto nivel)

- `src/app/`: API (FastAPI)
- `src/workflows/`: pipeline + nodos + cliente LLM
- `src/rag/`: ingest + índice + retriever
- `src/tools/`: herramientas (tool-calling)
- `src/observability/`: logs/métricas
- `data/docs/`: documentos para RAG
- `data/indexes/`: índices generados
- `scripts/`: comandos de operación
