from django.contrib import admin
from .models import Trade, Trader

admin.site.register(Trader)

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('trader', 'timestamp', 'profit_loss')
    list_filter = ('trader', 'timestamp')



