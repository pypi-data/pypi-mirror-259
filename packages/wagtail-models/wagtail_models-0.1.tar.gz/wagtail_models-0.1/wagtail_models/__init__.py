"""
Wagtail package

Modules 
-wagtails models: Contain custom wagtails Models Like StreamIndexPage and StandardPage
-wagtails extra_tag:Include some extra tag such as chunks

"""

from .wagtail_models import StandardIndexPage
from .wagtail_models import StandardPage
from templatetags.extra_tags import chunks
from templatetags.extra_tags import nonbreakhyphen
from django.conf import settings

def add_wagtail_app():
    """Add necessary Wagtail apps to the INSTALLED_APPS in Django project settings."""
    
    WAGTAIL_APPS = [
        'wagtail.contrib.forms',
        'wagtail.contrib.redirects',
        'wagtail.embeds',
        'wagtail.sites',
        'wagtail.users',
        'wagtail.snippets',
        'wagtail.documents',
        'wagtail.images',
        'wagtail.search',
        'wagtail.admin',
        'wagtail',
        'modelcluster',
        'taggit',
    ]
    # Ensure each app is in INSTALLED_APPS
    for app in WAGTAIL_APPS:
        if app not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS.append(app)


# settings.py

# from mypackage import add_wagtail_apps

# Call the function to add Wagtail apps
# add_wagtail_apps()
