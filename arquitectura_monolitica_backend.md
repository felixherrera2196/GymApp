# Arquitectura monolítica del backend

Este documento describe la arquitectura propuesta para el backend del proyecto bajo un enfoque monolítico utilizando **FastAPI** como framework web, **PostgreSQL** como gestor de base de datos, **SQLAlchemy** como ORM y **JWT** para autenticación.

## Visión general

El backend se empaqueta como un único servicio desplegable que expone una API REST. El proceso principal arranca un servidor ASGI de FastAPI y gestiona la comunicación con la base de datos PostgreSQL mediante SQLAlchemy. La aplicación se organiza en capas lógicas para facilitar el mantenimiento y la extensibilidad, aun en un contexto monolítico.

```
app/
├── api/
│   ├── routers/           # Endpoints agrupados por dominio
│   ├── dependencies/      # Dependencias reutilizables (auth, DB, etc.)
│   └── schemas/           # Modelos Pydantic para entrada/salida
├── core/
│   ├── config.py          # Configuración y variables de entorno
│   ├── security.py        # Utilidades de seguridad y JWT
│   └── logging.py         # Configuración de logging
├── services/              # Lógica de negocio y casos de uso
├── repositories/          # Capa de acceso a datos con SQLAlchemy
├── models/                # Modelos declarativos de SQLAlchemy
├── db/
│   ├── session.py         # Sesión de SQLAlchemy
│   └── migrations/        # Migraciones gestionadas por Alembic
└── main.py                # Punto de entrada de FastAPI
```

## Capas principales

### Capa de API (Presentación)
- Define los endpoints REST utilizando routers de FastAPI.
- Valida y serializa datos con modelos Pydantic ubicados en `api/schemas`.
- Gestiona dependencias como autenticación o acceso a la base de datos a través de `Depends`.

### Capa de Servicios (Aplicación)
- Implementa la lógica de negocio y orquesta los casos de uso.
- Invoca la capa de repositorios para interactuar con la base de datos.
- Realiza validaciones adicionales y gestiona transacciones si es necesario.

### Capa de Repositorios (Infraestructura)
- Proporciona una abstracción sobre SQLAlchemy para realizar operaciones CRUD.
- Define métodos específicos por agregado o entidad (por ejemplo, `UserRepository`, `MembershipRepository`).
- Facilita el testeo al permitir sustituir repositorios por dobles de prueba.

### Capa de Modelos (Dominio de datos)
- Contiene los modelos declarativos de SQLAlchemy que reflejan las tablas de PostgreSQL.
- Define relaciones, restricciones y metadatos de la base de datos.

## Autenticación y autorización con JWT
- Las credenciales se validan contra la base de datos utilizando la capa de servicios.
- Al autenticarse correctamente, se genera un JWT firmado con una clave secreta almacenada en configuración.
- El token incluye claims estándar (`sub`, `exp`, `iat`) y cualquier información adicional necesaria (roles, permisos).
- Un middleware o dependencia (`get_current_user`) valida los tokens en cada petición protegida y carga el usuario.

## Gestión de configuración
- Las variables sensibles (secretos JWT, credenciales de DB) se cargan mediante variables de entorno y se gestionan con Pydantic Settings (`core/config.py`).
- Se mantiene un archivo `.env` para desarrollo local y se utilizan secretos del entorno en producción.

## Migraciones de base de datos
- Se emplea Alembic para generar y aplicar migraciones, ubicadas en `db/migrations`.
- Los modelos de SQLAlchemy sirven de base para autogenerar migraciones, garantizando consistencia entre código y esquema.

## Flujo de petición típico
1. El cliente envía una petición HTTP al endpoint correspondiente.
2. FastAPI resuelve las dependencias (p. ej., verificación JWT, obtención de sesión de DB).
3. El router delega la lógica al servicio adecuado.
4. El servicio interactúa con los repositorios para persistir o recuperar datos.
5. Se devuelven los datos serializados con esquemas Pydantic.

## Logging y observabilidad
- La configuración centralizada en `core/logging.py` establece formatos y niveles de log.
- Se registra información relevante de cada petición (inicio, fin, errores) para facilitar el monitoreo.
- Se puede integrar Prometheus o herramientas similares para métricas si se requiere.

## Estrategia de pruebas
- **Tests unitarios** para servicios y utilidades utilizando `pytest` y dependencias inyectadas.
- **Tests de integración** para endpoints con la clase `TestClient` de FastAPI y una base de datos temporal (SQLite o PostgreSQL en contenedor).

## Configuración de pruebas con Pytest
- Crear un paquete `tests/` en la raíz del proyecto con submódulos que reflejen la estructura de la aplicación (`tests/services`, `tests/api`, etc.).
- Definir `conftest.py` para exponer fixtures compartidas, como la sesión de SQLAlchemy en memoria, un `TestClient` configurado y datos de prueba.
- Ejecutar los tests con `pytest` integrándolo al pipeline de CI/CD (`pytest -q`).
- Utilizar `pytest-cov` para medir cobertura y asegurar la calidad del código crítico del backend.

## Despliegue
- El monolito se empaca en un contenedor Docker con un servidor ASGI (Uvicorn o Gunicorn+Uvicorn workers).
- Las migraciones se ejecutan como parte del proceso de despliegue antes de arrancar la aplicación.
- El contenedor se despliega en una instancia única (VM, ECS, etc.), con balanceadores de carga externos si se requiere escalado horizontal.

## Consideraciones adicionales
- Mantener el dominio cohesionado dentro del monolito evitando dependencias cíclicas entre módulos.
- Documentar la API automáticamente con los esquemas de FastAPI (OpenAPI/Swagger).
- Preparar puntos de extensión para modularizar o extraer servicios en el futuro si se necesita evolucionar hacia microservicios.

