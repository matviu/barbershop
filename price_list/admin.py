from django.contrib import admin
from .models import PriceList, PriceItem


class PriceItemInline(admin.TabularInline):
	model = PriceItem
	extra = 1
	verbose_name = 'Услуга'


class PriceListAdmin(admin.ModelAdmin):
	inlines = [
		PriceItemInline,
	]


admin.site.register(PriceList, PriceListAdmin)