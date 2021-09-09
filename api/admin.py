from django.contrib import admin
from .models import stock,articles,optionsStocks,investments
# Register your models here.

admin.site.register(stock)
admin.site.register(articles)
admin.site.register(optionsStocks)
admin.site.register(investments)