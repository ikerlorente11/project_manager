import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos
user = os.getenv("MYSQL_USER", "default_user")
password = os.getenv("MYSQL_PASSWORD", "default_password")
database = os.getenv("MYSQL_DATABASE", "default_database")
host = "db"

flask_app = Flask(__name__)
flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"

# Inicializar la base de datos y migraciones
db = SQLAlchemy()
db.init_app(flask_app)
migrate = Migrate(flask_app, db)

# Definición del modelo Student
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)

    # Relación con la tabla Classes (one-to-many)
    classes = db.relationship('Class', backref='student', lazy=True, cascade="all, delete-orphan")

# Definición del modelo Class
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Integer)
    price = db.Column(db.Integer)
    paid = db.Column(db.Boolean)

    # Relación con Student (many-to-one)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id', ondelete="CASCADE"), nullable=False)

# SEEDERS
def seed():
    # Comprobar si ya existen estudiantes en la base de datos
    if not Student.query.first():
        student1 = Student(name="Alice", price=100)
        student2 = Student(name="Bob", price=150)

        db.session.add(student1)
        db.session.add(student2)
        db.session.commit()
        print("Estudiantes de prueba insertados correctamente.")

    # Comprobar si ya existen clases en la base de datos
    if not Class.query.first():
        class1 = Class(date="2025-02-12", time=10, price=50, paid=False, student_id=1)
        class2 = Class(date="2025-02-13", time=14, price=60, paid=True, student_id=1)
        class3 = Class(date="2025-02-14", time=9, price=55, paid=False, student_id=2)
        class4 = Class(date="2025-02-15", time=16, price=70, paid=True, student_id=2)

        db.session.add(class1)
        db.session.add(class2)
        db.session.add(class3)
        db.session.add(class4)
        db.session.commit()
        print("Clases de prueba insertadas correctamente.")

# Crear el evento de MySQL para resetear la base de datos
def create_mysql_event():
    env = os.getenv('ENV', 'production')

    with db.engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            # 🔹 Habilitar el event_scheduler
            cursor.execute("SET GLOBAL event_scheduler = ON;")

            # 🔹 Crear el evento si no existe
            cursor.execute("""
                CREATE EVENT IF NOT EXISTS reset_database_event
                ON SCHEDULE EVERY 1 DAY
                STARTS TIMESTAMP(CONCAT(CURRENT_DATE, ' 00:00:00'))
                DO
                BEGIN
                    DELETE FROM class;
                    DELETE FROM student;

                    -- Reiniciar IDs
                    ALTER TABLE class AUTO_INCREMENT = 1;
                    ALTER TABLE student AUTO_INCREMENT = 1;

                    -- Insertar estudiantes de prueba
                    INSERT INTO student (name, price) VALUES
                        ('Alice', 100),
                        ('Bob', 150);

                    -- Insertar clases de prueba
                    INSERT INTO class (date, time, price, paid, student_id) VALUES
                        ('2025-02-12', 10, 50, FALSE, 1),
                        ('2025-02-13', 14, 60, TRUE, 1),
                        ('2025-02-14', 9, 55, FALSE, 2),
                        ('2025-02-15', 16, 70, TRUE, 2);
                END;
            """)
            print("✅ Evento de MySQL programado para ejecutarse a las 00:00.")

            if env != 'demo':
                cursor.execute("ALTER EVENT reset_database_event DISABLE;")
                print("Deshabilitado reset")

if __name__ == "__main__":
    with flask_app.app_context():
        seed()  # Insertar datos iniciales si no existen
        create_mysql_event()  # Crear el evento MySQL
