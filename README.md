# Project: Project Manager

## Description
Este proyecto tiene el fin de la gestión de proyectos para controlar las horas empleadas y los gastos generados de ellas.

Este proyecto es una aplicación web desarrollada utilizando **Astro** (para el desarrollo del front), **Mysql** (como base de datos), **Flask-Migrate** (para el manejo de migraciones) y **FastAPI** (para el desarrollo de APIs). El objetivo de esta aplicación es proporcionar una solución robusta para manejar datos y servicios REST.

## Estructura del Proyecto
```
FastApi_Flask/
├── README.md
├── api
│   ├── Dockerfile
│   ├── controllers
│   │   ├── ProjectController.py
│   │   └── RegistryController.py
│   ├── database.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── b36ad629490c_initial_migration.py
│   ├── models
│   │   ├── Project.py
│   │   └── Registry.py
│   ├── requirements.txt
│   └── wait-for-db.sh
├── docker-compose.yml
└── front
    ├── Dockerfile
    ├── README.md
    ├── astro.config.mjs
    ├── package-lock.json
    ├── package.json
    ├── public
    │   └── favicon.svg
    ├── src
    │   ├── assets
    │   │   ├── astro.svg
    │   │   └── background.svg
    │   ├── components
    │   │   ├── Back.astro
    │   │   ├── Button.astro
    │   │   ├── Header.astro
    │   │   ├── Project.astro
    │   │   ├── ProjectForm.astro
    │   │   ├── Registry.astro
    │   │   └── RegistryForm.astro
    │   ├── layouts
    │   │   └── Layout.astro
    │   └── pages
    │       ├── index.astro
    │       └── projects
    │           ├── [id]
    │           │   └── registry
    │           │       ├── edit
    │           │       │   └── [registry_id].astro
    │           │       └── new.astro
    │           ├── [id].astro
    │           ├── edit
    │           │   └── [id].astro
    │           └── new.astro
    ├── startup.sh
    └── tsconfig.json
```

## Servicios
### 1. Front Prod
   - Tecnología: Node
   - Puerto: 5321

### 1. Front Dev
   - Tecnología: Astro
   - Puerto: 5322

### 3. API
   - Tecnología: Python
   - Puerto: 8001

### 4. Base de datos
   - Tecnología: MySQL
   - Puerto: 3307

## Estructura de case de datos
1. Projects

   ```
   Projects
        name: string(50) (Nombre del proyecto)
        price: int (Precio por hora)
   ```

2. Registries

   ```
   Registries
        date: date (Fecha del registro)
        time: int (Tiempo de duración del registro en minutos)
        price: int (Precio por hora del registro en el momento en que se llevo a cabo)
        paid: boolean (Registro pagado)
   ```

## Requisitos previos
- Tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) en su máquina local.

## Uso
1. Clone el repositorio en su máquina local:

   ```
   git clone <URL>
   ```

2. Configurar los puertos si es necesario en el docker-compose

3. Configurar variables de entorno en los ficheros .env

4. Navegar hasta la carpeta del proyecto creada y despliega el contenedor:

   ```
   cd project_manager
   docker-compose up -d
   ```

5. Abrir un navegador web y acceder a la aplicación en la dirección `http://localhost:5321`.

## Demo
Puedes probar la demo en el siguiente enlace
https://serveriker.ddns.net/project_manager/