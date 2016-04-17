# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


@admin.register(models.DocType)
class DocTypeAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'Тип документа', {'fields': ['name']}),
    ]

    list_display = ('name',)
