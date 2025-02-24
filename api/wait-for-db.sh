#!/bin/sh
set -e

# Cargar las variables desde el .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Wait until database is ready
echo "Wait until MySQL is prepared..."

until python -c "import pymysql, os; pymysql.connect(
    host=os.getenv('MYSQL_HOST'), 
    user=os.getenv('MYSQL_USER'), 
    password=os.getenv('MYSQL_PASSWORD'), 
    database=os.getenv('MYSQL_DATABASE')
)" 2>/dev/null; do
    echo "MySQL not prepared. Waiting..."
    sleep 2
done

echo "MySQL prepared. Launching migrations and API..."

# Execute migrations and run api
[ ! -d migrations ] && flask db init && flask db migrate -m "Initial migration."
flask db upgrade
python database.py
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
