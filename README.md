# مجلس الصادرات والتجارة السعودية
# Saudi Export & Trade Council

منصة وسيطة ثنائية اللغة (عربي/إنجليزي) تربط المصانع السعودية بالمستثمرين الأجانب.

A bilingual (Arabic/English) intermediary platform connecting Saudi factories with foreign investors.

---

## 🚀 تشغيل المشروع / Quick Start

```bash
# 1. تثبيت المتطلبات / Install requirements
pip3 install django pillow

# 2. تطبيق الـ migrations
python3 manage.py migrate

# 3. إضافة بيانات تجريبية (اختياري) / Load sample data (optional)
python3 manage.py shell < exports/sample_data.py

# 4. إنشاء مستخدم مدير / Create superuser
python3 manage.py createsuperuser

# 5. تشغيل السيرفر / Run server
python3 manage.py runserver
```

أو استخدم السكريبت المرفق / Or use the startup script:
```bash
bash start.sh
```

---

## 🌐 الروابط / URLs

| الصفحة | الرابط |
|--------|--------|
| الرئيسية (AR) | http://127.0.0.1:8000/ |
| الرئيسية (EN) | http://127.0.0.1:8000/en/ |
| الصادرات | http://127.0.0.1:8000/products/ |
| المصانع | http://127.0.0.1:8000/factories/ |
| اعرض مصنعك | http://127.0.0.1:8000/list-your-factory/ |
| استفسار مستثمر | http://127.0.0.1:8000/investor-inquiry/ |
| عن المجلس | http://127.0.0.1:8000/about/ |
| لوحة الإدارة | http://127.0.0.1:8000/admin/ |

---

## 🛠️ التقنيات المستخدمة / Tech Stack

- **Backend:** Django 6 (Python 3.14)
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Frontend:** Bootstrap 5 RTL/LTR + Font Awesome
- **Fonts:** Tajawal (AR) + Inter (EN)

---

## 📁 هيكل المشروع / Project Structure

```
├── exports/                  # Main app
│   ├── models.py             # Category, Factory, Product, Requests
│   ├── views.py              # All page views
│   ├── forms.py              # Factory listing & investor inquiry forms
│   ├── admin.py              # Django admin configuration
│   ├── urls.py               # URL patterns
│   ├── context_processors.py # Language context
│   ├── templates/exports/    # HTML templates
│   └── sample_data.py        # Demo data loader
├── saudi_exports_project/    # Django project settings
├── static/exports/           # CSS, JS, Images
├── start.sh                  # Startup script
└── manage.py
```

---

## 👤 بيانات المدير الافتراضية / Default Admin Credentials

> **تحذير:** غيّر هذه البيانات في بيئة الإنتاج!

- **Username:** `admin`
- **Password:** `admin123`

---

## 📄 الترخيص / License

MIT License — Saudi Export & Trade Council © 2025

