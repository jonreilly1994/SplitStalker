"""StartingBlocks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

import django.contrib.sites

from django.conf import settings
from django.conf.urls.static import static
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail
from django.views.generic.base import TemplateView







urlpatterns = [
    
    url(r'^$', 'signups.views.home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url(r'^botinfo', TemplateView.as_view(template_name='meetpingbot.html'),name='botinfo'),
    url(r'^meetPing', 'signups.views.meetPing'),
    url(r'^athlete/add', 'signups.views.add_athlete'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

