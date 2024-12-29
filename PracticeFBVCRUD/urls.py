"""
URL configuration for PracticeFBVCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from FBVApp.views import create_view,list_view,detail_view,update_view,delete_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/",create_view),
    path("PlayersList/",list_view),
    path("PlayerDetail/<id>",detail_view),
    path("update/<id>",update_view),
    path("delete/<id>",delete_view)
]
