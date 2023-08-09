from django.contrib import admin

from .models import Page, Block, PageBlock

admin.site.register(Block)
admin.site.register(Page)
admin.site.register(PageBlock)
