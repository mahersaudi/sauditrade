"""
Script to populate the database with sample Saudi export data.
Run: python manage.py shell < exports/sample_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saudi_exports_project.settings')
django.setup()

from exports.models import Category, Factory, Product

print("🌱 Creating sample data...")

# ===== CATEGORIES =====
categories_data = [
    {'name_ar': 'البتروكيماويات', 'name_en': 'Petrochemicals', 'icon': 'fas fa-flask', 'slug': 'petrochemicals'},
    {'name_ar': 'التمور والأغذية', 'name_en': 'Dates & Food', 'icon': 'fas fa-seedling', 'slug': 'dates-food'},
    {'name_ar': 'البلاستيك والمطاط', 'name_en': 'Plastics & Rubber', 'icon': 'fas fa-recycle', 'slug': 'plastics-rubber'},
    {'name_ar': 'الأثاث والديكور', 'name_en': 'Furniture & Décor', 'icon': 'fas fa-couch', 'slug': 'furniture-decor'},
    {'name_ar': 'مواد البناء', 'name_en': 'Building Materials', 'icon': 'fas fa-building', 'slug': 'building-materials'},
    {'name_ar': 'المنسوجات والملابس', 'name_en': 'Textiles & Clothing', 'icon': 'fas fa-tshirt', 'slug': 'textiles-clothing'},
    {'name_ar': 'المعادن والصلب', 'name_en': 'Metals & Steel', 'icon': 'fas fa-cog', 'slug': 'metals-steel'},
    {'name_ar': 'المنتجات الكيميائية', 'name_en': 'Chemical Products', 'icon': 'fas fa-vial', 'slug': 'chemical-products'},
    {'name_ar': 'الإلكترونيات', 'name_en': 'Electronics', 'icon': 'fas fa-microchip', 'slug': 'electronics'},
    {'name_ar': 'مستحضرات التجميل', 'name_en': 'Cosmetics', 'icon': 'fas fa-spa', 'slug': 'cosmetics'},
]

categories = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={
            'name_ar': cat_data['name_ar'],
            'name_en': cat_data['name_en'],
            'icon': cat_data['icon'],
        }
    )
    categories[cat_data['slug']] = cat
    status = "✅ Created" if created else "⏭️ Exists"
    print(f"  {status}: {cat_data['name_ar']}")

# ===== FACTORIES =====
factories_data = [
    {
        'name_ar': 'شركة سابك للبتروكيماويات',
        'name_en': 'SABIC Petrochemicals',
        'description_ar': 'شركة رائدة عالمياً في صناعة البتروكيماويات والبلاستيك والمعادن',
        'description_en': 'A world-leading company in petrochemicals, plastics and metals manufacturing',
        'city': 'الجبيل',
        'owner_name': 'محمد العبدالله',
        'email': 'info@sabic-factory.sa',
        'phone': '+966112345678',
        'status': 'approved',
    },
    {
        'name_ar': 'مصنع النخيل الذهبي للتمور',
        'name_en': 'Golden Palm Dates Factory',
        'description_ar': 'متخصصون في إنتاج وتصدير أجود أنواع التمور السعودية',
        'description_en': 'Specialized in producing and exporting the finest Saudi dates',
        'city': 'المدينة المنورة',
        'owner_name': 'عبدالرحمن الأنصاري',
        'email': 'dates@golden-palm.sa',
        'phone': '+966148765432',
        'status': 'approved',
    },
    {
        'name_ar': 'مصنع الرياض للمواد البلاستيكية',
        'name_en': 'Riyadh Plastics Factory',
        'description_ar': 'مصنع متخصص في إنتاج المنتجات البلاستيكية عالية الجودة',
        'description_en': 'A factory specializing in producing high-quality plastic products',
        'city': 'الرياض',
        'owner_name': 'خالد السلطان',
        'email': 'info@riyadh-plastics.sa',
        'phone': '+966115559900',
        'status': 'approved',
    },
    {
        'name_ar': 'مصنع الجبيل للصلب',
        'name_en': 'Jubail Steel Factory',
        'description_ar': 'منتجون رائدون للصلب والحديد في المنطقة الشرقية',
        'description_en': 'Leading steel and iron producers in the Eastern Region',
        'city': 'الجبيل',
        'owner_name': 'فيصل العمري',
        'email': 'steel@jubail-steel.sa',
        'phone': '+966133334444',
        'status': 'approved',
    },
]

factories = {}
for f_data in factories_data:
    factory, created = Factory.objects.get_or_create(
        email=f_data['email'],
        defaults=f_data
    )
    factories[f_data['email']] = factory
    status = "✅ Created" if created else "⏭️ Exists"
    print(f"  {status}: {f_data['name_ar']}")

# ===== PRODUCTS =====
products_data = [
    {
        'name_ar': 'إيثيلين عالي النقاء',
        'name_en': 'High-Purity Ethylene',
        'description_ar': 'إيثيلين بنسبة نقاء 99.9% يُستخدم في صناعة البوليمرات والبلاستيك، مُنتَج وفق أعلى معايير الجودة الدولية. يُصدَّر إلى أكثر من 20 دولة.',
        'description_en': 'High-purity ethylene at 99.9% purity used in polymer and plastic manufacturing, produced to the highest international quality standards. Exported to over 20 countries.',
        'category': 'petrochemicals',
        'factory_email': 'info@sabic-factory.sa',
        'price_min': 800,
        'price_max': 1200,
        'min_order_quantity': '20 طن',
        'availability': 'available',
        'is_featured': True,
        'slug': 'high-purity-ethylene',
    },
    {
        'name_ar': 'تمر المدينة المجفف',
        'name_en': 'Dried Madinah Dates',
        'description_ar': 'تمر المجدول والسكري من أجود أنواع التمور السعودية، مجفف طبيعياً ومعبأ بطرق حديثة للتصدير. يتميز بطعمه الفريد وقيمته الغذائية العالية.',
        'description_en': 'Medjool and Sukkari dates from the finest Saudi varieties, naturally dried and packed with modern methods for export. Distinguished by its unique taste and high nutritional value.',
        'category': 'dates-food',
        'factory_email': 'dates@golden-palm.sa',
        'price_min': 5,
        'price_max': 15,
        'min_order_quantity': '500 كيلوغرام',
        'availability': 'available',
        'is_featured': True,
        'slug': 'dried-madinah-dates',
    },
    {
        'name_ar': 'بولي بروبيلين',
        'name_en': 'Polypropylene (PP)',
        'description_ar': 'بولي بروبيلين عالي الجودة للاستخدام الصناعي، يتميز بمتانته وخواصه الحرارية الممتازة. مناسب لصناعة العبوات والمنتجات الصناعية المتنوعة.',
        'description_en': 'High-quality polypropylene for industrial use, characterized by its durability and excellent thermal properties. Suitable for packaging and various industrial products.',
        'category': 'plastics-rubber',
        'factory_email': 'info@riyadh-plastics.sa',
        'price_min': 1100,
        'price_max': 1500,
        'min_order_quantity': '10 أطنان',
        'availability': 'available',
        'is_featured': True,
        'slug': 'polypropylene-pp',
    },
    {
        'name_ar': 'حديد التسليح',
        'name_en': 'Reinforcement Steel Bars',
        'description_ar': 'حديد تسليح عالي الجودة يُستخدم في البناء والإنشاء، مُنتَج وفق المواصفات الدولية ASTM وBS. متوفر بأقطار مختلفة من 8 إلى 32 ملم.',
        'description_en': 'High-quality reinforcement steel bars used in construction, produced according to international ASTM and BS specifications. Available in various diameters from 8 to 32mm.',
        'category': 'metals-steel',
        'factory_email': 'steel@jubail-steel.sa',
        'price_min': 600,
        'price_max': 850,
        'min_order_quantity': '50 طن',
        'availability': 'available',
        'is_featured': True,
        'slug': 'reinforcement-steel-bars',
    },
    {
        'name_ar': 'اسمنت بورتلاند',
        'name_en': 'Portland Cement',
        'description_ar': 'إسمنت بورتلاند عالي الجودة بمقاومة 42.5N، مثالي للبناء والإنشاء. مطابق للمواصفات السعودية SASO والمعايير الدولية.',
        'description_en': 'High-quality Portland cement with 42.5N resistance, ideal for construction. Compliant with Saudi SASO standards and international standards.',
        'category': 'building-materials',
        'factory_email': 'steel@jubail-steel.sa',
        'price_min': 60,
        'price_max': 90,
        'min_order_quantity': '100 طن',
        'availability': 'available',
        'is_featured': False,
        'slug': 'portland-cement',
    },
    {
        'name_ar': 'زيت الزيتون السعودي العضوي',
        'name_en': 'Organic Saudi Olive Oil',
        'description_ar': 'زيت زيتون بكر ممتاز من مزارع الجوف وتبوك، مُنتَج بالطرق العضوية دون أي إضافات كيميائية. حائز على شهادات الجودة الدولية.',
        'description_en': 'Extra virgin olive oil from Al-Jouf and Tabuk farms, produced organically without any chemical additives. Holds international quality certifications.',
        'category': 'dates-food',
        'factory_email': 'dates@golden-palm.sa',
        'price_min': 8,
        'price_max': 20,
        'min_order_quantity': '200 لتر',
        'availability': 'seasonal',
        'is_featured': True,
        'slug': 'organic-saudi-olive-oil',
    },
    {
        'name_ar': 'ميثانول صناعي',
        'name_en': 'Industrial Methanol',
        'description_ar': 'ميثانول صناعي بدرجة نقاء عالية يُستخدم في الصناعات الكيميائية ووقود السيارات والطاقة المتجددة.',
        'description_en': 'High-purity industrial methanol used in chemical industries, automotive fuel and renewable energy.',
        'category': 'chemical-products',
        'factory_email': 'info@sabic-factory.sa',
        'price_min': 350,
        'price_max': 500,
        'min_order_quantity': '50 طن',
        'availability': 'available',
        'is_featured': False,
        'slug': 'industrial-methanol',
    },
    {
        'name_ar': 'ألواح الجبس الجاف',
        'name_en': 'Drywall Gypsum Boards',
        'description_ar': 'ألواح جبس جاف متعددة الاستخدامات للتشطيبات الداخلية، مقاومة للحريق والرطوبة. مقاسات متنوعة.',
        'description_en': 'Multi-purpose drywall gypsum boards for interior finishing, fire and moisture resistant. Available in various sizes.',
        'category': 'building-materials',
        'factory_email': 'steel@jubail-steel.sa',
        'price_min': 3,
        'price_max': 8,
        'min_order_quantity': '1000 لوح',
        'availability': 'available',
        'is_featured': False,
        'slug': 'drywall-gypsum-boards',
    },
]

for p_data in products_data:
    cat_slug = p_data.pop('category')
    factory_email = p_data.pop('factory_email')
    category = categories.get(cat_slug)
    factory = factories.get(factory_email)

    product, created = Product.objects.get_or_create(
        slug=p_data['slug'],
        defaults={
            **p_data,
            'category': category,
            'factory': factory,
            'is_active': True,
        }
    )
    status = "✅ Created" if created else "⏭️ Exists"
    print(f"  {status}: {p_data['name_ar']}")

print("\n✅ Sample data loaded successfully!")
print(f"   📦 Categories: {Category.objects.count()}")
print(f"   🏭 Factories:  {Factory.objects.count()}")
print(f"   📋 Products:   {Product.objects.count()}")

