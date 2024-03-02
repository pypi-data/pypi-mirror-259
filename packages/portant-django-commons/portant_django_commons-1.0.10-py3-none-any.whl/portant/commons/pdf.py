from contextlib import contextmanager
from io import BytesIO

from django.conf import settings

import weasyprint

from django.template.loader import get_template


@contextmanager
def generate_pdf(template, context={}, stylesheets=None):
    """
    Generate pdf content stored in BytesIO.

    PDF content retriavable from ret_val.get_value()
    """
    kwargs = {}
    if stylesheets:
        kwargs['stylesheets'] = stylesheets

    html = get_template(template).render(context)
    if settings.USE_LOCAL_STORAGE and hasattr(settings, 'BASE_URL'):
        base_url = settings.BASE_URL
    else:
        base_url = None

    try:
        pdf = BytesIO()
        weasyprint.HTML(string=html, base_url=base_url).write_pdf(pdf, **kwargs)
        yield pdf
    finally:
        pdf.close()
