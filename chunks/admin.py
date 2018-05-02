# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Chunk

class ChunkAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']

admin.site.register(Chunk, ChunkAdmin)