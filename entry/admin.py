# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','date_record', 'beard_model', 'email']


admin.site.register(Entry, EntryAdmin)