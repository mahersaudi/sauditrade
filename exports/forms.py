from django import forms
from django.utils.translation import gettext_lazy as _
from .models import FactoryListingRequest, InvestorInquiry

SAUDI_CITIES = [
    ('', '--- اختر المدينة / Select City ---'),
    ('الرياض', 'الرياض / Riyadh'),
    ('جدة', 'جدة / Jeddah'),
    ('مكة المكرمة', 'مكة المكرمة / Makkah'),
    ('المدينة المنورة', 'المدينة المنورة / Madinah'),
    ('الدمام', 'الدمام / Dammam'),
    ('الخبر', 'الخبر / Khobar'),
    ('الجبيل', 'الجبيل / Jubail'),
    ('ينبع', 'ينبع / Yanbu'),
    ('تبوك', 'تبوك / Tabuk'),
    ('أبها', 'أبها / Abha'),
    ('القصيم', 'القصيم / Qassim'),
    ('حائل', 'حائل / Hail'),
    ('نجران', 'نجران / Najran'),
    ('جازان', 'جازان / Jazan'),
    ('الطائف', 'الطائف / Taif'),
    ('أخرى', 'أخرى / Other'),
]


class FactoryListingRequestForm(forms.ModelForm):
    city = forms.ChoiceField(choices=SAUDI_CITIES, label=_("المدينة / City"))

    class Meta:
        model = FactoryListingRequest
        fields = [
            'factory_name_ar', 'factory_name_en', 'owner_name',
            'email', 'phone', 'city',
            'products_description_ar', 'products_description_en',
            'commercial_register', 'website', 'additional_notes'
        ]
        widgets = {
            'factory_name_ar': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'مثال: مصنع النجم للأغذية',
                'dir': 'rtl'
            }),
            'factory_name_en': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Al-Najm Food Factory',
                'dir': 'ltr'
            }),
            'owner_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'الاسم الكامل / Full Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com',
                'dir': 'ltr'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+966 5X XXX XXXX',
                'dir': 'ltr'
            }),
            'products_description_ar': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'صف المنتجات التي تريد عرضها بالتفصيل...',
                'dir': 'rtl'
            }),
            'products_description_en': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the products you want to list in detail...',
                'dir': 'ltr'
            }),
            'commercial_register': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'رقم السجل التجاري',
                'dir': 'ltr'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com',
                'dir': 'ltr'
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'أي معلومات إضافية...',
            }),
        }
        labels = {
            'factory_name_ar': _('اسم المصنع بالعربية *'),
            'factory_name_en': _('Factory Name in English'),
            'owner_name': _('اسم صاحب المصنع / Owner Name *'),
            'email': _('البريد الإلكتروني / Email *'),
            'phone': _('رقم الهاتف / Phone *'),
            'products_description_ar': _('وصف المنتجات بالعربية *'),
            'products_description_en': _('Products Description in English'),
            'commercial_register': _('رقم السجل التجاري'),
            'website': _('الموقع الإلكتروني'),
            'additional_notes': _('ملاحظات إضافية'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['class'] = 'form-select'


class InvestorInquiryForm(forms.ModelForm):
    class Meta:
        model = InvestorInquiry
        fields = [
            'name', 'company', 'country', 'email', 'phone',
            'product_interest', 'quantity_needed', 'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name / الاسم الكامل',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name / اسم الشركة',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. USA, Germany, China',
                'dir': 'ltr'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com',
                'dir': 'ltr'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 XXX XXX XXXX',
                'dir': 'ltr'
            }),
            'product_interest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Dates, Petrochemicals, Plastics / مثال: تمور، بتروكيماويات',
            }),
            'quantity_needed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 10 tons/month',
                'dir': 'ltr'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your message here... / اكتب رسالتك هنا...',
            }),
        }
        labels = {
            'name': 'Full Name / الاسم الكامل *',
            'company': 'Company / الشركة',
            'country': 'Country / الدولة *',
            'email': 'Email / البريد الإلكتروني *',
            'phone': 'Phone / الهاتف',
            'product_interest': 'Product Needed / المنتج المطلوب *',
            'quantity_needed': 'Quantity / الكمية',
            'message': 'Message / الرسالة *',
        }


class ProductSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'ابحث عن منتج... / Search for a product...',
        })
    )
    category = forms.CharField(required=False, widget=forms.HiddenInput())

