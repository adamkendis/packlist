from django.urls import path
from . import views

app_name = 'gear'

urlpatterns = [
  path('', views.gear_list, name='gear_list'),
  path('item/<int:pk>', views.gear_detail, name='gear_detail'),
  path('item/<int:pk>/edit', views.gear_edit, name='gear_edit'),
]