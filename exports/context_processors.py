from django.utils import translation


def language_context(request):
    lang = translation.get_language() or 'ar'
    is_rtl = lang == 'ar'
    return {
        'CURRENT_LANG': lang,
        'IS_RTL': is_rtl,
        'IS_AR': lang == 'ar',
        'IS_EN': lang == 'en',
    }

