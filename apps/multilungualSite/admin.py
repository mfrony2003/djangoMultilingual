from django.contrib import admin

from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.multilungualSite.models.model import Blog,Menu


admin.site.register(Blog, TranslatableAdmin)
admin.site.register(Menu, TranslatableAdmin)
