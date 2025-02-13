# Project: Gestor Clases

## Description
Este proyecto tiene el fin de la gestión de clases impartidas a estudiantes para controlar las horas impartidas y los gastos generados de ellas.

Este proyecto es una aplicación web desarrollada utilizando **Astro** (para el desarrollo del front), **Mysql** (como base de datos), **Flask-Migrate** (para el manejo de migraciones) y **FastAPI** (para el desarrollo de APIs). El objetivo de esta aplicación es proporcionar una solución robusta para manejar datos y servicios REST.

## Estructura del Proyecto
```
FastApi_Flask/
├── README.md
├── api
│   ├── Dockerfile
│   ├── controllers
│   │   ├── ClassController.py
│   │   ├── StudentController.py
│   ├── database.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 24a5c03010f7_initial_migration.py
│   ├── models
│   │   ├── Class.py
│   │   ├── Student.py
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
    │   │   ├── ClassForm.astro
    │   │   ├── Header.astro
    │   │   ├── Registry.astro
    │   │   ├── Student.astro
    │   │   └── StudentForm.astro
    │   ├── layouts
    │   │   └── Layout.astro
    │   └── pages
    │       ├── index.astro
    │       └── students
    │           ├── [id]
    │           │   └── clases
    │           │       ├── edit
    │           │       │   └── [class_id].astro
    │           │       └── new.astro
    │           ├── [id].astro
    │           ├── edit
    │           │   └── [id].astro
    │           └── new.astro
    ├── startup.sh
    └── tsconfig.json
```

## Servicios
### 1. Front
   - Tecnología: Astro
   - Puerto: 3000

### 2. API
   - Tecnología: Python
   - Puerto: 8000

### 3. Base de datos
   - Tecnología: MySQL
   - Puerto: 3306

## Estructura de case de datos
1. Students

   ```
   Students
        name: string(50) (Nombre del estudiante)
        price: int (Precio por hora)
   ```

2. Classes

   ```
   Classes
        date: date (Fecha de la clase)
        time: int (Tiempo de duración de la clase en minutos)
        price: int (Precio por hora de la clase en el momento en que se llevo a cabo)
        paid: boolean (Clase pagada)
   ```

## Requisitos previos
- Tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) en su máquina local.

## Uso
1. Clone el repositorio en su máquina local:

   ```
   git clone <URL>
   ```

2. Configurar los puertos si es necesario en el docker-compose

3. Navegar hasta la carpeta del proyecto creada y despliega el contenedor:

   ```
   cd gestor_clases
   docker-compose up -d
   ```

4. Abrir un navegador web y acceder a la aplicación en la dirección `http://localhost:3000`.