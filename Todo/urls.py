from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plans/', all_plans),
    path('', loginView),
    path('todo_ochir/<int:son>/', todo_ochir),
    path('logout/', logoutView),
    path('register/', register),
]



