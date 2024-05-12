# Ejercicios Básicos de Python3

Este repositorio contiene ejercicios básicos de Python3 para practicar y aprender el lenguaje.

## Requisitos

Para ejecutar el proyecto, necesitas tener instalado:

- [Python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)


## Instalación

Para configurar el entorno de desarrollo y ejecutar el proyecto, sigue los siguientes pasos:

```bash
# Haz un Fork del repositorio y clona desde tu cuenta de github
git clone <your-forked-repo>

# Navegar al directorio del proyecto
cd f5_python_basic

# Crear un entorno virtual
python3 -m venv env

# Activar el entorno virtual
source env/bin/activate  # En macOS/Linux
.\env\Scripts\Activate   # En Windows con PowerShell
./env/Scripts/Activate   # En Windows con Git Bash

# Instalar las dependencias
pip install -r requirements.txt
```

## Ejecución Test

Para ejecutar los test, sigue los siguientes pasos:

```bash
# Navegar al directorio del proyecto
cd f5_python_basic

# Ejecutar los test
pytest
```

