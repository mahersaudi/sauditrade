from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from .models import Category, Product, Factory, FactoryListingRequest, InvestorInquiry
from .forms import FactoryListingRequestForm, InvestorInquiryForm, ProductSearchForm


def home(request):
    lang = translation.get_language() or 'ar'
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    categories = Category.objects.all()
    total_products = Product.objects.filter(is_active=True).count()
    total_factories = Factory.objects.filter(status='approved').count()
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'total_products': total_products,
        'total_factories': total_factories,
        'lang': lang,
    }
    return render(request, 'exports/home.html', context)


def product_list(request):
    lang = translation.get_language() or 'ar'
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    search_form = ProductSearchForm(request.GET)

    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    selected_category = None

    if query:
        products = products.filter(
            Q(name_ar__icontains=query) |
            Q(name_en__icontains=query) |
            Q(description_ar__icontains=query) |
            Q(description_en__icontains=query)
        )

    if category_slug:
        selected_category = Category.objects.filter(slug=category_slug).first()
        if selected_category:
            products = products.filter(category=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'search_form': search_form,
        'query': query,
        'selected_category': selected_category,
        'lang': lang,
    }
    return render(request, 'exports/product_list.html', context)


def product_detail(request, slug):
    lang = translation.get_language() or 'ar'
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, is_active=True
    ).exclude(pk=product.pk)[:4]

    inquiry_form = InvestorInquiryForm(initial={'product_interest': product.name_ar if lang == 'ar' else product.name_en})

    if request.method == 'POST':
        inquiry_form = InvestorInquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry = inquiry_form.save(commit=False)
            inquiry.product = product
            inquiry.save()
            messages.success(request, _('تم إرسال استفسارك بنجاح! سنتواصل معك قريباً.') if lang == 'ar' else _('Your inquiry has been sent successfully! We will contact you soon.'))
            return redirect('product_detail', slug=slug)

    context = {
        'product': product,
        'related_products': related_products,
        'inquiry_form': inquiry_form,
        'lang': lang,
    }
    return render(request, 'exports/product_detail.html', context)


def factory_request(request):
    lang = translation.get_language() or 'ar'
    if request.method == 'POST':
        form = FactoryListingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'تم استلام طلبك بنجاح! سيتم مراجعة طلبك والتواصل معك خلال 3-5 أيام عمل.' if lang == 'ar'
                else 'Your request has been received successfully! We will review and contact you within 3-5 business days.'
            )
            return redirect('factory_request_success')
    else:
        form = FactoryListingRequestForm()

    context = {
        'form': form,
        'lang': lang,
    }
    return render(request, 'exports/factory_request.html', context)


def factory_request_success(request):
    lang = translation.get_language() or 'ar'
    return render(request, 'exports/factory_request_success.html', {'lang': lang})


def investor_inquiry(request):
    lang = translation.get_language() or 'ar'
    if request.method == 'POST':
        form = InvestorInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'تم إرسال استفسارك بنجاح! سنتواصل معك قريباً.' if lang == 'ar'
                else 'Your inquiry has been sent successfully! We will contact you soon.'
            )
            return redirect('investor_inquiry_success')
    else:
        form = InvestorInquiryForm()

    context = {
        'form': form,
        'lang': lang,
    }
    return render(request, 'exports/investor_inquiry.html', context)


def investor_inquiry_success(request):
    lang = translation.get_language() or 'ar'
    return render(request, 'exports/investor_inquiry_success.html', {'lang': lang})


def about(request):
    lang = translation.get_language() or 'ar'
    return render(request, 'exports/about.html', {'lang': lang})


def factories_list(request):
    lang = translation.get_language() or 'ar'
    factories = Factory.objects.filter(status='approved')
    context = {
        'factories': factories,
        'lang': lang,
    }
    return render(request, 'exports/factories_list.html', context)
