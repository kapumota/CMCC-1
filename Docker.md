### Instrucciones de uso de cuadernos (opcional)

#### 1. Preparar la carpeta de trabajo

1. Usa una carpeta raíz del curso (por ejemplo, `MCC1`) y coloca en ella:

* El archivo `Dockerfile`
* El archivo `requirements.txt`
* Las carpetas de clases (`Clase1`, `Clase2`, `Clase3`, etc.)
* Dentro de cada clase, los cuadernos Jupyter (`.ipynb`)

2. Estructura recomendada:

```text
MCC1/
├── Dockerfile
├── requirements.txt
├── Clase1/
│   ├── notebook1.ipynb
│   └── notebook2.ipynb
├── Clase2/
│   ├── notebook1.ipynb
│   └── notebook2.ipynb
├── Clase3/
│   └── notebook1.ipynb
└── ...
```

> Al abrir JupyterLab, verás todas las clases organizadas por carpetas.

#### 2. Construir la imagen Docker

> **Nombre de imagen:** `mcc1`

##### 2.1 Windows (Docker Desktop)

1. Abre **Docker Desktop**.
2. Abre **PowerShell** o **CMD**.
3. Ve a la carpeta raíz del curso:

```bash
cd C:\ruta\a\MCC1
```

4. Construye la imagen:

```bash
docker build -t mcc1 .
```

##### 2.2 Linux

1. Verifica que Docker esté instalado y ejecutándose.
2. Ve a la carpeta raíz del curso:

```bash
cd /ruta/a/MCC1
```

3. Construye la imagen:

```bash
docker build -t mcc1 .
```
#### 3. Ejecutar el contenedor y acceder a JupyterLab

#### 3.1 Recomendación general

Como el curso está dividido por clases dentro de `MCC1`, lo más práctico es **montar toda la carpeta `MCC1`** dentro del contenedor para:

* ver todas las clases (`Clase1`, `Clase2`, etc.),
* editar y guardar notebooks en tu máquina,
* mantener el curso ordenado.



##### 3.2 Ejecutar montando todo el curso (`MCC1`)

##### Opción A: Linux/Git Bash

```bash
docker run -it --rm \
  -p 8888:8888 \
  -v /ruta/a/MCC1:/home/jovyan/work \
  mcc1
```

##### Opción B: Windows PowerShell

```powershell
docker run -it --rm `
  -p 8888:8888 `
  -v "C:\ruta\a\MCC1:/home/jovyan/work" `
  mcc1
```

##### Opción C: Windows CMD (una sola línea)

```bash
docker run -it --rm -p 8888:8888 -v C:\ruta\a\MCC1:/home/jovyan/work mcc1
```

##### 3.3 Abrir directamente una clase específica (ejemplo: `Clase1`)

Si quieres que el estudiante trabaje **solo en una clase**, monta esa carpeta directamente como directorio de trabajo.

##### Linux / Git Bash

```bash
docker run -it --rm \
  -p 8888:8888 \
  -v /ruta/a/MCC1/Clase1:/home/jovyan/work \
  mcc1
```

##### Windows PowerShell

```powershell
docker run -it --rm `
  -p 8888:8888 `
  -v "C:\ruta\a\MCC1\Clase1:/home/jovyan/work" `
  mcc1
```

> Con esto, JupyterLab abrirá mostrando directamente los notebooks de `Clase1`.

##### 3.4 Explicación rápida del comando

* `-it`: modo interactivo
* `--rm`: elimina el contenedor al salir
* `-p 8888:8888`: expone JupyterLab en el puerto 8888
* `-v ...:/home/jovyan/work`: monta la carpeta local dentro del contenedor
* `mcc1`: nombre de la imagen

##### 3.5 Acceder a JupyterLab

1. Ejecuta el comando.
2. En la terminal aparecerá una URL similar a:

```text
http://127.0.0.1:8888/lab?token=...
```

3. Copia y pega la URL en el navegador.
4. Verás:

   * todas las clases (`Clase1`, `Clase2`, `Clase3`, …) si montaste `MCC1`, o
   * solo los notebooks de `Clase1` si montaste esa carpeta.

#### 4. Uso gráfico con Docker Desktop (Windows)

También puedes hacerlo sin terminal:

1. Ve a **Images** en Docker Desktop.
2. Busca la imagen **`mcc1`**.
3. Haz clic en **Run**.
4. Configura:

   * **Puerto:** `8888` (host) -> `8888` (container)
   * **Volumen:**

     * curso completo: `MCC1` -> `/home/jovyan/work`
     * una clase: `MCC1\Clase1` -> `/home/jovyan/work`
5. Inicia con **Run**.
6. Copia la URL con token desde los logs y ábrela en el navegador.

#### 5. Ajustes y consejos finales

* Si prefieres **Jupyter Notebook** (modo clásico) en vez de JupyterLab, cambia el comando final del `Dockerfile` a:

```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

* Mantén `Dockerfile` y `requirements.txt` en la raíz (`MCC1`) para que el entorno sea reproducible.
* Si agregas nuevas clases (`Clase4`, `Clase5`, ...), **no necesitas reconstruir** la imagen si solo agregas notebooks.
* Si cambias dependencias en `requirements.txt`, sí debes reconstruir:

```bash
docker build -t mcc1 .
```

#### 6. Tutoriales recomendados de Docker


1. **Docker Docs - Get started**

   * Punto de entrada oficial para aprender el flujo básico y los recursos principales de Docker. ([Docker Documentation][1]).

2. **Docker Workshop (oficial, ~45 min)**

   * Taller guiado paso a paso. Cubre contenedores, imágenes, compartir imágenes, apps con múltiples contenedores y Compose. ([Docker Documentation][2]).

3. **Docker 101 Tutorial (oficial)**

   * Tutorial hands-on para aprender a construir imágenes, correr contenedores, usar volúmenes/mounts y trabajar con Docker Compose. ([Docker][3]).

4. **Docker Compose Quickstart (oficial)**

   * Fundamental para proyectos reales. Enseña a definir servicios en un archivo Compose y ejecutar la app con `docker compose`. ([Docker Documentation][4]).

5. **Play with Docker Classroom**

   * Plataforma de práctica en navegador con labs/tutoriales; útil si el estudiante todavía no domina la instalación local. ([Play with Docker Classroom][5]).

6. **Dockerfile (overview)**

   * Para entender bien qué hace un `Dockerfile` y las instrucciones clave como `FROM`, `RUN`, `WORKDIR`, etc. ([Docker Documentation][6]).

7. **Building best practices (Docker Docs)**

   * Buenas prácticas de imágenes: multi-stage builds, base images confiables, `.dockerignore`, rebuilds frecuentes, caché, etc. ([Docker Documentation][7]).

8. **Educational resources + CLI cheat sheet**

   * Material de repaso oficial, incluyendo la hoja de comandos (CLI cheat sheet). ([Docker Documentation][8]).

[1]: https://docs.docker.com/get-started/ "Get started | Docker Docs"
[2]: https://docs.docker.com/get-started/workshop/ "Docker workshop | Docker Docs"
[3]: https://www.docker.com/101-tutorial/ "Docker 101 Tutorial | Docker"
[4]: https://docs.docker.com/compose/gettingstarted/ "Quickstart | Docker Docs"
[5]: https://training.play-with-docker.com/ "Play with Docker Classroom"
[6]: https://docs.docker.com/build/concepts/dockerfile/ "Dockerfile overview | Docker Docs"
[7]: https://docs.docker.com/build/building/best-practices/ "Best practices | Docker Docs"
[8]: https://docs.docker.com/get-started/resources/ "Educational resources | Docker Docs"
