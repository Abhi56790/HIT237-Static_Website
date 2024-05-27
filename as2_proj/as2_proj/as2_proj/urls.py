"""
URL configuration for as2_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from as2_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path('projects/', views.projectlist, name='project'),
    path('aboutus/', views.about, name='about'),
    path('project/<int:pk>', views.project_details, name='project_details'),
    path('display_forms/', views.display_forms, name='display_forms'),
   
    
]
