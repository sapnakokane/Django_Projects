"""allpro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/',v1.EmpListView.as_view(),name='employees'),
    path('<int:pk>/',v1.EmpDetailView.as_view(),name='detail'),
    path('create/',v1.EmpCreateView.as_view(),name='create'),
    path('update/<int:pk>/',v1.EmpUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',v1.EmpDeleteView.as_view(),name='delete'),

]
