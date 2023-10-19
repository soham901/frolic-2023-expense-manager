from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_expense/', add_expense, name='add_expense'),
    path('add_income/', add_income, name='add_income'),
    path('delete_expense/<int:id>/', delete_expense, name='delete_expense'),
    path('delete_income/<int:id>/', delete_income, name='delete_income'),
    # path('edit_expense/', edit_expense, name='edit_expense'),

    path('t/', test, name='test'),
]
