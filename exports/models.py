from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name=_("الاسم بالعربية"))
    name_en = models.CharField(max_length=100, verbose_name=_("Name in English"))
    icon = models.CharField(max_length=50, blank=True, default='fas fa-box', verbose_name=_("أيقونة"))
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("تصنيف")
        verbose_name_plural = _("التصنيفات")

    def __str__(self):
        return self.name_ar

    def get_name(self, lang='ar'):
        return self.name_ar if lang == 'ar' else self.name_en


class Factory(models.Model):
    STATUS_CHOICES = [
        ('pending', _('قيد المراجعة')),
        ('approved', _('موافق عليه')),
        ('rejected', _('مرفوض')),
    ]

    name_ar = models.CharField(max_length=200, verbose_name=_("اسم المصنع بالعربية"))
    name_en = models.CharField(max_length=200, verbose_name=_("Factory Name in English"))
    description_ar = models.TextField(verbose_name=_("وصف المصنع بالعربية"), blank=True)
    description_en = models.TextField(verbose_name=_("Factory Description in English"), blank=True)
    city = models.CharField(max_length=100, verbose_name=_("المدينة"), blank=True)
    owner_name = models.CharField(max_length=200, verbose_name=_("اسم صاحب المصنع"))
    email = models.EmailField(verbose_name=_("البريد الإلكتروني"))
    phone = models.CharField(max_length=20, verbose_name=_("رقم الهاتف"))
    website = models.URLField(blank=True, verbose_name=_("الموقع الإلكتروني"))
    logo = models.ImageField(upload_to='factories/', blank=True, null=True, verbose_name=_("شعار المصنع"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_("الحالة"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("مصنع")
        verbose_name_plural = _("المصانع")

    def __str__(self):
        return self.name_ar

    def get_name(self, lang='ar'):
        return self.name_ar if lang == 'ar' else self.name_en


class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ('available', _('متوفر')),
        ('seasonal', _('موسمي')),
        ('on_order', _('عند الطلب')),
    ]

    name_ar = models.CharField(max_length=200, verbose_name=_("اسم المنتج بالعربية"))
    name_en = models.CharField(max_length=200, verbose_name=_("Product Name in English"))
    description_ar = models.TextField(verbose_name=_("وصف المنتج بالعربية"))
    description_en = models.TextField(verbose_name=_("Product Description in English"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name=_("التصنيف"))
    factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name=_("المصنع"))
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name=_("صورة المنتج"))
    price_min = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=_("السعر الأدنى (USD)"))
    price_max = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name=_("السعر الأقصى (USD)"))
    min_order_quantity = models.CharField(max_length=100, blank=True, verbose_name=_("الحد الأدنى للطلب"))
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='available', verbose_name=_("التوفر"))
    is_featured = models.BooleanField(default=False, verbose_name=_("منتج مميز"))
    is_active = models.BooleanField(default=True, verbose_name=_("نشط"))
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, allow_unicode=True)

    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
        ordering = ['-created_at']

    def __str__(self):
        return self.name_ar

    def get_name(self, lang='ar'):
        return self.name_ar if lang == 'ar' else self.name_en

    def get_description(self, lang='ar'):
        return self.description_ar if lang == 'ar' else self.description_en


class FactoryListingRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', _('قيد المراجعة')),
        ('approved', _('موافق عليه')),
        ('rejected', _('مرفوض')),
        ('contacted', _('تم التواصل')),
    ]

    factory_name_ar = models.CharField(max_length=200, verbose_name=_("اسم المصنع بالعربية"))
    factory_name_en = models.CharField(max_length=200, blank=True, verbose_name=_("Factory Name in English"))
    owner_name = models.CharField(max_length=200, verbose_name=_("اسم صاحب المصنع"))
    email = models.EmailField(verbose_name=_("البريد الإلكتروني"))
    phone = models.CharField(max_length=20, verbose_name=_("رقم الهاتف"))
    city = models.CharField(max_length=100, verbose_name=_("المدينة"))
    products_description_ar = models.TextField(verbose_name=_("وصف المنتجات المراد عرضها"))
    products_description_en = models.TextField(blank=True, verbose_name=_("Products Description in English"))
    commercial_register = models.CharField(max_length=100, blank=True, verbose_name=_("رقم السجل التجاري"))
    website = models.URLField(blank=True, verbose_name=_("الموقع الإلكتروني"))
    additional_notes = models.TextField(blank=True, verbose_name=_("ملاحظات إضافية"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name=_("الحالة"))
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, verbose_name=_("ملاحظات الإدارة"))

    class Meta:
        verbose_name = _("طلب عرض مصنع")
        verbose_name_plural = _("طلبات عرض المصانع")
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.factory_name_ar} - {self.owner_name}"


class InvestorInquiry(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("الاسم الكامل"))
    company = models.CharField(max_length=200, blank=True, verbose_name=_("اسم الشركة"))
    country = models.CharField(max_length=100, verbose_name=_("الدولة"))
    email = models.EmailField(verbose_name=_("البريد الإلكتروني"))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("رقم الهاتف"))
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='inquiries', verbose_name=_("المنتج المطلوب"))
    product_interest = models.CharField(max_length=300, verbose_name=_("المنتج / السلعة المطلوبة"))
    quantity_needed = models.CharField(max_length=100, blank=True, verbose_name=_("الكمية المطلوبة"))
    message = models.TextField(verbose_name=_("الرسالة"))
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name=_("تمت القراءة"))

    class Meta:
        verbose_name = _("استفسار مستثمر")
        verbose_name_plural = _("استفسارات المستثمرين")
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.country} - {self.product_interest}"
