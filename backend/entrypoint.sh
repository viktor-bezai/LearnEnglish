#!/bin/sh

# Ensure we exit on error
set -e

echo "Waiting for PostgreSQL..."
timeout=30
count=0

while ! pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER"; do
  echo "Database not ready. Retrying..."
  sleep 1
  count=$((count+1))
  if [ $count -ge $timeout ]; then
    echo "⛔ ERROR: PostgreSQL is not ready after $timeout seconds. Exiting."
    exit 1
  fi
done

echo "✅ PostgreSQL is ready!"

# Ensure correct permissions for static and media directories
echo "Setting correct permissions..."
mkdir -p /app/staticfiles /app/media
chmod -R 777 /app/staticfiles /app/media
chown -R www-data:www-data /app/staticfiles /app/media

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the application
exec "$@"
