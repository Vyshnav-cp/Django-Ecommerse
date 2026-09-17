from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import LoginForm, RegistrationForm
from .models import Product


def register_view(request):
	if request.user.is_authenticated:
		return redirect('home')

	form = RegistrationForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		form.save()
		messages.success(request, 'Registration successful. Please log in.')
		return redirect('login')

	return render(request, 'store/register.html', {'form': form})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')

	form = LoginForm(request, data=request.POST or None)
	if request.method == 'POST' and form.is_valid():
		login(request, form.get_user())
		return redirect('home')

	return render(request, 'store/login.html', {'form': form})


@login_required
def home_view(request):
	products = Product.objects.all()
	return render(request, 'store/home.html', {'products': products})


@require_POST
def logout_view(request):
	logout(request)
	messages.success(request, 'You have been logged out.')
	return redirect('login')
