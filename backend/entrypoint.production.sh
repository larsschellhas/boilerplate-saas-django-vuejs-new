#!/bin/sh

if [ "$DBENGINE" = "django.db.backends.postgresql" ]
then
  echo "Waiting for postgres..."

  while ! nc -z $DBHOSTNAME $DBPORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec "$@"