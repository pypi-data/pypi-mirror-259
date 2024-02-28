from wagtail import hooks
from django.templatetags.static import static
from django.utils.html import format_html

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('wagtail_reading_time/panels/reading_time.css')
    )

@hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        '<script src="{}"></script>',
        static('wagtail_reading_time/panels/reading_time.js')
    )
