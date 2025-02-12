# Project: Gestor Clases

## Description
Este proyecto tiene el fin de la gestión de clases impartidas a estudiantes para controlar las horas impartidas y los gastos generados de ellas.

Este proyecto es una aplicación web desarrollada utilizando **Flask-Migrate** (para el manejo de migraciones) y **FastAPI** (para el desarrollo de APIs). El objetivo de esta aplicación es proporcionar una solución robusta para manejar datos y servicios REST.

## Estructura del Proyecto
```
FastApi_Flask/
├── Dockerfile
├── README.md
├── api
│   ├── controllers
│   │   ├── UserController.py
│   ├── database.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── __pycache__
│   │   │   └── env.cpython-39.pyc
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 6b836cb6b8f7_initial_migration.py
│   ├── models
│   │   ├── User.py
│   └── wait-for-db.sh
├── docker-compose.yml
└── requirements.txt
```

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

2. Navegar hasta la carpeta del proyecto creada y despliega el contenedor:

   ```
   cd FastApi_Flask
   docker-compose up -d
   ```

3. Abrir un navegador web y acceder a la aplicación en la dirección `http://localhost:8000/docs`.