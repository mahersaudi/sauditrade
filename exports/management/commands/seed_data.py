from django.core.management.base import BaseCommand
from exports.models import Category, Factory, Product


class Command(BaseCommand):
    help = 'Seed the database with initial Saudi export data'

    def handle(self, *args, **options):
        self.stdout.write('🌱 Seeding data...')

        # ── Categories ────────────────────────────────────────────────────────
        if Category.objects.exists():
            self.stdout.write('  Categories already exist, skipping.')
        else:
            cats = [
                ('البتروكيماويات', 'Petrochemicals', 'fas fa-flask', 'petrochemicals'),
                ('التمور والأغذية', 'Dates & Food', 'fas fa-seedling', 'dates-food'),
                ('البلاستيك والمطاط', 'Plastics & Rubber', 'fas fa-recycle', 'plastics-rubber'),
                ('الأثاث والديكور', 'Furniture & Decor', 'fas fa-couch', 'furniture-decor'),
                ('مواد البناء', 'Building Materials', 'fas fa-building', 'building-materials'),
                ('المنسوجات والملابس', 'Textiles & Clothing', 'fas fa-tshirt', 'textiles-clothing'),
                ('المعادن والصلب', 'Metals & Steel', 'fas fa-cog', 'metals-steel'),
                ('المنتجات الكيميائية', 'Chemical Products', 'fas fa-vial', 'chemical-products'),
                ('الإلكترونيات', 'Electronics', 'fas fa-microchip', 'electronics'),
                ('مستحضرات التجميل', 'Cosmetics', 'fas fa-spa', 'cosmetics'),
            ]
            for ar, en, icon, slug in cats:
                Category.objects.create(name_ar=ar, name_en=en, icon=icon, slug=slug)
            self.stdout.write(f'  Created {len(cats)} categories.')

        # ── Factories ─────────────────────────────────────────────────────────
        if Factory.objects.exists():
            self.stdout.write('  Factories already exist, skipping.')
        else:
            factories_data = [
                ('شركة سابك للبتروكيماويات', 'SABIC Petrochemicals', 'الجبيل',
                 'محمد العبدالله', 'info@sabic-factory.sa', '+966112345678',
                 'شركة رائدة في صناعة البتروكيماويات', 'Leading petrochemicals company'),
                ('مصنع النخيل الذهبي للتمور', 'Golden Palm Dates Factory', 'المدينة المنورة',
                 'عبدالرحمن الأنصاري', 'dates@golden-palm.sa', '+966148765432',
                 'متخصصون في إنتاج وتصدير أجود أنواع التمور', 'Specialized in premium dates'),
                ('مصنع الرياض للمواد البلاستيكية', 'Riyadh Plastics Factory', 'الرياض',
                 'خالد السلطان', 'info@riyadh-plastics.sa', '+966115559900',
                 'مصنع متخصص في المنتجات البلاستيكية', 'Specialized plastic products factory'),
                ('مصنع الجبيل للصلب', 'Jubail Steel Factory', 'الجبيل',
                 'فيصل العمري', 'steel@jubail-steel.sa', '+966133334444',
                 'منتجون رائدون للصلب والحديد', 'Leading steel and iron producers'),
            ]
            for ar, en, city, owner, email, phone, desc_ar, desc_en in factories_data:
                Factory.objects.create(
                    name_ar=ar, name_en=en, city=city, owner_name=owner,
                    email=email, phone=phone, status='approved',
                    description_ar=desc_ar, description_en=desc_en,
                )
            self.stdout.write(f'  Created {len(factories_data)} factories.')

        # ── Products ──────────────────────────────────────────────────────────
        if Product.objects.exists():
            self.stdout.write('  Products already exist, skipping.')
        else:
            cats = {c.slug: c for c in Category.objects.all()}
            facts = {f.email: f for f in Factory.objects.all()}

            products = [
                dict(name_ar='إيثيلين عالي النقاء', name_en='High-Purity Ethylene',
                     description_ar='إيثيلين بنسبة نقاء 99.9% للبوليمرات والبلاستيك.',
                     description_en='99.9% purity ethylene for polymer and plastic manufacturing.',
                     category=cats.get('petrochemicals'), factory=facts.get('info@sabic-factory.sa'),
                     price_min=800, price_max=1200, min_order_quantity='20 طن',
                     availability='available', is_featured=True, slug='high-purity-ethylene'),
                dict(name_ar='تمر المدينة المجفف', name_en='Dried Madinah Dates',
                     description_ar='تمر المجدول والسكري من أجود أنواع التمور السعودية.',
                     description_en='Medjool and Sukkari dates from finest Saudi varieties.',
                     category=cats.get('dates-food'), factory=facts.get('dates@golden-palm.sa'),
                     price_min=5, price_max=15, min_order_quantity='500 كيلوغرام',
                     availability='available', is_featured=True, slug='dried-madinah-dates'),
                dict(name_ar='بولي بروبيلين', name_en='Polypropylene (PP)',
                     description_ar='بولي بروبيلين عالي الجودة للاستخدام الصناعي.',
                     description_en='High-quality polypropylene for industrial use.',
                     category=cats.get('plastics-rubber'), factory=facts.get('info@riyadh-plastics.sa'),
                     price_min=1100, price_max=1500, min_order_quantity='10 أطنان',
                     availability='available', is_featured=True, slug='polypropylene-pp'),
                dict(name_ar='حديد التسليح', name_en='Reinforcement Steel Bars',
                     description_ar='حديد تسليح عالي الجودة للبناء والإنشاء.',
                     description_en='High-quality reinforcement steel bars for construction.',
                     category=cats.get('metals-steel'), factory=facts.get('steel@jubail-steel.sa'),
                     price_min=600, price_max=850, min_order_quantity='50 طن',
                     availability='available', is_featured=True, slug='reinforcement-steel-bars'),
                dict(name_ar='اسمنت بورتلاند', name_en='Portland Cement',
                     description_ar='إسمنت بورتلاند عالي الجودة بمقاومة 42.5N.',
                     description_en='High-quality Portland cement 42.5N resistance.',
                     category=cats.get('building-materials'), factory=facts.get('steel@jubail-steel.sa'),
                     price_min=60, price_max=90, min_order_quantity='100 طن',
                     availability='available', is_featured=False, slug='portland-cement'),
                dict(name_ar='زيت الزيتون السعودي العضوي', name_en='Organic Saudi Olive Oil',
                     description_ar='زيت زيتون بكر ممتاز من مزارع الجوف وتبوك.',
                     description_en='Extra virgin olive oil from Al-Jouf and Tabuk farms.',
                     category=cats.get('dates-food'), factory=facts.get('dates@golden-palm.sa'),
                     price_min=8, price_max=20, min_order_quantity='200 لتر',
                     availability='seasonal', is_featured=True, slug='organic-saudi-olive-oil'),
                dict(name_ar='ميثانول صناعي', name_en='Industrial Methanol',
                     description_ar='ميثانول صناعي بدرجة نقاء عالية للصناعات الكيميائية.',
                     description_en='High-purity industrial methanol for chemical industries.',
                     category=cats.get('chemical-products'), factory=facts.get('info@sabic-factory.sa'),
                     price_min=350, price_max=500, min_order_quantity='50 طن',
                     availability='available', is_featured=False, slug='industrial-methanol'),
                dict(name_ar='ألواح الجبس الجاف', name_en='Drywall Gypsum Boards',
                     description_ar='ألواح جبس جاف متعددة الاستخدامات للتشطيبات الداخلية.',
                     description_en='Multi-purpose drywall gypsum boards for interior finishing.',
                     category=cats.get('building-materials'), factory=facts.get('steel@jubail-steel.sa'),
                     price_min=3, price_max=8, min_order_quantity='1000 لوح',
                     availability='available', is_featured=False, slug='drywall-gypsum-boards'),
            ]
            for p in products:
                Product.objects.create(**p, is_active=True)
            self.stdout.write(f'  Created {len(products)} products.')

        self.stdout.write(self.style.SUCCESS('✅ Seed data complete!'))

