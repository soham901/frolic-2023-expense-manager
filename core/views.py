from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as login_user, logout as logout_user, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

from .models import *


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login_user(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_user(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout(request):
    logout_user(request)
    return redirect('home')


@login_required
def dashboard(request):

    expences = Expence.objects.all()
    incomes = Income.objects.all()

    total_income = incomes.aggregate(models.Sum('amount'))['amount__sum'] or 0
    total_expense = expences.aggregate(models.Sum('amount'))['amount__sum'] or 0

    net_amount = total_income - total_expense

    context = {
        'expences': expences,
        'incomes': incomes,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_amount': net_amount,
    }

    return render(request, 'dashboard.html', context)


def add_expense(request):
    form = ExpenceForm()

    if request.method == 'POST':
        form = ExpenceForm(request.POST)
        if form.is_valid():
            # save this to epence model
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'add_expense.html', context)


def add_income(request):
    form = IncomeForm()

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            # save this to income model
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'add_income.html', context)


def delete_expense(request, id):
    expence = Expence.objects.get(id=id)
    expence.delete()
    return redirect('dashboard')


def delete_income(request, id):
    income = Income.objects.get(id=id)
    income.delete()
    return redirect('dashboard')


def test(request):
    return render(request, 'test.html')