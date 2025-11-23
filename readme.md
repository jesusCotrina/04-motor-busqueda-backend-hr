# Documentación del Repositorio 04-motor-busqueda-backend-hr

Este repositorio contiene el código fuente para un servicio de backend construido con **FastAPI**. El propósito principal del servicio es actuar como un **motor de búsqueda inteligente** que utiliza un **modelo de lenguaje grande (LLM)** para detectar la intención del usuario y filtrar resultados (clínicas, lugares, especialidades y horarios) desde una base de datos **PostgreSQL**.

La estructura del proyecto sigue una organización modular para separar las diferentes responsabilidades:

| Archivo/Directorio | Descripción |
|-------------------|-------------|
| `app/api`         | Módulos que definen los endpoints de la API. |
| `app/models`      | Definiciones de los modelos de base de datos (SQLAlchemy/Alembic). |
| `app/schemas`     | Esquemas de validación de datos usando Pydantic. |
| `app/service`     | Lógica de negocio y servicios principales. |
| `app/sql`         | Configuración relacionada con la base de datos SQL. |
| `config.py`       | Archivo de configuración global del proyecto. |
| `database.py`     | Lógica de conexión y sesión de la base de datos. |
| `main.py`         | El punto de entrada principal de la aplicación FastAPI. |
| `Dockerfile`      | Instrucciones para construir la imagen de Docker del servicio. |
| `requirements.txt`| Lista de dependencias de Python requeridas. |
| `deploy.yaml`     | Archivo de configuración para despliegue automático (Cloud Build/Kubernetes). |
| `readme.md`       | Este archivo de documentación. |

---

## Uso e Instalación Local

Sigue estos pasos para levantar la aplicación en tu entorno local.

### Requisitos Previos

Asegúrate de tener instalado:

- Python 3.x  
- pip (gestor de paquetes de Python)  
- Una instancia de PostgreSQL accesible (configurada en `config.py`).

---

### 1. Clonar el Repositorio

Si aún no lo has hecho, clona el repositorio en tu máquina local:

```bash
git clone https://url-del-repositorio.git
cd 04-motor-busqueda-backend-hr
pip install -r requirements.txt
```
# Configuración de la Base de Datos y Levantamiento de la Aplicación

## 3. Configuración de la Base de Datos

Deberás configurar las variables de entorno o el archivo `config.py` con los detalles de tu conexión a **PostgreSQL**:

- **Usuario**  
- **Contraseña**  
- **Host**  
- **Puerto**  
- **Nombre de la base de datos**

---

## 4. Levantar la Aplicación con Uvicorn

Una vez que las dependencias estén instaladas y la base de datos configurada, puedes iniciar el servidor **FastAPI** usando **uvicorn**. El punto de entrada principal es el objeto `app` dentro del módulo `main`.

Ejecuta el siguiente comando en tu terminal desde la raíz del proyecto:

```bash
uvicorn main:app --reload
