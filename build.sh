#!/usr/bin/env bash
# Render Build Script for Saudi Export & Trade Council
set -o errexit

echo "========================================"
echo " Saudi Export & Trade Council - Build  "
echo "========================================"

echo ""
echo "📦 [1/5] Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "🗂️  [2/5] Collecting static files..."
python manage.py collectstatic --no-input

echo ""
echo "🗃️  [3/5] Running database migrations..."
python manage.py migrate --no-input

echo ""
echo "🌱 [4/5] Loading sample data (if empty)..."
python manage.py shell << 'PYEOF'
from exports.models import Category, Factory, Product

if Category.objects.count() == 0:
    print("  Seeding categories...")
    cats = [
        ("البتروكيماويات", "Petrochemicals", "fas fa-flask", "petrochemicals"),
        ("التمور والأغذية", "Dates & Food", "fas fa-seedling", "dates-food"),
        ("البلاستيك والمطاط", "Plastics & Rubber", "fas fa-recycle", "plastics-rubber"),
        ("الأثاث والديكور", "Furniture & Decor", "fas fa-couch", "furniture-decor"),
        ("مواد البناء", "Building Materials", "fas fa-building", "building-materials"),
        ("المنسوجات والملابس", "Textiles & Clothing", "fas fa-tshirt", "textiles-clothing"),
        ("المعادن والصلب", "Metals & Steel", "fas fa-cog", "metals-steel"),
        ("المنتجات الكيميائية", "Chemical Products", "fas fa-vial", "chemical-products"),
        ("الإلكترونيات", "Electronics", "fas fa-microchip", "electronics"),
        ("مستحضرات التجميل", "Cosmetics", "fas fa-spa", "cosmetics"),
    ]
    for ar, en, icon, slug in cats:
        Category.objects.get_or_create(slug=slug, defaults={"name_ar": ar, "name_en": en, "icon": icon})

if Factory.objects.count() == 0:
    print("  Seeding factories...")
    factories_data = [
        ("شركة سابك للبتروكيماويات", "SABIC Petrochemicals", "الجبيل", "محمد العبدالله", "info@sabic-factory.sa", "+966112345678"),
        ("مصنع النخيل الذهبي للتمور", "Golden Palm Dates Factory", "المدينة المنورة", "عبدالرحمن الأنصاري", "dates@golden-palm.sa", "+966148765432"),
        ("مصنع الرياض للمواد البلاستيكية", "Riyadh Plastics Factory", "الرياض", "خالد السلطان", "info@riyadh-plastics.sa", "+966115559900"),
        ("مصنع الجبيل للصلب", "Jubail Steel Factory", "الجبيل", "فيصل العمري", "steel@jubail-steel.sa", "+966133334444"),
    ]
    for ar, en, city, owner, email, phone in factories_data:
        Factory.objects.get_or_create(email=email, defaults={
            "name_ar": ar, "name_en": en, "city": city,
            "owner_name": owner, "phone": phone, "status": "approved",
            "description_ar": f"مصنع سعودي متخصص في {ar}",
            "description_en": f"Saudi factory specialized in {en}",
        })

if Product.objects.count() == 0:
    print("  Seeding products...")
    petro = Category.objects.filter(slug="petrochemicals").first()
    dates = Category.objects.filter(slug="dates-food").first()
    plastics = Category.objects.filter(slug="plastics-rubber").first()
    metals = Category.objects.filter(slug="metals-steel").first()
    building = Category.objects.filter(slug="building-materials").first()

    sabic = Factory.objects.filter(email="info@sabic-factory.sa").first()
    palm = Factory.objects.filter(email="dates@golden-palm.sa").first()
    riyadh_p = Factory.objects.filter(email="info@riyadh-plastics.sa").first()
    jubail = Factory.objects.filter(email="steel@jubail-steel.sa").first()

    products = [
        {"name_ar": "إيثيلين عالي النقاء", "name_en": "High-Purity Ethylene",
         "description_ar": "إيثيلين بنسبة نقاء 99.9% يُستخدم في صناعة البوليمرات والبلاستيك.",
         "description_en": "High-purity ethylene at 99.9% used in polymer and plastic manufacturing.",
         "category": petro, "factory": sabic, "price_min": 800, "price_max": 1200,
         "min_order_quantity": "20 طن", "availability": "available", "is_featured": True, "slug": "high-purity-ethylene"},
        {"name_ar": "تمر المدينة المجفف", "name_en": "Dried Madinah Dates",
         "description_ar": "تمر المجدول والسكري من أجود أنواع التمور السعودية.",
         "description_en": "Medjool and Sukkari dates from the finest Saudi varieties.",
         "category": dates, "factory": palm, "price_min": 5, "price_max": 15,
         "min_order_quantity": "500 كيلوغرام", "availability": "available", "is_featured": True, "slug": "dried-madinah-dates"},
        {"name_ar": "بولي بروبيلين", "name_en": "Polypropylene (PP)",
         "description_ar": "بولي بروبيلين عالي الجودة للاستخدام الصناعي.",
         "description_en": "High-quality polypropylene for industrial use.",
         "category": plastics, "factory": riyadh_p, "price_min": 1100, "price_max": 1500,
         "min_order_quantity": "10 أطنان", "availability": "available", "is_featured": True, "slug": "polypropylene-pp"},
        {"name_ar": "حديد التسليح", "name_en": "Reinforcement Steel Bars",
         "description_ar": "حديد تسليح عالي الجودة يُستخدم في البناء والإنشاء.",
         "description_en": "High-quality reinforcement steel bars used in construction.",
         "category": metals, "factory": jubail, "price_min": 600, "price_max": 850,
         "min_order_quantity": "50 طن", "availability": "available", "is_featured": True, "slug": "reinforcement-steel-bars"},
        {"name_ar": "اسمنت بورتلاند", "name_en": "Portland Cement",
         "description_ar": "إسمنت بورتلاند عالي الجودة بمقاومة 42.5N.",
         "description_en": "High-quality Portland cement with 42.5N resistance.",
         "category": building, "factory": jubail, "price_min": 60, "price_max": 90,
         "min_order_quantity": "100 طن", "availability": "available", "is_featured": False, "slug": "portland-cement"},
        {"name_ar": "زيت الزيتون السعودي العضوي", "name_en": "Organic Saudi Olive Oil",
         "description_ar": "زيت زيتون بكر ممتاز من مزارع الجوف وتبوك.",
         "description_en": "Extra virgin olive oil from Al-Jouf and Tabuk farms.",
         "category": dates, "factory": palm, "price_min": 8, "price_max": 20,
         "min_order_quantity": "200 لتر", "availability": "seasonal", "is_featured": True, "slug": "organic-saudi-olive-oil"},
    ]
    for p in products:
        Product.objects.get_or_create(slug=p["slug"], defaults={**p, "is_active": True})

print("  Done.")
PYEOF

echo ""
echo "👤 [5/5] Creating superuser..."
python manage.py shell << 'PYEOF'
import os
from django.contrib.auth import get_user_model
User = get_user_model()
username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email    = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@saudiexports.sa")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "admin123")
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"  Superuser '{username}' created.")
else:
    print(f"  Superuser '{username}' already exists.")
PYEOF

echo ""
echo "========================================"
echo "  ✅ Build complete!                    "
echo "========================================"
