from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Trade, Trader
import random
from datetime import datetime, timedelta
import json


# Create your views here.
class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('admin_dashboard')
        else:
            return reverse_lazy('user_dashboard')  # Replace 'dashboard' with the URL name of your dashboard page


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/signup.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not password:
            # Display an error message
            error_message = 'Please provide a username and password.'
            return render(request, 'users/signup.html', {'error_message': error_message})
        if password2 != password:
            error_message = 'Passwords does not match'
            return render(request, 'users/signup.html', {'error_message': error_message})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Create a new trader object for the new user
            user_model = User.objects.get(username=username)
            Trader.objects.create(trader=user_model)
            return redirect('login')

@login_required
def user_dashboard(request):
    trader = Trader.objects.get(trader=request.user)
    # Generate random profit/loss values for each timestamp
    trades = []
    timestamps = []
    starting_balance = 100
    current_balance = starting_balance
    formatted_balance = None

    for i in range(10):  # Generate 10 data points
        profit_loss = random.uniform(-10, 10)  # Generate random profit/loss between -10 and 10
        timestamp = datetime.now() + timedelta(minutes=i)
        trade = Trade(trader=trader, timestamp=timestamp, profit_loss=profit_loss)
        trades.append(trade)
        timestamps.append(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        current_balance += profit_loss
        formatted_balance = '{:.3f}'.format(current_balance)

    # Update trader's account balance
    trader.account_balance = formatted_balance
    trader.save()

    # Save trades to the database
    Trade.objects.bulk_create(trades)

    # Retrieve trades from the database
    trades = Trade.objects.filter(trader=trader).order_by('timestamp')
    profit_loss = [float(trade.profit_loss.to_decimal()) for trade in trades]

    context = {
        'timestamps': timestamps,
        'profit_loss': profit_loss,
        'starting_balance': starting_balance,
        'formatted_balance': formatted_balance
    }

    return render(request, 'users/user_dashboard.html', context)

@staff_member_required
def admin_dashboard(request):
    traders = Trader.objects.all()

    context = {
        'traders': traders,
    }
    return render(request, 'users/admin_dashboard.html', context)

@staff_member_required
def trade_history(request, trader_id):
    trades = Trade.objects.filter(trader_id=trader_id)
    trader = get_object_or_404(Trader, id=trader_id)

    context = {
        'trades': trades,
        'trader': trader
    }

    return render(request, 'users/admin_track.html', context)
