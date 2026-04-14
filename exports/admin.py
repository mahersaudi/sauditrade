from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Factory, Product, FactoryListingRequest, InvestorInquiry

admin.site.site_header = "مجلس الصادرات والتجارة السعودية - Saudi Export & Trade Council"
admin.site.site_title = "لوحة التحكم"
admin.site.index_title = "إدارة الموقع"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'name_en', 'icon', 'slug']
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ['name_ar', 'name_en']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'name_en', 'owner_name', 'city', 'email', 'phone', 'status', 'created_at']
    list_filter = ['status', 'city']
    search_fields = ['name_ar', 'name_en', 'owner_name', 'email']
    list_editable = ['status']
    readonly_fields = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_ar', 'name_en', 'category', 'factory', 'availability', 'is_featured', 'is_active', 'product_image_preview']
    list_filter = ['category', 'availability', 'is_featured', 'is_active']
    search_fields = ['name_ar', 'name_en', 'description_ar', 'description_en']
    list_editable = ['is_featured', 'is_active']
    prepopulated_fields = {'slug': ('name_en',)}
    readonly_fields = ['created_at', 'product_image_preview']

    def product_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px; border-radius:6px;" />', obj.image.url)
        return "لا توجد صورة"
    product_image_preview.short_description = "معاينة الصورة"


@admin.register(FactoryListingRequest)
class FactoryListingRequestAdmin(admin.ModelAdmin):
    list_display = ['factory_name_ar', 'owner_name', 'city', 'email', 'phone', 'status', 'submitted_at']
    list_filter = ['status', 'city']
    search_fields = ['factory_name_ar', 'factory_name_en', 'owner_name', 'email']
    list_editable = ['status']
    readonly_fields = ['submitted_at']
    fieldsets = (
        ('معلومات المصنع / Factory Info', {
            'fields': ('factory_name_ar', 'factory_name_en', 'city', 'commercial_register', 'website')
        }),
        ('معلومات صاحب المصنع / Owner Info', {
            'fields': ('owner_name', 'email', 'phone')
        }),
        ('وصف المنتجات / Products Description', {
            'fields': ('products_description_ar', 'products_description_en', 'additional_notes')
        }),
        ('الحالة الإدارية / Admin Status', {
            'fields': ('status', 'admin_notes', 'submitted_at')
        }),
    )


@admin.register(InvestorInquiry)
class InvestorInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'country', 'email', 'product_interest', 'quantity_needed', 'is_read', 'submitted_at']
    list_filter = ['country', 'is_read']
    search_fields = ['name', 'company', 'country', 'email', 'product_interest']
    list_editable = ['is_read']
    readonly_fields = ['submitted_at']
    fieldsets = (
        ('معلومات المستثمر / Investor Info', {
            'fields': ('name', 'company', 'country', 'email', 'phone')
        }),
        ('تفاصيل الطلب / Request Details', {
            'fields': ('product', 'product_interest', 'quantity_needed', 'message')
        }),
        ('الحالة / Status', {
            'fields': ('is_read', 'submitted_at')
        }),
    )
