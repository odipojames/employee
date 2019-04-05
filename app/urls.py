from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    url('^$',views.home, name = 'home'),
    url(r'^employee/new$',views.new_employee,name = 'new_employee'),
    url(r'^singleEmployee/(\d+)',views.singleEmployee,name ='singleEmployee'),
    url(r'^employee/(?P<pk>\d+)/update/', views.updateEmployee, name='update_Employee'),
    url(r'^employee/(?P<id>\d+)/delete/', views.delete_employee, name='delete_employee'),
    url(r'^confirm_delete/(\d+)',views.confirm_delete,name ='confirm_delete'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^csv/', views.download_csv, name='download_csv'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
