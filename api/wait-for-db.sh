#!/bin/sh
set -e

# Wait until database is ready
echo "Wait until MySQL is prepared..."

until python -c "import pymysql, os; pymysql.connect(
    host=os.getenv('MYSQL_HOST', 'db'), 
    user=os.getenv('MYSQL_USER', 'root'), 
    password=os.getenv('MYSQL_PASSWORD', 'password'), 
    database=os.getenv('MYSQL_DATABASE', 'data')
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
