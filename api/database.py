import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve database credentials from environment variables
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
host = os.getenv("MYSQL_HOST")

# Initialize the Flask application
flask_app = Flask(__name__)
# Configure the database URI for SQLAlchemy
flask_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{host}:3306/{database}"

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy()
db.init_app(flask_app)
migrate = Migrate(flask_app, db)

# Definition of the Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Project ID
    name = db.Column(db.String(50))  # Project name
    price = db.Column(db.Integer)  # Project price

    # One-to-many relationship with the Registry model
    registries = db.relationship('Registry', backref='project', lazy=True, cascade="all, delete-orphan")

# Definition of the Registry model
class Registry(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Registry ID
    date = db.Column(db.Date)  # Date of the registry
    time = db.Column(db.Integer)  # Time associated with the registry
    price = db.Column(db.Integer)  # Price of the registry
    paid = db.Column(db.Boolean)  # Payment status

    # Foreign key referencing the Project model
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete="CASCADE"), nullable=False)

# Function to seed initial data into the database
def seed():
    # Check if there are already projects in the database
    if not Project.query.first():
        # Create test projects
        project1 = Project(name="Project 1", price=100)
        project2 = Project(name="Project 2", price=250)

        # Add projects to the session and commit changes
        db.session.add(project1)
        db.session.add(project2)
        db.session.commit()
        print("Test projects added successfully.")

    # Check if there are already registries in the database
    if not Registry.query.first():
        # Create test registries
        registry1 = Registry(date="2025-02-12", time=60, price=100, paid=False, project_id=1)
        registry2 = Registry(date="2025-02-13", time=90, price=100, paid=True, project_id=1)
        registry3 = Registry(date="2025-02-14", time=120, price=250, paid=False, project_id=2)
        registry4 = Registry(date="2025-02-15", time=90, price=250, paid=True, project_id=2)

        # Add registries to the session and commit changes
        db.session.add(registry1)
        db.session.add(registry2)
        db.session.add(registry3)
        db.session.add(registry4)
        db.session.commit()
        print("Test registries added successfully.")

# Function to create a MySQL event that resets the database daily
def create_mysql_event():
    demo = os.getenv('DEMO', 'production')  # Get the operating mode (demo or production)

    # Connect to the database
    with db.engine.connect() as connection:
        with connection.connection.cursor() as cursor:
            # Enable the MySQL event scheduler
            cursor.execute("SET GLOBAL event_scheduler = ON;")

            # Create an event that runs daily
            cursor.execute("""
                CREATE EVENT IF NOT EXISTS reset_database_event
                ON SCHEDULE EVERY 1 DAY
                STARTS TIMESTAMP(CONCAT(CURRENT_DATE, ' 00:00:00'))
                DO
                BEGIN
                    DELETE FROM project;  -- Delete all projects
                    DELETE FROM registry;  -- Delete all registries

                    -- Reset IDs
                    ALTER TABLE project AUTO_INCREMENT = 1;
                    ALTER TABLE registry AUTO_INCREMENT = 1;

                    -- Insert test projects
                    INSERT INTO project (name, price) VALUES
                        ('Project 1', 100),
                        ('Project 2', 250);

                    -- Insert test registries
                    INSERT INTO registry (date, time, price, paid, project_id) VALUES
                        ('2025-02-12', 60, 100, FALSE, 1),
                        ('2025-02-13', 90, 100, TRUE, 1),
                        ('2025-02-14', 120, 250, FALSE, 2),
                        ('2025-02-15', 90, 250, TRUE, 2);
                END;
            """)
            print("✅ MySQL event scheduled to run at 00:00.")

            # Disable the event if not in demo mode
            if demo != "1":
                cursor.execute("ALTER EVENT reset_database_event DISABLE;")
                print("Reset event disabled")

# Entry point of the application
if __name__ == "__main__":
    with flask_app.app_context():
        seed()  # Seed initial data
        create_mysql_event()  # Create the MySQL event