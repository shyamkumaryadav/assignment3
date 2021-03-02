"""studentportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .models import Student
from .views import StudentViewSet

admin.AdminSite.site_title = 'Student Portal'
admin.AdminSite.site_header = 'Student portal CRUD'
admin.AdminSite.index_title = 'App List'
admin.AdminSite.site_url = '/'
admin.AdminSite.enable_nav_sidebar = False
admin.AdminSite.empty_value_display = '<i>undefined</i>'




router = DefaultRouter()
router.register('students', StudentViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('leaderboard/', TemplateView.as_view(template_name="leaderboard.html"), name='leaderboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

handler404 = 'studentportal.views.Handler404'