"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from index.views import home
from database.views import visit_record_list,lab_member_list,database_view,imgs_show_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('imgs_show_list/', imgs_show_list, name='imgs_show_list'),  #debug用
    path('visit_record_list/', visit_record_list, name='visit_record_list'),  #debug用
    path('lab_member_list/', lab_member_list, name='lab_member_list'),  #debug用
    path('database_view/', database_view, name='database_view'),  #debug用
    # path('',)

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
