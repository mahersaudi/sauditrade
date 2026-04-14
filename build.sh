#!/usr/bin/env bash
# Render Build Script — Saudi Export & Trade Council
set -o errexit

echo "========================================"
echo " Saudi Export & Trade Council - Build  "
echo "========================================"

echo ""
echo "[1/5] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "[2/5] Collecting static files..."
python manage.py collectstatic --no-input

echo ""
echo "[3/5] Running migrations..."
python manage.py migrate --no-input

echo ""
echo "[4/5] Seeding sample data..."
python manage.py seed_data

echo ""
echo "[5/5] Creating superuser..."
python manage.py ensure_superuser

echo ""
echo "========================================"
echo "  Build complete!"
echo "========================================"
