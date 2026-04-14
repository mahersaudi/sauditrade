#!/bin/bash
# ================================================
# مجلس الصادرات والتجارة السعودية
# Saudi Export & Trade Council - Startup Script
# ================================================

echo ""
echo "╔══════════════════════════════════════════════════╗"
echo "║     مجلس الصادرات والتجارة السعودية             ║"
echo "║     Saudi Export & Trade Council                 ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Change to project directory
cd "$(dirname "$0")"

echo "🔄 Applying migrations..."
python3 manage.py migrate --run-syncdb 2>&1 | grep -v "^$"

echo ""
echo "✅ Starting development server..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🌐 Website:        http://127.0.0.1:8000/"
echo "🔧 Admin Panel:    http://127.0.0.1:8000/admin/"
echo "👤 Admin Login:    admin / admin123"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📌 Pages:"
echo "   🏠 Home (AR):       http://127.0.0.1:8000/"
echo "   🌍 Home (EN):       http://127.0.0.1:8000/en/"
echo "   📦 Products:        http://127.0.0.1:8000/products/"
echo "   🏭 Factories:       http://127.0.0.1:8000/factories/"
echo "   📝 List Factory:    http://127.0.0.1:8000/list-your-factory/"
echo "   🔍 Investor Inquiry: http://127.0.0.1:8000/investor-inquiry/"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 manage.py runserver 0.0.0.0:8000

