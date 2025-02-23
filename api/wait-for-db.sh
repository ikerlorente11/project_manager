#!/bin/sh
set -e

# Wait until database is ready
echo "Wait until MySQL is prepared..."

until python -c "import pymysql; pymysql.connect(host='db', user='user', password='password', database='data')" 2>/dev/null; do
    echo "MySQL not prepared. Waiting..."
    sleep 2
done

echo "MySQL prepared. Launching migrations and API..."

# Execute migrations and run api
[ ! -d migrations ] && flask db init && flask db migrate -m "Initial migration."
flask db upgrade
python database.py
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
