from django.urls import path
from .views import user_dashboard, admin_dashboard, trade_history

urlpatterns = [
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('trade_history/<int:trader_id>/', trade_history, name='trade_history'),
]
